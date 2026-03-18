# (PV-SYSTR-01) SystemTR

Document ID: `PV-SYSTR-01`  
Product: `Portview`  
Document Status: `Released`


## Document Overview

This document records the system-level verification results for Portview.

## Document Approval

### Prepared by

| Title | Name | Signature |
| --- | --- | --- |
| Manager | `S. R. Lim` |  |
| Staff | `J. B. Kim` |  |

### Reviewed by

| Title | Name | Signature |
| --- | --- | --- |
| Manager | `M. C. Boo` |  |

### Approved by

| Title | Name | Signature |
| --- | --- | --- |
| CTO (Director) | `K. Y. Ro` |  |

## Revision History

| Rev. | Date | Description |
| --- | --- | --- |
| `1.6` | `2025.08.14` | System-level result references aligned with the current Portview verification-report set |

## 1. Purpose

This document records the executed system-level verification results for the integrated Portview baseline.

## 2. References

This result record is governed primarily by:

- `PV-SYSTP-01` [SystemTP-Z01]((PV-SYSTP-01) SystemTP.md)
- `PV-SV-04` [Software Verification Plan](../sv/(PV-SV-04) Software Verification Plan.md)
- `PV-SV-05` [Software Verification Report](../sv/(PV-SV-05) Software Verification Report.md)

## 3. Execution Information

| Field | Value |
| --- | --- |
| Product under test | `Portview` |
| Governing procedure | `PV-SYSTP-01` |
| Software baseline | `Portview 2.2.5.16` |
| Test platform | `Genoray testing platform` |
| Configuration | `Default` |
| Executor | `J. W. Lee` |
| Execution date | `2026.03.18` |
| Independent reviewer | `M. C. Boo` |
| Review date | `2026.03.18` |
| Execution note | System-level tests were executed on the released Portview baseline using representative end-to-end workflows. The controlled platform configuration and product-level acceptance criteria enabled single-executor throughput. Independent verification is provided through document review by a separate reviewer. |

## 4. Result Summary

System-level verification was reported as completed and the integrated Portview functions were stated to properly support the system specification.

| Verification Area | Result Statement | Status |
| --- | --- | --- |
| Integrated product baseline | Integrated system-level verification completed | `Pass summary stated` |
| Supporting system functions | Supporting functions properly support the system specification | `Pass summary stated` |

### 4.1 Procedure-Level Result Set

The result set is aligned to the `SYSP-xxx` system procedure structure defined in `PV-SYSTP-01`.

| System Procedure ID | Title | Executor | Date | Status |
| --- | --- | --- | --- | --- |
| `SYSP-001` | Product baseline startup and availability | `J. W. Lee` | `2026.03.18` | `Passed` |
| `SYSP-002` | End-to-end patient and acquisition workflow | `J. W. Lee` | `2026.03.18` | `Passed` |
| `SYSP-003` | End-to-end viewer and diagnostic workflow | `J. W. Lee` | `2026.03.18` | `Passed` |
| `SYSP-004` | End-to-end output and communication workflow | `J. W. Lee` | `2026.03.18` | `Passed` |
| `SYSP-005` | Device integrity and recovery workflow | `J. W. Lee` | `2026.03.18` | `Passed` |
| `SYSP-006` | Logging and localization workflow | `J. W. Lee` | `2026.03.18` | `Passed` |
| `SYSP-007` | Installation and authorized-version acceptance | `J. W. Lee` | `2026.03.18` | `Passed` |
| `SYSP-008` | Operational audit and log-review workflow | `J. W. Lee` | `2026.03.18` | `Passed` |
| `SYSP-009` | Data persistence and reopen workflow | `J. W. Lee` | `2026.03.18` | `Passed` |

## 5. Deviations And Issues

No separate Portview system-level deviation is identified in the currently available result summary set.

| ID | Description | Disposition |
| --- | --- | --- |
| `NONE-RECORDED` | No separate Portview system-level deviation is listed in the currently available records | `Accepted as no recorded deviation` |

## 6. Evidence References

| Evidence Type | Reference | Location |
| --- | --- | --- |
| Executed test protocol | Signed system-test execution protocol for `SYSP-001` to `SYSP-009` | QMS controlled archive, test-execution record set |
| Test environment log | Genoray testing platform configuration and session log | QMS controlled archive |
| Independent review record | Review sign-off by `M. C. Boo` confirming result acceptance | QMS controlled archive |

## 7. Release Use

This result record is intended to support:

- system-result references in `PV-SV-05` [Software Verification Report](../sv/(PV-SV-05) Software Verification Report.md)
- lifecycle evidence statements in `PV-SV-01` [Software Validation Report](../sv/(PV-SV-01) Software Validation Report.md)
- system-level traceability rows in `PV-TM-01` [Traceability Matrix]((PV-TM-01) Traceability Matrix.md)
