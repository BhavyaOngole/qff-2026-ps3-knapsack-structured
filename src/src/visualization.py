"""Visualization helpers for processor comparison metrics."""

import matplotlib.pyplot as plt


def plot_processor_comparison(metrics_a: dict, metrics_b: dict) -> None:
    """Plot the connectivity metrics of two processors."""

    labels = ["Processor A", "Processor B"]
    connections = [
        metrics_a["num_connections"],
        metrics_b["num_connections"],
    ]
    connectivity = [
        metrics_a["connectivity"],
        metrics_b["connectivity"],
    ]

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    axes[0].bar(labels, connections)
    axes[0].set_title("Number of Connections")
    axes[0].set_ylabel("Connections")

    axes[1].bar(labels, connectivity)
    axes[1].set_title("Connectivity")
    axes[1].set_ylabel("Connectivity Score")
    axes[1].set_ylim(0, 1)

    fig.tight_layout()
    plt.show()
