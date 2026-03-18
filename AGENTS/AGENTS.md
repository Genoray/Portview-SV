# AGENTS.md

## Scope

This workspace is used to author standalone software verification documents for `Portview`.
All controlled documents are in `docs/sv/` as the single source of truth.

## Document Identity

- Treat each document as a standalone controlled document.
- Do not describe a document as migrated, regenerated, rewritten, derived, or based on another file.
- Do not include provenance-style wording in the document body.
- Do not place repository rules or drafting-process guidance in the controlled document body.

## Product Scope

- Keep `Portview` as the primary document scope.
- Exclude `GIX`, `IP System`, and `ImageProcess` content unless the user explicitly asks to reintroduce it.

## Document Set

All documents are in `docs/sv/`. File naming convention: `(ID) Title.md`

| ID | File | Type |
| --- | --- | --- |
| `PV-SV-01` | `(PV-SV-01) Software Validation Report.md` | SV core |
| `PV-SV-02` | `(PV-SV-02) Software Development Planning.md` | SV core |
| `PV-SV-03` | `(PV-SV-03) Software High Level Design.md` | SV core |
| `PV-SV-04` | `(PV-SV-04) Software Verification Plan.md` | SV core |
| `PV-SV-05` | `(PV-SV-05) Software Verification Report.md` | SV core |
| `PV-RS-01` | `(PV-RS-01) RS.md` | Specification |
| `PV-SRS-01` | `(PV-SRS-01) SwSRS.md` | Specification |
| `PV-SDS-01` | `(PV-SDS-01) SwSDS.md` | Specification |
| `PV-TM-01` | `(PV-TM-01) Traceability Matrix.md` | Traceability |
| `PV-STP-01` | `(PV-STP-01) SwSTP.md` | Procedure |
| `PV-STR-01` | `(PV-STR-01) SwSTR.md` | Result |
| `PV-TP-01` | `(PV-TP-01) SwTP.md` | Procedure |
| `PV-TR-01` | `(PV-TR-01) SwTR.md` | Result |
| `PV-SYSTP-01` | `(PV-SYSTP-01) SystemTP.md` | Procedure |
| `PV-SYSTR-01` | `(PV-SYSTR-01) SystemTR.md` | Result |
| `PV-CSRS-01` | `(PV-CSRS-01) SwRS for Cybersecurity.md` | Risk |
| `FMEA-Z01` | `(FMEA-Z01) Risks FMEA.md` | Risk |
| `NSE-Z01` | `(NSE-Z01) Network Security Enclosure.md` | Verification |

## Document Header Pattern

Every document starts with:

```
# (ID) Title

Document ID: `ID`
Product: `Portview`
Document Status: `Released`
```

Followed by Document Approval (Prepared / Reviewed / Approved) and Revision History.
No Document Overview section in release-ready documents.

## Identifier Policies

### Document IDs

- Use short product-prefixed identifiers: `PV-{type}-{seq}`
- Keep the ID stable even if the title wording changes.

### Requirement IDs

- `RS-xxx` for system-level requirements
- `SRS-xxx` for software-level requirements

### Design IDs

- `SDS-xxx` for design items (SDS-001 to SDS-031)

### Procedure IDs

- `UTP-xxx` for unit procedures
- `ITP-xxx` for integration procedures
- `SYSP-xxx` for system procedures

### Risk IDs

- `FMEA-xxx` for FMEA risk items

### Legacy IDs

- Do not use legacy `CA-xxxx` identifiers as primary IDs.
- Legacy mappings are kept outside the controlled document body.

## Verification-Level Separation

- `SwSTP` (unit) and `SwTP` (integration) are separate document concepts.
- `SystemTP` is the system-level procedure set.
- Do not merge procedure levels into one document.

## Result Document Pairing

- `PV-STP-01` -> `PV-STR-01`
- `PV-TP-01` -> `PV-TR-01`
- `PV-SYSTP-01` -> `PV-SYSTR-01`
- Result documents mirror the procedure structure with execution status, executor, date, and deviation fields.

## Table Conventions

- Document Approval: Prepared by / Reviewed by / Approved by (Title, Name, Signature)
- Revision History: Rev., Date, Description
- Wide tables (7+ columns): split into two related tables linked by ID column.

## Markdown Rules

- Prefer pure Markdown over embedded HTML.
- Keep documents GitHub-friendly (renders in GitHub, VS Code, MkDocs).
- Split wide tables rather than using HTML merged cells.

## Diagrams

- Mermaid flowcharts for all design item specifications.
- Mermaid state diagrams where state transitions are meaningful.
- Center-aligned via CSS (`.md-typeset .mermaid { text-align: center; }`).

## MkDocs And PDF

- Local authoring: `py -3.11 -m mkdocs serve --dirtyreload`
- PDF export: `py -3.11 scripts/export-pdf.py` (requires mkdocs serve running)
- PDF margins: `@page { margin: 10mm }` in `docs/stylesheets/pdf.css`
- Mermaid in PDF: Playwright injects source from markdown and calls `mermaid.run()` in batches.

## Companion Files

- `AGENTS.Compliance.md` — IEC 62304 clause-to-document mapping and compliance actions taken
- `AGENTS.Concerns.md` — Known residual compliance concerns
- `AGENTS.Policy.md` — General certification document creation and management policy (product-independent)
