import numpy as np
import random

matriz1 = np.random.randint(1,10, size=(3,3))
matriz2 = np.random.randint(11,30, size=(3,3))
matriz3 = np.random.randint(-10,-1, size=(3,3))

matrizAB = matriz1 + matriz2
resultado1 = np.dot(matrizAB,matriz3)

resultado2 = np.dot(matriz1, matriz3) + np.dot(matriz2,matriz3)

print(resultado1)
print()
print(resultado2)
print()

if np.array_equal(resultado1,resultado2):
    print("La propiedad se puede demostrar")

else:
    print("La propiedad no es valida")