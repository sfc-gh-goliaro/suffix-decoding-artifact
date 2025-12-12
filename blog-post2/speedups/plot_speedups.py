import numpy as np
import platform
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# Don't use seaborn style - it may interfere with Unicode rendering
# Use matplotlib's default style which has better font support for the star character

# Data setup
benchmarks = ['AgenticSQL', 'SWE-Bench']
baselines = ['Vanilla', 'Eagle', 'Eagle 2', 'Eagle 3', 'PLD', 'Token Recycling', 'SuffixDecoding', 'SuffixDecoding (Hybrid)']

# Speedup data - using best performing variant for Suffix and Hybrid
# For AgenticSQL: Suffix (linear) = 5.345 > Suffix (tree) = 5.175, so use linear
# For AgenticSQL: Hybrid (tree) = 4.068 > Hybrid (linear) = 3.799, so use tree
# For SWE-Bench: Suffix (linear) = 2.452 > Suffix (tree) = 2.433, so use linear
# For SWE-Bench: Hybrid data not available (both are NaN)
speedup_data = np.array([
    # Vanilla   Eagle   Eagle2      Eagle3      PLD         Recycling   Suffix (best)      Hybrid (best)
    [1,         1.595,  1.864,      1.623,     2.105,       2.710,      5.345,              4.068],  # AgenticSQL
    [1,         np.nan, np.nan,     np.nan,     1.495,      1.358,      2.452,              np.nan],  # SWE-Bench
])

# Mean accepted tokens data - using best performing variant for Suffix and Hybrid
# For AgenticSQL: Suffix (linear) = 6.349 > Suffix (tree) = 6.236, so use linear
# For AgenticSQL: Hybrid (tree) = 7.500 > Hybrid (linear) = 7.262, so use tree
# For SWE-Bench: Suffix (linear) = 7.821 > Suffix (tree) = 7.552, so use linear
# For SWE-Bench: Hybrid data not available (both are NaN)
tokens_data = np.array([
    # Vanilla   Eagle   Eagle2      Eagle3      PLD         Recycling   Suffix (best)      Hybrid (best)
    [1.000,     2.851,  3.572,      3.160,     2.373,      3.169,      6.349,              7.500],  # AgenticSQL
    [1.000,     np.nan, np.nan,     np.nan,     3.168,      3.054,      7.821,              np.nan],  # SWE-Bench
])

# Set width of bars
bar_width = 0.09
positions = np.arange(len(benchmarks))

# Colors for different baselines
# Vanilla -> Eagle -> Eagle 2 -> Eagle 3 -> PLD -> Token Recycling -> Suffix -> Hybrid
# Using shades of gray/black for baselines except Suffix (#29B5E8) and Hybrid (#11567F)
colors = ['#1a1a1a', '#404040', '#666666', '#808080', '#999999', '#b3b3b3', '#29B5E8', '#11567F']

# ===================== FIGURE 1: Speedup Plot =====================
fig1, ax1 = plt.subplots(figsize=(16, 5))

# Plot speedup data
for i, baseline in enumerate(baselines):
    offset = (i - len(baselines)/2 + 0.5) * bar_width
    for j, value in enumerate(speedup_data[:, i]):
        x_pos = positions[j] + offset
        if np.isnan(value):
            ax1.plot(x_pos, 0.2, 'x', color='red', markersize=14, markeredgewidth=3, label=None)
        else:
            ax1.bar(x_pos, value, bar_width, label=baseline if j == 0 else None,
                    color=colors[i], edgecolor='black', linewidth=1)
            # Calculate and annotate the speedup ratio with respect to the vanilla bar (col 0)
            vanilla_value = speedup_data[j, 0]
            if not np.isnan(vanilla_value) and vanilla_value != 0:
                speedup = value / vanilla_value
                # Determine if this is Suffix or Hybrid (indices 6 and 7)
                is_suffix = (i == 6)
                is_hybrid = (i == 7)
                
                # Format text - add star for Suffix, bold for both Suffix and Hybrid
                text_content = f"{speedup:.1f}x"
                if is_suffix:
                    text_content = "★ " + text_content
                fontweight = 'bold' if (is_suffix or is_hybrid) else 'normal'
                
                # Add text annotation above the bar with larger font size
                ax1.text(x_pos, value + 0.05, text_content, ha='center', va='bottom', 
                        fontsize=15, fontweight=fontweight)

# Customize speedup plot
# ax1.set_xlabel('Benchmarks', fontsize=16, fontweight='bold')
ax1.set_ylabel('Speedup', fontsize=16, fontweight='bold')
ax1.set_title('Speculative Speedups over Vanilla Decoding', fontsize=18, fontweight='bold')
ax1.set_xticks(positions)
ax1.set_xticklabels(benchmarks, fontsize=16, fontweight='bold')
ax1.tick_params(axis='y', labelsize=16)
ax1.legend(title='Baselines', fontsize=12, title_fontsize=14, frameon=True, ncols=2)
ax1.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
ax1.set_ylim(0, 6)  # Set y-axis to 600%
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Save speedup plot
plt.tight_layout()
plt.savefig('speedup_comparison.png', format='png', dpi=300, bbox_inches='tight')
print("Saved: speedup_comparison.png")

# ===================== FIGURE 2: Mean Accepted Tokens Plot =====================
fig2, ax2 = plt.subplots(figsize=(16, 5))

# Plot mean accepted tokens data
for i, baseline in enumerate(baselines):
    offset = (i - len(baselines)/2 + 0.5) * bar_width
    for j, value in enumerate(tokens_data[:, i]):
        x_pos = positions[j] + offset
        if np.isnan(value):
            ax2.plot(x_pos, 0.2, 'x', color='red', markersize=14, markeredgewidth=3, label=None)
        else:
            ax2.bar(x_pos, value, bar_width, label=baseline if j == 0 else None,
                    color=colors[i], edgecolor='black', linewidth=1)
            # Determine if this is Suffix or Hybrid (indices 6 and 7)
            is_suffix = (i == 6)
            is_hybrid = (i == 7)
            # Add text annotation above the bar with bold weight for Suffix and Hybrid and larger font
            fontweight = 'bold' if (is_suffix or is_hybrid) else 'normal'
            ax2.text(x_pos, value + 0.1, f"{value:.1f}", ha='center', va='bottom', fontsize=15, fontweight=fontweight)

# Customize mean accepted tokens plot
# ax2.set_xlabel('Benchmarks', fontsize=16, fontweight='bold')
ax2.set_ylabel('Mean Accepted Tokens\n(tokens/step)', fontsize=16, fontweight='bold')
ax2.set_title('Mean Accepted Tokens per Step', fontsize=18, fontweight='bold')
ax2.set_xticks(positions)
ax2.set_xticklabels(benchmarks, fontsize=16, fontweight='bold')
ax2.tick_params(axis='y', labelsize=16)
ax2.legend(title='Baselines', fontsize=12, title_fontsize=14, frameon=True, ncols=2)
ax2.set_ylim(0, 9)  # Set y-axis maximum to 9
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Save mean accepted tokens plot
plt.tight_layout()
plt.savefig('tokens_comparison.png', format='png', dpi=300, bbox_inches='tight')
print("Saved: tokens_comparison.png")

# Show both plots
plt.show()
