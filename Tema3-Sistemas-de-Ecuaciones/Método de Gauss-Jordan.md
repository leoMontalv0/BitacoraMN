# Método de Eliminación Gauss-Jordan

## Definición

El método de Gauss-Jordan es un procedimiento algebraico utilizado para resolver sistemas de ecuaciones lineales mediante transformaciones sucesivas de la matriz aumentada. A diferencia de la eliminación gaussiana tradicional, este método continúa las operaciones hasta convertir la matriz de coeficientes en una matriz identidad. Cuando esto ocurre, los valores de las incógnitas pueden leerse directamente en la última columna de la matriz.

Es un método directo ampliamente utilizado en álgebra lineal debido a que permite obtener la solución sin realizar sustitución regresiva.

---

## Fórmula

### Normalización del pivote

Para convertir el pivote en 1:

Filaₖ = Filaₖ / A[k][k]

### Eliminación de la columna

Para cada fila i ≠ k:

factor = A[i][k]

Filaᵢ = Filaᵢ − factor · Filaₖ

Donde:

* A = matriz de coeficientes.
* b = vector de términos independientes.
* k = posición del pivote.
* factor = multiplicador utilizado para anular elementos.
* La solución se obtiene cuando la matriz de coeficientes se transforma en la identidad.

---

## Algoritmo

1. Escribir el sistema de ecuaciones en forma matricial.
2. Construir la matriz aumentada [A|b].
3. Seleccionar un pivote en la diagonal principal.
4. Dividir toda la fila por el pivote para convertirlo en 1.
5. Utilizar la fila pivote para eliminar los elementos de la misma columna en las demás filas.
6. Repetir el proceso para cada columna de la matriz.
7. Continuar hasta obtener una matriz identidad.
8. Leer directamente los valores de las incógnitas en la última columna.
9. Presentar la solución final.

---

## Ejemplo

Sistema 3×3:

x + 2y + z = 8

2x − y + z = 3

3x + y − z = 2

Matriz aumentada inicial:

```text
[ 1   2   1 | 8 ]
[ 2  -1   1 | 3 ]
[ 3   1  -1 | 2 ]
```

### Paso 1

Eliminar la primera columna:

```text
[ 1   2    1 |  8 ]
[ 0  -5   -1 | -13 ]
[ 0  -5   -4 | -22 ]
```

### Paso 2

Normalizar la segunda fila y eliminar la segunda columna:

```text
[ 1   0   0.6 | 2.8 ]
[ 0   1   0.2 | 2.6 ]
[ 0   0  -3.0 | -9 ]
```

### Paso 3

Normalizar la tercera fila y eliminar la tercera columna:

```text
[ 1   0   0 | 1 ]
[ 0   1   0 | 2 ]
[ 0   0   1 | 3 ]
```

Solución:

x = 1

y = 2

z = 3

---

## Ejemplo y Caso de Prueba

**Caso de prueba:** Sistema 3×3 con solución conocida.

Sistema:

x + 2y + z = 8

2x − y + z = 3

3x + y − z = 2

### Operaciones principales

| Paso | Operación          | Resultado         |
| ---- | ------------------ | ----------------- |
| 1    | F₂ ← F₂ − 2F₁      | [0, -5, -1 | -13] |
| 2    | F₃ ← F₃ − 3F₁      | [0, -5, -4 | -22] |
| 3    | F₂ ÷ (-5)          | [0, 1, 0.2 | 2.6] |
| 4    | F₁ ← F₁ − 2F₂      | [1, 0, 0.6 | 2.8] |
| 5    | F₃ ← F₃ + 5F₂      | [0, 0, -3 | -9]   |
| 6    | F₃ ÷ (-3)          | [0, 0, 1 | 3]     |
| 7    | Eliminar columna 3 | Matriz identidad  |

### Resultado obtenido

| Variable | Valor |
| -------- | ----- |
| x        | 1     |
| y        | 2     |
| z        | 3     |

---

## Ejercicio

Sistema 4×4:

5x + y + z + w = 8

x + 6y + z + w = 9

x + y + 7z + w = 10

x + y + z + 8w = 11

### Operaciones relevantes

| Paso | Pivote | Acción                     |
| ---- | ------ | -------------------------- |
| 1    | 5      | Eliminar columna 1         |
| 2    | 5.8    | Eliminar columna 2         |
| 3    | 6.65   | Eliminar columna 3         |
| 4    | 7.47   | Eliminar columna 4         |
| 5    | —      | Reducir a matriz identidad |

### Resultado

* Entrada: sistema lineal 4×4.
* Resultado esperado: x = 1, y = 1, z = 1, w = 1.
* Resultado obtenido: x = 1.0000, y = 1.0000, z = 1.0000, w = 1.0000.
* Operaciones realizadas: normalización y eliminación completa de columnas.
* Error numérico: aproximadamente 0.

