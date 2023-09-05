import numpy as np

# Guardado Binario
print("Array aleatorio")
arr_1 = np.random.randint(0, 4, [3, 3])
print(arr_1)

# Guardamos en binario con extensión .npy
np.save('arr_1.npy', arr_1)

# Borramos el array de la memoria para asegurarnos que ya no existe
del (arr_1)

# Lo cargamos desde el binario
print("Cargados desde binario")
arr_1 = np.load('arr_1.npy')
print(arr_1)

# Guardar varios arrays en binarios
print("Nuevo array")
arr_2 = np.random.randint(-4, 0, [3, 3])
print(arr_2)

print("Guardamos varios arrays")
np.savez('arrays.npz', arr_1 = arr_1, arr_2 = arr_2)

# Borramos arrays de memoria
del (arr_1)
del (arr_2)

# Cargamos desde binario
print("Cargados desde binario")
arrays = np.load('arrays.npz')
print('Array 1:\n', arrays['arr_1'], '\n', 'Array 2:\n', arrays['arr_2'])

# Guardamos en texto
print("Creamos un nuevo array")
arr_3 = np.random.randint(-10, 10, [3, 3])
print(arr_3)

print("Guardamos en archivo texto")
np.savetxt('arrayTexto.txt', arr_3)

print("Guardamos separando las columnas con ,")
np.savetxt('arrayTexto.txt',arr_3,  delimiter=',')

# Borramos de la memoria
del(arr_3)

# Lo recuperamos del archivo de texto
array_txt = np.loadtxt('arrayTexto.txt', delimiter=',')
print(array_txt)







