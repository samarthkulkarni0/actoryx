"""
agent.py
Gemini AI Agent with MCP Tool Integration
The agent calls the MCP tools to get standards results,
then uses Gemini to generate a real AI diagnostic report.
"""

import json
import subprocess
import sys
import os

# ── Gemini setup ──────────────────────────────────────────────────────────────
from google import genai
from google.genai import types

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "AQ.Ab8RN6J3eEQCW1iqDeruuT-oHNMS3DawDrY_n2F2a1neAVcD3w")
client = genai.Client(api_key=GEMINI_API_KEY)

# ── MCP tool caller (calls mcp_server.py via subprocess) ──────────────────────
def call_mcp_tool(tool_name: str, arguments: dict) -> dict:
    """Calls a tool on the MCP server via subprocess stdin/stdout."""
    request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": tool_name,
            "arguments": arguments
        }
    }

    proc = subprocess.run(
        [sys.executable, "mcp_server.py"],
        input=json.dumps(request),
        capture_output=True,
        text=True,
        timeout=30
    )

    # Parse MCP response
    for line in proc.stdout.splitlines():
        line = line.strip()
        if line.startswith("{"):
            try:
                resp = json.loads(line)
                if "result" in resp:
                    content = resp["result"].get("content", [])
                    for item in content:
                        if item.get("type") == "text":
                            return json.loads(item["text"])
            except Exception:
                continue

    raise RuntimeError(f"MCP tool call failed.\nSTDOUT: {proc.stdout}\nSTDERR: {proc.stderr}")


# ── Main agent function ───────────────────────────────────────────────────────
def run_agent(voltage_kv: float, ir_1min: float, ir_10min: float,
              dc_resistance: float, vibration: float) -> dict:
    """
    Full AI agent pipeline:
    1. Call MCP tool to get standards check results
    2. Call MCP tool to get standard limits
    3. Send everything to Gemini for real AI analysis
    4. Return combined results + AI report
    """

    # ── Step 1: Run standards checks via MCP ─────────────────────────────────
    check_results = call_mcp_tool("check_motor_health", {
        "voltage_kv"   : voltage_kv,
        "ir_1min"      : ir_1min,
        "ir_10min"     : ir_10min,
        "dc_resistance": dc_resistance,
        "vibration"    : vibration
    })

    # ── Step 2: Get standard limits via MCP ──────────────────────────────────
    standards = call_mcp_tool("get_motor_standards", {
        "voltage_kv": voltage_kv
    })

    # ── Step 3: Build prompt for Gemini AI ───────────────────────────────────
    pi_val  = check_results["check3"]["measured"]
    pi_cond = check_results["check3"]["pi_condition"]
    overall = check_results["overall"]

    prompt = f"""You are a senior electrical engineer specialising in induction motor 
diagnostics and maintenance. You have just run a full IS 900 / IEEE 43 standards 
assessment on an induction motor. Analyse the results below and generate a detailed, 
specific professional diagnostic report.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MOTOR TEST INPUTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Motor Voltage Class : {check_results['motor_type']}
IR @ 1 minute       : {ir_1min} MΩ  (standard limit: >= {standards['ir_1min_limit_MΩ']} MΩ)
IR @ 10 minutes     : {ir_10min} MΩ  (standard limit: >= {standards['ir_10min_limit_MΩ']} MΩ)
DC Winding Resistance: {dc_resistance} Ω  (design: 0.05 Ω, acceptable: {standards['dc_resistance_min_Ω']}–{standards['dc_resistance_max_Ω']} Ω)
Vibration           : {vibration} mm/sec  (limit: < {standards['vibration_limit_mm_per_sec']} mm/sec)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STANDARDS CHECK RESULTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Check I  — IR @ 1 min     : {check_results['check1']['status']}  (measured: {ir_1min} MΩ, limit: >= {standards['ir_1min_limit_MΩ']} MΩ)
Check II — IR @ 10 min    : {check_results['check2']['status']}  (measured: {ir_10min} MΩ, limit: >= {standards['ir_10min_limit_MΩ']} MΩ)
Check III— PI = IR10/IR1  : {check_results['check3']['status']}  (PI = {pi_val}, condition: {pi_cond}, limit >= 1.2)
Check IV — DC Resistance  : {check_results['check4']['status']}  (measured: {dc_resistance} Ω, acceptable: {standards['dc_resistance_min_Ω']}–{standards['dc_resistance_max_Ω']} Ω)
Check V  — Vibration      : {check_results['check5']['status']}  (measured: {vibration} mm/sec, limit < 3.0 mm/sec)

Overall Result: {overall['status']}
Failed Checks : {overall['fail_count']} out of 5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RECOMMENDATIONS FROM STANDARDS ENGINE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{chr(10).join(f"- {r}" for r in overall['recommendations'])}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Based on these SPECIFIC values, write a professional diagnostic report with:

1. EXECUTIVE SUMMARY
   - State the overall health clearly
   - Mention the specific measured values that are good or bad
   - Be specific, not generic

2. DETAILED ANALYSIS OF EACH CHECK
   - Explain what each measured value means physically for THIS motor
   - Compare each value to the standard limit
   - Explain the engineering significance

3. ROOT CAUSE ANALYSIS
   - Based on the pattern of failures (if any), identify the most likely root cause
   - Explain the relationship between different failed parameters

4. MAINTENANCE RECOMMENDATIONS
   - Numbered, prioritised, specific actions
   - Include urgency level (Immediate / Within 1 week / Scheduled)

5. RETURN TO SERVICE CRITERIA
   - What exact values need to be achieved before this motor can be run

Make the report specific to the values given — do NOT give generic answers.
"""

    # ── Step 4: Call Gemini AI ────────────────────────────────────────────────
    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.3,
            max_output_tokens=2048,
        )
    )

    ai_report = response.text

    return {
        "check_results": check_results,
        "standards"    : standards,
        "ai_report"    : ai_report
    }