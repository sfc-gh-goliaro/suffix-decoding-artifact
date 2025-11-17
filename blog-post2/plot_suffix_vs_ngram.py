import numpy as np
import matplotlib.pyplot as plt

# Data for spec_len = 32 only
concurrency_levels = [1, 4, 16, 64]

# First dataset: Suffix vs N-gram
suffix_times_55 = [4.28, 4.73, 6.17, 12.27]  # ms
ngram55_times = [5.37, 5.73, 6.87, 11.76]   # ms

# Second dataset: Suffix vs N-gram [3,5] (spec-bench)
suffix_times_35 = [4.39, 4.63, 5.82, 10.67]  # ms
ngram35_times = [5.18, 5.52, 6.87, 13.37]  # ms

# Third dataset: Suffix vs N-gram [3,5] (blazedit)
suffix_times_blazedit = [1.82, 2.01, 2.88, 5.63]  # ms
ngram35_times_blazedit = [1.86, 2.22, 3.33, 8.13]  # ms

# Fourth dataset: Suffix vs N-gram [3,5] vs Vanilla (spec-bench)
vanilla_times_35 = [5.56, 5.82, 6.72, 10.42]  # ms
suffix_times_35_with_vanilla = [4.39, 4.63, 5.82, 10.67]  # ms
ngram35_times_with_vanilla = [5.18, 5.52, 6.87, 13.37]  # ms

# Fifth dataset: Suffix vs N-gram [3,5] vs Vanilla (blazedit)
vanilla_times_blazedit = [5.65, 6.01, 7.46, 11.14]  # ms
suffix_times_blazedit_with_vanilla = [1.82, 2.01, 2.88, 5.63]  # ms
ngram35_times_blazedit_with_vanilla = [1.86, 2.22, 3.33, 8.13]  # ms

# Set width of bars
bar_width = 0.35
positions = np.arange(len(concurrency_levels))

# Snowflake colors - using primary and secondary colors
# Vanilla: #FF9F36 (orange) on the left
# Ngram: #11567F (darker blue) in the middle
# Suffix: #29B5E8 (bright blue) on the right
vanilla_color = '#FF9F36'
ngram_color = '#11567F'
suffix_color = '#29B5E8'

# ===================== FIGURE 1: Suffix vs N-gram =====================
fig1, ax1 = plt.subplots(figsize=(12, 6))

# Plot bars - N-gram on the left, Suffix on the right
ngram_bars = ax1.bar(positions - bar_width/2, ngram55_times, bar_width,
                     label='N-gram', color=ngram_color, edgecolor='black', linewidth=1)
suffix_bars = ax1.bar(positions + bar_width/2, suffix_times_55, bar_width, 
                      label='Suffix', color=suffix_color, edgecolor='black', linewidth=1)

# Add value labels on top of bars
for i, (suffix_val, ngram_val) in enumerate(zip(suffix_times_55, ngram55_times)):
    ax1.text(positions[i] - bar_width/2, ngram_val + 0.3, f'{ngram_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')
    ax1.text(positions[i] + bar_width/2, suffix_val + 0.3, f'{suffix_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')

# Customize plot
ax1.set_xlabel('Concurrency Level', fontsize=16, fontweight='bold')
ax1.set_ylabel('TPOT (ms)', fontsize=16, fontweight='bold')
ax1.set_title('Time per Output Token Comparison: Suffix and N-gram', fontsize=18, fontweight='bold')
ax1.set_xticks(positions)
ax1.set_xticklabels(concurrency_levels, fontsize=14, fontweight='bold')
ax1.tick_params(axis='y', labelsize=14)
ax1.legend(fontsize=14, frameon=True, loc='upper left')
ax1.set_ylim(0, 14)
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Save plot
plt.tight_layout()
plt.savefig('suffix_vs_ngram_comparison.png', format='png', dpi=300, bbox_inches='tight')
print("Saved: suffix_vs_ngram_comparison.png")
plt.close()

# ===================== FIGURE 2: Suffix vs N-gram [3,5] =====================
fig2, ax2 = plt.subplots(figsize=(12, 6))

# Plot bars - N-gram[3,5] on the left, Suffix on the right
ngram_bars2 = ax2.bar(positions - bar_width/2, ngram35_times, bar_width,
                      label='N-gram', color=ngram_color, edgecolor='black', linewidth=1)
suffix_bars2 = ax2.bar(positions + bar_width/2, suffix_times_35, bar_width, 
                       label='Suffix', color=suffix_color, edgecolor='black', linewidth=1)

# Add value labels on top of bars
for i, (suffix_val, ngram_val) in enumerate(zip(suffix_times_35, ngram35_times)):
    ax2.text(positions[i] - bar_width/2, ngram_val + 0.3, f'{ngram_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')
    ax2.text(positions[i] + bar_width/2, suffix_val + 0.3, f'{suffix_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')

# Customize plot
ax2.set_xlabel('Concurrency Level', fontsize=16, fontweight='bold')
ax2.set_ylabel('TPOT (ms)', fontsize=16, fontweight='bold')
ax2.set_title('Time per Output Token Comparison: Suffix and N-gram', fontsize=18, fontweight='bold')
ax2.set_xticks(positions)
ax2.set_xticklabels(concurrency_levels, fontsize=14, fontweight='bold')
ax2.tick_params(axis='y', labelsize=14)
ax2.legend(fontsize=14, frameon=True, loc='upper left')
ax2.set_ylim(0, 15)
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Save plot
plt.tight_layout()
plt.savefig('suffix_vs_ngram35_comparison.png', format='png', dpi=300, bbox_inches='tight')
print("Saved: suffix_vs_ngram35_comparison.png")
plt.close()

# ===================== FIGURE 3: Suffix vs N-gram [3,5] (blazedit) =====================
fig3, ax3 = plt.subplots(figsize=(12, 6))

# Plot bars - N-gram[3,5] on the left, Suffix on the right
ngram_bars3 = ax3.bar(positions - bar_width/2, ngram35_times_blazedit, bar_width,
                      label='N-gram', color=ngram_color, edgecolor='black', linewidth=1)
suffix_bars3 = ax3.bar(positions + bar_width/2, suffix_times_blazedit, bar_width, 
                       label='Suffix', color=suffix_color, edgecolor='black', linewidth=1)

# Add value labels on top of bars
for i, (suffix_val, ngram_val) in enumerate(zip(suffix_times_blazedit, ngram35_times_blazedit)):
    ax3.text(positions[i] - bar_width/2, ngram_val + 0.2, f'{ngram_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')
    ax3.text(positions[i] + bar_width/2, suffix_val + 0.2, f'{suffix_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')

# Customize plot
ax3.set_xlabel('Concurrency Level', fontsize=16, fontweight='bold')
ax3.set_ylabel('TPOT (ms)', fontsize=16, fontweight='bold')
ax3.set_title('Time per Output Token Comparison: Suffix and N-gram (blazedit)', fontsize=18, fontweight='bold')
ax3.set_xticks(positions)
ax3.set_xticklabels(concurrency_levels, fontsize=14, fontweight='bold')
ax3.tick_params(axis='y', labelsize=14)
ax3.legend(fontsize=14, frameon=True, loc='upper left')
ax3.set_ylim(0, 9)
ax3.grid(axis='y', linestyle='--', alpha=0.7)

# Save plot
plt.tight_layout()
plt.savefig('suffix_vs_ngram35_blazedit_comparison.png', format='png', dpi=300, bbox_inches='tight')
print("Saved: suffix_vs_ngram35_blazedit_comparison.png")
plt.close()

# ===================== FIGURE 4: Suffix vs N-gram [3,5] vs Vanilla (spec-bench) =====================
fig4, ax4 = plt.subplots(figsize=(12, 6))

# Set width of bars for 3 bars
bar_width_3 = 0.25
positions_3 = np.arange(len(concurrency_levels))

# Plot bars - Vanilla on the left, N-gram in the middle, Suffix on the right
vanilla_bars4 = ax4.bar(positions_3 - bar_width_3, vanilla_times_35, bar_width_3,
                        label='Vanilla', color=vanilla_color, edgecolor='black', linewidth=1)
ngram_bars4 = ax4.bar(positions_3, ngram35_times_with_vanilla, bar_width_3,
                      label='N-gram', color=ngram_color, edgecolor='black', linewidth=1)
suffix_bars4 = ax4.bar(positions_3 + bar_width_3, suffix_times_35_with_vanilla, bar_width_3, 
                       label='Suffix', color=suffix_color, edgecolor='black', linewidth=1)

# Add value labels on top of bars
for i, (vanilla_val, ngram_val, suffix_val) in enumerate(zip(vanilla_times_35, ngram35_times_with_vanilla, suffix_times_35_with_vanilla)):
    ax4.text(positions_3[i] - bar_width_3, vanilla_val + 0.3, f'{vanilla_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')
    ax4.text(positions_3[i], ngram_val + 0.3, f'{ngram_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')
    ax4.text(positions_3[i] + bar_width_3, suffix_val + 0.3, f'{suffix_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')

# Customize plot
ax4.set_xlabel('Concurrency Level', fontsize=16, fontweight='bold')
ax4.set_ylabel('TPOT (ms)', fontsize=16, fontweight='bold')
ax4.set_title('Time per Output Token Comparison: spec-bench', fontsize=18, fontweight='bold')
ax4.set_xticks(positions_3)
ax4.set_xticklabels(concurrency_levels, fontsize=14, fontweight='bold')
ax4.tick_params(axis='y', labelsize=14)
ax4.legend(fontsize=14, frameon=True, loc='upper left')
ax4.set_ylim(0, 15)
ax4.grid(axis='y', linestyle='--', alpha=0.7)

# Save plot
plt.tight_layout()
plt.savefig('suffix_vs_ngram35_vs_vanilla_comparison.png', format='png', dpi=300, bbox_inches='tight')
print("Saved: suffix_vs_ngram35_vs_vanilla_comparison.png")
plt.close()

# ===================== FIGURE 5: Suffix vs N-gram [3,5] vs Vanilla (blazedit) =====================
fig5, ax5 = plt.subplots(figsize=(12, 6))

# Plot bars - Vanilla on the left, N-gram in the middle, Suffix on the right
vanilla_bars5 = ax5.bar(positions_3 - bar_width_3, vanilla_times_blazedit, bar_width_3,
                        label='Vanilla', color=vanilla_color, edgecolor='black', linewidth=1)
ngram_bars5 = ax5.bar(positions_3, ngram35_times_blazedit_with_vanilla, bar_width_3,
                      label='N-gram', color=ngram_color, edgecolor='black', linewidth=1)
suffix_bars5 = ax5.bar(positions_3 + bar_width_3, suffix_times_blazedit_with_vanilla, bar_width_3, 
                       label='Suffix', color=suffix_color, edgecolor='black', linewidth=1)

# Add value labels on top of bars
for i, (vanilla_val, ngram_val, suffix_val) in enumerate(zip(vanilla_times_blazedit, ngram35_times_blazedit_with_vanilla, suffix_times_blazedit_with_vanilla)):
    ax5.text(positions_3[i] - bar_width_3, vanilla_val + 0.25, f'{vanilla_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')
    ax5.text(positions_3[i], ngram_val + 0.25, f'{ngram_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')
    ax5.text(positions_3[i] + bar_width_3, suffix_val + 0.25, f'{suffix_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')

# Customize plot
ax5.set_xlabel('Concurrency Level', fontsize=16, fontweight='bold')
ax5.set_ylabel('TPOT (ms)', fontsize=16, fontweight='bold')
ax5.set_title('Time per Output Token Comparison: blazedit', fontsize=18, fontweight='bold')
ax5.set_xticks(positions_3)
ax5.set_xticklabels(concurrency_levels, fontsize=14, fontweight='bold')
ax5.tick_params(axis='y', labelsize=14)
ax5.legend(fontsize=14, frameon=True, loc='upper left')
ax5.set_ylim(0, 12)
ax5.grid(axis='y', linestyle='--', alpha=0.7)

# Save plot
plt.tight_layout()
plt.savefig('suffix_vs_ngram35_vs_vanilla_blazedit_comparison.png', format='png', dpi=300, bbox_inches='tight')
print("Saved: suffix_vs_ngram35_vs_vanilla_blazedit_comparison.png")
plt.close()

