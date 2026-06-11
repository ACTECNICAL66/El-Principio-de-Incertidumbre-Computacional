"""
Visualización del rendimiento comparativo de algoritmos de optimización
para el TSP, mostrando la brecha entre complejidad teórica y desempeño empírico.
"""

import math
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    import matplotlib.pyplot as plt
    HAS_MPL = True
except ImportError:
    HAS_MPL = False


ALGORITHM_INFO = {
    'Fuerza Bruta': {
        'complexity': 'O(n!)',
        'guarantee': 'Optimalidad global',
        'max_feasible_n': 15,
        'color': 'red',
    },
    'Prog. Dinámica': {
        'complexity': 'O(n²2ⁿ)',
        'guarantee': 'Optimalidad global',
        'max_feasible_n': 25,
        'color': 'orange',
    },
    'Christofides': {
        'complexity': 'O(n³)',
        'guarantee': '1.5-aproximación',
        'max_feasible_n': 1000,
        'color': 'green',
    },
    'Vecino Cercano': {
        'complexity': 'O(n²)',
        'guarantee': 'Sin garantía',
        'max_feasible_n': 10000,
        'color': 'blue',
    },
    '2-opt': {
        'complexity': 'O(n²·iter)',
        'guarantee': 'Óptimo local',
        'max_feasible_n': 5000,
        'color': 'purple',
    },
    'Recocido Simulado': {
        'complexity': 'O(iter·n²)',
        'guarantee': 'Probabilística',
        'max_feasible_n': 5000,
        'color': 'cyan',
    },
}


def estimate_runtime(algorithm: str, n: int) -> float:
    ops_per_second = 1e8
    if algorithm == 'Fuerza Bruta':
        ops = math.factorial(n)
    elif algorithm == 'Prog. Dinámica':
        ops = n**2 * 2**n
    elif algorithm == 'Christofides':
        ops = n**3
    elif algorithm == 'Vecino Cercano':
        ops = n**2
    elif algorithm in ('2-opt', 'Recocido Simulado'):
        ops = n**2 * 1000
    else:
        ops = n**3
    return ops / ops_per_second


def compute_quality_ratio(algorithm: str, n: int) -> float:
    if algorithm == 'Fuerza Bruta':
        return 1.0
    elif algorithm == 'Prog. Dinámica':
        return 1.0
    elif algorithm == 'Christofides':
        return 1.5
    elif algorithm == 'Vecino Cercano':
        return 1.0 + 0.5 * math.log(n) / math.log(10)
    elif algorithm == '2-opt':
        return 1.0 + 0.1 * math.log(n) / math.log(10)
    elif algorithm == 'Recocido Simulado':
        return 1.0 + 0.05 * math.log(n) / math.log(10)
    return 2.0


if __name__ == "__main__":
    print("=" * 60)
    print("RENDIMIENTO DE ALGORITMOS TSP")
    print("=" * 60)

    print(f"\n{'Algoritmo':20} {'Complejidad':20} {'Garantía':22} {'n máx':8}")
    print("-" * 70)
    for name, info in ALGORITHM_INFO.items():
        print(f"{name:20} {info['complexity']:20} {info['guarantee']:22} {info['max_feasible_n']:<8}")

    print("\n--- Estimación de tiempos de ejecución ---")
    for n in [10, 20, 50, 100]:
        print(f"\nn = {n}:")
        for algo in ['Fuerza Bruta', 'Prog. Dinámica', 'Christofides', 'Vecino Cercano']:
            t = estimate_runtime(algo, n)
            if t < 1:
                print(f"  {algo:20} {t*1000:.4f} ms")
            elif t < 60:
                print(f"  {algo:20} {t:.2f} s")
            else:
                print(f"  {algo:20} {t/60:.2f} min")

    print("\n--- Calidad de solución esperada (ratio vs óptimo) ---")
    for n in [10, 50, 100]:
        print(f"\nn = {n}:")
        for algo in ['Fuerza Bruta', 'Christofides', 'Vecino Cercano', '2-opt', 'Recocido Simulado']:
            q = compute_quality_ratio(algo, n)
            print(f"  {algo:20} ratio={q:.3f}")

    if HAS_MPL:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

        ns = list(range(2, 31))
        for algo in ['Vecino Cercano', 'Christofides', 'Fuerza Bruta']:
            times = [estimate_runtime(algo, n) for n in ns]
            ax1.plot(ns, times, label=algo, linewidth=2)
        ax1.set_yscale('log')
        ax1.set_xlabel('n')
        ax1.set_ylabel('Tiempo estimado (s)')
        ax1.set_title('Complejidad Computacional')
        ax1.legend()
        ax1.grid(True, alpha=0.3)

        ns2 = list(range(5, 101))
        for algo in ['Vecino Cercano', 'Christofides', '2-opt', 'Recocido Simulado']:
            ratios = [compute_quality_ratio(algo, n) for n in ns2]
            ax2.plot(ns2, ratios, label=algo, linewidth=2)
        ax2.set_xlabel('n')
        ax2.set_ylabel('Ratio respecto al óptimo')
        ax2.set_title('Calidad de Aproximación')
        ax2.legend()
        ax2.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig('algorithm_performance.png', dpi=150)
        plt.close()
        print("\nGráfico guardado: algorithm_performance.png")
