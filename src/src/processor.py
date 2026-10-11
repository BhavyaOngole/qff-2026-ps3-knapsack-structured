"""Processor configuration and comparison utilities."""

from dataclasses import dataclass


@dataclass
class Processor:
    """Represent a quantum processor's basic configuration."""

    name: str
    num_qubits: int
    coupling_map: list[tuple[int, int]]


def compare_processors(processor_a: Processor, processor_b: Processor) -> dict:
    """Compare two processor configurations."""

    return {
        "processor_a": processor_a.name,
        "processor_b": processor_b.name,
        "processor_a_qubits": processor_a.num_qubits,
        "processor_b_qubits": processor_b.num_qubits,
        "processor_a_connections": len(processor_a.coupling_map),
        "processor_b_connections": len(processor_b.coupling_map),
    }
