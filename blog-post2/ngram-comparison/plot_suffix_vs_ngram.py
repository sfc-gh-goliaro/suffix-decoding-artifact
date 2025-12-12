import numpy as np
import matplotlib.pyplot as plt

# Data for spec_len = 32 only
concurrency_levels = [1, 4, 16, 64]

# First dataset: Suffix vs N-gram (old unoptimized)
# Use best of ngram [3,5] and [5,5] for each concurrency level
old_suffix_times = [4.33, 4.76, 6.20, 12.03]  # ms (suffix_old)
ngram35_times_old = [5.07, 5.43, 6.73, 13.07]  # ms (ngram [3,5])
ngram55_times_old = [5.49, 5.80, 6.87, 11.55]  # ms (ngram [5,5])
# Best N-gram for each concurrency: min of [3,5] and [5,5]
ngram_times_old = [min(ngram35_times_old[i], ngram55_times_old[i]) for i in range(len(concurrency_levels))]

# Second dataset: Suffix vs N-gram [3,5] and N-gram [5,5] (spec-bench)
# Using suffix_new (depth=24) from results_summary.md
vanilla_times_specbench = [5.53, 5.78, 6.73, 10.36]  # ms
new_suffix_times_specbench = [4.32, 4.62, 5.70, 10.37]  # ms (suffix_new depth=24)
ngram35_times_specbench = [5.07, 5.43, 6.73, 13.07]  # ms
ngram55_times_specbench = [5.49, 5.80, 6.87, 11.55]  # ms


# Third dataset: Suffix vs N-gram [3,5] and N-gram [5,5] (blazedit)
# Using suffix_new (depth=24) from results_summary.md
vanilla_times_blazedit = [5.62, 5.98, 7.44, 10.96]  # ms
new_suffix_times_blazedit = [1.80, 2.01, 2.79, 5.58]  # ms (suffix_new depth=24)
ngram35_times_blazedit = [1.84, 2.16, 3.37, 7.99]  # ms
ngram55_times_blazedit = [2.15, 2.49, 3.54, 7.33]  # ms

# Set width of bars
bar_width = 0.35
positions = np.arange(len(concurrency_levels))

# Colors - grey for baselines (darker to lighter left to right), different blues for SuffixDecoding
# Vanilla: darkest grey (leftmost)
# Ngram [3,5]: medium grey
# Ngram [5,5]: lighter grey (rightmost grey)
# SuffixDecoding (unoptimized): #29B5E8 (bright blue)
# SuffixDecoding (optimized): #29B5E8 (bright blue)
vanilla_color = '#4d4d4d'  # darkest grey
ngram35_color = '#808080'  # medium grey
ngram55_color = '#b3b3b3'  # lighter grey
suffix_color_old = '#29B5E8'  # for unoptimized version (changed from #11567F)
suffix_color = '#29B5E8'  # for optimized version

# ===================== FIGURE 1: Suffix (unoptimized) vs N-gram =====================
fig1, ax1 = plt.subplots(figsize=(12, 6))

# Plot bars - N-gram (best) on the left, SuffixDecoding (unoptimized) on the right
ngram_bars = ax1.bar(positions - bar_width/2, ngram_times_old, bar_width,
                     label='N-gram (best of [3,5] and [5,5])', color=ngram35_color, edgecolor='black', linewidth=1)
suffix_bars = ax1.bar(positions + bar_width/2, old_suffix_times, bar_width, 
                      label='SuffixDecoding (unoptimized)', color=suffix_color_old, edgecolor='black', linewidth=1)

# Add value labels on top of bars
for i, (suffix_val, ngram_val) in enumerate(zip(old_suffix_times, ngram_times_old)):
    ax1.text(positions[i] - bar_width/2, ngram_val + 0.3, f'{ngram_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')
    ax1.text(positions[i] + bar_width/2, suffix_val + 0.3, f'{suffix_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')

# Customize plot
ax1.set_xlabel('Concurrency Level', fontsize=16, fontweight='bold')
ax1.set_ylabel('TPOT (ms)', fontsize=16, fontweight='bold')
ax1.set_title('TPOT Comparison: SuffixDecoding (unoptimized) and N-gram (best)\nSpec-Bench dataset', fontsize=18, fontweight='bold')
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

# Plot bars - Vanilla, N-gram[3,5], N-gram[5,5], and SuffixDecoding
bar_width_4bars = 0.20
vanilla_bars2 = ax2.bar(positions - 1.5*bar_width_4bars, vanilla_times_specbench, bar_width_4bars,
                        label='Vanilla', color=vanilla_color, edgecolor='black', linewidth=1)
ngram35_bars2 = ax2.bar(positions - 0.5*bar_width_4bars, ngram35_times_specbench, bar_width_4bars,
                        label='N-gram [3,5]', color=ngram35_color, edgecolor='black', linewidth=1)
ngram55_bars2 = ax2.bar(positions + 0.5*bar_width_4bars, ngram55_times_specbench, bar_width_4bars,
                        label='N-gram [5,5]', color=ngram55_color, edgecolor='black', linewidth=1)
suffix_bars2 = ax2.bar(positions + 1.5*bar_width_4bars, new_suffix_times_specbench, bar_width_4bars, 
                       label='SuffixDecoding', color=suffix_color, edgecolor='black', linewidth=1)

# Add speedup labels on top of bars (relative to vanilla)
for i, (vanilla_val, ngram35_val, ngram55_val, suffix_val) in enumerate(zip(vanilla_times_specbench, ngram35_times_specbench, ngram55_times_specbench, new_suffix_times_specbench)):
    # Calculate speedups relative to vanilla
    vanilla_speedup = 1.0
    ngram35_speedup = vanilla_val / ngram35_val
    ngram55_speedup = vanilla_val / ngram55_val
    suffix_speedup = vanilla_val / suffix_val
    
    ax2.text(positions[i] - 1.5*bar_width_4bars, vanilla_val + 0.3, f'{vanilla_speedup:.1f}x', 
            ha='center', va='bottom', fontsize=11, fontweight='bold')
    ax2.text(positions[i] - 0.5*bar_width_4bars, ngram35_val + 0.3, f'{ngram35_speedup:.2f}x', 
            ha='center', va='bottom', fontsize=11, fontweight='bold')
    ax2.text(positions[i] + 0.5*bar_width_4bars, ngram55_val + 0.3, f'{ngram55_speedup:.2f}x', 
            ha='center', va='bottom', fontsize=11, fontweight='bold')
    ax2.text(positions[i] + 1.5*bar_width_4bars, suffix_val + 0.3, f'{suffix_speedup:.2f}x', 
            ha='center', va='bottom', fontsize=11, fontweight='bold')

# Customize plot
ax2.set_xlabel('Concurrency Level', fontsize=16, fontweight='bold')
ax2.set_ylabel('TPOT (ms)', fontsize=16, fontweight='bold')
ax2.set_title('TPOT Comparison: SuffixDecoding and N-gram\nSpec-Bench dataset', fontsize=18, fontweight='bold')
ax2.set_xticks(positions)
ax2.set_xticklabels(concurrency_levels, fontsize=14, fontweight='bold')
ax2.tick_params(axis='y', labelsize=14)
ax2.legend(fontsize=14, frameon=True, loc='upper left')
ax2.set_ylim(0, 16)  # Max value is 13.14, need room for labels
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Save plot
plt.tight_layout()
plt.savefig('new_suffix_vs_ngram_specbench.png', format='png', dpi=300, bbox_inches='tight')
print("Saved: new_suffix_vs_ngram_specbench.png")

# Print speedup comparisons for Spec-Bench
print("\n=== Spec-Bench: SuffixDecoding speedup vs N-gram baselines ===")
for i, conc in enumerate(concurrency_levels):
    suffix_vs_ngram35 = ngram35_times_specbench[i] / new_suffix_times_specbench[i]
    suffix_vs_ngram55 = ngram55_times_specbench[i] / new_suffix_times_specbench[i]
    best_ngram = min(ngram35_times_specbench[i], ngram55_times_specbench[i])
    suffix_vs_best = best_ngram / new_suffix_times_specbench[i]
    print(f"Concurrency {conc}: vs N-gram[3,5]={suffix_vs_ngram35:.2f}x, vs N-gram[5,5]={suffix_vs_ngram55:.2f}x, vs best={suffix_vs_best:.2f}x")

plt.close()

# ===================== FIGURE 3: Suffix vs N-gram [3,5] and [5,5] (blazedit) =====================
fig3, ax3 = plt.subplots(figsize=(12, 6))

# Plot bars - Vanilla, N-gram[3,5], N-gram[5,5], and SuffixDecoding
vanilla_bars3 = ax3.bar(positions - 1.5*bar_width_4bars, vanilla_times_blazedit, bar_width_4bars,
                        label='Vanilla', color=vanilla_color, edgecolor='black', linewidth=1)
ngram35_bars3 = ax3.bar(positions - 0.5*bar_width_4bars, ngram35_times_blazedit, bar_width_4bars,
                        label='N-gram [3,5]', color=ngram35_color, edgecolor='black', linewidth=1)
ngram55_bars3 = ax3.bar(positions + 0.5*bar_width_4bars, ngram55_times_blazedit, bar_width_4bars,
                        label='N-gram [5,5]', color=ngram55_color, edgecolor='black', linewidth=1)
suffix_bars3 = ax3.bar(positions + 1.5*bar_width_4bars, new_suffix_times_blazedit, bar_width_4bars, 
                       label='SuffixDecoding', color=suffix_color, edgecolor='black', linewidth=1)

# Add speedup labels on top of bars (relative to vanilla)
for i, (vanilla_val, ngram35_val, ngram55_val, suffix_val) in enumerate(zip(vanilla_times_blazedit, ngram35_times_blazedit, ngram55_times_blazedit, new_suffix_times_blazedit)):
    # Calculate speedups relative to vanilla
    vanilla_speedup = 1.0
    ngram35_speedup = vanilla_val / ngram35_val
    ngram55_speedup = vanilla_val / ngram55_val
    suffix_speedup = vanilla_val / suffix_val
    
    ax3.text(positions[i] - 1.5*bar_width_4bars, vanilla_val + 0.2, f'{vanilla_speedup:.1f}x', 
            ha='center', va='bottom', fontsize=11, fontweight='bold')
    ax3.text(positions[i] - 0.5*bar_width_4bars, ngram35_val + 0.2, f'{ngram35_speedup:.2f}x', 
            ha='center', va='bottom', fontsize=11, fontweight='bold')
    ax3.text(positions[i] + 0.5*bar_width_4bars, ngram55_val + 0.2, f'{ngram55_speedup:.2f}x', 
            ha='center', va='bottom', fontsize=11, fontweight='bold')
    ax3.text(positions[i] + 1.5*bar_width_4bars, suffix_val + 0.2, f'{suffix_speedup:.2f}x', 
            ha='center', va='bottom', fontsize=11, fontweight='bold')

# Customize plot
ax3.set_xlabel('Concurrency Level', fontsize=16, fontweight='bold')
ax3.set_ylabel('TPOT (ms)', fontsize=16, fontweight='bold')
ax3.set_title('TPOT Comparison: SuffixDecoding and N-gram\nBlazedit dataset', fontsize=18, fontweight='bold')
ax3.set_xticks(positions)
ax3.set_xticklabels(concurrency_levels, fontsize=14, fontweight='bold')
ax3.tick_params(axis='y', labelsize=14)
ax3.legend(fontsize=14, frameon=True, loc='upper left')
ax3.set_ylim(0, 13)  # Max value is 11.12, need room for labels
ax3.grid(axis='y', linestyle='--', alpha=0.7)

# Save plot
plt.tight_layout()
plt.savefig('new_suffix_vs_ngram_blazedit.png', format='png', dpi=300, bbox_inches='tight')
print("Saved: new_suffix_vs_ngram_blazedit.png")

# Print speedup comparisons for Blazedit
print("\n=== Blazedit: SuffixDecoding speedup vs N-gram baselines ===")
for i, conc in enumerate(concurrency_levels):
    suffix_vs_ngram35 = ngram35_times_blazedit[i] / new_suffix_times_blazedit[i]
    suffix_vs_ngram55 = ngram55_times_blazedit[i] / new_suffix_times_blazedit[i]
    best_ngram = min(ngram35_times_blazedit[i], ngram55_times_blazedit[i])
    suffix_vs_best = best_ngram / new_suffix_times_blazedit[i]
    print(f"Concurrency {conc}: vs N-gram[3,5]={suffix_vs_ngram35:.2f}x, vs N-gram[5,5]={suffix_vs_ngram55:.2f}x, vs best={suffix_vs_best:.2f}x")

plt.close()
