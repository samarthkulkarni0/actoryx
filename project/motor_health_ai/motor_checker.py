"""
motor_checker.py
IS 900 / IEEE 43 Standards Engine — pure logic, no AI
"""

def assess_motor(voltage_kv, ir_1min, ir_10min, dc_resistance, vibration):
    results = {}
    recommendations = []
    DESIGN_DC = 0.05
    TOLERANCE = 0.10

    ir_threshold = 1.5 if voltage_kv <= 1.0 else 6.5
    motor_type   = "415V (LT)" if voltage_kv <= 1.0 else "6.6kV (HT)"
    results["motor_type"] = motor_type

    # Check I — IR @ 1 min
    c1 = ir_1min >= ir_threshold
    results["check1"] = {"name": "IR @ 1 min (IS 900/IEEE 43)", "measured": ir_1min,
                         "limit": f">= {ir_threshold} MΩ", "status": "PASS" if c1 else "FAIL", "unit": "MΩ"}
    if not c1:
        recommendations.append(f"IR @ 1 min ({ir_1min} MΩ) is BELOW limit of {ir_threshold} MΩ — "
                                "dry out winding at 90-100°C for 8-12 hours, check for moisture or contamination.")

    # Check II — IR @ 10 min
    c2 = ir_10min >= ir_threshold
    results["check2"] = {"name": "IR @ 10 min (IS 900/IEEE 43)", "measured": ir_10min,
                         "limit": f">= {ir_threshold} MΩ", "status": "PASS" if c2 else "FAIL", "unit": "MΩ"}
    if not c2:
        recommendations.append(f"IR @ 10 min ({ir_10min} MΩ) is BELOW limit — "
                                "schedule hipot test, consider rewinding if IR doesn't improve after drying.")

    # Check III — PI
    pi = round(ir_10min / ir_1min, 3) if ir_1min > 0 else 0.0
    c3 = pi >= 1.2
    if pi < 1.0:       pi_cond = "DANGEROUS"
    elif pi < 1.2:     pi_cond = "QUESTIONABLE"
    elif pi < 2.0:     pi_cond = "FAIR"
    elif pi < 4.0:     pi_cond = "GOOD"
    else:              pi_cond = "EXCELLENT"
    results["check3"] = {"name": "Polarisation Index PI=IR10/IR1 (IEEE 43)", "measured": pi,
                         "limit": ">= 1.2", "status": "PASS" if c3 else "FAIL",
                         "unit": "", "pi_condition": pi_cond}
    if not c3:
        recommendations.append(f"PI = {pi} ({pi_cond}) — winding has moisture or aged insulation. "
                                "Perform drying cycle and retest.")

    # Check IV — DC Resistance
    dc_upper = round(DESIGN_DC * (1 + TOLERANCE), 4)
    dc_lower = round(DESIGN_DC * (1 - TOLERANCE), 4)
    c4 = dc_lower <= dc_resistance <= dc_upper
    results["check4"] = {"name": "DC Winding Resistance (±10% design)", "measured": dc_resistance,
                         "limit": f"{dc_lower} – {dc_upper} Ω", "status": "PASS" if c4 else "FAIL", "unit": "Ω"}
    if not c4:
        if dc_resistance > dc_upper:
            recommendations.append(f"DC resistance ({dc_resistance} Ω) is HIGH — "
                                    "check for loose connections, broken strands or corroded joints.")
        else:
            recommendations.append(f"DC resistance ({dc_resistance} Ω) is LOW — "
                                    "possible turn-to-turn short circuit. Perform surge comparison test.")

    # Check V — Vibration
    c5 = vibration < 3.0
    results["check5"] = {"name": "Vibration (IS 12075/ISO 10816)", "measured": vibration,
                         "limit": "< 3.0 mm/sec", "status": "PASS" if c5 else "FAIL", "unit": "mm/sec"}
    if not c5:
        recommendations.append(f"Vibration ({vibration} mm/sec) EXCEEDS limit — "
                                "check rotor balance, bearing condition, shaft alignment and foundation bolts.")

    fails = sum(1 for c in ["check1","check2","check3","check4","check5"]
                if results[c]["status"] == "FAIL")
    if   fails == 0: overall = "HEALTHY ✅";  msg = "Motor passes all checks. Safe to operate."
    elif fails == 1: overall = "MARGINAL ⚠️"; msg = "Minor issue found. Monitor and address recommendation."
    else:            overall = "CRITICAL ❌";  msg = "Multiple failures detected. Do NOT operate until rectified."

    results["overall"] = {
        "status": overall, "message": msg, "fail_count": fails,
        "recommendations": recommendations if recommendations else ["No corrective action required."]
    }
    return results