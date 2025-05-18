# Calculadora de Interés Simple:
# Solicita al usuario que ingrese el monto principal, la tasa de interés y elperíodo de tiempo

p = float(input("Ingrese el monto principal: "))

r = float(input("Ingrese la tasa de interés: "))

t = float(input("Ingrese el período de tiempo: "))

# Calcula el interés simple utilizando la fórmula: interés = (principal * tasa * tiempo) / 100

interest = (p * r * t) / 100

# Muestra el interés simple calculado.

print("Interés Simple:", interest)