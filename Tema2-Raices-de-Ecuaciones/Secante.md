# Método de la Secante

## Definición

El método de la secante es una técnica numérica utilizada para aproximar raíces de ecuaciones no lineales. A diferencia del método de Newton-Raphson, no requiere calcular la derivada de la función. Para estimar la siguiente aproximación utiliza la recta que pasa por dos puntos consecutivos de la curva, generando una sucesión de valores que converge hacia la raíz. Su velocidad de convergencia suele ser mayor que la de bisección y menor que la de Newton-Raphson.

---

## Fórmula

**Iteración de la secante:**

xₙ₊₁ = xₙ − [f(xₙ)(xₙ − xₙ₋₁)] / [f(xₙ) − f(xₙ₋₁)]

Donde:

* xₙ = aproximación actual.
* xₙ₋₁ = aproximación previa.
* f(x) = función evaluada.
* Error = |xₙ₊₁ − xₙ|.

---

## Algoritmo

1. Definir la función f(x).
2. Seleccionar dos valores iniciales x₀ y x₁.
3. Evaluar la función en ambos puntos.
4. Calcular una nueva aproximación utilizando la ecuación de la secante.
5. Determinar el error entre las dos últimas aproximaciones.
6. Si el error es menor que la tolerancia, detener el proceso.
7. Actualizar los valores: x₀ ← x₁ y x₁ ← x₂.
8. Repetir hasta obtener la precisión deseada.
9. Mostrar la raíz aproximada encontrada.

---

## Ejemplo

f(x) = x² − 5

x₀ = 2.0

x₁ = 3.0

```text
x₂ = 3.0 - 4(3.0 - 2.0)/(4 - (-1))
    = 2.20000

x₃ = 2.20000 - (-0.1600)(2.20000 - 3.0)/(-0.1600 - 4)
    = 2.23077

x₄ = 2.23600

x₅ = 2.23606798...
```

Raíz exacta: √5 = 2.236067977...

---

## Ejemplo y Caso de Prueba

**Caso de prueba:** f(x) = x² − 5, x₀ = 2.0, x₁ = 3.0, tolerancia = 1e-6

| n | xₙ           | f(xₙ)      | |xₙ₊₁ − xₙ| |
| - | ------------ | ---------- | ----------- |
| 0 | 2.0000000000 | -1.0000e+0 | —           |
| 1 | 3.0000000000 | 4.0000e+0  | 1.0000e+0   |
| 2 | 2.2000000000 | -1.6000e-1 | 8.0000e-1   |
| 3 | 2.2307692308 | -2.3669e-2 | 3.0769e-2   |
| 4 | 2.2360201511 | -2.1389e-4 | 5.2509e-3   |
| 5 | 2.2360679250 | -2.3608e-7 | 4.7774e-5   |
| 6 | 2.2360679775 | 0.0000e+0  | 5.2500e-8   |

---

**Ejercicio:** f(x) = x³ − 8, x₀ = 1.0, x₁ = 3.0, tolerancia = 1e-6

| n | xₙ           | f(xₙ)      | |xₙ₊₁ − xₙ| |
| - | ------------ | ---------- | ----------- |
| 0 | 1.0000000000 | -7.0000e+0 | —           |
| 1 | 3.0000000000 | 1.9000e+1  | 2.0000e+0   |
| 2 | 1.5384615385 | -4.3600e+0 | 1.4615e+0   |
| 3 | 1.8405797101 | -1.7645e+0 | 3.0212e-1   |
| 4 | 2.0460829493 | 5.6616e-1  | 2.0550e-1   |
| 5 | 1.9961940873 | -4.5554e-2 | 4.9889e-2   |
| 6 | 1.9999472680 | -6.3276e-4 | 3.7532e-3   |
| 7 | 2.0000000490 | 5.8800e-7  | 5.2781e-5   |

---

**Resultado:**

* Entrada: f(x) = x³ − 8, x₀ = 1.0, x₁ = 3.0, tolerancia = 1e-6
* Resultado esperado: 2.0000
* Resultado float:    2.0000
* Iteraciones:        7
* Error acumulado:    5.88e-7

