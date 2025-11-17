import numpy as np
import matplotlib.pyplot as plt

# ===================== Raw data (unchanged) =====================
raw_baselines = [
    "Vanilla",
    "Eagle",
    "Eagle 2",
    "Eagle 3",
    "PLD",
    "Token Recycling",
    "Suffix (linear)",
    "Suffix (tree)",
    "Hybrid (linear)",
    "Hybrid (tree)",
]

bench_order_keys = ["AgenticSQL", "SWE-Bench", "Spec-Bench"]
bench_order_labels = ["AgenticSQL", "SWE-Bench", "SpecBench"]

speedup = {
    "Spec-Bench": [1.0, 1.8, 1.8, 2.4, 1.4, 2.2, 1.7, 1.7, 2.5, 2.5],
    "AgenticSQL": [1.0, 1.6, 1.9, 1.6, 2.1, 2.7, 5.3, 5.2, 3.8, 4.1],
    "SWE-Bench":  [1.0, np.nan, np.nan, np.nan, 1.5, 1.4, 2.5, 2.4, np.nan, np.nan],
}

tokens = {
    "Spec-Bench": [1.0, 3.1, 3.5, 4.6, 1.6, 2.5, 1.8, 1.8, 4.6, 4.7],
    "AgenticSQL": [1.0, 2.9, 3.6, 3.2, 2.4, 3.2, 6.3, 6.2, 7.3, 7.5],
    "SWE-Bench":  [1.0, np.nan, np.nan, np.nan, 3.2, 3.1, 7.8, 7.6, np.nan, np.nan],
}

# ===================== Reduction to 5 bars =====================
# Groups -> indices in raw_baselines
group_indices = {
    "Vanilla": [0],
    "EAGLE-{1,2,3}": [1, 2, 3],
    "Model-free": [4, 5],
    "Suffix": [6, 7],
    "Suffix (hybrid)": [8, 9],
}
series_labels = ["Vanilla", "EAGLE-{1,2,3}", "Model-free", "Suffix", "Suffix (hybrid)"]

def reduce_groups(data_dict):
    """For each benchmark, take the max (ignoring NaNs) within each group."""
    out = {}
    for bench, arr in data_dict.items():
        arr = np.array(arr, dtype=float)
        reduced = []
        for lbl in series_labels:
            sel = arr[group_indices[lbl]]
            if np.isnan(sel).all():
                reduced.append(np.nan)
            else:
                reduced.append(np.nanmax(sel))
        out[bench] = reduced
    return out

speedup5 = reduce_groups(speedup)
tokens5  = reduce_groups(tokens)

# ===================== Styling =====================
# Professional palette: neutral gray for Vanilla, then Tab10 for the rest
tab10 = plt.get_cmap("tab10")
series_colors = ["0.6", tab10(0), tab10(1), tab10(2), tab10(3)]

plt.rcParams.update({
    "font.size": 10,
    "axes.titlesize": 12,
    "axes.labelsize": 10,
    "legend.fontsize": 9,
})

def _nanmax_dict(d):
    vals = []
    for _, v in d.items():
        a = np.array(v, dtype=float)
        a = a[~np.isnan(a)]
        if a.size:
            vals.append(a.max())
    return max(vals) if vals else 1.0

# ===================== Plot helper =====================
def plot_grouped(ax, data_by_bench, title, ylabel, annotate_fmt, num_bars_to_show=5, fixed_ylim=None, highlight_our_results=False):
    """
    Plot grouped bar chart.
    
    Args:
        num_bars_to_show: How many bars to actually show (1-5). Others are invisible.
        fixed_ylim: Tuple (ymin, ymax) to fix y-axis limits across all plots.
        highlight_our_results: If True, highlight the Suffix and Suffix (hybrid) bars.
    """
    n_groups = len(bench_order_keys)
    n_series = len(series_labels)

    bar_w = 0.75 / n_series
    group_gap = 0.2  # space between groups

    group_offsets = np.arange(n_groups) * (n_series * bar_w + group_gap)
    xs = [group_offsets + i * bar_w for i in range(n_series)]

    # Use fixed ylim if provided, otherwise compute
    if fixed_ylim:
        ax.set_ylim(fixed_ylim)
    else:
        ymax = _nanmax_dict(data_by_bench)
        ax.set_ylim(0, ymax * 1.12)

    # Indices for our results (Suffix and Suffix (hybrid))
    our_results_indices = [3, 4]  # Suffix is index 3, Suffix (hybrid) is index 4

    # Draw bars per series
    for i, (label, color) in enumerate(zip(series_labels, series_colors)):
        vals = [data_by_bench[b][i] for b in bench_order_keys]
        
        # Show or hide based on num_bars_to_show
        if i < num_bars_to_show:
            alpha = 1.0
            show_label = True
        else:
            # Make invisible but keep the space
            alpha = 0.0
            show_label = False
        
        # Highlighting for our results - keep normal styling
        is_our_result = i in our_results_indices
        edgecolor = "white"
        linewidth = 0.6
            
        bars = ax.bar(
            xs[i], vals, width=bar_w,
            label=label if show_label else None,
            color=color,
            edgecolor=edgecolor,
            linewidth=linewidth,
            alpha=alpha,
        )

        # Labels (centered above each bar) or red X for missing - only for visible bars
        if i < num_bars_to_show:
            y_offset = (ax.get_ylim()[1] - ax.get_ylim()[0]) * 0.015
            for rect, v in zip(bars.patches, vals):
                cx = rect.get_x() + rect.get_width() / 2.0
                if np.isnan(v):
                    ax.plot(cx, ax.get_ylim()[0] + y_offset * 2.0,
                            marker='x', color='red', markersize=8, mew=1.8)
                else:
                    # Make text bold for our results
                    if highlight_our_results and is_our_result:
                        fontweight = 'bold'
                        fontsize = 10
                    else:
                        fontweight = 'normal'
                        fontsize = 9
                    
                    # Add star emoji for the biggest speedup (5.3x)
                    text_content = annotate_fmt(v)
                    if highlight_our_results and title == "Speculative Speedups over Vanilla Decoding" and abs(v - 5.3) < 0.01:
                        text_content = "★ " + text_content
                    
                    ax.text(
                        cx, v + y_offset,
                        text_content,
                        ha="center", va="bottom",
                        fontsize=fontsize,
                        fontweight=fontweight,
                    )

    centers = group_offsets + (n_series * bar_w) / 2.0
    ax.set_xticks(centers, bench_order_labels)
    ax.set_title(title, pad=8)
    ax.set_xlabel("Benchmarks")
    ax.set_ylabel(ylabel)
    ax.grid(axis='y', linestyle=':', alpha=0.5)
    
    # Legend only shows visible bars
    ax.legend(ncols=3, title="Speculation Methods", frameon=True, fancybox=True, framealpha=0.9)

# ===================== Compute fixed y-limits =====================
# Calculate y-limits based on full data to keep them consistent across all plots
speedup_ymax = _nanmax_dict(speedup5) * 1.12
tokens_ymax = _nanmax_dict(tokens5) * 1.12

# ===================== Generate 5 progressive plots =====================
for num_bars in range(1, 6):
    fig = plt.figure(figsize=(10.5, 6.2))
    
    # Enable highlighting only for the final plot (5of5)
    highlight = (num_bars == 5)
    
    # Top: Speedups
    ax1 = fig.add_subplot(2, 1, 1)
    plot_grouped(
        ax1,
        speedup5,
        title="Speculative Speedups over Vanilla Decoding",
        ylabel="Speedup (×)",
        annotate_fmt=lambda v: f"{v:.1f}x",
        num_bars_to_show=num_bars,
        fixed_ylim=(0, speedup_ymax),
        highlight_our_results=highlight,
    )
    
    # Bottom: Mean accepted tokens per step
    ax2 = fig.add_subplot(2, 1, 2)
    plot_grouped(
        ax2,
        tokens5,
        title="Mean Accepted Tokens per Step",
        ylabel="Mean Accepted Tokens\n(tokens/step)",
        annotate_fmt=lambda v: f"{v:.1f}",
        num_bars_to_show=num_bars,
        fixed_ylim=(0, tokens_ymax),
        highlight_our_results=highlight,
    )
    
    fig.tight_layout()
    
    # Save to PNG with progressive numbering
    out_path = f"benchmark_progressive_{num_bars}of5.png"
    plt.savefig(out_path, format="png", bbox_inches="tight", dpi=300)
    print(f"Saved: {out_path}")
    plt.close(fig)
