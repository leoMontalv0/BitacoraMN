# Método de Gauss-Seidel

## Definición

El método de Gauss-Seidel es una técnica numérica iterativa empleada para aproximar la solución de sistemas de ecuaciones lineales. Su principal característica es que cada valor calculado se utiliza inmediatamente en los cálculos posteriores de la misma iteración, permitiendo obtener resultados más rápidamente que otros métodos iterativos.

Este procedimiento resulta especialmente eficiente cuando la matriz de coeficientes posee una diagonal dominante, ya que en esas condiciones la convergencia suele ser estable y rápida.

---

## Fórmula

Para cada variable del sistema:

xᵢ^(k+1) = (bᵢ − ΣAᵢⱼxⱼ) / Aᵢᵢ

considerando:

* Los valores actualizados en la iteración actual para j < i.
* Los valores de la iteración anterior para j > i.

El error puede calcularse mediante:

Error = max |xᵢ^(k+1) − xᵢ^(k)|

Donde:

* A = matriz de coeficientes.
* b = vector independiente.
* x = vector solución.
* k = número de iteración.

---

## Algoritmo

1. Escribir el sistema de ecuaciones en forma matricial.
2. Elegir valores iniciales para las incógnitas.
3. Despejar cada variable de su ecuación correspondiente.
4. Calcular la primera variable utilizando los valores disponibles.
5. Utilizar inmediatamente el nuevo resultado para calcular la siguiente variable.
6. Continuar hasta actualizar todas las incógnitas.
7. Comparar los nuevos valores con los de la iteración anterior.
8. Si el error es menor que la tolerancia establecida, detener el proceso.
9. En caso contrario, repetir una nueva iteración.
10. Mostrar la aproximación obtenida.

---

## Ejemplo

Sistema 3×3:

5x + y + z = 7

x + 6y + z = 9

x + y + 7z = 10

Valores iniciales:

x⁽⁰⁾ = 0

y⁽⁰⁾ = 0

z⁽⁰⁾ = 0

### Iteración 1

x = (7 − 0 − 0)/5 = 1.4000

y = (9 − 1.4000 − 0)/6 = 1.2667

z = (10 − 1.4000 − 1.2667)/7 = 1.0476

### Iteración 2

x = (7 − 1.2667 − 1.0476)/5 = 0.9371

y = (9 − 0.9371 − 1.0476)/6 = 1.1692

z = (10 − 0.9371 − 1.1692)/7 = 1.1277

Después de varias iteraciones:

x ≈ 1

y ≈ 1

z ≈ 1

---

## Ejemplo y Caso de Prueba

**Caso de prueba:** Sistema 3×3 diagonal dominante.

Sistema:

5x + y + z = 7

x + 6y + z = 9

x + y + 7z = 10

| Iteración | x      | y      | z      | Error máximo |
| --------- | ------ | ------ | ------ | ------------ |
| 0         | 0.0000 | 0.0000 | 0.0000 | —            |
| 1         | 1.4000 | 1.2667 | 1.0476 | 1.4000       |
| 2         | 0.9371 | 1.1692 | 1.1277 | 0.4629       |
| 3         | 0.9406 | 1.1553 | 1.1292 | 0.0139       |
| 4         | 0.9431 | 1.1546 | 1.1289 | 0.0025       |
| 5         | 0.9433 | 1.1546 | 1.1289 | 0.0002       |

Solución aproximada:

x = 0.9433

y = 1.1546

z = 1.1289

---

## Ejercicio

Sistema 4×4:

8x + y + z + w = 11

x + 8y + z + w = 11

x + y + 8z + w = 11

x + y + z + 8w = 11

| Iteración | x      | y      | z      | w      | Error máximo |
| --------- | ------ | ------ | ------ | ------ | ------------ |
| 0         | 0.0000 | 0.0000 | 0.0000 | 0.0000 | —            |
| 1         | 1.3750 | 1.2031 | 1.0527 | 0.9211 | 1.3750       |
| 2         | 0.9779 | 1.0060 | 1.0119 | 1.0005 | 0.3971       |
| 3         | 0.9977 | 0.9987 | 1.0004 | 1.0004 | 0.0198       |
| 4         | 1.0001 | 0.9999 | 1.0000 | 1.0000 | 0.0024       |
| 5         | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0001       |

### Resultado

* Entrada: sistema lineal 4×4 diagonal dominante.
* Resultado esperado: x = 1, y = 1, z = 1, w = 1.
* Resultado obtenido: x = 1.0000, y = 1.0000, z = 1.0000, w = 1.0000.
* Iteraciones requeridas: 5.
* Error final: menor que 1×10⁻⁴.

