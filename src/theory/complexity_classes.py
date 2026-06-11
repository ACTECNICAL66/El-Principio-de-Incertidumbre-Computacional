"""
Complexity classes analysis through the lens of the
Computational Uncertainty Principle (CUP/PIC).
"""

import math


class ComplexityClass:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"{self.name}: {self.description}"


P = ComplexityClass("P", 
    "Problemas resolubles en tiempo polinómico por una máquina de Turing determinista.")

NP = ComplexityClass("NP",
    "Problemas cuyas soluciones pueden verificarse en tiempo polinómico.")

NP_hard = ComplexityClass("NP-hard",
    "Problemas al menos tan difíciles como cualquier problema en NP.")

NP_complete = ComplexityClass("NP-complete",
    "Problemas que están tanto en NP como en NP-hard.")

coNP = ComplexityClass("coNP",
    "Problemas complementarios a los de NP (la respuesta 'no' es verificable).")

PSPACE = ComplexityClass("PSPACE",
    "Problemas resolubles con cantidad polinómica de memoria.")

EXPTIME = ComplexityClass("EXPTIME",
    "Problemas resolubles en tiempo exponencial.")


CERTIFICATION_GAP_EXAMPLE = """
Bajo el Principio de Incertidumbre Computacional, incluso si P = NP,
la certificación de optimalidad podría requerir recursos superpolinomiales.
Esto sugiere una separación más sutil:
  P-cert (encontrar y certificar optimalidad en tiempo polinómico)
  vs NP-cert (verificar la certificación en tiempo polinómico)
"""


def information_characterization(complexity_class: ComplexityClass) -> str:
    if complexity_class.name == "P":
        return ("Información adquirible en tiempo polinómico suficiente "
                "para resolver el problema.")
    elif complexity_class.name == "NP":
        return ("Información necesaria para verificar una solución es "
                "polinómica, pero adquirirla desde cero puede requerir "
                "información superpolinómica.")
    elif complexity_class.name == "NP-complete":
        return ("El espacio de soluciones tiene entropía superpolinómica, "
                "y ningún algoritmo polinómico puede certificar optimalidad "
                "en el peor caso.")
    elif complexity_class.name == "coNP":
        return ("Requiere certificados universales ('para toda asignación...'), "
                "que desde la perspectiva del PIC demandan más información.")
    return "No hay caracterización informacional disponible."


def entropy_of_complexity_class(n: int, class_name: str) -> float:
    if class_name == "P":
        return n * math.log2(n)
    elif class_name == "NP":
        return math.log2(2**n)
    elif class_name == "NP-complete":
        return math.log2(math.factorial(n))
    elif class_name == "PSPACE":
        return n**2
    elif class_name == "EXPTIME":
        return 2**n
    return 0.0


if __name__ == "__main__":
    print("=" * 60)
    print("Complexity Classes - PIC Perspective")
    print("=" * 60)

    classes = [P, NP, NP_hard, NP_complete, coNP, PSPACE, EXPTIME]
    for cls in classes:
        print(f"\n{cls.name}")
        print(f"  {cls.description}")
        print(f"  Caracterización informacional: {information_characterization(cls)}")

    print("\n" + "=" * 60)
    print("Entropy comparison for n=100:")
    print("-" * 60)
    for name in ["P", "NP", "NP-complete", "PSPACE", "EXPTIME"]:
        ent = entropy_of_complexity_class(100, name)
        print(f"  {name:15} ~ {ent:.1f} bits")
