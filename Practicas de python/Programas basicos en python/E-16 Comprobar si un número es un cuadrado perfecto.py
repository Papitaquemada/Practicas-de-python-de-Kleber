import math

def es_cuadrado_perfecto(n):

    raiz = math.isqrt(n)

    return raiz * raiz == n

numero = int(input("Introduce un número: "))

if es_cuadrado_perfecto(numero):

    print("cuadrado perfecto")

else:

    print("no es cuadrado perfecto")