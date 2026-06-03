# ==================================================
# MÉTODO DE TAYLOR
# Ejercicio 2
# Orden 2
# dy/dx = x² - y
# ==================================================

def f(x, y):
    return x**2 - y

def df(x, y):
    return 2*x - f(x, y)

x = 0
y = 1

h = 0.2
n = 5

print("Paso\t x\t\t y")

for i in range(n):

    y = y + h*f(x, y) + (h**2/2)*df(x, y)

    x += h

    print(i+1, "\t", round(x,4), "\t", round(y,6))

# Resultado aproximado:
# Paso     x               y
#1        0.2     0.82
#2        0.4     0.6876
#3        0.6     0.608632
#4        0.8     0.587878
#5        1.0     0.62926