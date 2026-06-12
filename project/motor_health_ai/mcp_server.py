"""
mcp_server.py
MCP Server with HTTP transport — works with MCP Inspector
Run: python mcp_server.py
Then connect Inspector to: http://localhost:8000/mcp
"""

from mcp.server.fastmcp import FastMCP
from motor_checker import assess_motor

mcp = FastMCP("Motor Health Assessment", host="0.0.0.0", port=8000)

@mcp.tool()
def check_motor_health(
    voltage_kv: float,
    ir_1min: float,
    ir_10min: float,
    dc_resistance: float,
    vibration: float
) -> dict:
    """
    Run IS 900 / IEEE 43 standards checks on induction motor readings.

    Args:
        voltage_kv    : Motor voltage in kV — use 0.415 for 415V, 6.6 for 6.6kV
        ir_1min       : Insulation Resistance at 1 minute in MΩ
        ir_10min      : Insulation Resistance at 10 minutes in MΩ
        dc_resistance : Measured DC winding resistance in Ω (design = 0.05 Ω)
        vibration     : Vibration reading in mm/sec

    Returns:
        Full standards check results with PASS/FAIL for all 5 checks,
        Polarisation Index, and maintenance recommendations.
    """
    return assess_motor(voltage_kv, ir_1min, ir_10min, dc_resistance, vibration)

@mcp.tool()
def get_motor_standards(voltage_kv: float) -> dict:
    """
    Get IS 900 / IEEE 43 standard limits for a given motor voltage class.

    Args:
        voltage_kv: Motor voltage in kV (0.415 or 6.6)

    Returns:
        All standard limits and thresholds
    """
    ir_threshold = 1.5 if voltage_kv <= 1.0 else 6.5
    motor_type   = "415V (LT)" if voltage_kv <= 1.0 else "6.6kV (HT)"
    return {
        "motor_type"                : motor_type,
        "ir_1min_limit_MΩ"          : ir_threshold,
        "ir_10min_limit_MΩ"         : ir_threshold,
        "pi_minimum"                : 1.2,
        "dc_resistance_design_Ω"    : 0.05,
        "dc_resistance_min_Ω"       : 0.045,
        "dc_resistance_max_Ω"       : 0.055,
        "vibration_limit_mm_per_sec": 3.0,
        "standards"                 : ["IS 900", "IEEE 43", "IS 12075", "ISO 10816"]
    }

if __name__ == "__main__":
    print("Starting Motor Health Assessment MCP Server...")
    print("MCP endpoint: http://localhost:8000/mcp")
    print("Connect MCP Inspector to: http://localhost:8000/mcp")
    mcp.run(transport="streamable-http")