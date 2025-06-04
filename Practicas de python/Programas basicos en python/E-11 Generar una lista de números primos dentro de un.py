def generar_primos(inicio, fin):

    primos = []

    for num in range(inicio, fin + 1):

        if num > 1:  # Los números menores o iguales a 1 no son primos

            for i in range(2, int(num**0.5) + 1):

                if (num % i) == 0:

                    break

            else:

                primos.append(num)

    return primos
  
inicio = int(input("Ingrese el inicio del rango: "))

fin = int(input("Ingrese el fin del rango: "))

print("Números primos entre", inicio, "y", fin, ":", generar_primos(inicio, fin))