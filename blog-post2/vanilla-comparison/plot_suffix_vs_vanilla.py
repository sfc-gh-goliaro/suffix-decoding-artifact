import numpy as np
import matplotlib.pyplot as plt

# Data for spec_len = 32 only
concurrency_levels = [1, 4, 16, 64]

# First dataset: Suffix vs Unoptimized Suffix vs Vanilla (spec-bench)
vanilla_times_specbench = [5.53, 5.80, 6.75, 10.48]  # ms
new_suffix_times_specbench = [4.43, 4.70, 5.92, 10.96]  # ms
old_suffix_times_specbench = [4.46, 4.78, 6.23, 12.11]

# Second dataset: Suffix vs Unoptimized Suffix vs Vanilla (blazedit)
vanilla_times_blazedit = [5.61, 5.99, 7.46, 11.12]  # ms
new_suffix_times_blazedit = [1.71, 1.92, 2.86, 6.06]  # ms
old_suffix_times_blazedit = [1.71, 1.99, 3.02, 6.58]  # ms

# Set width of bars for 3 bars
bar_width_3 = 0.25
positions_3 = np.arange(len(concurrency_levels))

# Snowflake colors - using primary and secondary colors
# Vanilla: #FF9F36 (orange) on the left
# Unoptimized Suffix: #11567F (darker blue) in the middle
# Suffix: #29B5E8 (bright blue) on the right
vanilla_color = '#FF9F36'
unoptimized_suffix_color = '#11567F'
suffix_color = '#29B5E8'

# ===================== FIGURE 1: Suffix vs Unoptimized Suffix vs Vanilla (spec-bench) =====================
fig1, ax1 = plt.subplots(figsize=(12, 6))

# Plot bars - Vanilla on the left, Unoptimized Suffix in the middle, Suffix on the right
vanilla_bars1 = ax1.bar(positions_3 - bar_width_3, vanilla_times_specbench, bar_width_3,
                        label='Vanilla', color=vanilla_color, edgecolor='black', linewidth=1)
unoptimized_suffix_bars1 = ax1.bar(positions_3, old_suffix_times_specbench, bar_width_3,
                      label='Suffix (unoptimized)', color=unoptimized_suffix_color, edgecolor='black', linewidth=1)
suffix_bars1 = ax1.bar(positions_3 + bar_width_3, new_suffix_times_specbench, bar_width_3, 
                       label='Suffix', color=suffix_color, edgecolor='black', linewidth=1)

# Add value labels on top of bars
for i, (vanilla_val, unoptimized_suffix_val, suffix_val) in enumerate(zip(vanilla_times_specbench, old_suffix_times_specbench, new_suffix_times_specbench)):
    ax1.text(positions_3[i] - bar_width_3, vanilla_val + 0.3, f'{vanilla_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')
    ax1.text(positions_3[i], unoptimized_suffix_val + 0.3, f'{unoptimized_suffix_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')
    ax1.text(positions_3[i] + bar_width_3, suffix_val + 0.3, f'{suffix_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')

# Customize plot
ax1.set_xlabel('Concurrency Level', fontsize=16, fontweight='bold')
ax1.set_ylabel('TPOT (ms)', fontsize=16, fontweight='bold')
ax1.set_title('TPOT Comparison: Suffix vs Suffix (unoptimized) vs Vanilla\nSpec-Bench dataset', fontsize=18, fontweight='bold')
ax1.set_xticks(positions_3)
ax1.set_xticklabels(concurrency_levels, fontsize=14, fontweight='bold')
ax1.tick_params(axis='y', labelsize=14)
ax1.legend(fontsize=14, frameon=True, loc='upper left')
ax1.set_ylim(0, 15)
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Save plot
plt.tight_layout()
plt.savefig('suffix_vs_vanilla.png', format='png', dpi=300, bbox_inches='tight')
print("Saved: suffix_vs_vanilla.png")
plt.close()

# ===================== FIGURE 2: Suffix vs Unoptimized Suffix vs Vanilla (blazedit) =====================
fig2, ax2 = plt.subplots(figsize=(12, 6))

# Plot bars - Vanilla on the left, Unoptimized Suffix in the middle, Suffix on the right
vanilla_bars2 = ax2.bar(positions_3 - bar_width_3, vanilla_times_blazedit, bar_width_3,
                        label='Vanilla', color=vanilla_color, edgecolor='black', linewidth=1)
unoptimized_suffix_bars2 = ax2.bar(positions_3, old_suffix_times_blazedit, bar_width_3,
                      label='Suffix (unoptimized)', color=unoptimized_suffix_color, edgecolor='black', linewidth=1)
suffix_bars2 = ax2.bar(positions_3 + bar_width_3, new_suffix_times_blazedit, bar_width_3, 
                       label='Suffix', color=suffix_color, edgecolor='black', linewidth=1)

# Add value labels on top of bars
for i, (vanilla_val, unoptimized_suffix_val, suffix_val) in enumerate(zip(vanilla_times_blazedit, old_suffix_times_blazedit, new_suffix_times_blazedit)):
    ax2.text(positions_3[i] - bar_width_3, vanilla_val + 0.25, f'{vanilla_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')
    ax2.text(positions_3[i], unoptimized_suffix_val + 0.25, f'{unoptimized_suffix_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')
    ax2.text(positions_3[i] + bar_width_3, suffix_val + 0.25, f'{suffix_val:.2f}', 
            ha='center', va='bottom', fontsize=13, fontweight='bold')

# Customize plot
ax2.set_xlabel('Concurrency Level', fontsize=16, fontweight='bold')
ax2.set_ylabel('TPOT (ms)', fontsize=16, fontweight='bold')
ax2.set_title('TPOT Comparison: Suffix vs Suffix (unoptimized) vs Vanilla\nBlazedit dataset', fontsize=18, fontweight='bold')
ax2.set_xticks(positions_3)
ax2.set_xticklabels(concurrency_levels, fontsize=14, fontweight='bold')
ax2.tick_params(axis='y', labelsize=14)
ax2.legend(fontsize=14, frameon=True, loc='upper left')
ax2.set_ylim(0, 12)
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Save plot
plt.tight_layout()
plt.savefig('suffix_vs_vanilla_blazedit.png', format='png', dpi=300, bbox_inches='tight')
print("Saved: suffix_vs_vanilla_blazedit.png")
plt.close()

