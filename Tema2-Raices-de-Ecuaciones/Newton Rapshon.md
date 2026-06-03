# Método de Newton-Raphson

## Definición

Algoritmo iterativo para encontrar raíces de funciones no lineales f(x) = 0.
Parte de una aproximación inicial x₀ y utiliza la pendiente de la función en
cada iteración para acercarse rápidamente a la solución. Presenta convergencia
cuadrática cuando la estimación inicial está suficientemente cerca de la raíz.

## Fórmula

x_(n+1) = x_n - f(x_n) / f'(x_n)

Donde:

* f(x) = función original
* f'(x) = derivada de la función
* xₙ = aproximación actual
* xₙ₊₁ = aproximación siguiente

## Algoritmo

1. Definir la función f(x) y obtener su derivada f'(x).
2. Seleccionar un valor inicial x₀.
3. Evaluar la función y su derivada en xₙ.
4. Calcular una nueva aproximación mediante la fórmula de Newton-Raphson.
5. Determinar el error como |xₙ₊₁ − xₙ|.
6. Si el error es menor que la tolerancia establecida, finalizar.
7. En caso contrario, actualizar xₙ ← xₙ₊₁ y repetir el proceso.
8. Reportar la raíz aproximada obtenida.

## Ejemplo

f(x) = x² - 5

f'(x) = 2x

x₀ = 2

x₁ = 2 - (-1)/4 = 2.25

x₂ = 2.25 - (0.0625)/4.5 = 2.23611

x₃ = 2.23611 - (...) = 2.23606798

Raíz exacta: √5 = 2.236067977...

## Ejemplo y Caso de Prueba

**Caso de prueba:** f(x) = x² - 5, x₀ = 2, tolerancia = 1e-6

| n | xₙ           | f(xₙ)     | f′(xₙ) | |xₙ₊₁ − xₙ| |
| - | ------------ | --------- | ------ | ----------- |
| 0 | 2.0000000000 | -1.000e+0 | 4.0000 | 2.500e-1    |
| 1 | 2.2500000000 | 6.250e-2  | 4.5000 | 1.389e-2    |
| 2 | 2.2361111111 | 1.929e-4  | 4.4722 | 4.313e-5    |
| 3 | 2.2360679779 | 1.860e-9  | 4.4721 | 4.160e-10   |

**Ejercicio:** f(x) = x³ - 8, x₀ = 1.5, tolerancia = 1e-6

f'(x) = 3x²

| n | xₙ           | f(xₙ)     | f′(xₙ)  | |xₙ₊₁ − xₙ| |
| - | ------------ | --------- | ------- | ----------- |
| 0 | 1.5000000000 | -4.625e+0 | 6.7500  | 6.852e-1    |
| 1 | 2.1851851852 | 2.435e+0  | 14.3241 | 1.700e-1    |
| 2 | 2.0152476019 | 1.845e-1  | 12.1837 | 1.514e-2    |
| 3 | 2.0001115573 | 1.339e-3  | 12.0013 | 1.116e-4    |
| 4 | 2.0000000062 | 7.452e-8  | 12.0000 | 6.200e-9    |

**Resultado:**

* Entrada: f(x) = x³ - 8, x₀ = 1.5, tolerancia = 1e-6
* Resultado esperado: 2.0000
* Resultado float:    2.0000
* Iteraciones:        4
* Error acumulado:    6.20e-9
