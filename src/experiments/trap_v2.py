"""
=======================================
EXPERIMENTO: LA TRAMPA V2.0
=======================================
Instancia del TSP diseñada para engañar al algoritmo greedy (Vecino Más Cercano),
demostrando el Principio de Incertidumbre Computacional.

La matriz de distancias está construida para que las decisiones localmente
óptimas del greedy conduzcan a un resultado globalmente catastrófico.
"""

from itertools import permutations


def construir_matriz_trampa_v2():
    ciudades = ['A', 'B', 'C', 'D']
    matriz = {
        'A': {'A': 0, 'B': 1, 'C': 2, 'D': 10},
        'B': {'A': 1, 'B': 0, 'C': 1, 'D': 10},
        'C': {'A': 2, 'B': 1, 'C': 0, 'D': 1},
        'D': {'A': 100, 'B': 10, 'C': 1, 'D': 0}
    }
    return ciudades, matriz


def algoritmo_vecino_mas_cercano(matriz, ciudad_inicio):
    ruta = [ciudad_inicio]
    ciudades_no_visitadas = set(matriz.keys()) - {ciudad_inicio}
    ciudad_actual = ciudad_inicio
    while ciudades_no_visitadas:
        siguiente = min(ciudades_no_visitadas, key=lambda c: matriz[ciudad_actual][c])
        ruta.append(siguiente)
        ciudades_no_visitadas.remove(siguiente)
        ciudad_actual = siguiente
    ruta.append(ciudad_inicio)
    return ruta


def calcular_costo(matriz, ruta):
    costo = 0
    for i in range(len(ruta) - 1):
        costo += matriz[ruta[i]][ruta[i + 1]]
    return costo


def fuerza_bruta_tsp(matriz):
    ciudades = list(matriz.keys())
    inicio = ciudades[0]
    resto = ciudades[1:]
    mejor_costo = float('inf')
    mejor_ruta = None
    for perm in permutations(resto):
        ruta = (inicio,) + perm + (inicio,)
        costo = calcular_costo(matriz, ruta)
        if costo < mejor_costo:
            mejor_costo = costo
            mejor_ruta = ruta
    return mejor_ruta, mejor_costo


if __name__ == "__main__":
    print("=" * 60)
    print("EXPERIMENTO: LA TRAMPA V2.0")
    print("=" * 60)

    ciudades, matriz = construir_matriz_trampa_v2()

    print("\nMatriz de distancias:")
    print("     " + "  ".join(f"{c:>4}" for c in ciudades))
    for c in ciudades:
        print(f"  {c}: " + "  ".join(f"{matriz[c][d]:>4}" for d in ciudades))

    ruta_greedy = algoritmo_vecino_mas_cercano(matriz, 'A')
    costo_greedy = calcular_costo(matriz, ruta_greedy)

    print(f"\n--- Vecino Más Cercano (Greedy) ---")
    print(f"Ruta: {' -> '.join(ruta_greedy)}")
    print(f"Costo: {costo_greedy}")

    mejor_ruta, mejor_costo = fuerza_bruta_tsp(matriz)

    print(f"\n--- Fuerza Bruta (Óptimo Global) ---")
    print(f"Ruta: {' -> '.join(mejor_ruta)}")
    print(f"Costo: {mejor_costo}")

    proporcion = costo_greedy / mejor_costo
    print(f"\n--- Conclusión ---")
    print(f"El algoritmo greedy produce un costo {proporcion:.1f} veces mayor que el óptimo.")
    print(f"La información local (distancias inmediatas) es insuficiente para")
    print(f"garantizar la optimalidad global: el Principio de Incertidumbre")
    print(f"Computacional en acción.")
