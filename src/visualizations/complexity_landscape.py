"""
Visualización del panorama de complejidad: clases de complejidad,
entropía informacional, y la brecha entre verificación y búsqueda.
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


PANOAMA_COMPLEJIDAD = {
    'P': {
        'crecimiento_entropia': 'O(log n)',
        'verificacion': 'Fácil',
        'busqueda': 'Fácil',
        'ejemplo': 'Ordenamiento, camino mínimo',
        'color': 'green',
    },
    'NP': {
        'crecimiento_entropia': 'O(poly(n))',
        'verificacion': 'Fácil',
        'busqueda': 'Difícil (conjetura)',
        'ejemplo': 'SAT, TSP decisión',
        'color': 'orange',
    },
    'NP-completo': {
        'crecimiento_entropia': 'O(n log n) o mayor',
        'verificacion': 'Fácil',
        'busqueda': 'Muy difícil',
        'ejemplo': 'TSP, clique, mochila',
        'color': 'red',
    },
    'PSPACE': {
        'crecimiento_entropia': 'O(poly(n)) espacio',
        'verificacion': 'Difícil',
        'busqueda': 'Muy difícil',
        'ejemplo': 'QBF, juegos',
        'color': 'purple',
    },
    'EXPTIME': {
        'crecimiento_entropia': 'O(2^n)',
        'verificacion': 'Muy difícil',
        'busqueda': 'Intratable',
        'ejemplo': 'GO generalizado',
        'color': 'darkred',
    },
}


def brecha_informacional(n: int, clase: str) -> float:
    if clase == 'P':
        return 0.0
    elif clase == 'NP':
        return math.log2(n)
    elif clase == 'NP-completo':
        return (n * math.log2(n) - n + 0.5 * math.log2(2 * math.pi * n)) - n**2
    elif clase == 'EXPTIME':
        return 2**n - n**3
    return math.log2(n)


def dificultad_certificacion(n: int, clase: str) -> float:
    if clase == 'P':
        return n
    elif clase == 'NP':
        return n**2
    elif clase == 'NP-completo':
        return math.factorial(n)
    elif clase == 'PSPACE':
        return 2**n
    return 2**n


if __name__ == "__main__":
    print("=" * 60)
    print("PANOAMA DE COMPLEJIDAD - PIC")
    print("=" * 60)

    print(f"\n{'Clase':15} {'Entropía':20} {'Verificación':15} {'Búsqueda':20} {'Ejemplo':25}")
    print("-" * 95)
    for nombre, info in PANOAMA_COMPLEJIDAD.items():
        print(f"{nombre:15} {info['crecimiento_entropia']:20} {info['verificacion']:15} "
              f"{info['busqueda']:20} {info['ejemplo']:25}")

    print("\n--- Brecha Informacional (n=100) ---")
    for cls in ['P', 'NP', 'NP-completo']:
        gap = brecha_informacional(100, cls)
        print(f"  {cls:15} brecha ≈ {gap:.1f} bits")

    print("\n--- Dificultad de Certificación ---")
    for n in [10, 20, 50]:
        print(f"\nn = {n}:")
        for cls in ['P', 'NP', 'NP-completo']:
            d = dificultad_certificacion(n, cls)
            if d > 1e6:
                print(f"  {cls:15} ~ {d:.1e} operaciones (intratable)")
            else:
                print(f"  {cls:15} ~ {d:.0f} operaciones")

    if TIENE_MPL:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

        ns = list(range(1, 31))
        for cls in ['P', 'NP', 'NP-completo']:
            gaps = [brecha_informacional(n, cls) for n in ns]
            ax1.plot(ns, gaps, label=cls, linewidth=2)
        ax1.set_xlabel('n')
        ax1.set_ylabel('Brecha Informacional (bits)')
        ax1.set_title('Brecha Informacional vs Tamaño del Problema')
        ax1.legend()
        ax1.grid(True, alpha=0.3)

        ns2 = list(range(1, 16))
        for cls in ['P', 'NP', 'NP-completo']:
            diffs = [dificultad_certificacion(n, cls) for n in ns2]
            ax2.plot(ns2, diffs, label=cls, linewidth=2)
        ax2.set_yscale('log')
        ax2.set_xlabel('n')
        ax2.set_ylabel('Dificultad de Certificación')
        ax2.set_title('Dificultad de Certificación de Optimalidad')
        ax2.legend()
        ax2.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig('panorama_complejidad.png', dpi=150)
        plt.close()
        print("\nGráfico guardado: panorama_complejidad.png")
