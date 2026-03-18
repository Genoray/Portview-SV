# (TR-603) SwTR

Document ID: `TR-603`  
Product: `Portview`  
Document Status: `Released`


## Document Overview

This document records the integration-level verification results for Portview.

## Document Approval

### Prepared by

| Title | Name | Signature |
| --- | --- | --- |
| Manager | `J. W. Lee` |  |

### Reviewed by

| Title | Name | Signature |
| --- | --- | --- |
| General Manager | `S. I. Choi` |  |

### Approved by

| Title | Name | Signature |
| --- | --- | --- |
| CTO (Director) | `K. Y. Ro` |  |

## Revision History

| Rev. | Date | Description |
| --- | --- | --- |
| `0.0` | `2024-01-22` | Initial integration result record prepared according to verification-item subdivision |
| `0.1` | `2025-07-24` | Integration result set updated with translation-related verification coverage |

## 1. Purpose

This document records the executed integration verification results for Portview and provides the evidence summary associated with the integration procedure baseline.

## 2. References

This result record is governed primarily by:

- `RS-603` [RS for Portview]((RS-603) RS.md)
- `TP-603` [SwTP for Portview]((TP-603) SwTP.md)
- `SV-603-04` [Software Verification Plan](../sv/(SV-603-04) Software Verification Plan.md)
- `SV-603-05` [Software Verification Report](../sv/(SV-603-05) Software Verification Report.md)

## 3. Execution Information

| Field | Value |
| --- | --- |
| Executor | `J. W. Lee` |
| Execution date | `2025.07.24` |
| Independent reviewer | `M. C. Boo` |
| Review date | `2025.07.24` |
| Execution note | Tests were executed using a pre-configured Genoray testing platform with standardized test data sets. The controlled test environment and procedure-level acceptance criteria enabled single-executor throughput. Independent verification is provided through document review by a separate reviewer. |
| Test location | `Genoray testing platform` |
| Configuration | `Default` |
| Software baseline | `Portview 2.2.5.16` |
| Governing procedure | `TP-603` |

## 4. Result Coverage

The integration result record covers the following authored integration procedures.

| Procedure Range | Coverage |
| --- | --- |
| `ITP-001` to `ITP-006` | Patient and data workflow |
| `ITP-007` to `ITP-012`, `ITP-031` to `ITP-034` | Device acquisition and source integration |
| `ITP-013` to `ITP-026` | Viewer and annotation workflow |
| `ITP-027` to `ITP-030` | Output and exchange workflow |
| `ITP-035` to `ITP-036` | Logging and localization |

## 5. Result Summary

The integration verification activities were executed against the released Portview integration baseline and were reported as successfully completed.

| Area | Result Statement | Status |
| --- | --- | --- |
| Patient and data workflow | Workflow actions were executed and the expected handling behavior was observed | `Pass summary stated` |
| Device acquisition and source integration | Device, source, and acquisition transitions were executed successfully | `Pass summary stated` |
| Viewer and annotation workflow | Integrated viewer and annotation actions behaved as intended | `Pass summary stated` |
| Output and exchange workflow | Print, export, and DICOM-related actions were reported as completed successfully | `Pass summary stated` |
| Logging and localization | Support and localization behaviors were reported as acceptable | `Pass summary stated` |

### 5.1 Procedure-Level Result Set

The current authored result set is aligned to the `ITP-xxx` integration procedure structure defined in `TP-603`.

| Integration Procedure ID | Title | Result Summary | Status | Notes |
| --- | --- | --- | --- | --- |
| `ITP-001` | System instability check | Integrated instability and guided-recovery behavior was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-002` | Patient registration | Patient registration workflow was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-003` | Modify patient information | Patient-modification workflow was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-004` | Patient search | Patient-search workflow was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-005` | Delete patient information | Patient-delete workflow was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-006` | Export patient information | Patient export workflow was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-007` | Select device | Integrated device-selection workflow was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-008` | Acquire intraoral sensor image | Integrated sensor-acquisition workflow was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-009` | Acquire image from digital camera | Integrated digital-camera workflow was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-010` | Acquire image from file | Integrated file-import workflow was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-011` | Acquire image from TWAIN device | Integrated TWAIN workflow was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-012` | Show status of device | Integrated device-status behavior was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-013` | Main viewer | Main-viewer workflow was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-014` | Thumbnail viewer | Thumbnail-viewer workflow was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-015` | Compare viewer | Compare-viewer workflow was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-016` | Tooth map window | Tooth-map workflow was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-017` | Pan behavior | Pan behavior in integrated workflow was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-018` | Zoom behavior | Zoom behavior in integrated workflow was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-019` | Reset | Reset behavior in integrated workflow was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-020` | Delete | Delete behavior in integrated workflow was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-021` | Rotate | Rotate behavior in integrated workflow was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-022` | Text | Text annotation workflow was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-023` | Arrow | Arrow annotation workflow was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-024` | Pencil | Pencil annotation workflow was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-025` | Angle | Angle measurement workflow was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-026` | Length | Length measurement workflow was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-027` | Print image | Integrated print workflow was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-028` | Print to DICOM printer | Integrated DICOM-print workflow was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-029` | CD burning | Integrated media workflow was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-030` | Send image to DICOM server | Integrated DICOM-send workflow was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-031` | Multi-sensor selection | Multi-sensor workflow was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-032` | Intraoral sensor FMX layout | FMX workflow was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-033` | USB integrity | USB integrity behavior was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-034` | Local-network connection check | Network-dependent integrated workflow was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-035` | Activity logging | Integrated logging behavior was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `ITP-036` | GUI translation | Integrated GUI translation behavior was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |

## 6. Deviations And Issues

No Portview-specific integration deviation is separately listed in the current result set.

| ID | Description | Disposition |
| --- | --- | --- |
| `NONE-RECORDED` | No separate Portview integration deviation is recorded in the current result summary set | `Accepted as no recorded deviation` |

## 7. Evidence References

| Evidence Type | Reference | Location |
| --- | --- | --- |
| Executed test protocol | Signed integration-test execution protocol for `ITP-001` to `ITP-036` | QMS controlled archive, test-execution record set |
| Test environment log | Genoray testing platform configuration and session log | QMS controlled archive |
| Independent review record | Review sign-off by `M. C. Boo` confirming result acceptance | QMS controlled archive |

## 8. Traceability Use

This result record is intended to support:

- integration-result linkage in `TM-603` [Traceability Matrix]((TM-603) Traceability Matrix.md)
- integration-result references in `SV-603-05` [Software Verification Report](../sv/(SV-603-05) Software Verification Report.md)
- release-support statements in `SV-603-01` [Software Validation Report](../sv/(SV-603-01) Software Validation Report.md)
