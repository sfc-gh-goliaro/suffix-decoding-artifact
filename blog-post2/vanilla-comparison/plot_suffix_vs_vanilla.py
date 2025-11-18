import numpy as np
import matplotlib.pyplot as plt

# Data for spec_len = 32 only
concurrency_levels = [1, 4, 16, 64]

# First dataset: Suffix vs N-gram [3,5] vs Vanilla (spec-bench)
vanilla_times_35 = [5.56, 5.82, 6.72, 10.42]  # ms
suffix_times_35_with_vanilla = [4.39, 4.63, 5.82, 10.67]  # ms
ngram35_times_with_vanilla = [5.18, 5.52, 6.87, 13.37]  # ms

# Second dataset: Suffix vs N-gram [3,5] vs Vanilla (blazedit)
vanilla_times_blazedit = [5.65, 6.01, 7.46, 11.14]  # ms
suffix_times_blazedit_with_vanilla = [1.82, 2.01, 2.88, 5.63]  # ms
ngram35_times_blazedit_with_vanilla = [1.86, 2.22, 3.33, 8.13]  # ms

# Set width of bars for 3 bars
bar_width_3 = 0.25
positions_3 = np.arange(len(concurrency_levels))

# Snowflake colors - using primary and secondary colors
# Vanilla: #FF9F36 (orange) on the left
# Ngram: #11567F (darker blue) in the middle
# Suffix: #29B5E8 (bright blue) on the right
vanilla_color = '#FF9F36'
ngram_color = '#11567F'
suffix_color = '#29B5E8'

# ===================== FIGURE 1: Suffix vs N-gram [3,5] vs Vanilla (spec-bench) =====================
fig1, ax1 = plt.subplots(figsize=(12, 6))

# Plot bars - Vanilla on the left, N-gram in the middle, Suffix on the right
vanilla_bars1 = ax1.bar(positions_3 - bar_width_3, vanilla_times_35, bar_width_3,
                        label='Vanilla', color=vanilla_color, edgecolor='black', linewidth=1)
ngram_bars1 = ax1.bar(positions_3, ngram35_times_with_vanilla, bar_width_3,
                      label='N-gram', color=ngram_color, edgecolor='black', linewidth=1)
suffix_bars1 = ax1.bar(positions_3 + bar_width_3, suffix_times_35_with_vanilla, bar_width_3, 
                       label='Suffix', color=suffix_color, edgecolor='black', linewidth=1)

# Add value labels on top of bars
for i, (vanilla_val, ngram_val, suffix_val) in enumerate(zip(vanilla_times_35, ngram35_times_with_vanilla, suffix_times_35_with_vanilla)):
    ax1.text(positions_3[i] - bar_width_3, vanilla_val + 0.3, f'{vanilla_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')
    ax1.text(positions_3[i], ngram_val + 0.3, f'{ngram_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')
    ax1.text(positions_3[i] + bar_width_3, suffix_val + 0.3, f'{suffix_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')

# Customize plot
ax1.set_xlabel('Concurrency Level', fontsize=16, fontweight='bold')
ax1.set_ylabel('TPOT (ms)', fontsize=16, fontweight='bold')
ax1.set_title('Time per Output Token Comparison: spec-bench', fontsize=18, fontweight='bold')
ax1.set_xticks(positions_3)
ax1.set_xticklabels(concurrency_levels, fontsize=14, fontweight='bold')
ax1.tick_params(axis='y', labelsize=14)
ax1.legend(fontsize=14, frameon=True, loc='upper left')
ax1.set_ylim(0, 15)
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Save plot
plt.tight_layout()
plt.savefig('suffix_vs_vanilla_comparison.png', format='png', dpi=300, bbox_inches='tight')
print("Saved: suffix_vs_vanilla_comparison.png")
plt.close()

# ===================== FIGURE 2: Suffix vs N-gram [3,5] vs Vanilla (blazedit) =====================
fig2, ax2 = plt.subplots(figsize=(12, 6))

# Plot bars - Vanilla on the left, N-gram in the middle, Suffix on the right
vanilla_bars2 = ax2.bar(positions_3 - bar_width_3, vanilla_times_blazedit, bar_width_3,
                        label='Vanilla', color=vanilla_color, edgecolor='black', linewidth=1)
ngram_bars2 = ax2.bar(positions_3, ngram35_times_blazedit_with_vanilla, bar_width_3,
                      label='N-gram', color=ngram_color, edgecolor='black', linewidth=1)
suffix_bars2 = ax2.bar(positions_3 + bar_width_3, suffix_times_blazedit_with_vanilla, bar_width_3, 
                       label='Suffix', color=suffix_color, edgecolor='black', linewidth=1)

# Add value labels on top of bars
for i, (vanilla_val, ngram_val, suffix_val) in enumerate(zip(vanilla_times_blazedit, ngram35_times_blazedit_with_vanilla, suffix_times_blazedit_with_vanilla)):
    ax2.text(positions_3[i] - bar_width_3, vanilla_val + 0.25, f'{vanilla_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')
    ax2.text(positions_3[i], ngram_val + 0.25, f'{ngram_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')
    ax2.text(positions_3[i] + bar_width_3, suffix_val + 0.25, f'{suffix_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')

# Customize plot
ax2.set_xlabel('Concurrency Level', fontsize=16, fontweight='bold')
ax2.set_ylabel('TPOT (ms)', fontsize=16, fontweight='bold')
ax2.set_title('Time per Output Token Comparison: blazedit', fontsize=18, fontweight='bold')
ax2.set_xticks(positions_3)
ax2.set_xticklabels(concurrency_levels, fontsize=14, fontweight='bold')
ax2.tick_params(axis='y', labelsize=14)
ax2.legend(fontsize=14, frameon=True, loc='upper left')
ax2.set_ylim(0, 12)
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Save plot
plt.tight_layout()
plt.savefig('suffix_vs_vanilla_blazedit_comparison.png', format='png', dpi=300, bbox_inches='tight')
print("Saved: suffix_vs_vanilla_blazedit_comparison.png")
plt.close()

