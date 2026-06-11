"""
Generación de gráficos de entropía del espacio de soluciones del TSP
y límites de información para algoritmos polinómicos.
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


def compute_entropy_curve(max_n=100):
    ns = list(range(2, max_n + 1))
    entropies = []
    for n in ns:
        if n > 20:
            H = (n * math.log(n) - n + 0.5 * math.log(2 * math.pi * n) - math.log(2)) / math.log(2)
        else:
            H = math.log(math.factorial(n - 1) / 2, 2)
        entropies.append(H)
    return ns, entropies


def compute_information_bounds(max_n=100):
    ns = list(range(2, max_n + 1))
    greedy = [n**2 for n in ns]
    christofides = [n**3 for n in ns]
    dp = [n**2 * 2**n for n in ns]
    brute = [math.factorial(n) for n in ns]
    return ns, greedy, christofides, dp, brute


if HAS_MPL:
    def plot_entropy_vs_n(max_n=100):
        ns, entropies = compute_entropy_curve(max_n)
        plt.figure(figsize=(10, 6))
        plt.plot(ns, entropies, 'b-', linewidth=2)
        plt.xlabel('Número de ciudades (n)', fontsize=12)
        plt.ylabel('Entropía H₀ (bits)', fontsize=12)
        plt.title('Entropía del Espacio de Soluciones del TSP')
        plt.grid(True, alpha=0.3)
        plt.savefig('entropy_vs_n.png', dpi=150)
        plt.close()
        print("Gráfico guardado: entropy_vs_n.png")

    def plot_information_gap(max_n=50):
        ns, greedy, christofides, dp, brute = compute_information_bounds(max_n)
        entropies = compute_entropy_curve(max_n)[1][:len(ns)]

        plt.figure(figsize=(12, 7))
        plt.plot(ns, entropies, 'k-', linewidth=2.5, label='Entropía H₀')
        plt.plot(ns, greedy, 'r--', label='Greedy O(n²)')
        plt.plot(ns, christofides, 'g--', label='Christofides O(n³)')
        plt.plot(ns, dp, 'b--', label='Prog. Dinámica O(n²2ⁿ)')
        plt.plot(ns, brute, 'm--', label='Fuerza Bruta O(n!)')

        plt.yscale('log')
        plt.xlabel('n (ciudades)', fontsize=12)
        plt.ylabel('Bits (escala log)', fontsize=12)
        plt.title('Brecha Informacional: Entropía vs Información Adquirible')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.xlim(2, 50)
        plt.savefig('information_gap.png', dpi=150)
        plt.close()
        print("Gráfico guardado: information_gap.png")


if __name__ == "__main__":
    print("Generando gráficos de entropía...")
    ns, entropies = compute_entropy_curve(100)
    print(f"Entropía para n=10:  {entropies[8]:.2f} bits")
    print(f"Entropía para n=50:  {entropies[48]:.2f} bits")
    print(f"Entropía para n=100: {entropies[98]:.2f} bits")

    if HAS_MPL:
        plot_entropy_vs_n(100)
        plot_information_gap(50)
    else:
        print("matplotlib no está instalado. Los gráficos no se generaron.")
