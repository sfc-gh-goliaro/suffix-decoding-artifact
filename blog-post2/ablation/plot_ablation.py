import numpy as np
import matplotlib.pyplot as plt

# Data from the ablation study
methods = ['Baseline', '+Custom Hashmap', '+Custom Hashmap\n+Double Linked List']
spec_times = [27.5, 8.10, 3.72]  # us (microseconds)
update_times = [3.17, 2.06, 2.60]  # us (microseconds)
memory = [671, 292, 433]  # MB

# Snowflake colors - using colors from the palette
# Use different colors for each method
method_colors = ['#11567F', '#7D44CF', '#29B5E8']  # darker blue, purple, bright blue

# Create figure with two subplots side by side
# Use width_ratios to make left plot 2x wider than right plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'width_ratios': [2, 1]})

# Set width of bars
bar_width = 0.25
metrics = ['Spec\ntime/token', 'Update\ntime/token']
x = np.arange(len(metrics))

# ===================== LEFT PLOT: Speculation and Update Time =====================
# Plot bars grouped by metric
for i, method in enumerate(methods):
    offset = (i - 1) * bar_width
    values = [spec_times[i], update_times[i]]
    bars = ax1.bar(x + offset, values, bar_width, 
                   label=method, color=method_colors[i], edgecolor='black', linewidth=1)
    
    # Add speedup labels on top of bars
    for j, val in enumerate(values):
        baseline_val = spec_times[0] if j == 0 else update_times[0]
        if i == 0:
            # Baseline - show 1.0x
            label = '1.0x'
        else:
            # Calculate speedup
            speedup = baseline_val / val
            label = f'{speedup:.1f}x'
        ax1.text(x[j] + offset, val + 0.8, label, 
                ha='center', va='bottom', fontsize=11, fontweight='bold')

# Customize left plot
ax1.set_ylabel('Time (μs)', fontsize=16, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(metrics, fontsize=14, fontweight='bold')
ax1.tick_params(axis='y', labelsize=14)
ax1.legend(fontsize=12, frameon=True, loc='upper right')
ax1.set_ylim(0, 32)
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# ===================== RIGHT PLOT: Memory Usage =====================
# Plot bars grouped by metric (only one metric: memory)
bar_width = 0.2
x_mem = np.arange(1)
for i, method in enumerate(methods):
    offset = (i - 1) * bar_width
    bars = ax2.bar(x_mem + offset, [memory[i]], bar_width, 
                   label=method, color=method_colors[i], edgecolor='black', linewidth=1)
    
    # Add speedup labels on top of bars (memory reduction factor)
    if i == 0:
        # Baseline - show 1.0x
        label = '1.0x'
    else:
        # Calculate memory reduction (baseline / current)
        reduction = memory[0] / memory[i]
        label = f'{reduction:.1f}x'
    ax2.text(x_mem[0] + offset, memory[i] + 20, label, 
            ha='center', va='bottom', fontsize=11, fontweight='bold')

# Customize right plot
ax2.set_ylabel('Memory (MB)', fontsize=16, fontweight='bold')
ax2.set_xticks(x_mem)
ax2.set_xticklabels(['Memory Consumption'], fontsize=14, fontweight='bold')
ax2.tick_params(axis='y', labelsize=14)
ax2.legend(fontsize=12, frameon=True, loc='upper right')
ax2.set_ylim(0, 750)
ax2.set_xlim(-0.4, 0.4)  # Adjust x-axis limits to make bars same visual width as left plot
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Add overall title
fig.suptitle('Impact of Optimizations on Suffix Decoding Operation Performance', fontsize=18, fontweight='bold', y=0.98)

# Save plot
plt.tight_layout()
plt.savefig('ablation_comparison.png', format='png', dpi=300, bbox_inches='tight')
print("Saved: ablation_comparison.png")
plt.close()

# ===================== CREATE PARTIAL PLOT (without third method) =====================
# This is for PowerPoint animation - shows only first two methods
# Third method is plotted in transparent colors (not visible) to maintain spacing

# Create figure with two subplots side by side
# Use width_ratios to make left plot 2x wider than right plot
fig2, (ax1_partial, ax2_partial) = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'width_ratios': [2, 1]})

# Set width of bars
bar_width = 0.25
metrics = ['Spec\ntime/token', 'Update\ntime/token']
x = np.arange(len(metrics))

# ===================== LEFT PLOT: Speculation and Update Time =====================
# Plot bars grouped by metric
for i, method in enumerate(methods):
    offset = (i - 1) * bar_width
    values = [spec_times[i], update_times[i]]
    
    # Only show first two methods visibly
    if i < 2:
        bars = ax1_partial.bar(x + offset, values, bar_width, 
                       label=method, color=method_colors[i], edgecolor='black', linewidth=1)
        
        # Add speedup labels on top of bars
        for j, val in enumerate(values):
            baseline_val = spec_times[0] if j == 0 else update_times[0]
            if i == 0:
                # Baseline - show 1.0x
                label = '1.0x'
            else:
                # Calculate speedup
                speedup = baseline_val / val
                label = f'{speedup:.1f}x'
            ax1_partial.text(x[j] + offset, val + 0.8, label, 
                    ha='center', va='bottom', fontsize=11, fontweight='bold')
    else:
        # Plot third method transparently (invisible but maintains spacing)
        bars = ax1_partial.bar(x + offset, values, bar_width, 
                       color='none', edgecolor='none', linewidth=0)

# Customize left plot
ax1_partial.set_ylabel('Time (μs)', fontsize=16, fontweight='bold')
ax1_partial.set_xticks(x)
ax1_partial.set_xticklabels(metrics, fontsize=14, fontweight='bold')
ax1_partial.tick_params(axis='y', labelsize=14)
ax1_partial.legend(fontsize=12, frameon=True, loc='upper right')
ax1_partial.set_ylim(0, 32)
ax1_partial.grid(axis='y', linestyle='--', alpha=0.7)

# ===================== RIGHT PLOT: Memory Usage =====================
# Plot bars grouped by metric (only one metric: memory)
bar_width = 0.2
x_mem = np.arange(1)
for i, method in enumerate(methods):
    offset = (i - 1) * bar_width
    
    # Only show first two methods visibly
    if i < 2:
        bars = ax2_partial.bar(x_mem + offset, [memory[i]], bar_width, 
                       label=method, color=method_colors[i], edgecolor='black', linewidth=1)
        
        # Add speedup labels on top of bars (memory reduction factor)
        if i == 0:
            # Baseline - show 1.0x
            label = '1.0x'
        else:
            # Calculate memory reduction (baseline / current)
            reduction = memory[0] / memory[i]
            label = f'{reduction:.1f}x'
        ax2_partial.text(x_mem[0] + offset, memory[i] + 20, label, 
                ha='center', va='bottom', fontsize=11, fontweight='bold')
    else:
        # Plot third method transparently (invisible but maintains spacing)
        bars = ax2_partial.bar(x_mem + offset, [memory[i]], bar_width, 
                       color='none', edgecolor='none', linewidth=0)

# Customize right plot
ax2_partial.set_ylabel('Memory (MB)', fontsize=16, fontweight='bold')
ax2_partial.set_xticks(x_mem)
ax2_partial.set_xticklabels(['Memory Consumption'], fontsize=14, fontweight='bold')
ax2_partial.tick_params(axis='y', labelsize=14)
ax2_partial.legend(fontsize=12, frameon=True, loc='upper right')
ax2_partial.set_ylim(0, 750)
ax2_partial.set_xlim(-0.4, 0.4)  # Adjust x-axis limits to make bars same visual width as left plot
ax2_partial.grid(axis='y', linestyle='--', alpha=0.7)

# Add overall title
fig2.suptitle('Impact of Optimizations on Suffix Decoding Operation Performance', fontsize=18, fontweight='bold', y=0.98)

# Save partial plot
plt.tight_layout()
plt.savefig('ablation_comparison_partial.png', format='png', dpi=300, bbox_inches='tight')
print("Saved: ablation_comparison_partial.png")
plt.close()

