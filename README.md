# Portview SV Document Set

IEC 62304:2006/AMD1:2015 Class B compliant software verification document set for Portview intraoral imaging software.

## Documents

| ID | Document | Type |
| --- | --- | --- |
| `PV-SV-01` | Software Validation Report | SV core |
| `PV-SV-02` | Software Development Planning | SV core |
| `PV-SV-03` | Software High Level Design | SV core |
| `PV-SV-04` | Software Verification Plan | SV core |
| `PV-SV-05` | Software Verification Report | SV core |
| `PV-RS-01` | RS | Specification |
| `PV-SRS-01` | SwSRS | Specification |
| `PV-SDS-01` | SwSDS | Specification |
| `PV-TM-01` | Traceability Matrix | Traceability |
| `PV-STP-01` | SwSTP (Unit Procedures) | Procedure |
| `PV-STR-01` | SwSTR (Unit Results) | Result |
| `PV-TP-01` | SwTP (Integration Procedures) | Procedure |
| `PV-TR-01` | SwTR (Integration Results) | Result |
| `PV-SYSTP-01` | SystemTP (System Procedures) | Procedure |
| `PV-SYSTR-01` | SystemTR (System Results) | Result |
| `PV-CSRS-01` | SwRS for Cybersecurity | Risk |
| `FMEA-Z01` | Risks FMEA | Risk |
| `NSE-Z01` | Network Security Enclosure | Verification |

## Setup

```bash
setup.bat
```

Or manually:

```bash
py -3.11 -m pip install -r requirements.txt
py -3.11 -m playwright install chromium
```

## Usage

### Preview

```bash
py -3.11 -m mkdocs serve
```

Open http://127.0.0.1:8000 in your browser.

### Export PDF

With `mkdocs serve` running in another terminal:

```bash
py -3.11 scripts/export-pdf.py
```

PDFs are generated in `output/pdf-export/`. Mermaid diagrams are rendered via Playwright.

## Project Structure

```
docs/sv/           Controlled document set (18 documents)
docs/stylesheets/  Screen and print CSS
docs/js/           PDF rendering scripts
scripts/           Export tooling
output/            Generated PDF output
overrides/         MkDocs theme overrides
```

## Traceability

Full traceability chain maintained in `PV-TM-01`:

```
RS -> SRS -> SDS -> UTP/ITP -> STR/TR -> SYSP -> SYSTR
```

## Compliance

- IEC 62304:2006/AMD1:2015 (Software lifecycle processes)
- ISO 14971 (Risk management)
- MDCG 2019-16 Rev.1 (Cybersecurity guidance)
- AAMI TIR 57 (Medical device security)
