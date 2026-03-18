# (PV-STR-01) SwSTR

Document ID: `PV-STR-01`  
Product: `Portview`  
Document Status: `Released`

## Document Overview

This document records the unit-level verification results for Portview.

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
| `0.0` | `2024-01-17` | Initial unit result record prepared according to verification-item subdivision |
| `0.1` | `2025.07.24` | Unit result set updated with GUI translation-related verification coverage |

## 1. Purpose

This document records the executed unit verification results for Portview and provides the evidence summary associated with the unit procedure baseline.

## 2. References

This result record is governed primarily by:

- `PV-SRS-01` [SwSRS for Portview]((PV-SRS-01) SwSRS.md)
- `PV-STP-01` [SwSTP for Portview]((PV-STP-01) SwSTP.md)
- `PV-SV-04` [Software Verification Plan](../sv/(PV-SV-04) Software Verification Plan.md)
- `PV-SV-05` [Software Verification Report](../sv/(PV-SV-05) Software Verification Report.md)

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
| Governing procedure | `PV-STP-01` |

## 4. Result Coverage

The unit result record covers the following authored unit procedures.

| Procedure Range | Coverage |
| --- | --- |
| `UTP-001` to `UTP-005`, `UTP-018` to `UTP-022` | Acquisition and device access |
| `UTP-006` to `UTP-012` | Viewer and image interaction |
| `UTP-013` to `UTP-017` | Output and communication |
| `UTP-023` to `UTP-025` | Administrative and support functions |

## 5. Result Summary

The unit verification activities were executed against the released Portview unit baseline and were reported as successfully completed.

| Area | Result Statement | Status |
| --- | --- | --- |
| Acquisition and device access | Unit-level acquisition and device actions were executed successfully | `Pass summary stated` |
| Viewer and image interaction | Unit-level viewer interactions were reported as acceptable | `Pass summary stated` |
| Output and communication | Unit-level output and communication actions were reported as acceptable | `Pass summary stated` |
| Administrative and support functions | Unit-level support and administrative actions were reported as acceptable | `Pass summary stated` |

### 5.1 Procedure-Level Result Set

The current authored result set is aligned to the `UTP-xxx` unit procedure structure defined in `PV-STP-01`.

| Unit Procedure ID | Title | Result Summary | Status | Notes |
| --- | --- | --- | --- | --- |
| `UTP-001` | Acquire intraoral sensor image | Unit sensor acquisition was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `UTP-002` | Acquire image from file | File import at unit level was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `UTP-003` | Acquire image from TWAIN device | TWAIN unit behavior was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `UTP-004` | Show status of device | Device-status behavior was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `UTP-005` | Select device | Device selection behavior was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `UTP-006` | Main-window behavior | Main-window behavior was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `UTP-007` | Tooth map window | Tooth-map behavior was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `UTP-008` | Compare image display | Compare-view behavior was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `UTP-009` | Pan behavior | Pan interaction was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `UTP-010` | Zoom behavior | Zoom interaction was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `UTP-011` | Rotate behavior | Rotate behavior was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `UTP-012` | Thumbnail viewer | Thumbnail-view behavior was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `UTP-013` | Print image | Standard print behavior was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `UTP-014` | Transmit to DICOM printer | DICOM-print behavior was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `UTP-015` | Export image to file | File export behavior was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `UTP-016` | Export images to CD | Media export behavior was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `UTP-017` | Send image to DICOM server | DICOM-send behavior was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `UTP-018` | FMX continuous acquisition | FMX continuous acquisition behavior was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `UTP-019` | Multi-sensor selection | Multi-sensor selection behavior was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `UTP-020` | Sensor status | Sensor-status behavior was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `UTP-021` | USB integrity check | USB integrity behavior was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `UTP-022` | Local-network connection check | Network-dependent unit behavior was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `UTP-023` | Logging | Logging behavior was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `UTP-024` | Patient management | Patient-management behavior was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |
| `UTP-025` | GUI translation | GUI translation behavior was reported as acceptable | `Pass summary claimed` | Detailed execution note to add if separately controlled |

## 6. Deviations And Issues

No Portview-specific unit deviation is separately listed in the current result set.

| ID | Description | Disposition |
| --- | --- | --- |
| `NONE-RECORDED` | No separate Portview unit deviation is recorded in the current result summary set | `Accepted as no recorded deviation` |

## 7. Evidence References

| Evidence Type | Reference | Location |
| --- | --- | --- |
| Executed test protocol | Signed unit-test execution protocol for `UTP-001` to `UTP-025` | QMS controlled archive, test-execution record set |
| Test environment log | Genoray testing platform configuration and session log | QMS controlled archive |
| Independent review record | Review sign-off by `M. C. Boo` confirming result acceptance | QMS controlled archive |

## 8. Traceability Use

This result record is intended to support:

- unit-result linkage in `PV-TM-01` [Traceability Matrix]((PV-TM-01) Traceability Matrix.md)
- unit-result references in `PV-SV-05` [Software Verification Report](../sv/(PV-SV-05) Software Verification Report.md)
- release-support statements in `PV-SV-01` [Software Validation Report](../sv/(PV-SV-01) Software Validation Report.md)
