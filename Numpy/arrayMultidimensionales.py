import numpy as np

arr_2d = np.array([[0, 5, 10], [15, 20, 25], [30, 35, 40]])
print(arr_2d)

# Primera fila
print(arr_2d[0])

# Primera fila y primera columna
print(arr_2d[0][0])

# Última fila y último elemento
print(arr_2d[-1][-1])

# ******   Slicing 2D  *******
# Tenemos que doblar los índices de inicio
# SubArray con todas las filas y columnas
subArr = arr_2d.copy()[:,:]
print(subArr)

# SubArray de las dos primeras filas
subArr = arr_2d.copy()[:2,:]
print(subArr)

# SubArray de la primera columna
subArr = arr_2d.copy()[:,:1]
print(subArr)

# FANCY INDEX
# Creamos array de 0 de 3 filas y 5 columnas
array = np.zeros((5, 10))
print(array)

# Modificación masiva de la primera, tercera y última columna
array[[0,2,-1]] = 5
print(array)

