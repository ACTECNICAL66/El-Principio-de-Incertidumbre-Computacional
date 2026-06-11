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
    TIENE_MPL = True
except ImportError:
    TIENE_MPL = False


INFO_ALGORITMOS = {
    'Fuerza Bruta': {
        'complejidad': 'O(n!)',
        'garantia': 'Optimalidad global',
        'n_max_factible': 15,
        'color': 'red',
    },
    'Prog. Dinámica': {
        'complejidad': 'O(n²2ⁿ)',
        'garantia': 'Optimalidad global',
        'n_max_factible': 25,
        'color': 'orange',
    },
    'Christofides': {
        'complejidad': 'O(n³)',
        'garantia': '1.5-aproximación',
        'n_max_factible': 1000,
        'color': 'green',
    },
    'Vecino Cercano': {
        'complejidad': 'O(n²)',
        'garantia': 'Sin garantía',
        'n_max_factible': 10000,
        'color': 'blue',
    },
    '2-opt': {
        'complejidad': 'O(n²·iter)',
        'garantia': 'Óptimo local',
        'n_max_factible': 5000,
        'color': 'purple',
    },
    'Recocido Simulado': {
        'complejidad': 'O(iter·n²)',
        'garantia': 'Probabilística',
        'n_max_factible': 5000,
        'color': 'cyan',
    },
}


def estimar_tiempo_ejecucion(algoritmo: str, n: int) -> float:
    ops_por_segundo = 1e8
    if algoritmo == 'Fuerza Bruta':
        ops = math.factorial(n)
    elif algoritmo == 'Prog. Dinámica':
        ops = n**2 * 2**n
    elif algoritmo == 'Christofides':
        ops = n**3
    elif algoritmo == 'Vecino Cercano':
        ops = n**2
    elif algoritmo in ('2-opt', 'Recocido Simulado'):
        ops = n**2 * 1000
    else:
        ops = n**3
    return ops / ops_por_segundo


def calcular_ratio_calidad(algoritmo: str, n: int) -> float:
    if algoritmo == 'Fuerza Bruta':
        return 1.0
    elif algoritmo == 'Prog. Dinámica':
        return 1.0
    elif algoritmo == 'Christofides':
        return 1.5
    elif algoritmo == 'Vecino Cercano':
        return 1.0 + 0.5 * math.log(n) / math.log(10)
    elif algoritmo == '2-opt':
        return 1.0 + 0.1 * math.log(n) / math.log(10)
    elif algoritmo == 'Recocido Simulado':
        return 1.0 + 0.05 * math.log(n) / math.log(10)
    return 2.0


if __name__ == "__main__":
    print("=" * 60)
    print("RENDIMIENTO DE ALGORITMOS TSP")
    print("=" * 60)

    print(f"\n{'Algoritmo':20} {'Complejidad':20} {'Garantía':22} {'n máx':8}")
    print("-" * 70)
    for nombre, info in INFO_ALGORITMOS.items():
        print(f"{nombre:20} {info['complejidad']:20} {info['garantia']:22} {info['n_max_factible']:<8}")

    print("\n--- Estimación de tiempos de ejecución ---")
    for n in [10, 20, 50, 100]:
        print(f"\nn = {n}:")
        for algo in ['Fuerza Bruta', 'Prog. Dinámica', 'Christofides', 'Vecino Cercano']:
            t = estimar_tiempo_ejecucion(algo, n)
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
            q = calcular_ratio_calidad(algo, n)
            print(f"  {algo:20} ratio={q:.3f}")

    if TIENE_MPL:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

        ns = list(range(2, 31))
        for algo in ['Vecino Cercano', 'Christofides', 'Fuerza Bruta']:
            tiempos = [estimar_tiempo_ejecucion(algo, n) for n in ns]
            ax1.plot(ns, tiempos, label=algo, linewidth=2)
        ax1.set_yscale('log')
        ax1.set_xlabel('n')
        ax1.set_ylabel('Tiempo estimado (s)')
        ax1.set_title('Complejidad Computacional')
        ax1.legend()
        ax1.grid(True, alpha=0.3)

        ns2 = list(range(5, 101))
        for algo in ['Vecino Cercano', 'Christofides', '2-opt', 'Recocido Simulado']:
            ratios = [calcular_ratio_calidad(algo, n) for n in ns2]
            ax2.plot(ns2, ratios, label=algo, linewidth=2)
        ax2.set_xlabel('n')
        ax2.set_ylabel('Ratio respecto al óptimo')
        ax2.set_title('Calidad de Aproximación')
        ax2.legend()
        ax2.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig('rendimiento_algoritmos.png', dpi=150)
        plt.close()
        print("\nGráfico guardado: rendimiento_algoritmos.png")
