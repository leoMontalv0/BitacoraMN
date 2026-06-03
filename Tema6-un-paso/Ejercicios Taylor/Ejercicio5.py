# ==================================================
# MÉTODO DE TAYLOR
# Ejercicio 5
# Orden 3
# dy/dx = y
# ==================================================

def f(x, y):
    return y

def d2f(x, y):
    return y

def d3f(x, y):
    return y

x = 0
y = 1

h = 0.2
n = 5

print("Paso\t x\t\t y")

for i in range(n):

    y = (
        y +
        h*f(x, y) +
        (h**2/2)*d2f(x, y) +
        (h**3/6)*d3f(x, y)
    )

    x += h

    print(i+1, "\t", round(x,4), "\t", round(y,6))

# Resultado aproximado:
# Paso     x               y
#1        0.2     1.221333
#2        0.4     1.491655
#3        0.6     1.821808
#4        0.8     2.225035
#5        1.0     2.717509