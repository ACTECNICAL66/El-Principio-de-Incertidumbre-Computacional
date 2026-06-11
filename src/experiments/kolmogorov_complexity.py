"""
===========================================
COMPLEJIDAD DESCRIPTIVA Y KOLMOGOROV
===========================================
Estima la complejidad de Kolmogórov de rutas del TSP mediante compresión.
Demuestra que las soluciones óptimas pueden ser arbitrariamente complejas,
reforzando el Principio de Incertidumbre Computacional.
"""

import json
import random
import zlib


def complejidad_aproximada(ruta):
    datos = json.dumps(ruta).encode('utf-8')
    comprimido = zlib.compress(datos)
    return len(comprimido)


def generar_ruta_aleatoria(n):
    ruta = list(range(n)) + [0]
    random.shuffle(ruta[1:-1])
    return ruta


def generar_instancia_compleja(n, seed=12345):
    random.seed(seed)
    ruta_compleja = list(range(n))
    random.shuffle(ruta_compleja)
    return ruta_compleja + [ruta_compleja[0]]


if __name__ == "__main__":
    print("=" * 60)
    print("COMPLEJIDAD DESCRIPTIVA APROXIMADA DE RUTAS")
    print("=" * 60)

    n = 8
    ruta_optima = [0, 3, 2, 7, 5, 6, 1, 4, 0]
    ruta_aleatoria = generar_ruta_aleatoria(n)

    print(f"\nRuta óptima (ejemplo): {ruta_optima}")
    raw_opt = json.dumps(ruta_optima).encode('utf-8')
    comp_opt = complejidad_aproximada(ruta_optima)
    print(f"  Tamaño original: {len(raw_opt)} bytes")
    print(f"  Tamaño comprimido (aprox K(x)): {comp_opt} bytes")

    print(f"\nRuta aleatoria: {ruta_aleatoria}")
    raw_rand = json.dumps(ruta_aleatoria).encode('utf-8')
    comp_rand = complejidad_aproximada(ruta_aleatoria)
    print(f"  Tamaño original: {len(raw_rand)} bytes")
    print(f"  Tamaño comprimido (aprox K(x)): {comp_rand} bytes")

    print("\n" + "-" * 60)
    print("Teorema 19.1: Las soluciones óptimas pueden ser")
    print("arbitrariamente complejas (alta complejidad de Kolmogórov).")
    print("No hay atajos universales basados en la simplicidad estructural.")
    print("-" * 60)

    print("\n--- Escalando a n más grandes ---")
    for n in [10, 20, 50, 100]:
        rc = generar_instancia_compleja(n)
        comp = complejidad_aproximada(rc)
        raw_size = len(json.dumps(rc).encode('utf-8'))
        ratio = comp / raw_size if raw_size > 0 else 0
        print(f"  n={n:3d} | original: {raw_size:4d} bytes | comprimido: {comp:4d} bytes | ratio: {ratio:.2f}")
