def assess_motor(voltage_kv, ir_1min, ir_10min, dc_resistance, vibration):

    results = {}
    recommendations = []
    DESIGN_DC = 0.05
    TOLERANCE = 0.10

    ir_threshold = 1.5 if voltage_kv <= 1.0 else 6.5
    motor_type   = "415V (LT)" if voltage_kv <= 1.0 else "6.6kV (HT)"
    results["motor_type"] = motor_type

    # Check I
    c1 = ir_1min >= ir_threshold
    results["check1"] = {"name": "IR @ 1 min", "measured": ir_1min,
                         "limit": f">= {ir_threshold} MΩ", "status": "PASS" if c1 else "FAIL", "unit": "MΩ"}
    if not c1:
        recommendations.append("IR @ 1 min is LOW. Dry out winding, check for moisture or contamination.")

    # Check II
    c2 = ir_10min >= ir_threshold
    results["check2"] = {"name": "IR @ 10 min", "measured": ir_10min,
                         "limit": f">= {ir_threshold} MΩ", "status": "PASS" if c2 else "FAIL", "unit": "MΩ"}
    if not c2:
        recommendations.append("IR @ 10 min is LOW. Schedule hipot test, consider rewinding.")

    # Check III — PI
    pi = round(ir_10min / ir_1min, 3) if ir_1min > 0 else 0
    c3 = pi >= 1.2
    if pi < 1.0:       pi_cond = "DANGEROUS"
    elif pi < 1.2:     pi_cond = "QUESTIONABLE"
    elif pi < 2.0:     pi_cond = "FAIR"
    elif pi < 4.0:     pi_cond = "GOOD"
    else:              pi_cond = "EXCELLENT"
    results["check3"] = {"name": "Polarisation Index (PI)", "measured": pi,
                         "limit": ">= 1.2", "status": "PASS" if c3 else "FAIL",
                         "unit": "", "pi_condition": pi_cond}
    if not c3:
        recommendations.append(f"PI = {pi} ({pi_cond}). Perform drying cycle, retest.")

    # Check IV
    dc_upper = round(DESIGN_DC * (1 + TOLERANCE), 4)
    dc_lower = round(DESIGN_DC * (1 - TOLERANCE), 4)
    c4 = dc_lower <= dc_resistance <= dc_upper
    results["check4"] = {"name": "DC Winding Resistance", "measured": dc_resistance,
                         "limit": f"{dc_lower} – {dc_upper} Ω", "status": "PASS" if c4 else "FAIL", "unit": "Ω"}
    if not c4:
        recommendations.append("DC resistance out of range. Check connections and winding integrity.")

    # Check V
    c5 = vibration < 3.0
    results["check5"] = {"name": "Vibration", "measured": vibration,
                         "limit": "< 3.0 mm/sec", "status": "PASS" if c5 else "FAIL", "unit": "mm/sec"}
    if not c5:
        recommendations.append("Vibration HIGH. Check balance, bearings, alignment, foundation.")

    # Overall
    fails = sum(1 for c in ["check1","check2","check3","check4","check5"]
                if results[c]["status"] == "FAIL")
    if   fails == 0: overall = "HEALTHY ✅";  msg = "Motor passes all checks. Safe to operate."
    elif fails == 1: overall = "MARGINAL ⚠️"; msg = "Minor issues found. Monitor and address."
    else:            overall = "CRITICAL ❌";  msg = "Multiple failures. Do NOT operate."

    results["overall"] = {"status": overall, "message": msg, "fail_count": fails,
                          "recommendations": recommendations or ["No action required."]}
    return results