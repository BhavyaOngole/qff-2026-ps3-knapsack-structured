from itertools import product


def solve_knapsack(weights, values, capacity):
    """
    Solve the 0-1 knapsack problem by checking every combination.
    Each item can be selected at most once.
    """
    if len(weights) != len(values):
        raise ValueError("Weights and values must have equal lengths.")

    if capacity < 0 or any(w < 0 for w in weights):
        raise ValueError("Capacity and weights must be non-negative.")

    if any(v < 0 for v in values):
        raise ValueError("Values must be non-negative.")

    best_value = 0
    best_weight = 0
    best_selection = [0] * len(weights)

    for selection in product([0, 1], repeat=len(weights)):
        total_weight = sum(
            selection[i] * weights[i] for i in range(len(weights))
        )
        total_value = sum(
            selection[i] * values[i] for i in range(len(values))
        )

        if total_weight <= capacity and total_value > best_value:
            best_value = total_value
            best_weight = total_weight
            best_selection = list(selection)

    return {
        "selection": best_selection,
        "total_weight": best_weight,
        "total_value": best_value,
    }
