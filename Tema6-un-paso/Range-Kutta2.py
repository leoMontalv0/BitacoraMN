# Metodo RK2

h = 0.5
t = 0
T = 80

print("t\tT")

while t <= 1.5:

    print(round(t,2), "\t", round(T,4))

    k1 = -0.1 * (T - 20)

    k2 = -0.1 * ((T + h*k1) - 20)

    T = T + (h/2) * (k1 + k2)

    t = t + h