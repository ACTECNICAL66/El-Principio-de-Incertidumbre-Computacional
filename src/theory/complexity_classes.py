"""
Análisis de clases de complejidad a través del lente del
Principio de Incertidumbre Computacional (PIC).
"""

import math


class ClaseComplejidad:
    def __init__(self, nombre: str, descripcion: str):
        self.nombre = nombre
        self.descripcion = descripcion

    def __repr__(self):
        return f"{self.nombre}: {self.descripcion}"


P = ClaseComplejidad("P",
    "Problemas resolubles en tiempo polinómico por una máquina de Turing determinista.")

NP = ClaseComplejidad("NP",
    "Problemas cuyas soluciones pueden verificarse en tiempo polinómico.")

NP_hard = ClaseComplejidad("NP-hard",
    "Problemas al menos tan difíciles como cualquier problema en NP.")

NP_complete = ClaseComplejidad("NP-completo",
    "Problemas que están tanto en NP como en NP-hard.")

coNP = ClaseComplejidad("coNP",
    "Problemas complementarios a los de NP (la respuesta 'no' es verificable).")

PSPACE = ClaseComplejidad("PSPACE",
    "Problemas resolubles con cantidad polinómica de memoria.")

EXPTIME = ClaseComplejidad("EXPTIME",
    "Problemas resolubles en tiempo exponencial.")


EJEMPLO_BRECHA_CERTIFICACION = """
Bajo el Principio de Incertidumbre Computacional, incluso si P = NP,
la certificación de optimalidad podría requerir recursos superpolinomiales.
Esto sugiere una separación más sutil:
  P-cert (encontrar y certificar optimalidad en tiempo polinómico)
  vs NP-cert (verificar la certificación en tiempo polinómico)
"""


def caracterizacion_informacional(clase: ClaseComplejidad) -> str:
    if clase.nombre == "P":
        return ("Información adquirible en tiempo polinómico suficiente "
                "para resolver el problema.")
    elif clase.nombre == "NP":
        return ("Información necesaria para verificar una solución es "
                "polinómica, pero adquirirla desde cero puede requerir "
                "información superpolinómica.")
    elif clase.nombre == "NP-completo":
        return ("El espacio de soluciones tiene entropía superpolinómica, "
                "y ningún algoritmo polinómico puede certificar optimalidad "
                "en el peor caso.")
    elif clase.nombre == "coNP":
        return ("Requiere certificados universales ('para toda asignación...'), "
                "que desde la perspectiva del PIC demandan más información.")
    return "No hay caracterización informacional disponible."


def entropia_clase_complejidad(n: int, nombre_clase: str) -> float:
    if nombre_clase == "P":
        return n * math.log2(n)
    elif nombre_clase == "NP":
        return math.log2(2**n)
    elif nombre_clase == "NP-completo":
        return math.log2(math.factorial(n))
    elif nombre_clase == "PSPACE":
        return n**2
    elif nombre_clase == "EXPTIME":
        return 2**n
    return 0.0


if __name__ == "__main__":
    print("=" * 60)
    print("Clases de Complejidad - Perspectiva del PIC")
    print("=" * 60)

    clases = [P, NP, NP_hard, NP_complete, coNP, PSPACE, EXPTIME]
    for cls in clases:
        print(f"\n{cls.nombre}")
        print(f"  {cls.descripcion}")
        print(f"  Caracterización informacional: {caracterizacion_informacional(cls)}")

    print("\n" + "=" * 60)
    print("Comparación de entropía para n=100:")
    print("-" * 60)
    for nombre in ["P", "NP", "NP-completo", "PSPACE", "EXPTIME"]:
        ent = entropia_clase_complejidad(100, nombre)
        print(f"  {nombre:15} ~ {ent:.1f} bits")
