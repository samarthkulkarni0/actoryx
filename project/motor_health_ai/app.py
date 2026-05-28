import json
from flask import Flask, request, jsonify, render_template
from motor_checker import assess_motor

app = Flask(__name__)

def get_ai_analysis(motor_data, check_results):
    overall = check_results["overall"]
    recs    = overall["recommendations"]
    pi      = check_results["check3"]["measured"]
    pi_cond = check_results["check3"]["pi_condition"]
    report  = "MOTOR HEALTH DIAGNOSTIC REPORT\n"
    report += "=" * 40 + "\n\n"
    report += "1. EXECUTIVE SUMMARY\n" + "-" * 30 + "\n"
    report += f"Overall Status: {overall['status']}\n"
    report += f"{overall['message']}\n"
    report += f"Failed checks: {overall['fail_count']} out of 5\n\n"
    report += "2. DETAILED FINDINGS\n" + "-" * 30 + "\n"
    for key in ["check1","check2","check3","check4","check5"]:
        c = check_results[key]
        report += f"* {c['name']}: {c['measured']} {c['unit']} - {c['status']}\n"
        report += f"  Limit: {c['limit']}\n"
    report += f"\nPI = {pi} - Condition: {pi_cond}\n\n"
    report += "3. ROOT CAUSE ANALYSIS\n" + "-" * 30 + "\n"
    if overall["fail_count"] == 0:
        report += "No failures. Motor is in healthy condition.\n\n"
    else:
        if check_results["check1"]["status"]=="FAIL" or check_results["check2"]["status"]=="FAIL":
            report += "* Low IR: moisture ingress or insulation degradation.\n"
        if check_results["check3"]["status"]=="FAIL":
            report += "* Low PI: moisture, carbon tracking or aged insulation.\n"
        if check_results["check4"]["status"]=="FAIL":
            report += "* DC resistance deviation: loose joints or inter-turn short.\n"
        if check_results["check5"]["status"]=="FAIL":
            report += "* High vibration: rotor imbalance, bearing wear or misalignment.\n"
        report += "\n"
    report += "4. MAINTENANCE RECOMMENDATIONS\n" + "-" * 30 + "\n"
    for i, rec in enumerate(recs, 1):
        report += f"{i}. {rec}\n"
    report += "\n5. RETURN-TO-SERVICE CRITERIA\n" + "-" * 30 + "\n"
    report += "* IR @ 1 min and 10 min must meet minimum threshold\n"
    report += "* PI must be >= 1.2\n"
    report += "* DC resistance within +/-10% of 0.05 ohm\n"
    report += "* Vibration < 3.0 mm/sec\n"
    return report

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/assess", methods=["POST"])
def assess():
    try:
        data          = request.get_json()
        voltage_kv    = float(data["voltage_kv"])
        ir_1min       = float(data["ir_1min"])
        ir_10min      = float(data["ir_10min"])
        dc_resistance = float(data["dc_resistance"])
        vibration     = float(data["vibration"])
        results       = assess_motor(voltage_kv, ir_1min, ir_10min, dc_resistance, vibration)
        motor_data    = {"motor_type": results["motor_type"], "ir_1min": ir_1min,
                         "ir_10min": ir_10min, "dc_resistance": dc_resistance, "vibration": vibration}
        ai_report     = get_ai_analysis(motor_data, results)
        return jsonify({"success": True, "results": results, "ai_report": ai_report})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)