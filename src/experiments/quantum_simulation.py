"""
===========================================
SIMULACIÓN CUÁNTICA Y PIC
===========================================
Explora los límites de la computación cuántica desde la perspectiva
del Principio de Incertidumbre Computacional.

Aunque la computación cuántica ofrece ventajas para ciertos problemas
(ej. factorización con Shor), el PIC predice que para problemas NP-duros
como el TSP, la barrera informacional persiste incluso para algoritmos cuánticos.
"""

import math
import random


def quantum_information_bound(T: int, max_qubits: int) -> float:
    return min(T, max_qubits)


def shor_entropy_reduction(n_bits: int) -> float:
    bits_factorization = n_bits
    return bits_factorization


def quantum_tsp_limit(n_cities: int) -> float:
    H0 = math.log2(math.factorial(n_cities - 1) // 2)
    return H0


def grover_search_speedup(n_items: int) -> float:
    return math.sqrt(n_items)


def simulate_quantum_oracle(n_qubits: int, target_state: int, shots: int = 1024):
    results = {}
    for _ in range(shots):
        meas = random.randint(0, (1 << n_qubits) - 1)
        prob = 1.0 / (1 << n_qubits)
        if meas == target_state:
            prob += 0.5
        if random.random() < prob:
            results[meas] = results.get(meas, 0) + 1
    return results


if __name__ == "__main__":
    print("=" * 60)
    print("COMPUTACIÓN CUÁNTICA Y PIC")
    print("=" * 60)

    print("\n--- Límite de Shor (Factorización) ---")
    for bits in [16, 32, 64, 128, 256]:
        ent = shor_entropy_reduction(bits)
        print(f"  n={bits:3d} bits | entropía de factorización: {ent:.1f} bits | "
              f"Shor requiere O({bits**3}) operaciones cuánticas")

    print("\n--- Límite Informacional Cuántico para TSP ---")
    for n in [10, 20, 50, 100]:
        H0 = quantum_tsp_limit(n)
        q_bound = quantum_information_bound(n**3, n)
        residual = max(H0 - q_bound, 0)
        print(f"  n={n:3d} | H0={H0:.1f} bits | info cuántica max={q_bound:.1f} | "
              f"residual={residual:.1f} bits | certificable={residual < 1e-9}")

    print("\n--- Aceleración de Grover ---")
    for n in [100, 1000, 10**6, 10**9]:
        sqrt_n = grover_search_speedup(n)
        print(f"  N={n:10d} | búsqueda clásica O(N)={n} | Grover O(√N)={sqrt_n:.0f}")

    print("\n--- Simulación de Oracle Cuántico ---")
    n_qubits = 4
    target = 7
    results = simulate_quantum_oracle(n_qubits, target, shots=2048)
    top_states = sorted(results.items(), key=lambda x: -x[1])[:5]
    print(f"  Qubits: {n_qubits}, Estado objetivo: |{target}⟩")
    for state, count in top_states:
        print(f"    |{state}⟩: {count} mediciones ({count/2048*100:.1f}%)")
