# ErrorDeTruncamiento.py

numero_real = 3.14159265

numero_truncado = int(numero_real * 100) / 100

error = abs(numero_real - numero_truncado)

print("Número real:", numero_real)
print("Número truncado:", numero_truncado)
print("Error de truncamiento:", error)