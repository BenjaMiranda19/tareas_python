import random

filas = int(input("Ingrese la cantidad de filas:"))
columnas = int(input("Ingresar la cantidad de columnas:"))

m1=[[random.randint(0,5)]]

for i in range(filas):
    for j in range(columnas):
        print(m1[filas][columnas])

#Esta parte del codigo deberia de poder imprimir y guardar la primera matriz

m2=[[random.randint(0,5)]]

filas_2 = int(input("Ingrese la cantidad de filas:"))
columnas_2 = int(input("Ingresar la cantidad de columnas:"))

for i in range(filas_2):
    for j in range(columnas_2):
        print(m1[filas_2][columnas_2])