# Interpolacion de Newton

x = [1,2,3]
y = [2,3,5]

b0 = y[0]
b1 = (y[1]-y[0])/(x[1]-x[0])
b2 = (((y[2]-y[1])/(x[2]-x[1])) - b1)/(x[2]-x[0])

xp = 2.5

yp = b0 + b1*(xp-x[0]) + b2*(xp-x[0])*(xp-x[1])

print("Valor aproximado:", round(yp,4))