# AGENTS.Concerns.md

This file records known compliance concerns that are not currently addressed in the controlled document set. These items should be reviewed before regulatory submission.

## 1. Execution Evidence Not Embedded

All verification result documents (`STR-603`, `TR-603`, `SystemTR-603`) record pass/fail status at summary level. No detailed execution evidence (test logs, screenshots, signed step-by-step protocols) is embedded or formally cross-referenced from the controlled document set.

**Risk**: An auditor may request objective evidence that each test procedure was actually executed. The current documents are self-declarations.

**Mitigation options**:
- Attach test-execution logs as appendices or linked controlled records
- Reference a controlled test-management system (e.g., Polarion, TestRail) with traceable execution IDs
- Maintain signed paper-based test protocols in the quality-system archive and reference their controlled identifiers

## 2. Single Executor Throughput

`J. W. Lee` is recorded as the sole executor for 25 unit tests, 36 integration tests, and 9 system tests (70 total). Unit and integration tests share the same execution date (`2025.07.24`). System tests are dated `2026.03.18`.

**Risk**: An auditor may question whether one person can realistically execute 61 tests in a single day, and whether independent verification principles are met.

**Current mitigation**: Independent reviewer (`M. C. Boo`) is recorded in each result document's Execution Information section. Document approval includes a separate Reviewed By signatory.

**Additional options if challenged**:
- Document that test execution leverages pre-configured automated or semi-automated test environments
- Provide evidence that tests were executed over multiple sessions with the same formal sign-off date
- Add a second executor for a subset of tests to demonstrate independence

## 3. External Document References Removed

The following external documents were previously referenced in `FMEA-603` and have been removed to keep the controlled document set self-contained:

| Removed Reference | Original Context |
| --- | --- |
| `lpTR-Z01` (IP System Test Report) | Image processing verification for FMEA-007, FMEA-008, FMEA-014 |
| `UEF-Z01` (Usability Engineering File) | Usability task verification for FMEA-005, FMEA-015, FMEA-016, FMEA-020 |
| `UM-Z01` (User Manual) | Error-message verification for multiple FMEA items |
| `SM-603` (Software Manual) | Data security reference for FMEA-006 |
| `F715-1` (Outsourcing Supplier Evaluation) | Sensor hardware quality for FMEA-021 |

**Risk**: If an auditor traces FMEA records back to their original verification evidence, the removed references may raise questions about completeness of risk-control verification.

**Mitigation**: FMEA items now reference equivalent Portview-controlled verification procedures (`TR-603`, `SystemTR-603`, `NSE-603`). If the original external documents are needed, they remain available as controlled records in the company quality-management system.
