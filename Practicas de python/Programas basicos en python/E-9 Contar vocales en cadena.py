def contar_vocales(cadena):
    vocales = 'aeiouáéíóú'

    contador = 0

    for char in cadena:

        if char in vocales:

            contador += 1

    return contador

cadena = input("Ingrese una cadena:")

print("numeros de vocales", contar_vocales(cadena))