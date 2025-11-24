import numpy as np
import matplotlib.pyplot as plt

# Data for spec_len = 32 only
concurrency_levels = [1, 4, 16, 64]

# First dataset: Suffix vs N-gram
old_suffix_times = [4.46, 4.78, 6.23, 12.11]  # ms
ngram_times_old = [5.37, 5.73, 6.87, 11.76]   # ms

# Second dataset: Suffix vs N-gram [3,5] and N-gram [5,5] (spec-bench)
new_suffix_times_specbench = [4.43, 4.70, 5.92, 10.96]  # ms
ngram35_times_specbench = [5.21, 5.49, 6.80, 13.14]  # ms
ngram55_times_specbench = [5.63, 5.83, 6.91, 11.57]  # ms


# Third dataset: Suffix vs N-gram [3,5] and N-gram [5,5] (blazedit)
new_suffix_times_blazedit = [1.71, 1.92, 2.86, 6.06]  # ms
ngram35_times_blazedit = [1.86, 2.16, 3.40, 7.99]  # ms
ngram55_times_blazedit = [2.17, 2.50, 3.59, 7.42]  # ms

# Set width of bars
bar_width = 0.35
positions = np.arange(len(concurrency_levels))

# Snowflake colors - using primary and secondary colors
# Ngram [3,5]: #11567F (darker blue) on the left
# Ngram [5,5]: #FF9F36 (orange) in the middle
# Suffix: #29B5E8 (bright blue) on the right
ngram35_color = '#11567F'
ngram55_color = '#FF9F36'
suffix_color = '#29B5E8'

# ===================== FIGURE 1: Suffix (unoptimized) vs N-gram =====================
fig1, ax1 = plt.subplots(figsize=(12, 6))

# Plot bars - N-gram on the left, Suffix on the right
ngram_bars = ax1.bar(positions - bar_width/2, ngram_times_old, bar_width,
                     label='N-gram', color=ngram35_color, edgecolor='black', linewidth=1)
suffix_bars = ax1.bar(positions + bar_width/2, old_suffix_times, bar_width, 
                      label='Suffix (unoptimized)', color=suffix_color, edgecolor='black', linewidth=1)

# Add value labels on top of bars
for i, (suffix_val, ngram_val) in enumerate(zip(old_suffix_times, ngram_times_old)):
    ax1.text(positions[i] - bar_width/2, ngram_val + 0.3, f'{ngram_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')
    ax1.text(positions[i] + bar_width/2, suffix_val + 0.3, f'{suffix_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')

# Customize plot
ax1.set_xlabel('Concurrency Level', fontsize=16, fontweight='bold')
ax1.set_ylabel('TPOT (ms)', fontsize=16, fontweight='bold')
ax1.set_title('TPOT Comparison: Suffix (unoptimized) and N-gram\nSpec-Bench dataset', fontsize=18, fontweight='bold')
ax1.set_xticks(positions)
ax1.set_xticklabels(concurrency_levels, fontsize=14, fontweight='bold')
ax1.tick_params(axis='y', labelsize=14)
ax1.legend(fontsize=14, frameon=True, loc='upper left')
ax1.set_ylim(0, 14)
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Save plot
plt.tight_layout()
plt.savefig('old_suffix_vs_ngram.png', format='png', dpi=300, bbox_inches='tight')
print("Saved: old_suffix_vs_ngram.png")
plt.close()

# ===================== FIGURE 2: Suffix vs N-gram [3,5] and [5,5] =====================
fig2, ax2 = plt.subplots(figsize=(12, 6))

# Plot bars - N-gram[3,5] on the left, N-gram[5,5] in the middle, Suffix on the right
bar_width_3bars = 0.25
ngram35_bars2 = ax2.bar(positions - bar_width_3bars, ngram35_times_specbench, bar_width_3bars,
                        label='N-gram [3,5]', color=ngram35_color, edgecolor='black', linewidth=1)
ngram55_bars2 = ax2.bar(positions, ngram55_times_specbench, bar_width_3bars,
                        label='N-gram [5,5]', color=ngram55_color, edgecolor='black', linewidth=1)
suffix_bars2 = ax2.bar(positions + bar_width_3bars, new_suffix_times_specbench, bar_width_3bars, 
                       label='Suffix', color=suffix_color, edgecolor='black', linewidth=1)

# Add value labels on top of bars
for i, (ngram35_val, ngram55_val, suffix_val) in enumerate(zip(ngram35_times_specbench, ngram55_times_specbench, new_suffix_times_specbench)):
    ax2.text(positions[i] - bar_width_3bars, ngram35_val + 0.3, f'{ngram35_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')
    ax2.text(positions[i], ngram55_val + 0.3, f'{ngram55_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')
    ax2.text(positions[i] + bar_width_3bars, suffix_val + 0.3, f'{suffix_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')

# Customize plot
ax2.set_xlabel('Concurrency Level', fontsize=16, fontweight='bold')
ax2.set_ylabel('TPOT (ms)', fontsize=16, fontweight='bold')
ax2.set_title('TPOT Comparison: Suffix and N-gram\nSpec-Bench dataset', fontsize=18, fontweight='bold')
ax2.set_xticks(positions)
ax2.set_xticklabels(concurrency_levels, fontsize=14, fontweight='bold')
ax2.tick_params(axis='y', labelsize=14)
ax2.legend(fontsize=14, frameon=True, loc='upper left')
ax2.set_ylim(0, 15)
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Save plot
plt.tight_layout()
plt.savefig('new_suffix_vs_ngram_specbench.png', format='png', dpi=300, bbox_inches='tight')
print("Saved: new_suffix_vs_ngram_specbench.png")
plt.close()

# ===================== FIGURE 3: Suffix vs N-gram [3,5] and [5,5] (blazedit) =====================
fig3, ax3 = plt.subplots(figsize=(12, 6))

# Plot bars - N-gram[3,5] on the left, N-gram[5,5] in the middle, Suffix on the right
ngram35_bars3 = ax3.bar(positions - bar_width_3bars, ngram35_times_blazedit, bar_width_3bars,
                        label='N-gram [3,5]', color=ngram35_color, edgecolor='black', linewidth=1)
ngram55_bars3 = ax3.bar(positions, ngram55_times_blazedit, bar_width_3bars,
                        label='N-gram [5,5]', color=ngram55_color, edgecolor='black', linewidth=1)
suffix_bars3 = ax3.bar(positions + bar_width_3bars, new_suffix_times_blazedit, bar_width_3bars, 
                       label='Suffix', color=suffix_color, edgecolor='black', linewidth=1)

# Add value labels on top of bars
for i, (ngram35_val, ngram55_val, suffix_val) in enumerate(zip(ngram35_times_blazedit, ngram55_times_blazedit, new_suffix_times_blazedit)):
    ax3.text(positions[i] - bar_width_3bars, ngram35_val + 0.2, f'{ngram35_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')
    ax3.text(positions[i], ngram55_val + 0.2, f'{ngram55_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')
    ax3.text(positions[i] + bar_width_3bars, suffix_val + 0.2, f'{suffix_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')

# Customize plot
ax3.set_xlabel('Concurrency Level', fontsize=16, fontweight='bold')
ax3.set_ylabel('TPOT (ms)', fontsize=16, fontweight='bold')
ax3.set_title('TPOT Comparison: Suffix and N-gram\nBlazedit dataset', fontsize=18, fontweight='bold')
ax3.set_xticks(positions)
ax3.set_xticklabels(concurrency_levels, fontsize=14, fontweight='bold')
ax3.tick_params(axis='y', labelsize=14)
ax3.legend(fontsize=14, frameon=True, loc='upper left')
ax3.set_ylim(0, 9)
ax3.grid(axis='y', linestyle='--', alpha=0.7)

# Save plot
plt.tight_layout()
plt.savefig('new_suffix_vs_ngram_blazedit.png', format='png', dpi=300, bbox_inches='tight')
print("Saved: new_suffix_vs_ngram_blazedit.png")
plt.close()
