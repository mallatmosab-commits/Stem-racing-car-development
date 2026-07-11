"""
CFD Iteration Analysis - Astra Racing STEM Car
------------------------------------------------
Analyzes drag and lift force data collected across our Ansys CFD
simulation iterations (AR-M01 through AR-M07) to identify which
body design offered the best aerodynamic performance.

Data source: our team's Ansys CFD simulation results, recorded
during the body design phase of the Astra Racing project.
"""

import matplotlib.pyplot as plt

# Real CFD results from our Ansys simulations (Drag force, Lift force)
iterations = ["AR-M01", "AR-M02", "AR-M03", "AR-M04", "AR-M05", "AR-M06", "AR-M07"]
drag_force = [0.314233, 0.250334, 0.220369, 0.239762, 0.224150, 0.225613, 0.209763]
lift_force = [-0.135098, 0.043523, 0.056658, 0.080045, 0.085715, -0.046079, 0.062014]

notes = {
    "AR-M01": "Baseline / ground truth design",
    "AR-M03": "Slimmer sidepods, smoothed CO2 holder",
    "AR-M06": "Regionals car",
    "AR-M07": "Nationals car (final design)",
}


def best_drag_iteration():
    """Return the iteration with the lowest drag force."""
    min_index = drag_force.index(min(drag_force))
    return iterations[min_index], drag_force[min_index]


def drag_reduction_from_baseline():
    """Compute % drag reduction from AR-M01 to AR-M07."""
    baseline = drag_force[0]
    final = drag_force[-1]
    return (baseline - final) / baseline * 100


def plot_results():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5))

    ax1.plot(iterations, drag_force, marker="o", color="#e0b400")
    ax1.set_title("Drag Force per Iteration")
    ax1.set_ylabel("Drag Force")
    ax1.grid(alpha=0.3)

    ax2.plot(iterations, lift_force, marker="o", color="#2b3a67")
    ax2.axhline(0, color="gray", linewidth=0.8)
    ax2.set_title("Lift Force per Iteration")
    ax2.set_ylabel("Lift Force")
    ax2.grid(alpha=0.3)

    fig.suptitle("Astra Racing — CFD Iteration Results (Body Design)")
    plt.tight_layout()
    plt.savefig("cfd_results.png", dpi=150)
    print("Saved chart to cfd_results.png")


if __name__ == "__main__":
    best_name, best_val = best_drag_iteration()
    reduction = drag_reduction_from_baseline()

    print("=== Astra Racing CFD Iteration Analysis ===\n")
    for i, name in enumerate(iterations):
        note = f" ({notes[name]})" if name in notes else ""
        print(f"{name}: drag={drag_force[i]:.6f}, lift={lift_force[i]:.6f}{note}")

    print(f"\nLowest-drag iteration: {best_name} (drag = {best_val:.6f})")
    print(f"Drag reduced by {reduction:.1f}% from AR-M01 to AR-M07")

    plot_results()
