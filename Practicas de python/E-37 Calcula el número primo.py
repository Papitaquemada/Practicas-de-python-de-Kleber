def es_primo(x):

    if x < 2:

        return False
    
    if x % 2 == 0:

        return False
    
    for i in range(3, int(x**0.5)+1, 2):

        if x % i == 0:

            return False
        
    return True

def generar_primo(primo_actual):
    nuevo_primo = primo_actual + 1

    while True:
       
        if not es_primo(nuevo_primo):

            nuevo_primo += 1

        else:

            break

    return nuevo_primo

def main():

    primo_actual = 2
    
    while True:

        respuesta = input('¿Desea generar un número primo? (s/n)')

        if respuesta.lower() .startswith('s'):

            print(primo_actual)

            primo_actual = generar_primo(primo_actual)

        else:

            break

if __name__ == '__main__':

    main()


