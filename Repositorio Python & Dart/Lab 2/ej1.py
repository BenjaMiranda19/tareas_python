import numpy as np

filas1 = np.random.randint(2, 6)
columnas1 = np.random.randint(2, 6)

filas2 = np.random.randint(2, 6)
columnas2 = np.random.randint(2, 6)


matriz1 = np.zeros((filas1, columnas1))
matriz2 = np.zeros((filas2, columnas2))

print("Ingrese los elementos de la primera matriz:")
for i in range(filas1):
    for j in range(columnas1):
        matriz1[i][j] = float(input("Elemento ({},{}): ".format(i+1,j+1)))

print("Ingrese los elementos de la segunda matriz:")
for i in range(filas2):
    for j in range(columnas2):
        matriz2[i][j] = float(input("Elemento ({},{}): ".format(i+1,j+1)))

matriz_resultado = np.zeros((filas1, columnas1))

for i in range(filas1):
    for j in range(columnas1):
        matriz_resultado[i][j] = matriz1[i][j] - matriz2[i][j]

filas3 = int(input("Ingrese la cantidad de filas para la tercera matriz: "))
columnas3 = int(input("Ingrese la cantidad de columnas para la tercera matriz: "))

matriz3 = np.zeros((filas3, columnas3))
print("Ingrese los elementos para la tercera matriz:")
for i in range(filas3):
    for j in range(columnas3):
        matriz3[i][j] = float(input("Elemento ({},{}): ".format(i+1,j+1)))

matriz_final = np.dot(matriz_resultado, matriz3)

print("\nMatriz 1:")
print(matriz1)

print("\nMatriz 2:")
print(matriz2)

print("\nMatriz Resultado:")
print(matriz_resultado)

print("\nMatriz 3:")
print(matriz3)

print("\nMatriz Final:")
print(matriz_final)