# Interpolacion de Newton

# Ejercicio: Estimar la presión a 2500 metros de altitud
# Altitud (km): 1, 2, 3
# Presión (atm): 0.89, 0.78, 0.69

x = [1, 2, 3]
y = [0.89, 0.78, 0.69]

b0 = y[0]
b1 = (y[1]-y[0])/(x[1]-x[0])
b2 = (((y[2]-y[1])/(x[2]-x[1])) - b1)/(x[2]-x[0])

xp = 2.5

yp = b0 + b1*(xp-x[0]) + b2*(xp-x[0])*(xp-x[1])

print("Valor aproximado:", round(yp,4), "atm")