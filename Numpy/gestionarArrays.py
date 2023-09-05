import numpy as np

arr = np.arange(0, 50, 5)

print(arr)

# Primera posición
print(arr[0])

# Quinta posición
print(arr[4])

# Asignar valor
arr[1] = -5
print(arr)
arr.put(0, 100)
print(arr)

# copia completa del array (OJO es la misma referencia en memoria)
arr2 = arr[:]
print(arr2)

# subarray de los tres primeros elementos
arr2 = arr[:3]
print(arr2)

# Modificar rango de forma masiva menos primero y último
arr[1:-1] = 50
print(arr)
print(arr2) # Se modifica también el arr2 porque es una referencia a la memoria

# Para hacer una copia del array (objeto) en otra referencia
arr3 = arr.copy()
print(arr3)