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
    HAS_MPL = True
except ImportError:
    HAS_MPL = False


COMPLEXITY_LANDSCAPE = {
    'P': {
        'entropy_growth': 'O(log n)',
        'verification': 'Fácil',
        'search': 'Fácil',
        'example': 'Ordenamiento, camino mínimo',
        'color': 'green',
    },
    'NP': {
        'entropy_growth': 'O(poly(n))',
        'verification': 'Fácil',
        'search': 'Difícil (conjetura)',
        'example': 'SAT, TSP decisión',
        'color': 'orange',
    },
    'NP-complete': {
        'entropy_growth': 'O(n log n) o mayor',
        'verification': 'Fácil',
        'search': 'Muy difícil',
        'example': 'TSP, clique, mochila',
        'color': 'red',
    },
    'PSPACE': {
        'entropy_growth': 'O(poly(n)) espacio',
        'verification': 'Difícil',
        'search': 'Muy difícil',
        'example': 'QBF, juegos',
        'color': 'purple',
    },
    'EXPTIME': {
        'entropy_growth': 'O(2^n)',
        'verification': 'Muy difícil',
        'search': 'Intratable',
        'example': 'GO generalizado',
        'color': 'darkred',
    },
}


def information_gap_function(n: int, problem_class: str) -> float:
    if problem_class == 'P':
        return 0.0
    elif problem_class == 'NP':
        return math.log2(n)
    elif problem_class == 'NP-complete':
        return (n * math.log2(n) - n + 0.5 * math.log2(2 * math.pi * n)) - n**2
    elif problem_class == 'EXPTIME':
        return 2**n - n**3
    return math.log2(n)


def certification_difficulty(n: int, class_name: str) -> float:
    if class_name == 'P':
        return n
    elif class_name == 'NP':
        return n**2
    elif class_name == 'NP-complete':
        return math.factorial(n)
    elif class_name == 'PSPACE':
        return 2**n
    return 2**n


if __name__ == "__main__":
    print("=" * 60)
    print("PANOAMA DE COMPLEJIDAD - PIC")
    print("=" * 60)

    print(f"\n{'Clase':15} {'Entropía':20} {'Verificación':15} {'Búsqueda':20} {'Ejemplo':25}")
    print("-" * 95)
    for name, info in COMPLEXITY_LANDSCAPE.items():
        print(f"{name:15} {info['entropy_growth']:20} {info['verification']:15} "
              f"{info['search']:20} {info['example']:25}")

    print("\n--- Brecha Informacional (n=100) ---")
    for cls in ['P', 'NP', 'NP-complete']:
        gap = information_gap_function(100, cls)
        print(f"  {cls:15} brecha ≈ {gap:.1f} bits")

    print("\n--- Dificultad de Certificación ---")
    for n in [10, 20, 50]:
        print(f"\nn = {n}:")
        for cls in ['P', 'NP', 'NP-complete']:
            d = certification_difficulty(n, cls)
            if d > 1e6:
                print(f"  {cls:15} ~ {d:.1e} operaciones (intratable)")
            else:
                print(f"  {cls:15} ~ {d:.0f} operaciones")

    if HAS_MPL:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

        ns = list(range(1, 31))
        for cls in ['P', 'NP', 'NP-complete']:
            gaps = [information_gap_function(n, cls) for n in ns]
            ax1.plot(ns, gaps, label=cls, linewidth=2)
        ax1.set_xlabel('n')
        ax1.set_ylabel('Brecha Informacional (bits)')
        ax1.set_title('Brecha Informacional vs Tamaño del Problema')
        ax1.legend()
        ax1.grid(True, alpha=0.3)

        ns2 = list(range(1, 16))
        for cls in ['P', 'NP', 'NP-complete']:
            diffs = [certification_difficulty(n, cls) for n in ns2]
            ax2.plot(ns2, diffs, label=cls, linewidth=2)
        ax2.set_yscale('log')
        ax2.set_xlabel('n')
        ax2.set_ylabel('Dificultad de Certificación')
        ax2.set_title('Dificultad de Certificación de Optimalidad')
        ax2.legend()
        ax2.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig('complexity_landscape.png', dpi=150)
        plt.close()
        print("\nGráfico guardado: complexity_landscape.png")
