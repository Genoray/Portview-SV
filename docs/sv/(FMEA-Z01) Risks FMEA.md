# (FMEA-Z01) Portview Risks FMEA

Document ID: `FMEA-Z01`
Product: `Portview`
Document Status: `Released`

## Document Approval

### Prepared by

| Title | Name | Signature |
| --- | --- | --- |
| Manager | `S. R. Lim` |  |

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
| `0.0` | `2025-01-08` | Initial creation |

## 1. Purpose

This document records the Failure Mode and Effects Analysis (FMEA) for the Portview software, covering foreseeable hazardous situations, severity ratings, risk controls, acceptability determinations, and traceability to verification evidence.

## 2. Risk Scoring Method

| Factor | Scale | Description |
| --- | --- | --- |
| Severity (S) | 1–2 | 1 = temporary discomfort or delayed diagnosis; 2 = re-exposure to radiation |
| Occurrence (O) | 1–3 | 1 = unlikely; 2 = occasional; 3 = frequent |
| Risk Priority (RP) | S x O | 1–2 = acceptable; 3–4 = acceptable with controls; 5–6 = unacceptable |

## 3. Risk Identification And Control

### 3.1 Device Linkage And Display

| ID | Title | Harm | Risk Control |
| --- | --- | --- | --- |
| `FMEA-001` | Device linkage status not visible | Delayed diagnosis | Device status indicator with real-time connection monitoring |
| `FMEA-002` | Viewer cannot display images | Delayed diagnosis | Image load verification with error fallback display |
| `FMEA-003` | Install on outside-spec PC | Delayed diagnosis | Installation requirement check and version display |

### 3.2 Version And Audit

| ID | Title | Harm | Risk Control |
| --- | --- | --- | --- |
| `FMEA-004` | Audit not possible due to incomplete logs | Temporary discomfort | Automated activity logging for all auditable operations |
| `FMEA-005` | Unauthorized version update | Temporary discomfort | Controlled installation with version identification |

### 3.3 Data Security

| ID | Title | Harm | Risk Control |
| --- | --- | --- | --- |
| `FMEA-006` | Leakage or forgery of transmitted data | Re-exposure to radiation | P2P-only transmission; AES-CBC encryption; network access limited to approved interfaces |

### 3.4 Image Processing And Calibration

| ID | Title | Harm | Risk Control |
| --- | --- | --- | --- |
| `FMEA-007` | Image processing module failure | Delayed diagnosis | Error detection with user-visible message; viewer fallback to unprocessed image |
| `FMEA-008` | Inaccurate calibration data | Delayed diagnosis | Calibration metadata preserved in TII; validated on image load |

### 3.5 Device And Driver

| ID | Title | Harm | Risk Control |
| --- | --- | --- | --- |
| `FMEA-009` | Sensor driver removed during reinstallation | Delayed diagnosis | Installation preserves driver; error message on absence |
| `FMEA-010` | Third-party program connection error | Temporary discomfort | Device selection UI with connection-state feedback |
| `FMEA-015` | Driver not installed or device connection invalid | Delayed diagnosis | Device-status monitoring with connection-state indicator |

### 3.6 Output And Communication

| ID | Title | Harm | Risk Control |
| --- | --- | --- | --- |
| `FMEA-011` | CD burning error | Temporary discomfort | Media availability check; user-visible error on failure |
| `FMEA-012` | Image export storage error | Service delay | Target path validation; error message on storage failure |
| `FMEA-013` | DICOM printer network error | Temporary discomfort | DICOM connection check; user-visible error on network failure |
| `FMEA-014` | Image processing error in acquired image | Delayed diagnosis | Image load validation; error display on processing failure |

### 3.7 Annotation

| ID | Title | Harm | Risk Control |
| --- | --- | --- | --- |
| `FMEA-016` | Annotations display improperly | Temporary discomfort | Annotation rendering validation; persistent storage in managed file structure |

### 3.8 Patient Management

| ID | Title | Harm | Risk Control |
| --- | --- | --- | --- |
| `FMEA-017` | Fail to open patient information | Temporary discomfort | Input validation; error message on invalid data or access failure |
| `FMEA-018` | Patient search failure (special characters) | Temporary discomfort | Input sanitization; controlled search query handling |
| `FMEA-019` | Patient information not opened despite selection | Temporary discomfort | Database record validation; error handling on open failure |
| `FMEA-020` | Fail to register patient | Temporary discomfort | Field validation; duplicate-check; error on registration failure |

### 3.9 Sensor Malfunction

| ID | Title | Harm | Risk Control |
| --- | --- | --- | --- |
| `FMEA-021` | Sensor malfunction prevents image acquisition | Re-exposure to radiation | Sensor error detection with user-visible message; workflow blocked until operator acknowledges; prevents repeated exposure |

## 4. Risk Scoring And Verification

### 4.1 Device Linkage And Display

| ID | S | O (pre) | RP (pre) | O (post) | RP (post) | Acceptable | Verification |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `FMEA-001` | `1` | `2` | `2` | `1` | `1` | `yes` | `PV-TR-01` / `ITP-012` |
| `FMEA-002` | `1` | `2` | `2` | `1` | `1` | `yes` | `PV-TR-01` / `ITP-013` |
| `FMEA-003` | `1` | `1` | `1` | `1` | `1` | `yes` | `PV-SYSTR-01` / `SYSP-007` |

### 4.2 Version And Audit

| ID | S | O (pre) | RP (pre) | O (post) | RP (post) | Acceptable | Verification |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `FMEA-004` | `1` | `2` | `2` | `1` | `1` | `yes` | `PV-TR-01` / `ITP-035`; Cybersecurity no 8 |
| `FMEA-005` | `1` | `1` | `1` | `1` | `1` | `yes` | `PV-SYSTR-01` / `SYSP-007`; Cybersecurity no 3 |

### 4.3 Data Security

| ID | S | O (pre) | RP (pre) | O (post) | RP (post) | Acceptable | Verification |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `FMEA-006` | `2` | `2` | `4` | `1` | `2` | `yes` | Cybersecurity no 2; `PV-TR-01` / `ITP-034`; `NSE-Z01` #9 |

### 4.4 Image Processing And Calibration

| ID | S | O (pre) | RP (pre) | O (post) | RP (post) | Acceptable | Verification |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `FMEA-007` | `1` | `2` | `2` | `1` | `1` | `yes` | `PV-TR-01` / `ITP-013` to `ITP-021` |
| `FMEA-008` | `1` | `1` | `1` | `1` | `1` | `yes` | `PV-TR-01` / `ITP-008` |

### 4.5 Device And Driver

| ID | S | O (pre) | RP (pre) | O (post) | RP (post) | Acceptable | Verification |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `FMEA-009` | `1` | `1` | `1` | `1` | `1` | `yes` | `PV-SYSTR-01` / `SYSP-007` |
| `FMEA-010` | `1` | `1` | `1` | `1` | `1` | `yes` | `PV-TR-01` / `ITP-007` |
| `FMEA-015` | `1` | `2` | `2` | `1` | `1` | `yes` | `PV-TR-01` / `ITP-007` to `ITP-012` |

### 4.6 Output And Communication

| ID | S | O (pre) | RP (pre) | O (post) | RP (post) | Acceptable | Verification |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `FMEA-011` | `1` | `1` | `1` | `1` | `1` | `yes` | `PV-TR-01` / `ITP-029` |
| `FMEA-012` | `1` | `1` | `1` | `1` | `1` | `yes` | `PV-TR-01` / `ITP-006`, `ITP-029` |
| `FMEA-013` | `1` | `2` | `2` | `1` | `1` | `yes` | `PV-TR-01` / `ITP-028`, `ITP-030` |
| `FMEA-014` | `1` | `2` | `2` | `1` | `1` | `yes` | `PV-TR-01` / `ITP-013` to `ITP-021` |

### 4.7 Annotation

| ID | S | O (pre) | RP (pre) | O (post) | RP (post) | Acceptable | Verification |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `FMEA-016` | `1` | `1` | `1` | `1` | `1` | `yes` | `PV-TR-01` / `ITP-022` to `ITP-026` |

### 4.8 Patient Management

| ID | S | O (pre) | RP (pre) | O (post) | RP (post) | Acceptable | Verification |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `FMEA-017` | `1` | `2` | `2` | `1` | `1` | `yes` | `PV-TR-01` / `ITP-002`, `ITP-004`; Cybersecurity no 1, 7 |
| `FMEA-018` | `1` | `1` | `1` | `1` | `1` | `yes` | `PV-TR-01` / `ITP-004`; Cybersecurity no 1, 7 |
| `FMEA-019` | `1` | `1` | `1` | `1` | `1` | `yes` | `PV-TR-01` / `ITP-002`, `ITP-004`; Cybersecurity no 1, 7 |
| `FMEA-020` | `1` | `1` | `1` | `1` | `1` | `yes` | `PV-TR-01` / `ITP-002`; Cybersecurity no 1, 7 |

### 4.9 Sensor Malfunction

| ID | S | O (pre) | RP (pre) | O (post) | RP (post) | Acceptable | Verification |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `FMEA-021` | `2` | `2` | `4` | `1` | `2` | `yes` | `PV-TR-01` / `ITP-008`; `PV-SYSTR-01` / `SYSP-002` |

## 5. Cybersecurity Risk Integration

The following FMEA items have cybersecurity-related controls that are also addressed in `PV-CSRS-01` (SwRS for Cybersecurity). This cross-reference ensures that functional-safety FMEA and cybersecurity risk management are integrated.

| FMEA ID | Cybersecurity Checklist Item | Risk Category | Control Integration |
| --- | --- | --- | --- |
| `FMEA-004` | Checklist no 8 (audit trail) | Detect / Respond / Recover | Activity logging provides audit trail for cybersecurity event detection |
| `FMEA-005` | Checklist no 3 (trusted content) | Identify / Protect | Controlled installation prevents unauthorized software updates |
| `FMEA-006` | Checklist no 2 (block unauthorized network) | Identify / Protect | P2P-only transmission + AES-CBC encryption mitigate data leakage |
| `FMEA-017` | Checklist no 1, 7 (access control, logging) | Identify / Protect; Detect | Account management restricts access; logging enables incident detection |
| `FMEA-018` | Checklist no 1, 7 | Identify / Protect; Detect | Input sanitization prevents injection; logging tracks search failures |
| `FMEA-019` | Checklist no 1, 7 | Identify / Protect; Detect | Database validation prevents unauthorized access to patient records |
| `FMEA-020` | Checklist no 1, 7 | Identify / Protect; Detect | Field validation + duplicate check prevent data integrity compromise |

The cybersecurity essentials checklist in `PV-CSRS-01` Section 5.1 provides the detailed control requirements and verification mapping for these items. Network security enclosure testing (`NSE-Z01`) provides additional evidence for FMEA-006.

## 6. Summary

- 21 risk items identified (`FMEA-001` through `FMEA-021`)
- Severity ratings: 19 items at severity `1`, 2 items at severity `2` (`FMEA-006`, `FMEA-021`)
- Pre-control RP range: `1` to `4`; post-control RP range: `1` to `2`
- All items assessed as acceptable after risk controls applied
- Severity `2` items (radiation re-exposure) reduced from RP `4` to RP `2` through specific controls
- All records reference Portview-controlled verification documents only
