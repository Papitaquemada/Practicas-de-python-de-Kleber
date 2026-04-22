import random

filas = 3
columnas = 3
matriz_aleatoria = [[random.random() for _ in range(columnas)] for _ in range(filas)]

print("Matriz aleatoria:")
for fila in matriz_aleatoria:
    print(fila)