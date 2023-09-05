import numpy as np


# Datos aleatorios
print("Creamos decimal entre 0 y 1")
print(np.random.rand())

print("Array de 1 dimension 4 elementos de decimales entre 0 y 1")
print(np.random.rand(4))

print("Array de 2 dimensiones  de decimales entre 0 y 1")
print(np.random.rand(4,2))

print("Array de 3 dimensiones de decimales entre 0 y N")
print(np.random.uniform(10, size=[2, 2, 2]))

print("Array de 4 dimensiones de decimales entre -N y N")
print(np.random.uniform(10, -10, size=[2, 2, 2, 2]))

print("Número entero entre 0 y N")
print(np.random.randint(10))

print("Array de enteros entre 0 y N")
print(np.random.randint(10, size=[3, 2]))

print("Array de enteros entre N y M")
print(np.random.randint(-10, 10, size=[3, 2]))

print("Array uniforme con curva Gaussiana")
print(np.random.normal(size=20))


# Permutaciones
print("Array del 0 al 10(no incluido)")
arr2 = np.arange(10)
print(arr2)

print("Desordenamos el array")
np.random.shuffle(arr2)
print(arr2)

print("Generar secuencia permutada a partir de un número")
print(np.random.permutation(15))


