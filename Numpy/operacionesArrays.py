import numpy as np

array = np.array([3, 5, 9])
array2 = np.array([5, 9, 8])

print(array * array2)
print (array + array2)
print(array / array2)
print(2 ** array)
print(array ** -1.)
print(array ** array2)

## 2 Dimensiones

arr1 = np.array([[2,4], [6, 8]])
arr2 = np.array([[10, 12], [14, 16]])

print(arr1 + arr2)
print(arr1 * arr2)
print(arr1 ** arr2)
print(arr1 ** -1.)
