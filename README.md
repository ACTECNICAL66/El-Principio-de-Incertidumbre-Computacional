# El Principio de Incertidumbre Computacional (PIC)

**Hacia una Teoría de la Dificultad Computacional**

Autor: **Alejandro Cantón**

---

## Resumen

El **Principio de Incertidumbre Computacional (PIC)** es un marco teórico que postula que la barrera fundamental entre los problemas tratables (P) y los intratables (NP) no es de naturaleza computacional, sino **informacional y termodinámica**.

La idea central es que la dificultad de los problemas NP-duros no reside en la falta de poder de cálculo, sino en el **coste energético e informacional** de adquirir la certeza necesaria para garantizar la optimización en un espacio de posibilidades combinatorio vasto.

### Conceptos clave

- **Asimetría verificación vs. búsqueda**: Verificar una solución es un proceso local y barato; encontrar la solución óptima requiere información global costosa.
- **Entropía del espacio de soluciones**: La incertidumbre inicial sobre cuál es la solución óptima se mide mediante la entropía de Shannon.
- **Barrera informacional**: Los algoritmos polinómicos solo pueden adquirir información polinómica, insuficiente para disipar la entropía superpolinómica de los problemas NP-duros.
- **Coste termodinámico**: La certificación de optimalidad tiene un coste energético fundamental (límite de Landauer).

---

## Estructura del repositorio

```
├── README.md
├── requirements.txt
├── src/
│   ├── theory/
│   │   ├── entropy_calculations.py   # Cálculos de entropía y brecha informacional
│   │   ├── lower_bounds.py           # Cotas inferiores y modelo adversarial
│   │   └── complexity_classes.py     # Clases de complejidad desde la óptica del PIC
│   ├── experiments/
│   │   ├── trap_v2.py               # Experimento: La Trampa V2.0
│   │   ├── algorithm_comparison.py   # Comparativa de algoritmos de optimización
│   │   ├── kolmogorov_complexity.py  # Complejidad descriptiva de rutas TSP
│   │   └── quantum_simulation.py     # Límites cuánticos y PIC
│   └── visualizations/
│       ├── entropy_plots.py          # Gráficos de entropía vs. n
│       ├── algorithm_performance.py   # Rendimiento comparativo de algoritmos
│       └── complexity_landscape.py    # Panorama de clases de complejidad
├── notebooks/
│   ├── Chapter_10_Trap_Experiment.ipynb
│   ├── Chapter_11_Algorithm_Spectrum.ipynb
│   ├── Chapter_12_Kolmogorov_Complexity.ipynb
│   └── Chapter_17_Physics_Connections.ipynb
├── data/
│   ├── tsp_instances/
│   ├── random_graphs/
│   └── adversarial_examples/
└── papers/
    ├── main_paper.tex
    └── proofs/
```

---

## Experimentos principales

### 1. La Trampa V2.0

Instancia adversarial del TSP con 4 ciudades diseñada para engañar al algoritmo greedy. Demuestra cómo decisiones localmente óptimas conducen a resultados globalmente catastróficos (ratio 7.9x respecto al óptimo).

```bash
python src/experiments/trap_v2.py
```

### 2. Comparativa de algoritmos

Evalúa Fuerza Bruta, Vecino Más Cercano, 2-opt y Recocido Simulado en instancias aleatorias y adversariales.

```bash
python src/experiments/algorithm_comparison.py
```

### 3. Complejidad de Kolmogórov

Estima mediante compresión la complejidad descriptiva de rutas del TSP, demostrando que las soluciones óptimas pueden ser arbitrariamente complejas.

```bash
python src/experiments/kolmogorov_complexity.py
```

### 4. Cálculos de entropía

Analiza la entropía del espacio de soluciones del TSP y la brecha informacional para distintos algoritmos.

```bash
python src/theory/entropy_calculations.py
```

---

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/ACTECNICAL66/El-Principio-de-Incertidumbre-Computacional.git
cd El-Principio-de-Incertidumbre-Computacional

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar experimentos
python src/experiments/trap_v2.py

# Notebooks interactivos
jupyter notebook notebooks/
```

---

## Dependencias

- Python ≥ 3.8
- numpy
- scipy
- matplotlib (para visualizaciones)
- jupyter (para notebooks)

---

## Implicaciones

El PIC tiene profundas consecuencias en:

- **Teoría de la complejidad**: Reformula P vs NP como una cuestión de límites informacionales.
- **Criptografía**: Proporciona una base teórica para la seguridad basada en la dificultad informacional.
- **Inteligencia Artificial**: Explica el sobreajuste, los ataques adversariales y los sesgos.
- **Física de la computación**: Conecta la complejidad computacional con la termodinámica y los límites de Landauer.

---

## Licencia

Este proyecto está bajo la licencia MIT.
