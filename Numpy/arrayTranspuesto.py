# Array transpuesto es un reflejo de otro array (Filas se convierten en columnas y columnas en filas)
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

# Transpuesto
print(arr.T)

# swapaxes cambia de posición los dos ejes de un array (sirve para lo mismo)
print(arr.swapaxes(0, 1))

# 3 dimensiones
arr_3d = np.arange(8).reshape(2, 2, 2)
print(arr_3d.T)
print(arr_3d.swapaxes(0, 2))

print(arr_3d.swapaxes(0, 1))
