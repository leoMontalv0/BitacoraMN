```python
# Método de Falsa Posición

def metodo_falsa_posicion(funcion, limite_inferior, limite_superior,
                          tol=1e-6, iteraciones_max=100):

    if funcion(limite_inferior) * funcion(limite_superior) > 0:
        print("El intervalo no contiene una raíz válida.")
        return None

    print(f"{'Paso':<8}{'Inferior':<12}{'Superior':<12}"
          f"{'Aprox.':<12}{'f(x)':<15}{'Error':<12}")
    print("=" * 75)

    paso = 1

    while paso <= iteraciones_max:

        valor_inf = funcion(limite_inferior)
        valor_sup = funcion(limite_superior)

        aproximacion = limite_superior - (
            valor_sup * (limite_superior - limite_inferior)
        ) / (valor_sup - valor_inf)

        valor_aprox = funcion(aproximacion)

        error = abs(valor_aprox)

        print(
            f"{paso:<8}"
            f"{limite_inferior:<12.6f}"
            f"{limite_superior:<12.6f}"
            f"{aproximacion:<12.6f}"
            f"{valor_aprox:<15.6f}"
            f"{error:<12.6f}"
        )

        if error <= tol:
            print(f"\nRaíz aproximada: {aproximacion:.6f}")
            print(f"Iteraciones realizadas: {paso}")
            return aproximacion

        if valor_inf * valor_aprox < 0:
            limite_superior = aproximacion
        else:
            limite_inferior = aproximacion

        paso += 1

    print("\nNo se alcanzó la convergencia.")
    return None


# Ejemplo
print("=== Ejemplo: f(x) = x³ - 4 ===")

def funcion1(x):
    return x**3 - 4

metodo_falsa_posicion(funcion1, 1.0, 2.0)


# Ejercicio
print("\n=== Ejercicio: f(x) = x² - 5 ===")

def funcion2(x):
    return x**2 - 5

metodo_falsa_posicion(funcion2, 2.0, 3.0)
```
