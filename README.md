# State of the Map Africa 2019: Programme Insights Report

[![Python](https://img.shields.io/badge/Python-3.8%2B-0D2B5E?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-C8830A?style=flat-square)](LICENSE)
[![OpenStreetMap](https://img.shields.io/badge/OpenStreetMap-Africa-0D2B5E?style=flat-square)](https://openstreetmap.africa)

A professional data analysis and reporting project examining the Call for Proposals (CFP) submission pipeline and programme curation decisions for the **2019 State of the Map Africa conference**, held in Grand-Bassam, Ivory Coast under the theme *Transforming Lives Through Mapping*.

---

## About the Project

The [State of the Map Africa](https://2019.stateofthemap.africa) conference is the premier annual gathering of the OpenStreetMap Africa community. This report was conducted by **Yusuf**, who served as Programme Lead for SotM Africa from 2019 to 2021.

The report examines 232 CFP submissions across 28 data fields and the final programme selection workbook across five session format tracks, producing insights on:

- **Geographic reach** — which communities submitted, and who was missing
- **Access equity** — scholarship demand as a structural access signal
- **Language inclusion** — validation of the bilingual (EN/FR) conference design
- **Programme curation** — selection rates by format and deliberate design choices
- **Content themes** — community priorities reflected in submission data

---

## Outputs

Running the script produces three outputs:

| Output | Description |
|--------|-------------|
| `figures/` | 9 publication-quality PNG charts |
| `sotm_africa_2019_report.html` | Interactive HTML report (self-contained, base64-embedded images) |
| `sotm_africa_2019_report.pdf` | Print-ready A4 PDF report (McKinsey/World Bank register) |

---

## Getting Started

### Prerequisites

```bash
pip install matplotlib numpy weasyprint
```

> **Note on WeasyPrint:** WeasyPrint requires system-level dependencies (Cairo, Pango).
> On Ubuntu/Debian: `sudo apt-get install libpango-1.0-0 libpangocairo-1.0-0`
> On macOS: `brew install pango`

### Run

```bash
python sotm_africa_2019_analysis.py
```

Expected output:

```
✅  All 9 figures saved to figures/
✅  HTML report saved → sotm_africa_2019_report.html
✅  PDF  report saved → sotm_africa_2019_report.pdf

🎉  All outputs complete.
```

---

## Report Structure

```
Cover + Key Statistics Strip
│
├── Executive Summary
├── Key Findings (4 findings)
├── Methodology (metrics table)
│
├── Section 1 — Submission Pipeline & Timeline
├── Section 2 — Geographic Reach & Community Representation
├── Section 3 — Session Formats & Programme Design
├── Section 4 — Language Inclusion & Access Equity
├── Section 5 — Content Themes & Thematic Priorities
├── Section 6 — Programme Curation & Selection Analysis
│
└── Recommendations (4 actionable recommendations)
```

---

## Design System

The report uses a professional two-colour palette derived from OSM Africa's visual identity:

| Token | Hex | Usage |
|-------|-----|-------|
| Navy | `#0D2B5E` | Primary headings, chart bars, background |
| Navy Light | `#1A4B8C` | Gradient, secondary elements |
| Amber | `#C8830A` | Accent, highlights, selected data |
| Slate | `#4A5568` | Body text, supporting elements |

---

## Data

The analysis uses reconstructed data from the original CFP response files (250 records) and programme selection workbook (5 format tracks). The data was verified through live exploration of the original `.xlsx` source files.

**Data fields analysed:**
- Timestamp, Country, Region, Intended Session Format
- Language preference, Scholarship application, Multi-presenter flag
- Content categories (multi-select), Conference focus tracks
- Reviewer scores and selection decisions per format track

---

## Project Structure

```
sotm-africa-2019-analysis/
├── sotm_africa_2019_analysis.py   # Main analysis and report generation script
├── README.md                       # This file
├── figures/                        # Generated chart PNGs (created on run)
├── sotm_africa_2019_report.html   # Generated HTML report (created on run)
└── sotm_africa_2019_report.pdf    # Generated PDF report (created on run)
```

---

## About the Author

**Yusuf** served as Programme Lead for the State of the Map Africa Conference from 2019 to 2021. In that role, he managed the full CFP pipeline — from multilingual call design through multi-track review committee coordination to final programme curation — for two consecutive conference editions.


- Email: yusuf.suleiman@localpathways.org
- LinkedIn: [linkedin.com/in/yusufsuleiman](https://linkedin.com/in/yusufsuleiman)

---

## Licence

MIT — see [LICENSE](LICENSE) for details.
