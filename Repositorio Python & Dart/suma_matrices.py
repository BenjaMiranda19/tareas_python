import numpy as np

matriz1 = np.array = [[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]]

matriz2 = np.array = [[10, 11, 12],
                      [13, 14, 15],
                      [16, 17, 18]]

resultado = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

for i in range(len(matriz1)):
    for j in range(len(matriz1[0])):
        resultado[i][j] = matriz1[i][j] + matriz2[i][j]

if matriz1.shape == matriz2.shape:
    for fila in resultado:
        print(fila)

else:
    print("No se puede hacer la suma")

while True:
    print("Estoy atrapado dentro de un bucle.")

