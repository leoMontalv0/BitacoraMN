# ==================================================
# MÉTODO DE TAYLOR
# Ejercicio 4
# dT/dt = -0.25(T - 20)
# ==================================================

def f(t, T):
    return -0.25*(T - 20)

def df(t, T):
    return -0.25*f(t, T)

t = 0
T = 100

h = 1
n = 10

print("Tiempo\t Temperatura")

for i in range(n):

    T = T + h*f(t, T) + (h**2/2)*df(t, T)

    t += h

    print(t, "\t", round(T,4))

# Resultado aproximado:
# Tiempo   Temperatura
#1        82.5
#2        68.8281
#3        58.147
#4        49.8023
#5        43.2831
#6        38.1899
#7        34.2109
#8        31.1022
#9        28.6736
#10       26.7763