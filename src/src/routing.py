"""Utilities for checking quantum circuit routing connectivity."""

from collections import deque


def is_connected(num_qubits: int, coupling_map: list[tuple[int, int]]) -> bool:
    """Check whether all qubits are connected in the coupling graph."""
    if num_qubits <= 0:
        return False

    graph = {qubit: set() for qubit in range(num_qubits)}

    for a, b in coupling_map:
        if a not in graph or b not in graph:
            raise ValueError("Coupling map contains an invalid qubit index.")
        graph[a].add(b)
        graph[b].add(a)

    visited = {0}
    queue = deque([0])

    while queue:
        current = queue.popleft()
        for neighbor in graph[current] - visited:
            visited.add(neighbor)
            queue.append(neighbor)

    return len(visited) == num_qubits
