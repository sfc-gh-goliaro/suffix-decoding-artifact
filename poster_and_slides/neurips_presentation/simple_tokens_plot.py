import numpy as np
import matplotlib.pyplot as plt

# ===================== Data =====================
# Methods to show
methods = ["EAGLE-3", "Suffix", "Suffix (hybrid)"]

# Benchmarks
benchmarks = ["Agentic workload\n(AgenticSQL)", "Open ended workload\n(SpecBench)"]

# Mean accepted tokens data
# From the original data: tokens dict
# EAGLE-3 is index 3, Suffix is index 6, Suffix (hybrid) is index 8
tokens_data = {
    "Agentic workload\n(AgenticSQL)": [3.2, 6.3, 7.5],  # EAGLE-3, Suffix, Suffix (hybrid)
    "Open ended workload\n(SpecBench)": [4.6, 1.8, 4.7],
}

# ===================== Styling =====================
tab10 = plt.get_cmap("tab10")
method_colors = [tab10(0), tab10(1), tab10(2)]

plt.rcParams.update({
    "font.size": 11,
    "axes.titlesize": 13,
    "axes.labelsize": 11,
    "legend.fontsize": 10,
})

# ===================== Plot helper function =====================
def create_plot(num_methods_to_show, fixed_ylim):
    """Create a plot showing the specified number of methods."""
    fig, ax = plt.subplots(figsize=(8, 5))
    
    n_benchmarks = len(benchmarks)
    n_methods = len(methods)
    
    bar_width = 0.25
    group_gap = 0.3
    
    # Calculate positions for each benchmark group
    group_positions = np.arange(n_benchmarks) * (n_methods * bar_width + group_gap)
    
    # Plot bars for each method
    for i, (method, color) in enumerate(zip(methods, method_colors)):
        values = [tokens_data[bench][i] for bench in benchmarks]
        positions = group_positions + i * bar_width
        
        # Show or hide based on num_methods_to_show
        if i < num_methods_to_show:
            alpha = 1.0
            show_label = True
        else:
            # Make invisible but keep the space
            alpha = 0.0
            show_label = False
        
        bars = ax.bar(
            positions, values, width=bar_width,
            label=method if show_label else None,
            color=color,
            edgecolor="white", linewidth=0.8,
            alpha=alpha,
        )
        
        # Add value labels on top of bars - only for visible bars
        if i < num_methods_to_show:
            for bar, val in zip(bars, values):
                height = bar.get_height()
                ax.text(
                    bar.get_x() + bar.get_width() / 2.0, height,
                    f'{val:.1f}',
                    ha='center', va='bottom',
                    fontsize=10,
                )
    
    # Set x-axis labels at the center of each group
    centers = group_positions + (n_methods * bar_width) / 2.0 - bar_width / 2.0
    ax.set_xticks(centers, benchmarks)
    
    # Labels and styling
    ax.set_ylabel("Mean Accepted Tokens\n(tokens/step)")
    ax.set_title("Mean Accepted Tokens per Step")
    ax.grid(axis='y', linestyle=':', alpha=0.5)
    ax.legend(title="Speculation Methods", frameon=True, fancybox=True, framealpha=0.9)
    
    # Use fixed y-axis limits
    ax.set_ylim(fixed_ylim)
    
    fig.tight_layout()
    
    return fig

# ===================== Calculate fixed y-limits =====================
# Calculate y-limits based on full data to keep them consistent across all plots
ymax = max([max(tokens_data[b]) for b in benchmarks]) * 1.15
fixed_ylim = (0, ymax)

# ===================== Generate incremental plots =====================
# Plot 1: EAGLE-3 and Suffix (linear) only (first 2 methods)
fig1 = create_plot(num_methods_to_show=2, fixed_ylim=fixed_ylim)
out_path1 = "simple_tokens_plot_1of2.png"
plt.savefig(out_path1, format="png", bbox_inches="tight", dpi=300)
print(f"Saved: {out_path1}")
plt.close(fig1)

# Plot 2: All three methods
fig2 = create_plot(num_methods_to_show=3, fixed_ylim=fixed_ylim)
out_path2 = "simple_tokens_plot_2of2.png"
plt.savefig(out_path2, format="png", bbox_inches="tight", dpi=300)
print(f"Saved: {out_path2}")
plt.close(fig2)

