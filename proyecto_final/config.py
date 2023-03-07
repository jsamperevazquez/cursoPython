import sys

"""
Módulo con configuraciones de la aplicación
"""
DATABASE_PATH='clientes.csv'

# Cambiamos el path de clientes si recibe como argumento de sistema pytest
if "pytest" in sys.argv[0]:
    DATABASE_PATH = 'tests/clientes_test.csv'
