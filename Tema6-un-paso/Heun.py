# Metodo de Euler Mejorado

h = 0.5
t = 0
T = 80

print("t\tT")

while t <= 1.5:

    print(round(t,2), "\t", round(T,4))

    # primera pendiente
    k1 = -0.1 * (T - 20)

    # valor estimado
    Ttemp = T + h * k1

    # segunda pendiente
    k2 = -0.1 * (Ttemp - 20)

    # formula de Heun
    T = T + (h/2) * (k1 + k2)

    t = t + h