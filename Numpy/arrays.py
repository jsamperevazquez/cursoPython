import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


array = np.array([1, 2, 3, 4, 5])

print(array)

print(type(array))
print(np.ndim(array))
print(np.shape(array))

array = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10.5]
])

print(array)
print(array.ndim)
print(array.shape)
print(array.dtype)

array = np.array(["Hola", "que", "tal"])
print(array.dtype)

array = np.array(["Hola", 5, 3.1416])
print(array.dtype)

tabla = pd.DataFrame(
    np.random.randint(0, 100, size=(5, 3)),
    columns= ['Pepe', 'María', 'Juan']
)

print(tabla)

tabla.plot()
plt.show()
