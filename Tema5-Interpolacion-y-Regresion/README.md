# Tema 5 - Interpolación y Regresión

Este tema abarca los principales métodos numéricos para estimar valores desconocidos a partir de datos conocidos, así como para encontrar la tendencia general de un conjunto de datos.

Cada método cuenta con dos archivos:
- El **primero** contiene el ejercicio base del tema.
- El **segundo** (`*2.py`) contiene un ejercicio adicional con datos de contexto real.

---

## ¿Qué es la interpolación?

La interpolación es una técnica matemática que permite **estimar valores intermedios** dentro de un conjunto de datos conocidos. Es útil cuando no se puede medir directamente un valor, pero sí se tienen mediciones cercanas a él.

---

## Métodos

### 📐 Interpolación Lineal
**Archivos:** `InterpoLineal.py` / `InterpoLineal2.py`

Método más simple de interpolación. Estima un valor desconocido entre dos puntos conocidos trazando una línea recta entre ellos. Funciona bien cuando los datos tienen un comportamiento aproximadamente lineal en el intervalo de interés. Usa solo **2 puntos**: uno a cada lado del valor buscado.

**Fórmula:**
```
y = y0 + ((x - x0) * (y1 - y0)) / (x1 - x0)
```

---

### 🔢 Interpolación de Lagrange
**Archivos:** `interpoLagange.py` / `interpoLagange2.py`

Método que construye un polinomio que pasa exactamente por todos los puntos conocidos. Para cada punto calcula un "peso" (polinomio base) que vale 1 en ese punto y 0 en los demás, luego los combina. No requiere que los puntos estén igualmente espaciados y es fácil de implementar, aunque puede volverse inestable con muchos puntos.

**Ventaja:** funciona con cualquier número de puntos.

---

### 📊 Interpolación de Newton
**Archivos:** `interpolNewton.py` / `interpolNewton2.py`

Similar a Lagrange en resultado, pero usa **diferencias divididas** para construir el polinomio de forma incremental. Su ventaja es que si se agregan más puntos, no hay que recalcular todo desde cero, solo añadir un término. Es más eficiente computacionalmente que Lagrange para conjuntos grandes de datos.

**Fórmula:**
```
yp = b0 + b1*(xp-x0) + b2*(xp-x0)*(xp-x1)
```

---

### 📉 Mínimos Cuadrados
**Archivos:** `minCuadrados.py` / `minCuadrados2.py`

A diferencia de los métodos anteriores, **no busca pasar exactamente por todos los puntos**, sino encontrar la recta que mejor los representa minimizando el error total. Es ideal cuando los datos tienen ruido o pequeñas imprecisiones, como mediciones experimentales. El resultado es una ecuación de la forma `y = a + bx` que describe la tendencia general.

**Útil para:** datos experimentales, tendencias, predicciones.

---

## Resumen comparativo

| Método | Puntos necesarios | Pasa por todos los puntos | Ideal para |
|---|---|---|---|
| Lineal | 2 | ✅ | Datos simples, comportamiento lineal |
| Lagrange | 3 o más | ✅ | Polinomio exacto, pocos puntos |
| Newton | 3 o más | ✅ | Cuando se pueden agregar más puntos |
| Mínimos Cuadrados | 3 o más | ❌ | Datos con ruido o imprecisiones |

---

*Tema 5 — Métodos Numéricos*
