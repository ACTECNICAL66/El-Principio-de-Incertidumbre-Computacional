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
    TIENE_MPL = True
except ImportError:
    TIENE_MPL = False


def calcular_curva_entropia(max_n=100):
    ns = list(range(2, max_n + 1))
    entropias = []
    for n in ns:
        if n > 20:
            H = (n * math.log(n) - n + 0.5 * math.log(2 * math.pi * n) - math.log(2)) / math.log(2)
        else:
            H = math.log(math.factorial(n - 1) / 2, 2)
        entropias.append(H)
    return ns, entropias


def calcular_cotas_informacion(max_n=100):
    ns = list(range(2, max_n + 1))
    voraz = [n**2 for n in ns]
    christofides = [n**3 for n in ns]
    prog_din = [n**2 * 2**n for n in ns]
    bruta = [math.factorial(n) for n in ns]
    return ns, voraz, christofides, prog_din, bruta


if TIENE_MPL:
    def graficar_entropia_vs_n(max_n=100):
        ns, entropias = calcular_curva_entropia(max_n)
        plt.figure(figsize=(10, 6))
        plt.plot(ns, entropias, 'b-', linewidth=2)
        plt.xlabel('Número de ciudades (n)', fontsize=12)
        plt.ylabel('Entropía H₀ (bits)', fontsize=12)
        plt.title('Entropía del Espacio de Soluciones del TSP')
        plt.grid(True, alpha=0.3)
        plt.savefig('entropia_vs_n.png', dpi=150)
        plt.close()
        print("Gráfico guardado: entropia_vs_n.png")

    def graficar_brecha_informacional(max_n=50):
        ns, voraz, christofides, prog_din, bruta = calcular_cotas_informacion(max_n)
        entropias = calcular_curva_entropia(max_n)[1][:len(ns)]

        plt.figure(figsize=(12, 7))
        plt.plot(ns, entropias, 'k-', linewidth=2.5, label='Entropía H₀')
        plt.plot(ns, voraz, 'r--', label='Voraz O(n²)')
        plt.plot(ns, christofides, 'g--', label='Christofides O(n³)')
        plt.plot(ns, prog_din, 'b--', label='Prog. Dinámica O(n²2ⁿ)')
        plt.plot(ns, bruta, 'm--', label='Fuerza Bruta O(n!)')

        plt.yscale('log')
        plt.xlabel('n (ciudades)', fontsize=12)
        plt.ylabel('Bits (escala log)', fontsize=12)
        plt.title('Brecha Informacional: Entropía vs Información Adquirible')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.xlim(2, 50)
        plt.savefig('brecha_informacional.png', dpi=150)
        plt.close()
        print("Gráfico guardado: brecha_informacional.png")


if __name__ == "__main__":
    print("Generando gráficos de entropía...")
    ns, entropias = calcular_curva_entropia(100)
    print(f"Entropía para n=10:  {entropias[8]:.2f} bits")
    print(f"Entropía para n=50:  {entropias[48]:.2f} bits")
    print(f"Entropía para n=100: {entropias[98]:.2f} bits")

    if TIENE_MPL:
        graficar_entropia_vs_n(100)
        graficar_brecha_informacional(50)
    else:
        print("matplotlib no está instalado. Los gráficos no se generaron.")
