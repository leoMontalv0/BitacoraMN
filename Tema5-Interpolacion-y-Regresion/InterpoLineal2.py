# Interpolacion lineal

# Ejercicio: Estimar la velocidad a los 4 segundos
# A los 2 segundos el auto va a 10 m/s
# A los 6 segundos el auto va a 30 m/s

x0 = 2
y0 = 10

x1 = 6
y1 = 30

x = 4

# formula
y = y0 + ((x - x0)*(y1 - y0))/(x1 - x0)

print("Valor interpolado:", y, "m/s")