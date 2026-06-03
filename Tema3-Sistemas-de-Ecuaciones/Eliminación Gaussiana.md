# Método de Eliminación Gaussiana

## Definición

La eliminación gaussiana es una técnica algebraica utilizada para resolver sistemas de ecuaciones lineales. El método consiste en transformar gradualmente la matriz de coeficientes en una forma triangular superior mediante operaciones elementales entre filas. Una vez obtenida esta estructura, las incógnitas se calculan comenzando por la última ecuación y sustituyendo los valores obtenidos en las ecuaciones anteriores.

Se trata de un método directo, por lo que la solución se obtiene en un número finito de pasos sin necesidad de aproximaciones sucesivas.

---

## Fórmula

Para anular los elementos que se encuentran debajo del pivote:

factor = A[i][k] / A[k][k]

Filaᵢ = Filaᵢ − factor · Filaₖ

Posteriormente, la solución se determina mediante sustitución regresiva:

x[i] = (b[i] − Σ(A[i][j] · x[j])) / A[i][i]

Donde:

* A = matriz de coeficientes.
* b = vector independiente.
* x = vector solución.
* factor = multiplicador utilizado para eliminar elementos.
* A[k][k] = pivote de la columna actual.

---

## Algoritmo

1. Escribir el sistema de ecuaciones en forma matricial.
2. Construir la matriz aumentada [A|b].
3. Seleccionar el pivote de la primera columna.
4. Eliminar los elementos situados debajo del pivote utilizando operaciones entre filas.
5. Repetir el procedimiento para las columnas restantes.
6. Obtener una matriz triangular superior.
7. Resolver la última ecuación para encontrar la última incógnita.
8. Sustituir el valor obtenido en las ecuaciones superiores.
9. Continuar hasta calcular todas las variables.
10. Presentar el vector solución.

---

## Ejemplo

Sistema 3×3:

x + y + z = 6

2x − y + z = 3

x + 2y − z = 2

Matriz aumentada:

[ 1   1   1 | 6 ]

[ 2  -1   1 | 3 ]

[ 1   2  -1 | 2 ]

### Eliminación

Usando el pivote de la primera fila:

F₂ ← F₂ − 2F₁

F₃ ← F₃ − F₁

Resultado:

[ 1   1   1 |  6 ]

[ 0  -3  -1 | -9 ]

[ 0   1  -2 | -4 ]

Usando el pivote de la segunda fila:

F₃ ← F₃ + (1/3)F₂

Resultado:

[ 1   1    1 |  6 ]

[ 0  -3   -1 | -9 ]

[ 0   0  -7/3 | -7 ]

### Sustitución hacia atrás

z = 3

y = 2

x = 1

Solución:

x = 1

y = 2

z = 3

---

## Ejemplo y Caso de Prueba

**Caso de prueba:** Sistema 3×3 con solución conocida.

Sistema:

x + y + z = 6

2x − y + z = 3

x + 2y − z = 2

### Eliminación hacia adelante

| Paso | Operación         | Resultado principal |     |
| ---- | ----------------- | ------------------- | --- |
| 1    | F₂ ← F₂ − 2F₁     | [0, -3, -1          | -9] |
| 2    | F₃ ← F₃ − F₁      | [0, 1, -2           | -4] |
| 3    | F₃ ← F₃ + (1/3)F₂ | [0, 0, -7/3         | -7] |

### Sustitución

| Variable | Valor |
| -------- | ----- |
| z        | 3     |
| y        | 2     |
| x        | 1     |

---

## Ejercicio

Sistema 4×4:

4x + y + z + w = 7

x + 5y + z + w = 8

x + y + 6z + w = 9

x + y + z + 7w = 10

### Operaciones principales

| Paso | Pivote | Fila modificada | Factor |
| ---- | ------ | --------------- | ------ |
| 1    | 4      | F₂              | 0.2500 |
| 2    | 4      | F₃              | 0.2500 |
| 3    | 4      | F₄              | 0.2500 |
| 4    | 4.75   | F₃              | 0.1579 |
| 5    | 4.75   | F₄              | 0.1579 |
| 6    | 5.58   | F₄              | 0.1270 |

### Resultado

* Entrada: sistema lineal 4×4.
* Resultado esperado: x = 1, y = 1, z = 1, w = 1.
* Resultado obtenido: x = 1.0000, y = 1.0000, z = 1.0000, w = 1.0000.
* Número de eliminaciones: 6.
* Error numérico: aproximadamente 0.

