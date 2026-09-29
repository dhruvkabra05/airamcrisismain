from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt


BASE_DIR = Path(__file__).resolve().parent
CHARTS_DIR = BASE_DIR / "charts"
CHARTS_DIR.mkdir(exist_ok=True)



years = ["2024", "2025", "2026"]

ai_server_ram = [13217, 18459, 23730]
human_consumer_ram = [14177, 17043, 15022]

x = list(range(len(years)))
width = 0.34

fig, ax = plt.subplots(figsize=(10, 5.5), dpi=160)

bars_ai = ax.bar(
    [i - width / 2 for i in x],
    ai_server_ram,
    width,
    label="AI / Server RAM",
    color="#e63b24"
)

bars_human = ax.bar(
    [i + width / 2 for i in x],
    human_consumer_ram,
    width,
    label="Human / Consumer RAM",
    color="#333333"
)

ax.set_title(
    "AI / Server RAM vs Human / Consumer RAM (2024–2026)",
    fontsize=16,
    fontweight="bold",
    pad=18
)

ax.set_xlabel("Year", fontsize=10)
ax.set_ylabel(
    "DRAM demand (million 8Gb-equivalent units)",
    fontsize=10
)

ax.set_xticks(x)
ax.set_xticklabels(years)

ax.grid(axis="y", alpha=0.18)
ax.set_axisbelow(True)

ax.bar_label(bars_ai, fmt="%.0f", padding=3, fontsize=8)
ax.bar_label(bars_human, fmt="%.0f", padding=3, fontsize=8)

ax.legend(frameon=False, ncols=2, loc="upper left")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

fig.text(
    0.01,
    0.01,
    "Server demand is used as a proxy for AI-infrastructure memory demand; "
    "2025–2026 values are estimates.",
    fontsize=7.5,
    color="#666666"
)

fig.tight_layout(rect=[0, 0.05, 1, 1])

fig.savefig(
    CHARTS_DIR / "ram_usage_chart.png",
    bbox_inches="tight",
    facecolor="white"
)

plt.close(fig)



labels = [
    "DDR5 16GB UDIMM",
    "DDR4 16GB UDIMM",
    "DDR5 32GB RDIMM"
]

prices = [
    235.67,
    164.30,
    2050.00
]

fig, ax = plt.subplots(figsize=(8, 6), dpi=160)

wedges, texts, autotexts = ax.pie(
    prices,
    labels=labels,
    autopct=lambda p: f"{p:.1f}%",
    startangle=90,
    counterclock=False,
    wedgeprops={
        "linewidth": 1,
        "edgecolor": "white"
    },
    colors=[
        "#e63b24",
        "#333333",
        "#999999"
    ],
    textprops={
        "fontsize": 9
    }
)

ax.set_title(
    "RAM Price Comparison — September 2026",
    fontsize=16,
    fontweight="bold",
    pad=18
)

legend_labels = [
    f"DDR5 16GB UDIMM — ${prices[0]:,.2f}",
    f"DDR4 16GB UDIMM — ${prices[1]:,.2f}",
    f"DDR5 32GB RDIMM — ${prices[2]:,.2f}"
]

ax.legend(
    wedges,
    legend_labels,
    title="Module spot-price average",
    loc="lower center",
    bbox_to_anchor=(0.5, -0.12),
    frameon=False,
    fontsize=8.5
)

fig.text(
    0.5,
    0.01,
    "Source: TrendForce module spot-price averages. "
    "Modules differ in capacity and application.",
    ha="center",
    fontsize=7.5,
    color="#666666"
)

fig.tight_layout(rect=[0, 0.08, 1, 1])

fig.savefig(
    CHARTS_DIR / "ram_price_pie.png",
    bbox_inches="tight",
    facecolor="white"
)

plt.close(fig)


print("Charts generated successfully.")
print("1. charts/ram_usage_chart.png")
print("2. charts/ram_price_pie.png")
