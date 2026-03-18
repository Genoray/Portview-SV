# (NSE-Z01) Network Security Enclosure

Document ID: `NSE-Z01`
Product: `Portview`
Document Status: `Released`

## Document Approval

| By | Title | Name | Sign |
| --- | --- | --- | --- |
| Prepared | Manager | `S. R. Lim` |  |
| Reviewed | General Manager | `S. I. Choi` |  |
| Approved | CTO (Director) | `K. Y. Ro` |  |

## Revision History

| Rev. | Author | Description | Date |
| --- | --- | --- | --- |
| `0.0` | `S. R. Lim` | Initial creation according to verification item subdivision | `2025-01-08` |

## 1. Verification And Validation

This document was prepared to guarantee that this network security function requirement meets its verification and validation expected criteria.

## 2. Roles

| Role | Name |
| --- | --- |
| Documentation Software Designer | `S. R. Lim` |
| Hazard Analysis Product Manager | `S. I. Choi` |

## 3. Test Case And Result

| Item | Action | Criteria | Result | Verdict |
| --- | --- | --- | --- | --- |
| Enclosure #1 | Configure device security measures | Ensure the system can protect core functions during a cybersecurity breach using device security features. | | `PASS` |
| Enclosure #2 | Automatic logoff | Ensure the system logs off automatically after designated minutes. | | `PASS` |
| Enclosure #3 | Run antivirus and anti-malware scans | Ensure no viruses or malware are detected. | | `PASS` |
| Enclosure #4 | Configure Firewall and Network Protection | Ensure the manufacturer provides defined response actions for detecting cybersecurity threats and communicates relevant information to the end user. | | `PASS` |
| Enclosure #5 | Check operation log | Check the log for device status and every command such as register patient, create data, delete data, etc. | Verified | `PASS` |
| Enclosure #6 | Integrity check during installation | After modifying the software installer, check the error message when running the installer. | | `PASS` |
| Enclosure #7 | PC unable to communicate with sensor unless Portview is installed | Prepare a P4 machine set and a PC without Portview. Connect the P4 machine set to the PC. | Nothing happened. | `PASS` |
| Enclosure #8 | Verify software version | Ensure the correct version information is displayed. | | `PASS` |
| Enclosure #9 | Windows OS saves personal data with 256-bit AES-CBC encryption | Ensure personal data is protected when safety-sensitive data is saved or transported. | Personal Data Encryption (Microsoft Learn) | `PASS` |
| Enclosure #10 | Use checksum to validate data | Ensure threat control process for the confidentials against field message corruption or secured key corruption. | | `PASS` |

