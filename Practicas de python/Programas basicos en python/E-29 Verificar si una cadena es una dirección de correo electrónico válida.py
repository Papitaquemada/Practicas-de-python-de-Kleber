import re

def es_direccion_email_valida(email):

    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

email_ingresado = input("Ingrese una dirección de correo electrónico: ")

if es_direccion_email_valida(email_ingresado):

    print("Dirección de correo electrónico válida")

else:

    print("Dirección de correo electrónico no válida")

    