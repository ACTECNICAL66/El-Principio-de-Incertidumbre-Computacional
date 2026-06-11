"""
Cotas inferiores para TSP y problemas NP-duros usando argumentos
informacionales. Implementa el modelo de consulta adversarial
y el teorema de la barrera informacional.
"""

import math
from typing import List, Tuple
import random


def teorema_barrera_informacional(n: int, func_entropia) -> float:
    H0 = func_entropia(n)
    return H0


def cota_inferior_consultas_tsp(n: int) -> int:
    grupos = n // 2
    pares_cruzados = grupos * (n - grupos)
    return pares_cruzados


def instancia_adversarial_tsp(n: int, semilla: int = 42) -> Tuple[List[int], List[int], Tuple[int, int]]:
    random.seed(semilla)
    grupo_a = list(range(n // 2))
    grupo_b = list(range(n // 2, n))
    a_secreto = random.choice(grupo_a)
    b_secreto = random.choice(grupo_b)
    return grupo_a, grupo_b, (a_secreto, b_secreto)


class OraculoAdversarial:
    def __init__(self, n: int, semilla: int = 42):
        self.n = n
        random.seed(semilla)
        self.grupo_a = list(range(n // 2))
        self.grupo_b = list(range(n // 2, n))
        self.secreto_a = random.choice(self.grupo_a)
        self.secreto_b = random.choice(self.grupo_b)
        self.consultas_realizadas = 0
        self.M = n * 10

    def consultar(self, i: int, j: int) -> float:
        self.consultas_realizadas += 1
        if i == j:
            return 0.0
        mismo_grupo = ((i in self.grupo_a and j in self.grupo_a) or
                       (i in self.grupo_b and j in self.grupo_b))
        es_par_secreto = ((i == self.secreto_a and j == self.secreto_b) or
                          (i == self.secreto_b and j == self.secreto_a))
        if es_par_secreto:
            return 1.0
        elif mismo_grupo:
            return 1.0
        else:
            return float(self.M)

    def obtener_consultas(self) -> int:
        return self.consultas_realizadas


def cota_inferior_arbol_decision_tsp(n: int) -> float:
    num_tours = math.factorial(n - 1) // 2
    return math.ceil(math.log2(num_tours))


if __name__ == "__main__":
    print("=" * 60)
    print("TEOREMA DE LA BARRERA INFORMACIONAL - Cotas Inferiores")
    print("=" * 60)

    for n in [10, 20, 50, 100]:
        cota_arbol = cota_inferior_arbol_decision_tsp(n)
        cota_adv = cota_inferior_consultas_tsp(n)
        print(f"\nn = {n}:")
        print(f"  Cota inferior árbol decisión: {cota_arbol} consultas")
        print(f"  Cota adversarial: ~{cota_adv} consultas (O(n²))")
        k_B = 1.380649e-23
        T = 300
        print(f"  Límite energía Landauer: {cota_arbol * k_B * T * math.log(2):.2e} J")
