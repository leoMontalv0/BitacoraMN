# Método de Jacobi

## Definición

El método de Jacobi es una técnica iterativa utilizada para aproximar la solución de sistemas de ecuaciones lineales. En cada iteración, todas las incógnitas se calculan empleando únicamente los valores obtenidos en la iteración anterior. Esto significa que ninguna variable se actualiza hasta que se hayan calculado todas las nuevas aproximaciones.

Su principal ventaja es la simplicidad de implementación y la posibilidad de realizar cálculos de forma independiente para cada variable. El método suele converger cuando la matriz de coeficientes presenta diagonal dominante.

---

## Fórmula

Para cada ecuación del sistema:

xᵢ^(k+1) = (bᵢ − Σ Aᵢⱼxⱼ^(k)) / Aᵢᵢ

con j ≠ i.

El error de la iteración se calcula mediante:

Error = max |xᵢ^(k+1) − xᵢ^(k)|

Donde:

* A = matriz de coeficientes.
* b = vector de términos independientes.
* x = vector solución.
* k = número de iteración.
* Aᵢᵢ = elemento de la diagonal principal.

---

## Algoritmo

1. Expresar el sistema en forma matricial.
2. Despejar cada incógnita de su ecuación correspondiente.
3. Asignar valores iniciales a todas las variables.
4. Calcular nuevas aproximaciones utilizando únicamente los valores de la iteración anterior.
5. Guardar los resultados obtenidos en un nuevo vector.
6. Determinar el error entre ambas iteraciones.
7. Comparar el error con la tolerancia establecida.
8. Si el error es suficientemente pequeño, finalizar el proceso.
9. En caso contrario, reemplazar los valores anteriores y repetir.
10. Mostrar la solución aproximada.

---

## Ejemplo

Sistema 3×3:

6x + y + z = 8

x + 5y + z = 7

x + y + 4z = 6

Valores iniciales:

x⁽⁰⁾ = 0

y⁽⁰⁾ = 0

z⁽⁰⁾ = 0

### Iteración 1

x = (8 − 0 − 0)/6 = 1.3333

y = (7 − 0 − 0)/5 = 1.4000

z = (6 − 0 − 0)/4 = 1.5000

### Iteración 2

x = (8 − 1.4000 − 1.5000)/6 = 0.8500

y = (7 − 1.3333 − 1.5000)/5 = 0.8333

z = (6 − 1.3333 − 1.4000)/4 = 0.8167

### Iteración 3

x = (8 − 0.8333 − 0.8167)/6 = 1.0583

y = (7 − 0.8500 − 0.8167)/5 = 1.0667

z = (6 − 0.8500 − 0.8333)/4 = 1.0792

Después de varias iteraciones:

x ≈ 1

y ≈ 1

z ≈ 1

---

## Ejemplo y Caso de Prueba

**Caso de prueba:** Sistema 3×3 diagonal dominante.

Sistema:

6x + y + z = 8

x + 5y + z = 7

x + y + 4z = 6

| Iteración | x      | y      | z      | Error máximo |
| --------- | ------ | ------ | ------ | ------------ |
| 0         | 0.0000 | 0.0000 | 0.0000 | —            |
| 1         | 1.3333 | 1.4000 | 1.5000 | 1.5000       |
| 2         | 0.8500 | 0.8333 | 0.8167 | 0.6833       |
| 3         | 1.0583 | 1.0667 | 1.0792 | 0.2625       |
| 4         | 0.9757 | 0.9725 | 0.9688 | 0.1104       |
| 5         | 1.0098 | 1.0111 | 1.0130 | 0.0442       |
| ...       | ...    | ...    | ...    | ...          |
| 18        | 1.0000 | 1.0000 | 1.0000 | 8.7×10⁻⁷     |

Solución aproximada:

x = 1

y = 1

z = 1

---

## Ejercicio

Sistema 4×4:

9x + y + z + w = 12

x + 9y + z + w = 12

x + y + 9z + w = 12

x + y + z + 9w = 12

| Iteración | x      | y      | z      | w      | Error máximo |
| --------- | ------ | ------ | ------ | ------ | ------------ |
| 0         | 0.0000 | 0.0000 | 0.0000 | 0.0000 | —            |
| 1         | 1.3333 | 1.3333 | 1.3333 | 1.3333 | 1.3333       |
| 2         | 0.8889 | 0.8889 | 0.8889 | 0.8889 | 0.4444       |
| 3         | 1.0370 | 1.0370 | 1.0370 | 1.0370 | 0.1481       |
| 4         | 0.9877 | 0.9877 | 0.9877 | 0.9877 | 0.0493       |
| 5         | 1.0041 | 1.0041 | 1.0041 | 1.0041 | 0.0164       |
| ...       | ...    | ...    | ...    | ...    | ...          |
| 16        | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 9.4×10⁻⁷     |

### Resultado

* Entrada: sistema lineal 4×4 diagonal dominante.
* Resultado esperado: x = 1, y = 1, z = 1, w = 1.
* Resultado obtenido: x = 1.0000, y = 1.0000, z = 1.0000, w = 1.0000.
* Iteraciones requeridas: 16.
* Error final: menor que 1×10⁻⁶.

### Comparación con Gauss-Seidel

| Método       | Iteraciones aproximadas |
| ------------ | ----------------------- |
| Jacobi       | 16                      |
| Gauss-Seidel | 9                       |

En este sistema, Gauss-Seidel alcanza la convergencia en menos iteraciones debido a que aprovecha los valores actualizados durante el mismo ciclo de cálculo.

