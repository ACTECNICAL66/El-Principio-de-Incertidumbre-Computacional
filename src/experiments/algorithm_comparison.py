"""
===========================================
COMPARATIVA DE ALGORITMOS
===========================================
Evalúa 4 algoritmos (Fuerza Bruta, Vecino Más Cercano, 2-opt, Recocido Simulado)
en instancia aleatoria y en la Trampa V2.0.

Valida el PIC: los algoritmos polinómicos encuentran óptimos en instancias
de baja entropía pero fallan en instancias adversariales de alta entropía.
"""

import math
import random
import time
import itertools


def distancia_euclidiana(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def generar_instancia(n, semilla=42):
    random.seed(semilla)
    return [(random.random() * 100, random.random() * 100) for _ in range(n)]


def matriz_distancias(ciudades):
    n = len(ciudades)
    matriz = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            d = distancia_euclidiana(ciudades[i], ciudades[j])
            matriz[i][j] = matriz[j][i] = d
    return matriz


def costo_ruta(matriz, ruta):
    costo = 0
    for i in range(len(ruta)):
        costo += matriz[ruta[i]][ruta[(i + 1) % len(ruta)]]
    return costo


def fuerza_bruta(matriz):
    n = len(matriz)
    mejor_costo = float('inf')
    mejor_ruta = None
    for perm in itertools.permutations(range(1, n)):
        ruta = (0,) + perm + (0,)
        costo = costo_ruta(matriz, ruta)
        if costo < mejor_costo:
            mejor_costo = costo
            mejor_ruta = ruta
    return list(mejor_ruta), mejor_costo


def vecino_mas_cercano(matriz, inicio=0):
    n = len(matriz)
    ruta = [inicio]
    no_visitados = set(range(n)) - {inicio}
    actual = inicio
    while no_visitados:
        siguiente = min(no_visitados, key=lambda c: matriz[actual][c])
        ruta.append(siguiente)
        no_visitados.remove(siguiente)
        actual = siguiente
    ruta.append(inicio)
    return ruta, costo_ruta(matriz, ruta)


def dos_opt(matriz, ruta_inicial):
    ruta = ruta_inicial[:]
    n = len(ruta)
    mejora = True
    while mejora:
        mejora = False
        for i in range(1, n - 2):
            for j in range(i + 1, n - 1):
                delta = (matriz[ruta[i - 1]][ruta[j]] +
                         matriz[ruta[i]][ruta[(j + 1) % n]]) - \
                        (matriz[ruta[i - 1]][ruta[i]] +
                         matriz[ruta[j]][ruta[(j + 1) % n]])
                if delta < -1e-9:
                    ruta[i:j + 1] = reversed(ruta[i:j + 1])
                    mejora = True
                    break
            if mejora:
                break
    return ruta, costo_ruta(matriz, ruta)


def recocido_simulado(matriz, temp_inicial=1000, enfriamiento=0.995, iteraciones=20000):
    n = len(matriz)
    ruta_actual = list(range(n)) + [0]
    random.shuffle(ruta_actual[1:-1])
    costo_actual = costo_ruta(matriz, ruta_actual)
    mejor_ruta, mejor_costo = ruta_actual[:], costo_actual
    temp = temp_inicial

    for _ in range(iteraciones):
        i, j = random.sample(range(1, n), 2)
        ruta_vecina = ruta_actual[:]
        ruta_vecina[i], ruta_vecina[j] = ruta_vecina[j], ruta_vecina[i]
        costo_vecino = costo_ruta(matriz, ruta_vecina)

        delta = costo_vecino - costo_actual
        if delta < 0 or random.random() < math.exp(-delta / temp):
            ruta_actual, costo_actual = ruta_vecina, costo_vecino
            if costo_actual < mejor_costo:
                mejor_ruta, mejor_costo = ruta_actual[:], costo_actual

        temp *= enfriamiento

    return mejor_ruta, mejor_costo


if __name__ == "__main__":
    print("=" * 60)
    print("COMPARATIVA DE ALGORITMOS EN INSTANCIA ALEATORIA (n=8)")
    print("=" * 60)

    ciudades = generar_instancia(8)
    matriz = matriz_distancias(ciudades)

    print("\nCoordenadas de las ciudades (índices 0..7):")
    for i, (x, y) in enumerate(ciudades):
        print(f"  {i}: ({x:.2f}, {y:.2f})")

    print("\n--- Fuerza Bruta (Óptimo Exacto) ---")
    inicio = time.time()
    ruta_fb, costo_fb = fuerza_bruta(matriz)
    tiempo_fb = time.time() - inicio
    print(f"Ruta: {ruta_fb}")
    print(f"Costo: {costo_fb:.6f}")
    print(f"Tiempo: {tiempo_fb:.6f} s")

    print("\n--- Vecino Más Cercano (Greedy) ---")
    inicio = time.time()
    ruta_g, costo_g = vecino_mas_cercano(matriz)
    tiempo_g = time.time() - inicio
    print(f"Ruta: {ruta_g}")
    print(f"Costo: {costo_g:.6f} (diferencia: {costo_g - costo_fb:.6f})")
    print(f"Tiempo: {tiempo_g:.6f} s")

    print("\n--- 2-opt (partiendo de Greedy) ---")
    inicio = time.time()
    ruta_2opt, costo_2opt = dos_opt(matriz, ruta_g[:-1])
    tiempo_2opt = time.time() - inicio
    print(f"Ruta: {ruta_2opt + [ruta_2opt[0]]}")
    print(f"Costo: {costo_2opt:.6f} (diferencia: {costo_2opt - costo_fb:.6f})")
    print(f"Tiempo: {tiempo_2opt:.6f} s")

    print("\n--- Recocido Simulado ---")
    inicio = time.time()
    ruta_sa, costo_sa = recocido_simulado(matriz, iteraciones=20000)
    tiempo_sa = time.time() - inicio
    print(f"Ruta: {ruta_sa}")
    print(f"Costo: {costo_sa:.6f} (diferencia: {costo_sa - costo_fb:.6f})")
    print(f"Tiempo: {tiempo_sa:.6f} s")

    print("\n" + "=" * 60)
    print("COMPARATIVA CON TRAMPA V2.0")
    print("=" * 60)

    from trap_v2 import construir_matriz_trampa_v2, algoritmo_vecino_mas_cercano
    from trap_v2 import calcular_costo, fuerza_bruta_tsp

    t_ciudades, t_matriz = construir_matriz_trampa_v2()
    tr_greedy = algoritmo_vecino_mas_cercano(t_matriz, 'A')
    tg_costo = calcular_costo(t_matriz, tr_greedy)
    topt_ruta, topt_costo = fuerza_bruta_tsp(t_matriz)

    print(f"\nGreedy:  {' -> '.join(tr_greedy)}  Costo: {tg_costo}")
    print(f"Óptimo:  {' -> '.join(topt_ruta)}  Costo: {topt_costo}")
    print(f"Ratio: {tg_costo / topt_costo:.1f}x")
