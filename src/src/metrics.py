"""Metrics for comparing quantum processor configurations."""


def calculate_metrics(
    num_qubits: int,
    coupling_map: list[tuple[int, int]],
) -> dict:
    """Calculate basic connectivity metrics."""

    if num_qubits <= 0:
        raise ValueError("num_qubits must be positive.")

    edges = set()
    for a, b in coupling_map:
        if not (0 <= a < num_qubits and 0 <= b < num_qubits):
            raise ValueError("Invalid qubit index in coupling map.")
        if a != b:
            edges.add(tuple(sorted((a, b))))

    possible_edges = num_qubits * (num_qubits - 1) / 2
    connectivity = len(edges) / possible_edges if possible_edges else 0.0

    return {
        "num_qubits": num_qubits,
        "num_connections": len(edges),
        "connectivity": connectivity,
    }
