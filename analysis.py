import numpy as np
import matplotlib.pyplot as plt
import os

# --- SETUP ---
os.makedirs("outputs", exist_ok=True)

PRIMARY = '#5C4BE8'
HIGHLIGHT = '#F77F00'
GREY = '#8D99AE'

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'axes.spines.top': False,
    'axes.spines.right': False
})

# ===============================
# DATA
# ===============================

timeline = {'Jul': 8, 'Aug': 22, 'Sep': 61, 'Oct': 94, 'Nov': 47, 'Dec': 18}

format_primary = {
    '30 Min Presentation': 77,
    'Lightning Talk': 52,
    'Workshop': 19,
    'Small Group Discussion': 21,
    'Panel': 11,
}

selected_by_format = {
    '30 Min Presentation': 22,
    'Lightning Talk': 11,
    'Workshop': 4,
    'Small Group Discussion': 6,
    'Panel': 3,
}

country_counts = {
    'Nigeria': 19, 'Kenya': 15, 'Tanzania': 10, 'Uganda': 10,
    'France': 7, 'Guinea': 5, 'Rwanda': 4, 'Ghana': 4,
    'United States': 4, 'Mali': 4, 'Togo': 4, 'Benin': 3
}

scholarship_yes = 97
scholarship_no = 52
scholarship_na = 101

# ===============================
# PLOTS
# ===============================

def plot_timeline():
    months = list(timeline.keys())
    values = list(timeline.values())
    colors = [HIGHLIGHT if v == max(values) else PRIMARY for v in values]

    plt.figure(figsize=(7,4))
    bars = plt.bar(months, values, color=colors)
    for bar, val in zip(bars, values):
        plt.text(bar.get_x()+bar.get_width()/2, val+1, str(val), ha='center', fontsize=8)
    plt.title("Submission Timeline", fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig("outputs/timeline.png", dpi=300)
    plt.close()


def plot_formats():
    names = list(format_primary.keys())
    values = list(format_primary.values())

    plt.figure(figsize=(7,4))
    bars = plt.barh(names, values, color=PRIMARY)
    for bar, val in zip(bars, values):
        plt.text(val+1, bar.get_y()+0.2, str(val), fontsize=8)
    plt.title("Session Format Distribution", fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig("outputs/formats.png", dpi=300)
    plt.close()


def plot_selection():
    names = list(selected_by_format.keys())
    selected = list(selected_by_format.values())
    submitted = [format_primary[n] for n in names]

    x = np.arange(len(names))

    plt.figure(figsize=(7,4))
    plt.bar(x - 0.2, submitted, 0.4, label='Submitted', color=GREY)
    plt.bar(x + 0.2, selected, 0.4, label='Selected', color=PRIMARY)

    plt.xticks(x, names, rotation=30)
    plt.legend()
    plt.title("Programme Selection", fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig("outputs/selection.png", dpi=300)
    plt.close()


def plot_geography():
    names = list(country_counts.keys())
    values = list(country_counts.values())

    plt.figure(figsize=(7,4))
    plt.barh(names, values, color=PRIMARY)
    plt.title("Top Contributing Countries", fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig("outputs/geography.png", dpi=300)
    plt.close()


def plot_equity():
    labels = ['Scholarship Yes', 'No', 'Not Stated']
    values = [scholarship_yes, scholarship_no, scholarship_na]

    plt.figure(figsize=(6,4))
    plt.bar(labels, values, color=[PRIMARY, GREY, GREY])
    plt.title("Scholarship Demand", fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig("outputs/equity.png", dpi=300)
    plt.close()


# Run all plots
plot_timeline()
plot_formats()
plot_selection()
plot_geography()
plot_equity()

print("All figures generated in /outputs")