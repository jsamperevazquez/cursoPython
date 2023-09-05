import numpy as np

arr1 = np.arange(1, 6)
arr2 = np.array([-3, 7, 3, 13, 0])

print("Primer array")
print(arr1)

print("Segundo array")
print(arr2)

# sumar los arrays
print("Suma de arrays")
print(np.add(arr1, arr2))

# resta
print("Resta de arrays")
print(np.subtract(arr2, arr1))

# raiz cuadrada
print("Raiz cuadrada de los elementos de un array")
print(np.sqrt(arr1))

# potencia
print("Potencia de elementos de array")
print(np.power(arr1, 2))

# signo
print("Signo de los elementos de array")
print(np.sign(arr1))

# Comparativas
print("Comparar cada posición de array con otra posición de otro array dando el mayor")
print(np.maximum(arr1, arr2))

print("Comparar cada posición de array con otra posición de otro array dando el mínimo")
print(np.minimum(arr1, arr2))

print("Compara si son iguales los elementos")
print(np.equal(arr1, arr2))

print("Compara si es mayor que los elementos")
print(np.greater(arr1, arr2))

# Flotantes
arr3 = np.array([3.14, 2.57, -5.4, 0.47, 5.5])

print("El valor absoluto de los elementos de un array")
print(np.fabs(arr3))

print("El redondeo al alza")
print(np.ceil(arr3))

print("El redondeo a la baja")
print(np.floor(arr3))

print("Redondeo normal")
print(np.round(arr3))

