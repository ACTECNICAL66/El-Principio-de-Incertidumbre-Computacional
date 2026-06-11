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
├── README.md                              # Este archivo
├── requirements.txt                       # Dependencias de Python
├── "Principio de Incertidumbre Computacional por Alejandro Cantón .pdf"  # Libro completo
├── src/
│   ├── theory/
│   │   ├── entropy_calculations.py        # Cálculos de entropía y brecha informacional
│   │   ├── lower_bounds.py                # Cotas inferiores y modelo adversarial
│   │   └── complexity_classes.py          # Clases de complejidad desde la óptica del PIC
│   ├── experiments/
│   │   ├── trap_v2.py                     # Experimento: La Trampa V2.0
│   │   ├── algorithm_comparison.py        # Comparativa de algoritmos de optimización
│   │   ├── kolmogorov_complexity.py       # Complejidad descriptiva de rutas TSP
│   │   └── quantum_simulation.py          # Límites cuánticos y PIC
│   └── visualizations/
│       ├── entropy_plots.py               # Gráficos de entropía vs. n
│       ├── algorithm_performance.py       # Rendimiento comparativo de algoritmos
│       └── complexity_landscape.py        # Panorama de clases de complejidad
├── notebooks/
│   ├── Chapter_10_Trap_Experiment.ipynb   # Notebook: Experimento Trampa V2.0
│   ├── Chapter_11_Algorithm_Spectrum.ipynb# Notebook: Espectro de algoritmos
│   ├── Chapter_12_Kolmogorov_Complexity.ipynb  # Notebook: Complejidad Kolmogórov
│   └── Chapter_17_Physics_Connections.ipynb    # Notebook: Conexiones físicas
├── data/
│   ├── tsp_instances/                     # Instancias de TSP
│   ├── random_graphs/                     # Grafos aleatorios
│   └── adversarial_examples/             # Ejemplos adversariales
└── papers/
    ├── main_paper.tex                    # Documento LaTeX del libro
    └── proofs/                           # Pruebas formales
```

---

## Explicación de cada archivo

### 📄 PDF del libro
- **`Principio de Incertidumbre Computacional por Alejandro Cantón .pdf`**: El libro completo en PDF con 6 partes, 25 capítulos, cubriendo desde los fundamentos de P vs NP hasta las conexiones con física cuántica y gravedad.

### 📁 `src/theory/` — Fundamentos teóricos
1. **`entropy_calculations.py`**: Implementa la clase `IncertidumbreComputacionalTSP` que calcula la entropía del espacio de soluciones del TSP usando la fórmula de Shannon, la cota de información adquirible por algoritmos polinómicos, y la brecha de certificación (residual). También calcula el límite energético de Landauer.

2. **`lower_bounds.py`**: Implementa el **teorema de la barrera informacional** mediante un modelo adversarial de consultas. Incluye la clase `OraculoAdversarial` que fuerza a cualquier algoritmo a realizar Ω(n²) consultas para certificar optimalidad en TSP.

3. **`complexity_classes.py`**: Define las clases de complejidad (P, NP, NP-completo, coNP, PSPACE, EXPTIME) y las caracteriza desde la perspectiva informacional del PIC, calculando la entropía asociada a cada una.

### 📁 `src/experiments/` — Experimentos del libro
4. **`trap_v2.py`**: Implementa la **Trampa V2.0**, una instancia adversarial de TSP con 4 ciudades diseñada para engañar al algoritmo voraz (greedy). El greedy produce un costo 7.9x mayor que el óptimo global, demostrando el PIC experimentalmente.

5. **`algorithm_comparison.py`**: Compara 4 algoritmos (Fuerza Bruta, Vecino Más Cercano, 2-opt, Recocido Simulado) en instancias aleatorias y en la Trampa V2.0. Mide tiempos de ejecución y calidad de solución.

6. **`kolmogorov_complexity.py`**: Estima la **complejidad de Kolmogórov** de rutas del TSP mediante compresión con zlib. Demuestra que las soluciones óptimas pueden ser arbitrariamente complejas (Teorema 19.1), cerrando la posibilidad de atajos basados en simplicidad estructural.

7. **`quantum_simulation.py`**: Explora los límites de la computación cuántica (Shor, Grover) desde la perspectiva del PIC. Muestra que incluso con algoritmos cuánticos, la barrera informacional persiste para problemas NP-duros.

### 📁 `src/visualizations/` — Visualizaciones
8. **`entropy_plots.py`**: Genera gráficos de la curva de entropía del TSP y la brecha informacional entre la entropía del espacio de soluciones y la información adquirible por algoritmos polinómicos.

9. **`algorithm_performance.py`**: Visualiza el rendimiento comparativo de algoritmos mostrando la brecha entre complejidad teórica (O-gran) y desempeño empírico. Tabla completa de garantías y tiempos estimados.

10. **`complexity_landscape.py`**: Genera el panorama de clases de complejidad con gráficos de brecha informacional y dificultad de certificación para cada clase.

### 📁 `notebooks/` — Jupyter Notebooks
- **Chapter_10**: Notebook interactivo del experimento Trampa V2.0
- **Chapter_11**: Notebook del espectro de algoritmos
- **Chapter_12**: Notebook de complejidad de Kolmogórov
- **Chapter_17**: Notebook de conexiones físicas (Landauer, límites energéticos)

---

## Experimentos principales

### 1. La Trampa V2.0
```bash
python src/experiments/trap_v2.py
```
Instancia adversarial del TSP con 4 ciudades diseñada para engañar al algoritmo greedy. Demuestra cómo decisiones localmente óptimas conducen a resultados globalmente catastróficos (ratio 7.9x respecto al óptimo).

### 2. Comparativa de algoritmos
```bash
python src/experiments/algorithm_comparison.py
```
Evalúa Fuerza Bruta, Vecino Más Cercano, 2-opt y Recocido Simulado en instancias aleatorias y adversariales.

### 3. Complejidad de Kolmogórov
```bash
python src/experiments/kolmogorov_complexity.py
```
Estima mediante compresión la complejidad descriptiva de rutas del TSP, demostrando que las soluciones óptimas pueden ser arbitrariamente complejas.

### 4. Cálculos de entropía
```bash
python src/theory/entropy_calculations.py
```
Analiza la entropía del espacio de soluciones del TSP y la brecha informacional para distintos algoritmos.

### 5. Cotas inferiores
```bash
python src/theory/lower_bounds.py
```
Demuestra el teorema de la barrera informacional mediante el modelo adversarial de consultas.

---

## Instalación

```bash
git clone https://github.com/ACTECNICAL66/El-Principio-de-Incertidumbre-Computacional.git
cd El-Principio-de-Incertidumbre-Computacional
pip install -r requirements.txt
python src/experiments/trap_v2.py
jupyter notebook notebooks/
```

## Dependencias

- Python ≥ 3.8
- numpy, scipy, matplotlib, jupyter

---

## Implicaciones del PIC

- **Teoría de la complejidad**: Reformula P vs NP como una cuestión de límites informacionales.
- **Criptografía**: Base teórica para seguridad basada en dificultad informacional (RSA, LWE).
- **Inteligencia Artificial**: Explica sobreajuste, ataques adversariales y sesgos.
- **Física**: Conecta complejidad computacional con termodinámica y límite de Landauer.
- **Filosofía**: Establece límites fundamentales al conocimiento computacional.

---

## Licencia

MIT
