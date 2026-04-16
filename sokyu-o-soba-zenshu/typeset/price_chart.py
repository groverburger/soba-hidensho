#!/usr/bin/env python3
"""
Sakata rice prices from Sōkyū-ō Soba Zenshū, 1776–1797.

Price unit: tawara per 10 ryō — LOWER number = MORE expensive rice.
Y-axis is inverted so "up" on the chart = more expensive.
"""

import matplotlib.pyplot as plt
from datetime import datetime

# Chronologically ordered, deduplicated price observations.
# When the same (year, month) appears twice (e.g. overlapping contract
# years), keep the one from the contract that "owns" that month.
raw = [
    # An'ei 5 (1776)
    (1776,  6, 38.0),
    (1776,  7, 31.2),
    (1776,  8, 26.7),
    (1777,  1, 24.0),
    # An'ei 6 (1777)
    (1777,  6, 37.0),
    (1777,  8, 26.0),
    (1777,  9, 23.7),
    (1778,  1, 34.0),
    # An'ei 7 (1778)
    (1778,  6, 46.0),
    (1778,  8, 31.7),
    (1779,  1, 30.9),
    # An'ei 9 (1780)
    (1780,  6, 50.0),
    (1780, 11, 37.6),
    (1781,  2, 41.6),
    # Tenmei 1 (1781)
    (1781,  7, 37.5),
    (1781, 12, 29.0),
    (1782,  4, 38.0),
    (1782,  5, 25.3),
    # Tenmei 2 (1782)
    (1782,  6, 37.0),
    (1782, 12, 24.0),
    (1783,  2, 20.5),
    # Tenmei 3 (1783)
    (1783,  6, 30.5),
    (1783, 12, 17.7),
    (1784,  1, 16.0),
    (1784,  3, 10.5),
    (1784,  9, 26.5),
    # Tenmei 4 (1784)
    (1785,  1, 20.2),
    # Tenmei 5 (1785)
    (1785,  9, 36.0),
    (1785, 12, 26.4),
    (1786,  2, 29.3),
    (1786,  7, 24.8),
    # Tenmei 6 (1786)
    (1786, 12, 18.2),
    (1787,  8, 11.2),
    (1787,  9, 19.1),
    # Tenmei 7 (1787) — overlap; use later points
    (1788,  2, 20.7),
    (1788,  9, 22.8),
    # Tenmei 8 (1788)
    (1789,  1, 23.6),
    # Kansei 1 (1789)
    (1789,  6, 29.5),
    (1789,  9, 26.6),
    # Kansei 2 (1790)
    (1790,  6, 40.0),
    (1790, 10, 44.0),
    (1790, 12, 33.1),
    # Kansei 3 (1791)
    (1791,  6, 38.0),
    (1791, 12, 20.2),
    (1792,  5, 18.5),
    (1792, 10, 27.0),
    # Kansei 4 (1792)
    (1793,  3, 18.8),
    # Kansei 5 (1793)
    (1793,  6, 26.0),
    (1793, 12, 38.0),
    (1794,  3, 25.5),
    (1794, 10, 34.0),
    # Kansei 6 (1794)
    (1795,  5, 29.0),
    (1795,  8, 25.5),
    # Kansei 7 (1795)
    (1795,  9, 23.5),
    (1796,  1, 20.0),
    (1796,  8, 28.5),
    # Kansei 8 (1796)
    (1797,  1, 22.8),
    (1797,  6, 22.7),
    (1797,  9, 22.4),
]

# Sort chronologically and deduplicate (keep last value for a given month)
seen = {}
for y, m, p in raw:
    seen[(y, m)] = p
points = sorted(seen.items())
dates = [datetime(ym[0], ym[1], 15) for ym, _ in points]
prices = [p for _, p in points]

# --- Plot ---
fig, ax = plt.subplots(figsize=(14, 5.5))

ax.plot(dates, prices, '-', color='#8B0000', linewidth=1.4, alpha=0.9)
ax.plot(dates, prices, 'o', color='#8B0000', markersize=3, alpha=0.6)

ax.invert_yaxis()
ax.set_ylabel('Tawara per 10 ryō\n(fewer tawara = more expensive rice)',
              fontsize=10)
ax.set_title('Sakata Rice Exchange Prices, 1776–1797',
             fontsize=13, fontweight='bold', color='#8B0000', pad=12)
ax.grid(True, alpha=0.2)

# Light background for readability
ax.set_facecolor('#FAFAF7')
fig.patch.set_facecolor('white')

plt.tight_layout()
plt.savefig('/Users/grob/Documents/projects/japanese/sokyu-o-soba-zenshu/typeset/price_chart.png',
            dpi=150, bbox_inches='tight')
plt.close()

print(f"{len(dates)} data points, {dates[0].year}–{dates[-1].year}")
