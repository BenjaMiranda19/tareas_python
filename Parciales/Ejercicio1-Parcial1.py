import numpy as np
import random

matrizA = np.random.randint(0,10, size=(4,4))
matrizB = np.random.randint(0,10, size=(4,4))
matrizC = np.random.randint(0,10, size=(4,4))

matrizA = matrizA**3
matrizB = np.linalg.inv(matrizB)

parte1 = matrizA * matrizB * matrizC

matrizA = np.linalg.inv(matrizA)

print(parte1 + matrizA)