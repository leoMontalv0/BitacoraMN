# Método de la Secante
def metodo_secante(funcion, anterior, actual, tol=1e-6, iter_max=100):

    print(f"{'Paso':<8}{'Aprox.':<15}{'f(x)':<15}{'Diferencia':<15}")
    print("=" * 55)

    contador = 0

    while contador < iter_max:

        fa = funcion(anterior)
        fb = funcion(actual)

        if abs(fb - fa) < 1e-12:
            print("\nNo es posible continuar: denominador cercano a cero.")
            return None

        siguiente = actual - (fb * (actual - anterior)) / (fb - fa)

        diferencia = abs(siguiente - actual)

        print(
            f"{contador+1:<8}"
            f"{siguiente:<15.6f}"
            f"{funcion(siguiente):<15.6f}"
            f"{diferencia:<15.6f}"
        )

        if diferencia <= tol:
            print(f"\nSolución aproximada: {siguiente:.6f}")
            print(f"Iteraciones realizadas: {contador+1}")
            return siguiente

        anterior = actual
        actual = siguiente
        contador += 1

    print("\nSe alcanzó el número máximo de iteraciones.")
    return None


# Ejemplo
print("=== Ejemplo: f(x) = x² - 5 ===")

def funcion1(x):
    return x**2 - 5

metodo_secante(funcion1, 2.0, 3.0)


# Ejercicio
print("\n=== Ejercicio: f(x) = x³ - 8 ===")

def funcion2(x):
    return x**3 - 8

metodo_secante(funcion2, 1.0, 3.0)
