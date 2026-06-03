import math

def f(x):
    return x**2 + 1

# Puntos y pesos para Gauss de 2 puntos
x1 = -1 / math.sqrt(3)
x2 = 1 / math.sqrt(3)

w1 = 1
w2 = 1

resultado = w1 * f(x1) + w2 * f(x2)

print("Resultado aproximado:", resultado)