# Metodo RK4

h = 0.5
t = 0
T = 80

print("t\tT")

while t <= 1.5:

    print(round(t,2), "\t", round(T,4))

    k1 = -0.1 * (T - 20)

    k2 = -0.1 * ((T + (h/2)*k1) - 20)

    k3 = -0.1 * ((T + (h/2)*k2) - 20)

    k4 = -0.1 * ((T + h*k3) - 20)

    T = T + (h/6) * (k1 + 2*k2 + 2*k3 + k4)

    t = t + h