"""
Implementación del Principio de Incertidumbre Computacional para TSP
- Entropía del espacio de soluciones
- Límites de información para algoritmos en tiempo polinómico
- Análisis de la brecha de certificación
"""

import math
from typing import Callable, Dict, Any


class IncertidumbreComputacionalTSP:
    def __init__(self, n_ciudades: int):
        self.n = n_ciudades

    def entropia_espacio_soluciones(self) -> float:
        if self.n <= 1:
            return 0.0
        if self.n > 20:
            H = (self.n * math.log(self.n) - self.n +
                 0.5 * math.log(2 * math.pi * self.n) -
                 math.log(2)) / math.log(2)
        else:
            factorial = math.factorial(self.n - 1)
            H = math.log(factorial / 2, 2)
        return H

    def cota_informacion_polinomica(self, complejidad_tiempo: Callable) -> float:
        max_ops = complejidad_tiempo(self.n)
        return max_ops

    def incertidumbre_residual(self, complejidad_tiempo: Callable) -> float:
        H_total = self.entropia_espacio_soluciones()
        I_adquirida = self.cota_informacion_polinomica(complejidad_tiempo)
        return max(H_total - I_adquirida, 0)

    def brecha_certificacion(self, nombre_algoritmo: str) -> Dict[str, Any]:
        algoritmos = {
            'fuerza_bruta': lambda n: math.factorial(n),
            'prog_dinamica': lambda n: n**2 * 2**n,
            'christofides': lambda n: n**3,
            'voraz': lambda n: n**2,
            '2-opt': lambda n: n**3,
        }
        if nombre_algoritmo not in algoritmos:
            raise ValueError(f"Algoritmo desconocido: {nombre_algoritmo}")

        func_tiempo = algoritmos[nombre_algoritmo]
        H_total = self.entropia_espacio_soluciones()
        I_max = self.cota_informacion_polinomica(func_tiempo)
        H_residual = self.incertidumbre_residual(func_tiempo)

        return {
            'algoritmo': nombre_algoritmo,
            'n_ciudades': self.n,
            'entropia_total_bits': H_total,
            'info_max_adquirida_bits': I_max,
            'incertidumbre_residual_bits': H_residual,
            'certificacion_posible': H_residual < 1e-9
        }


def entropia_shannon_tsp(n: int) -> float:
    if n <= 1:
        return 0.0
    num_tours = math.factorial(n - 1) // 2
    return math.log2(num_tours)


def limite_energia_landauer(bits_adquiridos: float, temperatura: float = 300.0) -> float:
    k_B = 1.380649e-23
    return bits_adquiridos * k_B * temperatura * math.log(2)


if __name__ == "__main__":
    print("=" * 60)
    print("PRINCIPIO DE INCERTIDUMBRE COMPUTACIONAL - Análisis de Entropía")
    print("=" * 60)
    for n in [10, 20, 50, 100]:
        analizador = IncertidumbreComputacionalTSP(n)
        print(f"\nTSP con n = {n} ciudades")
        print("-" * 40)
        H_total = analizador.entropia_espacio_soluciones()
        print(f"Entropía del espacio de soluciones: {H_total:.2f} bits")
        print(f"Límite energético (Landauer): {limite_energia_landauer(H_total):.2e} J")

        for algo in ['fuerza_bruta', 'prog_dinamica', 'christofides', 'voraz']:
            try:
                resultado = analizador.brecha_certificacion(algo)
                cert = "SÍ" if resultado['certificacion_posible'] else "NO"
                print(f"  {algo:15} | Incertidumbre residual: {resultado['incertidumbre_residual_bits']:.2f} bits | Certifica: {cert}")
            except Exception:
                pass
