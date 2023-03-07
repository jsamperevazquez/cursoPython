import csv
import config


PATH_CLIENTES = config.DATABASE_PATH

class Cliente:
    """
    Módulo para crear modelos de Cliente
    """
    def __init__(self, dni, nombre, apellido):
        """
        Constructor de la clase Cliente
        :param dni: DNI de cliente
        :param nombre: Nombre de cliente
        :param apellido: Apellido de cliente
        """
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        """
        Función para formatear retorno de datos
        :return: Datos de cliente formateados
        """
        return f"({self.dni} {self.nombre} {self.apellido})"


class Clientes:
    """
    Clase Clientes con Métodos para tratar datos (MVC)
    """
    lista_clientes = []  # Lista de clase
    with open(PATH_CLIENTES, newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for dni, nombre, apellido in reader:
            cliente = Cliente(dni, nombre, apellido)
            lista_clientes.append(cliente)

    # Método estático para buscar por dni del cliente
    @staticmethod
    def buscar(dni):
        """
        Función para buscar un cliente por su DNI
        :param dni: d.n.i de cliente
        :return: Cliente
        """
        for cliente in Clientes.lista_clientes:
            if cliente.dni == dni:
                return cliente

    # Método estático para crear un nuevo cliente
    @staticmethod
    def crear(dni, nombre, apellido):
        """
        Función para crear un nuevo cliente
        :param dni: Documento nacional identidad de cliente
        :param nombre: Nombre de cliente
        :param apellido: Apellido de cliente
        :return: Retorna cliente
        """
        cliente = Cliente(dni, nombre, apellido)
        Clientes.lista_clientes.append(cliente)
        Clientes.guardar()
        return cliente

    # Método estático para modificar campos del cliente
    @staticmethod
    def modificar(dni, nombre, apellido):
        """
        Función para modificar datos del cliente
        :param dni: Dni del cliente
        :param nombre: Nombre del cliente
        :param apellido: Apellido del cliente
        :return: Retorna cliente
        """
        for indice, cliente in enumerate(Clientes.lista_clientes):
            if cliente.dni == dni:
                Clientes.lista_clientes[indice].nombre = nombre
                Clientes.lista_clientes[indice].apellido = apellido
                Clientes.guardar()
                return Clientes.lista_clientes[indice]

    # Método estático para borrar el cliente por su dni
    @staticmethod
    def borrar(dni):
        """
        Función para borrar cliente del registro por DNI
        :param dni: Documenta Nacional de identidad del Cliente
        :return: Retorna cliente
        """
        for indice, cliente in enumerate(Clientes.lista_clientes):
            if cliente.dni == dni:
                cliente = Clientes.lista_clientes.pop(indice)
                Clientes.guardar()
                return cliente

    # Método estático para guardar en un fichero csv
    @staticmethod
    def guardar():
        """
        Función que guarda los clientes en fichero CSV (Persistencia)
        :return:
        """
        with open(PATH_CLIENTES, 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for cliente in Clientes.lista_clientes:
                writer.writerow((cliente.dni, cliente.nombre, cliente.apellido))
