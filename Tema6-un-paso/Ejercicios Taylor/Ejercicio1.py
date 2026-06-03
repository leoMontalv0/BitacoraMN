# ==================================================
# MÉTODO DE TAYLOR
# Ejercicio 1
# Orden 2
# dy/dx = x + y
# ==================================================

def f(x, y):
    return x + y

def df(x, y):
    return 1 + f(x, y)

x = 0
y = 1

h = 0.1
n = 10

print("Paso\t x\t\t y")

for i in range(n):

    y = y + h*f(x, y) + (h**2/2)*df(x, y)

    x = x + h

    print(i+1, "\t", round(x,4), "\t", round(y,6))

# Resultado aproximado:
# Paso     x               y
#1        0.1     1.11
#2        0.2     1.24205
#3        0.3     1.398465
#4        0.4     1.581804
#5        0.5     1.794894
#6        0.6     2.040857
#7        0.7     2.323147
#8        0.8     2.645578
#9        0.9     3.012364
#10       1.0     3.428162