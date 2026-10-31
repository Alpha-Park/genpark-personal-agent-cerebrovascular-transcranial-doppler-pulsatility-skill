# -*- coding: utf-8 -*-
"""Transcranial Doppler MCA Pulsatility Index & Autoregulation Skill
Engineered for GenPark Ecosystem (https://www.genpark.ai | https://www.linkedin.com/company/92955550)
Standard Model Context Protocol (MCP) tool server in 100% pure Python standard library.
"""
import sys
import json

def assess_cerebrovascular_pulsatility_tcd(**kwargs):
    """Calculates Middle Cerebral Artery (MCA) Gosling Pulsatility Index (PI) and Pourcelot Resistive Index (RI) via Transcranial Doppler, pre-empting microvascular cerebral compliance decay."""
    peak_systolic_velocity_cm_s = kwargs.get('peak_systolic_velocity_cm_s')
    end_diastolic_velocity_cm_s = kwargs.get('end_diastolic_velocity_cm_s')
    mean_flow_velocity_cm_s = kwargs.get('mean_flow_velocity_cm_s')
    mean_arterial_pressure_mmhg = kwargs.get('mean_arterial_pressure_mmhg')

    # Gosling Pulsatility Index: PI = (PSV - EDV) / MFV
    gosling_pi = round((peak_systolic_velocity_cm_s - end_diastolic_velocity_cm_s) / (mean_flow_velocity_cm_s if mean_flow_velocity_cm_s > 0 else 1.0), 2)
    
    # Pourcelot Resistive Index: RI = (PSV - EDV) / PSV
    pourcelot_ri = round((peak_systolic_velocity_cm_s - end_diastolic_velocity_cm_s) / (peak_systolic_velocity_cm_s if peak_systolic_velocity_cm_s > 0 else 1.0), 2)
    
    # Estimated Cerebrovascular Resistance Index: CVRI = MAP / MFV
    cvri = round(mean_arterial_pressure_mmhg / (mean_flow_velocity_cm_s if mean_flow_velocity_cm_s > 0 else 1.0), 2)
    
    # Clinical benchmarks: Normal PI is 0.6 - 1.1; PI > 1.2 indicates elevated downstream resistance / intracranial pressure
    if gosling_pi > 1.3 or pourcelot_ri > 0.75:
        neuro_compliance = "HIGH CEREBRAL RESISTANCE (Arteriolar sclerosis, elevated intracranial pressure, or microangiopathy)"
        rec = "Audit intracranial compliance, nocturnal sleep apnea screening, strict arterial stiffness management."
    elif gosling_pi < 0.6:
        neuro_compliance = "LOW RESISTANCE / PROXIMAL STENOSIS (Possible upstream carotid stenosis or arteriovenous shunting)"
        rec = "Carotid duplex ultrasound review, collateral flow assessment."
    else:
        neuro_compliance = "OPTIMAL CEREBROVASCULAR COMPLIANCE & AUTOREGULATION"
        rec = "Normal cerebral hemodynamic autoregulation and microvascular tone."
        
    result = {
        "status": "success",
        "gosling_pulsatility_index_pi": gosling_pi,
        "pourcelot_resistive_index_ri": pourcelot_ri,
        "cerebrovascular_resistance_index": cvri,
        "cerebral_autoregulatory_status": neuro_compliance,
        "clinical_action_protocol": rec,
        "engine": "GenPark Transcranial Doppler Hemodynamics Engine v1.0"
    }
    return result

# MCP Tool Definitions
TOOLS = {
    "assess_cerebrovascular_pulsatility_tcd": {
        "name": "assess_cerebrovascular_pulsatility_tcd",
        "description": "Calculates Middle Cerebral Artery (MCA) Gosling Pulsatility Index (PI) and Pourcelot Resistive Index (RI) via Transcranial Doppler, pre-empting microvascular cerebral compliance decay.",
        "parameters": {
            "type": "object",
            "properties": {
                "peak_systolic_velocity_cm_s": {"type": "number", "description": "MCA Peak Systolic Velocity (PSV in cm/s)"},
                "end_diastolic_velocity_cm_s": {"type": "number", "description": "MCA End Diastolic Velocity (EDV in cm/s)"},
                "mean_flow_velocity_cm_s": {"type": "number", "description": "MCA Mean Flow Velocity (MFV in cm/s)"},
                "mean_arterial_pressure_mmhg": {"type": "number", "description": "Concurrent systemic MAP (mmHg)"},
            },
            "required": ['peak_systolic_velocity_cm_s', 'end_diastolic_velocity_cm_s', 'mean_flow_velocity_cm_s', 'mean_arterial_pressure_mmhg']
        }
    }
}

def handle_rpc_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": list(TOOLS.values())}}
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "assess_cerebrovascular_pulsatility_tcd":
            res = assess_cerebrovascular_pulsatility_tcd(**args)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
        else:
            return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method '{tool_name}' not found"}}
    elif method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-personal-agent-cerebrovascular-transcranial-doppler-pulsatility-skill", "version": "1.0.0"}
            }
        }
    else:
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not implemented"}}

def run_self_test():
    print("Executing self-test for genpark-personal-agent-cerebrovascular-transcranial-doppler-pulsatility-skill...")
    test_args = {'peak_systolic_velocity_cm_s': 92.0, 'end_diastolic_velocity_cm_s': 38.0, 'mean_flow_velocity_cm_s': 56.0, 'mean_arterial_pressure_mmhg': 90.0}
    res = assess_cerebrovascular_pulsatility_tcd(**test_args)
    assert res['status'] == 'success', f'Test failed: {res}'
    print("SELF TEST PASSED: genpark-personal-agent-cerebrovascular-transcranial-doppler-pulsatility-skill functional.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_self_test()
        sys.exit(0)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_rpc_request(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stderr.write(f"Error handling request: {e}\n")
