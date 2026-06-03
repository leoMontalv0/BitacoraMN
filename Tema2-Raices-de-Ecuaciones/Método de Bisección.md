# Bisección

## Definición
Es uno de los métodos más simples para encontrar raíces de ecuaciones continuas.
Divide repetidamente un intervalo [a, b] a la mitad y selecciona el subintervalo
donde existe la raíz (donde f cambia de signo), hasta converger a ella. Su
convergencia es lineal: gana aproximadamente un bit de precisión por iteración.
Requiere que f(a) y f(b) tengan signos opuestos (teorema del valor intermedio).


## Fórmula

**Punto medio:**

    c = (a + b) / 2

**Error máximo garantizado tras n iteraciones:**

    |error| ≤ (b − a) / 2ⁿ

Donde:
- a   = extremo izquierdo del intervalo
- b   = extremo derecho del intervalo
- c   = punto medio (candidato a raíz)
- Criterio de paro: |b − a| < tolerancia


## Algoritmo
Verificar que f(a) · f(b) < 0 (cambio de signo en el intervalo).

Calcular punto medio c = (a + b) / 2.

Si |b − a| < tolerancia → retornar c como raíz.

Si f(a) · f(c) < 0 → la raíz está en [a, c], hacer b = c.

Si f(b) · f(c) < 0 → la raíz está en [c, b], hacer a = c.

Repetir desde el paso 2.


## Ejemplo

f(x) = x³ − 4    Intervalo [1, 2]    f(1) = −3 < 0    f(2) = 4 > 0

```text
iter 1: c = 1.5,     f(1.5)   = -0.6250 < 0 → a = 1.5    → [1.5,    2.0]
iter 2: c = 1.75,    f(1.75)  =  1.3594 > 0 → b = 1.75   → [1.5,    1.75]
iter 3: c = 1.625,   f(1.625) =  0.2910 > 0 → b = 1.625  → [1.5,    1.625]
iter 4: c = 1.5625,  f(1.5625)= -0.1853 < 0 → a = 1.5625 → [1.5625, 1.625]
...
Raíz aproximada: ∛4 = 1.587401...
```

## Ejemplo y Caso de Prueba

**Caso de prueba:** f(x) = x³ − 4, a = 1, b = 2, tolerancia = 1e-6

|  n  |       a      |       b      |       c      |    f(c)   |  |b − a|  |
| :-: | :----------: | :----------: | :----------: | :-------: | :-------: |
|  1  | 1.0000000000 | 2.0000000000 | 1.5000000000 | -6.250e-1 | 1.0000e+0 |
|  2  | 1.5000000000 | 2.0000000000 | 1.7500000000 |  1.359e+0 | 5.0000e-1 |
|  3  | 1.5000000000 | 1.7500000000 | 1.6250000000 |  2.910e-1 | 2.5000e-1 |
|  4  | 1.5000000000 | 1.6250000000 | 1.5625000000 | -1.853e-1 | 1.2500e-1 |
|  5  | 1.5625000000 | 1.6250000000 | 1.5937500000 |  4.868e-2 | 6.2500e-2 |
| ... |      ...     |      ...     |      ...     |    ...    |    ...    |
|  20 | 1.5874004364 | 1.5874023438 | 1.5874013901 | -1.198e-6 | 1.9073e-6 |
|  21 | 1.5874013901 | 1.5874023438 | 1.5874018669 |  2.407e-6 | 9.5367e-7 |

**Ejercicio:** f(x) = x² − 5, intervalo [2, 3], tolerancia = 1e-6

|  n  |       a      |       b      |       c      |    f(c)   |  |b − a|  |
| :-: | :----------: | :----------: | :----------: | :-------: | :-------: |
|  1  | 2.0000000000 | 3.0000000000 | 2.5000000000 |  1.250e+0 | 1.0000e+0 |
|  2  | 2.0000000000 | 2.5000000000 | 2.2500000000 |  6.250e-2 | 5.0000e-1 |
|  3  | 2.0000000000 | 2.2500000000 | 2.1250000000 | -4.844e-1 | 2.5000e-1 |
|  4  | 2.1250000000 | 2.2500000000 | 2.1875000000 | -2.148e-1 | 1.2500e-1 |
|  5  | 2.1875000000 | 2.2500000000 | 2.2187500000 | -7.715e-2 | 6.2500e-2 |
| ... |      ...     |      ...     |      ...     |    ...    |    ...    |
|  20 | 2.2360668182 | 2.2360687256 | 2.2360677719 | -1.273e-6 | 1.9073e-6 |
|  21 | 2.2360677719 | 2.2360687256 | 2.2360682487 |  8.589e-7 | 9.5367e-7 |

**Resultado:**

* Entrada: f(x) = x² − 5, a = 2, b = 3, tolerancia = 1e-6
* Resultado esperado: 2.2361
* Resultado float:    2.2361
* Iteraciones:        21
* Error acumulado:    8.59e-7

```
```

