"""
State of the Map Africa 2019 — Programme Insights Report
=========================================================
Author  : Yusuf Suleiman
Role    : Programme Lead, State of the Map Africa 2019
Contact : yusuf.suleiman@localpathways.org
Event   : Grand-Bassam, Ivory Coast · 22–24 November 2019
Theme   : Transforming Lives Through Mapping

Data sources
------------
  CFP Responses     : 232 submissions (Jul–Nov 2019), 28 fields
  Selection Workbook: 5 session-format tracks with reviewer scores

Note on dataset scope
---------------------
  The CFP window ran July–November 2019. The conference took place
  22–24 November 2019 in Grand-Bassam, Ivory Coast. December submissions
  are excluded as they post-date the event. Total = 232 submissions.

Outputs
-------
  figures/                        PNG charts (created on run)
  sotm_africa_2019_report.html    Interactive HTML report
  sotm_africa_2019_report.pdf     Print-ready A4 PDF report

Usage
-----
  python sotm_africa_2019_analysis.py
"""

import os, warnings, base64, pathlib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

warnings.filterwarnings("ignore")
os.makedirs("figures", exist_ok=True)

# ─────────────────────────────────────────────────────────────────────────────
# DESIGN SYSTEM
# ─────────────────────────────────────────────────────────────────────────────
NAVY     = "#0D2B5E"
NAVY_LT  = "#1A4B8C"
AMBER    = "#C8830A"
AMBER_LT = "#E8A832"
SLATE    = "#4A5568"
WHITE    = "#FFFFFF"
BLACK    = "#111827"

plt.rcParams.update({
    "font.family"       : "DejaVu Sans",
    "axes.spines.top"   : False,
    "axes.spines.right" : False,
    "axes.spines.left"  : True,
    "axes.spines.bottom": True,
    "axes.edgecolor"    : "#CBD5E0",
    "axes.grid"         : True,
    "grid.alpha"        : 0.18,
    "grid.linestyle"    : "--",
    "grid.color"        : "#CBD5E0",
    "figure.facecolor"  : WHITE,
    "axes.facecolor"    : WHITE,
    "text.color"        : BLACK,
    "axes.labelcolor"   : SLATE,
    "xtick.color"       : SLATE,
    "ytick.color"       : SLATE,
    "xtick.labelsize"   : 9,
    "ytick.labelsize"   : 9,
    "axes.labelsize"    : 10,
    "axes.titlesize"    : 11,
    "axes.titleweight"  : "bold",
    "axes.titlecolor"   : NAVY,
    "figure.dpi"        : 150,
})


def save_fig(name):
    path = f"figures/{name}.png"
    plt.savefig(path, dpi=150, bbox_inches="tight",
                facecolor=WHITE, edgecolor="none")
    plt.close()
    return path


def img64(path):
    return "data:image/png;base64," + base64.b64encode(
        pathlib.Path(path).read_bytes()).decode()


# ─────────────────────────────────────────────────────────────────────────────
# DATASET  (CFP window: Jul–Nov 2019; Dec excluded — post-dates conference)
# ─────────────────────────────────────────────────────────────────────────────
TOTAL_SUBMISSIONS = 232   # 250 raw minus 18 December submissions
TOTAL_SELECTED    = 46
ACCEPTANCE_RATE   = round(TOTAL_SELECTED / TOTAL_SUBMISSIONS * 100, 1)  # 19.8%

country_counts = {
    "Nigeria":19,"Kenya":15,"Tanzania":10,"Uganda":10,"France":7,
    "Guinea":6,"Rwanda":4,"Ghana":4,"United States":4,"Mali":4,
    "Togo":4,"Benin":3,"Zambia":3,"DR Congo":3,"Bangladesh":3,
    "Mozambique":2,"Ethiopia":2,"Senegal":2,"Cameroon":2,"Other":49,
}
region_counts = {
    "Africa":120,"Europe":11,"Asia":5,"North America":4,"Not stated":92
}
format_primary = {
    "30 Min Presentation":77,"Lightning Talk":52,"Workshop":19,
    "Small Group Discussion":21,"Panel":11,
}
selected_by_format = {
    "30 Min Presentation":22,"Lightning Talk":11,"Workshop":4,
    "Small Group Discussion":6,"Panel":3,
}
language_counts     = {"English":88,"Bilingual (EN/FR)":28,"French":24}
scholarship_yes, scholarship_no = 92, 48
collab_yes, collab_no           = 20, 120

# Content categories — % denominator now 232
categories = {
    "Cartography & Visualisation":68,
    "Contribution & Data Collection":62,
    "Community Growth & Diversity":55,
    "Humanitarian":44,
    "Skills & Training":41,
    "Development & Economics":35,
    "Documentation & Technical Writing":29,
    "Public Health":22,
    "Environment & Climate":18,
    "Navigation & Transport":14,
}

# Timeline — December excluded
timeline = {"Jul":8,"Aug":22,"Sep":61,"Oct":94,"Nov":47}

AFRICAN_COUNTRIES = {
    "Nigeria","Kenya","Tanzania","Uganda","Guinea","Rwanda","Ghana",
    "Mali","Togo","Benin","Zambia","DR Congo","Mozambique","Ethiopia",
    "Senegal","Cameroon",
}

# Derived stats used in text
oct_share        = round(94 / TOTAL_SUBMISSIONS * 100)       # 41%
sep_oct_share    = round((61 + 94) / TOTAL_SUBMISSIONS * 100) # 67%
bilingual_share  = round((language_counts["Bilingual (EN/FR)"] +
                          language_counts["French"]) /
                          sum(language_counts.values()) * 100) # 24%
scholarship_pct  = round(scholarship_yes /
                          (scholarship_yes + scholarship_no) * 100) # 66%


# ─────────────────────────────────────────────────────────────────────────────
# FIGURES
# ─────────────────────────────────────────────────────────────────────────────

# Figure 1 — Submission Timeline (Jul–Nov only)
fig, ax = plt.subplots(figsize=(10, 4))
months = list(timeline.keys())
counts = list(timeline.values())
colors = [AMBER if c == max(counts) else NAVY for c in counts]
bars   = ax.bar(months, counts, color=colors, width=0.55,
                edgecolor=WHITE, linewidth=1.4, zorder=3)
for bar, val in zip(bars, counts):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1.2,
            str(val), ha="center", va="bottom", fontsize=9.5,
            fontweight="bold",
            color=AMBER if val == max(counts) else NAVY)
ax.set_title("CFP Submissions by Month (July–November 2019)")
ax.set_xlabel("Month", labelpad=6)
ax.set_ylabel("Number of Submissions")
ax.set_ylim(0, 108)
ax.tick_params(axis="x", length=0)
ax.legend(handles=[mpatches.Patch(color=AMBER,
          label="Peak month — October (94 submissions)")],
          fontsize=9, framealpha=0.85, edgecolor="#CBD5E0")
fig.tight_layout()
save_fig("fig1_timeline")

# Figure 2 — Top 14 Countries
top14 = {k: v for k, v in sorted(
    country_counts.items(), key=lambda x: x[1], reverse=True)
    if k != "Other"}
top14 = dict(list(top14.items())[:14])
fig, ax = plt.subplots(figsize=(10, 5.5))
names      = list(top14.keys())
vals       = list(top14.values())
bar_colors = [NAVY if n in AFRICAN_COUNTRIES else SLATE for n in names]
hb = ax.barh(range(len(names)), vals, color=bar_colors, alpha=0.88,
             edgecolor=WHITE, linewidth=1.2, height=0.62)
for bar, val in zip(hb, vals):
    ax.text(bar.get_width() + 0.15,
            bar.get_y() + bar.get_height()/2,
            str(val), va="center", fontsize=9, fontweight="bold",
            color=NAVY if val > 5 else SLATE)
ax.set_yticks(range(len(names)))
ax.set_yticklabels(names, fontsize=9.5)
ax.set_xlim(0, 24)
ax.set_title("Submissions by Country — Top 14")
ax.set_xlabel("Number of Submissions")
ax.legend(handles=[
    mpatches.Patch(color=NAVY,  label="African country"),
    mpatches.Patch(color=SLATE, label="Non-African country"),
], fontsize=9, loc="lower right", framealpha=0.85, edgecolor="#CBD5E0")
fig.tight_layout()
save_fig("fig2_countries")

# Figure 3 — Regional Donut
fig, ax = plt.subplots(figsize=(7, 6))
r_vals   = list(region_counts.values())
r_labels = [f"{k}\n({v})" for k, v in region_counts.items()]
r_colors = [NAVY, "#2E7D9C", AMBER, AMBER_LT, "#CBD5E0"]
wedges, texts, autos = ax.pie(
    r_vals, labels=r_labels, colors=r_colors,
    autopct="%1.0f%%", startangle=140, pctdistance=0.8,
    wedgeprops={"edgecolor": WHITE, "linewidth": 2},
)
for t in texts:  t.set_fontsize(9)
for a in autos:  a.set_fontsize(8); a.set_color(WHITE); a.set_fontweight("bold")
ax.add_patch(plt.Circle((0, 0), 0.55, fc=WHITE))
ax.text(0,  0.08, str(TOTAL_SUBMISSIONS), ha="center", va="center",
        fontsize=22, fontweight="bold", color=NAVY)
ax.text(0, -0.18, "Submissions", ha="center", va="center",
        fontsize=9, color=SLATE)
ax.set_title("Submissions by World Region", pad=14)
fig.tight_layout()
save_fig("fig3_regions")

# Figure 4 — Format Distribution
fig, ax = plt.subplots(figsize=(10, 4))
f_names = list(format_primary.keys())
f_vals  = list(format_primary.values())
f_cols  = [NAVY, AMBER, "#2E7D9C", "#7B5EA7", "#2D6A4F"][:len(f_names)]
bars = ax.bar(f_names, f_vals, color=f_cols, width=0.52,
              edgecolor=WHITE, linewidth=1.4, zorder=3)
for bar, val in zip(bars, f_vals):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.6,
            str(val), ha="center", va="bottom",
            fontsize=9.5, fontweight="bold")
ax.set_title("Proposed Session Formats — Primary Classification")
ax.set_ylabel("Number of Submissions")
ax.set_ylim(0, 92)
ax.tick_params(axis="x", length=0)
fig.tight_layout()
save_fig("fig4_formats")

# Figure 5 — Language Inclusion
fig, ax = plt.subplots(figsize=(7, 4))
lang_l = list(language_counts.keys())
lang_v = list(language_counts.values())
total_lang = sum(lang_v)
bars = ax.bar(lang_l, lang_v,
              color=[NAVY, AMBER, "#2E7D9C"],
              width=0.45, edgecolor=WHITE, linewidth=1.4, zorder=3)
for bar, val in zip(bars, lang_v):
    pct = val / total_lang * 100
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.4,
            f"{val}\n({pct:.0f}%)", ha="center", va="bottom",
            fontsize=9.5, fontweight="bold")
ax.set_title("Presentation Language Preference\n(of respondents who answered)")
ax.set_ylabel("Submissions")
ax.set_ylim(0, 106)
ax.tick_params(axis="x", length=0)
fig.tight_layout()
save_fig("fig5_language")

# Figure 6 — Access & Equity
fig, ax = plt.subplots(figsize=(9, 4))
eq_cats  = ["Scholarship\nApplicants", "Collaborative\nSessions",
            "French or\nBilingual\nPresenters"]
yes_vals = [scholarship_yes, collab_yes,
            language_counts["Bilingual (EN/FR)"] + language_counts["French"]]
no_vals  = [scholarship_no, collab_no, language_counts["English"]]
na_vals  = [TOTAL_SUBMISSIONS - scholarship_yes - scholarship_no,
            TOTAL_SUBMISSIONS - collab_yes - collab_no,
            TOTAL_SUBMISSIONS - sum(language_counts.values())]
x, w = np.arange(len(eq_cats)), 0.26
b1 = ax.bar(x - w, yes_vals, w, label="Yes / Applicable",   color=NAVY,      alpha=0.9)
b2 = ax.bar(x,     no_vals,  w, label="No / Not applicable", color=AMBER,     alpha=0.9)
b3 = ax.bar(x + w, na_vals,  w, label="Not stated",          color="#CBD5E0", alpha=0.85)
for bars in [b1, b2, b3]:
    for bar in bars:
        h = bar.get_height()
        if h > 6:
            ax.text(bar.get_x() + bar.get_width()/2, h + 0.8,
                    str(int(h)), ha="center", va="bottom",
                    fontsize=8, fontweight="bold")
ax.set_xticks(x)
ax.set_xticklabels(eq_cats, fontsize=9.5)
ax.set_title("Access & Inclusion Indicators")
ax.set_ylabel("Number of Respondents")
ax.legend(fontsize=9, framealpha=0.85, edgecolor="#CBD5E0")
ax.set_ylim(0, 125)
fig.tight_layout()
save_fig("fig6_equity")

# Figure 7 — Content Categories
fig, ax = plt.subplots(figsize=(10, 5.5))
cats   = list(categories.keys())
c_vals = list(categories.values())
grad   = plt.cm.Blues(np.linspace(0.45, 0.9, len(cats)))
hb = ax.barh(range(len(cats)), c_vals, color=grad,
             edgecolor=WHITE, linewidth=1.2, height=0.6)
for bar, val in zip(hb, c_vals):
    pct = val / TOTAL_SUBMISSIONS * 100
    ax.text(bar.get_width() + 0.3,
            bar.get_y() + bar.get_height()/2,
            f"{val}  ({pct:.0f}%)", va="center", fontsize=9)
ax.set_yticks(range(len(cats)))
ax.set_yticklabels(cats, fontsize=9.5)
ax.set_title(f"Session Content Categories\n(multi-select — % of all {TOTAL_SUBMISSIONS} submissions)")
ax.set_xlabel("Submissions selecting category")
ax.set_xlim(0, 85)
fig.tight_layout()
save_fig("fig7_categories")

# Figure 8 — Submitted vs Selected
fig, ax = plt.subplots(figsize=(10, 4.5))
fmts_s = list(selected_by_format.keys())
sub_c  = [format_primary[f] for f in fmts_s]
sel_c  = list(selected_by_format.values())
x, w   = np.arange(len(fmts_s)), 0.36
b1 = ax.bar(x - w/2, sub_c, w, label="Submitted",
            color=NAVY,  alpha=0.8, edgecolor=WHITE, linewidth=1.2)
b2 = ax.bar(x + w/2, sel_c, w, label="Selected",
            color=AMBER, alpha=0.9, edgecolor=WHITE, linewidth=1.2)
for bar, val in zip(b1, sub_c):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.4,
            str(val), ha="center", fontsize=9,
            fontweight="bold", color=NAVY)
for bar, val in zip(b2, sel_c):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.4,
            str(val), ha="center", fontsize=9,
            fontweight="bold", color=AMBER)
ax.set_xticks(x)
ax.set_xticklabels([f.replace(" ", "\n") for f in fmts_s], fontsize=9.5)
ax.set_title("Submitted vs. Selected Sessions by Format")
ax.set_ylabel("Number of Sessions")
ax.legend(fontsize=10, framealpha=0.85, edgecolor="#CBD5E0")
ax.set_ylim(0, 90)
fig.tight_layout()
save_fig("fig8_selection")

# Figure 9 — Selection Rates
# Title: left-aligned | Legend: raised to upper left
fig, ax = plt.subplots(figsize=(9, 4))
overall_rate = round(TOTAL_SELECTED / TOTAL_SUBMISSIONS * 100, 1)
rates        = {f: round(selected_by_format[f] / format_primary[f] * 100, 1)
                for f in fmts_s}
r_vals       = list(rates.values())
r_labels     = list(rates.keys())
bar_colors   = [AMBER if r >= overall_rate else NAVY for r in r_vals]
hb = ax.barh(range(len(r_labels)), r_vals, color=bar_colors,
             edgecolor=WHITE, linewidth=1.2, height=0.5)
for bar, val in zip(hb, r_vals):
    ax.text(bar.get_width() + 0.3,
            bar.get_y() + bar.get_height()/2,
            f"{val}%", va="center", fontsize=10, fontweight="bold")
ax.set_yticks(range(len(r_labels)))
ax.set_yticklabels(r_labels, fontsize=10)
ax.axvline(overall_rate, color=SLATE, linestyle="--",
           linewidth=1.4, alpha=0.7)
ax.text(overall_rate + 0.3, len(r_labels) - 0.5,
        f"Overall avg\n{overall_rate}%", fontsize=8, color=SLATE)
ax.set_xlabel("Selection Rate (%)")
ax.set_xlim(0, 40)

# LEFT-ALIGNED title
ax.set_title("Selection Rate by Session Format", loc="left")

# Legend raised to upper left (bbox_to_anchor lifts it above default position)
ax.legend(handles=[
    mpatches.Patch(color=AMBER, label="Above overall average"),
    mpatches.Patch(color=NAVY,  label="Below overall average"),
], fontsize=9, loc="upper left",
   bbox_to_anchor=(0.0, 0.88),
   framealpha=0.85, edgecolor="#CBD5E0")

fig.tight_layout()
save_fig("fig9_rates")

print(f"✅  All 9 figures saved to figures/")
print(f"   Total submissions : {TOTAL_SUBMISSIONS}")
print(f"   Acceptance rate   : {ACCEPTANCE_RATE}%")
print(f"   Oct share         : {oct_share}%")
print(f"   Sep+Oct share     : {sep_oct_share}%")
print(f"   Bilingual share   : {bilingual_share}%")
print(f"   Scholarship pct   : {scholarship_pct}%")