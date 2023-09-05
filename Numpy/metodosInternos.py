import numpy as np

# Generamos array de 2x3 con aleatorios
arr = np.arange(1, 7).reshape(2, 3)
print(arr)

print("Hacemos el sumatorio")
print(np.sum(arr))

print("Media de array")
print(np.mean(arr))

print("Mediación")
print(np.std(arr))

print("Varianza")
print(np.var(arr))

# Métodos de ordenación
print("Nuevo array")
arr_2 = np.random.randint(-10, 10, [3, 3])
print(arr_2)

print("Ordenar array horizontalmente")
arr_2.sort()
print(arr_2)

print("Ordenar array verticalmente")
arr_2.sort(0)
print(arr_2)
