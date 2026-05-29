# Minimos cuadrados

x = [1,2,3,4]
y = [2,4,5,7]

n = len(x)

sumx = sum(x)
sumy = sum(y)
sumxy = 0
sumx2 = 0

for i in range(n):

    sumxy += x[i] * y[i]
    sumx2 += x[i]**2

b = ((n*sumxy) - (sumx*sumy)) / ((n*sumx2) - (sumx**2))

a = (sumy - b*sumx)/n

print("y =", round(a,4), "+", round(b,4), "x")