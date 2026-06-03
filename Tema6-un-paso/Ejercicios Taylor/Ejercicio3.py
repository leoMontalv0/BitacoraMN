# ==================================================
# MÉTODO DE TAYLOR
# Ejercicio 3
# dy/dx = 0.5y
# ==================================================

def f(x, y):
    return 0.5*y

def df(x, y):
    return 0.25*y

x = 0
y = 100

h = 0.5
n = 8

print("Tiempo\t Población")

for i in range(n):

    y = y + h*f(x, y) + (h**2/2)*df(x, y)

    x += h

    print(round(x,2), "\t", round(y,4))

# Resultado aproximado:
# Tiempo   Población
#0.5      128.125
#1.0      164.1602
#1.5      210.3302
#2.0      269.4856
#2.5      345.2784
#3.0      442.3879
#3.5      566.8095
#4.0      726.2247