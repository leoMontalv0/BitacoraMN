# Metodo de Euler
# dT/dt = -0.1(T-20)

h = 0.5
t = 0
T = 80

print("t\tT")

while t <= 1.5:

    print(round(t,2), "\t", round(T,4))

    # ecuacion diferencial
    f = -0.1 * (T - 20)

    # formula de Euler
    T = T + h * f

    # avanzar tiempo
    t = t + h