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


def cota_informacion_cuantica(T: int, max_qubits: int) -> float:
    return min(T, max_qubits)


def reduccion_entropia_shor(n_bits: int) -> float:
    return n_bits


def limite_tsp_cuantico(n_ciudades: int) -> float:
    H0 = math.log2(math.factorial(n_ciudades - 1) // 2)
    return H0


def aceleracion_grover(n_elementos: int) -> float:
    return math.sqrt(n_elementos)


def simular_oraculo_cuantico(n_qubits: int, estado_objetivo: int, mediciones: int = 1024):
    resultados = {}
    for _ in range(mediciones):
        medida = random.randint(0, (1 << n_qubits) - 1)
        prob = 1.0 / (1 << n_qubits)
        if medida == estado_objetivo:
            prob += 0.5
        if random.random() < prob:
            resultados[medida] = resultados.get(medida, 0) + 1
    return resultados


if __name__ == "__main__":
    print("=" * 60)
    print("COMPUTACIÓN CUÁNTICA Y PIC")
    print("=" * 60)

    print("\n--- Límite de Shor (Factorización) ---")
    for bits in [16, 32, 64, 128, 256]:
        ent = reduccion_entropia_shor(bits)
        print(f"  n={bits:3d} bits | entropía de factorización: {ent:.1f} bits | "
              f"Shor requiere O({bits**3}) operaciones cuánticas")

    print("\n--- Límite Informacional Cuántico para TSP ---")
    for n in [10, 20, 50, 100]:
        H0 = limite_tsp_cuantico(n)
        cota_q = cota_informacion_cuantica(n**3, n)
        residual = max(H0 - cota_q, 0)
        print(f"  n={n:3d} | H0={H0:.1f} bits | info cuántica max={cota_q:.1f} | "
              f"residual={residual:.1f} bits | certificable={residual < 1e-9}")

    print("\n--- Aceleración de Grover ---")
    for n in [100, 1000, 10**6, 10**9]:
        raiz = aceleracion_grover(n)
        print(f"  N={n:10d} | búsqueda clásica O(N)={n} | Grover O(√N)={raiz:.0f}")

    print("\n--- Simulación de Oracle Cuántico ---")
    n_qubits = 4
    objetivo = 7
    resultados = simular_oraculo_cuantico(n_qubits, objetivo, mediciones=2048)
    estados_top = sorted(resultados.items(), key=lambda x: -x[1])[:5]
    print(f"  Qubits: {n_qubits}, Estado objetivo: |{objetivo}⟩")
    for estado, conteo in estados_top:
        print(f"    |{estado}⟩: {conteo} mediciones ({conteo/2048*100:.1f}%)")
