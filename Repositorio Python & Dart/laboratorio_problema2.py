import random

filas = int(input("Ingrese la cantidad de filas:"))
columnas = int(input("Ingresar la cantidad de columnas:"))

m1=[[random.randint(0,10)]]

for i in range(filas):
    for j in range(columnas):
        print(m1[filas][columnas])

#Esto deberia de poder guardar e imprimir la primera matriz

escalar = int(input("Ingrese un numero:"))

multiplicacion = [m1[i][j]*escalar]

#Esto deberia de poder realizar la multiplicacione entre el escalar y la matriz