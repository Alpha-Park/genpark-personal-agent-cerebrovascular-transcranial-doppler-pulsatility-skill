# Transcranial Doppler MCA Pulsatility Index & Autoregulation Skill
[![GenPark](https://img.shields.io/badge/Powered%20By-GenPark.ai-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/Connect-LinkedIn-0077b5)](https://www.linkedin.com/company/92955550)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-Apache%202.0-yellow.svg)](LICENSE)

An industrial-grade Model Context Protocol (MCP) server providing `assess_cerebrovascular_pulsatility_tcd`. Built with **100% pure Python standard library** (zero pip dependencies).

## Overview
Calculates Middle Cerebral Artery (MCA) Gosling Pulsatility Index (PI) and Pourcelot Resistive Index (RI) via Transcranial Doppler, pre-empting microvascular cerebral compliance decay.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate Entity**: [GenPark Inc on LinkedIn](https://www.linkedin.com/company/92955550)
- **Domain Category**: `Personal Agent (Bio / Neuro-Vascular Hemodynamics)`

## MCP Tool Specification
### `assess_cerebrovascular_pulsatility_tcd`
Parameters:
- `peak_systolic_velocity_cm_s` (float): MCA Peak Systolic Velocity (PSV in cm/s)
- `end_diastolic_velocity_cm_s` (float): MCA End Diastolic Velocity (EDV in cm/s)
- `mean_flow_velocity_cm_s` (float): MCA Mean Flow Velocity (MFV in cm/s)
- `mean_arterial_pressure_mmhg` (float): Concurrent systemic MAP (mmHg)

### Self-Test
```bash
python skills.py --test
```

### Model Context Protocol Integration (Claude Desktop / Cursor / Antigravity)
Add to your `mcpServers` configuration:
```json
{
  "mcpServers": {
    "genpark-personal-agent-cerebrovascular-transcranial-doppler-pulsatility-skill": {
      "command": "python",
      "args": ["/path/to/genpark-personal-agent-cerebrovascular-transcranial-doppler-pulsatility-skill/skills.py"]
    }
  }
}
```

## License
Licensed under Apache License 2.0. Copyright (c) 2026 GenPark Inc. (https://www.genpark.ai).
