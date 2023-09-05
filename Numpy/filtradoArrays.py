import numpy as np

print("Generamos un array con números aleatorios repetidos")
arr = np.random.randint(0, 10, 40)

print(arr)

print("Aplicamos filtro unique")
print(np.unique(arr))

print("Array de una dimensión si los elementos están en otro array")
print(np.in1d([-1, 4, 8, 12], arr))

# Generamos array uniforme de 3x2
arr_1 = np.random.uniform(-5, 5, size=[3, 2])
print("Genera array filtrado con una condición y un valor por defecto")
# Creamos un array donde los menores de 0 los pongamos en 0 en arr_1
arr_2 = np.where(arr_1 < 0, 0, arr_1)
print(arr_2)

# Creamos segundo filtro donde positivos los ponemos a 1
arr_2 = np.where(arr_1 > 0, True, arr_1)
print(arr_2)

# Filtros Booleanos
arr_bool = np.array([True, True, True, False])

print("Comprobamos si los elementos son True")
print(arr_bool.all())

print("Comprobamos si algún elemento es True")
print(arr_bool.any())

print("Con array multidimensional")
arr_bool_2d = np.array([
    [ False, True],
    [ True, True],
    [ False, True]
])

print("Comprobamos si alguna de las columnas es todo true")
print(arr_bool_2d.all(0))

print("Comprobamos si alguna de las filas tiene algún True")
print(arr_bool_2d.any(1))


