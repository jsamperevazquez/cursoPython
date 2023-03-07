import os
import platform
import re

"""
Módulo para generar funciones auxiliares
"""

def limpiar_pantalla():
    """
    Función que en función del SO que usemos borra datos de la pantalla
    """
    os.system('cls') if platform.system() == "Windows" else os.system('clear')


def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    """
    Función aux para realizar lectura de texto
    :param longitud_min: Mínimo del texto establecido en 0 por defecto
    :param longitud_max: Máximo del texto establecido en 100 por defecto
    :param mensaje: Mensaje recibido en función
    :return: Texto validado con condiciones
    """
    print(mensaje) if mensaje else None
    while True:
        texto = input(">")
        if longitud_min <= len(texto) <= longitud_max:
            return texto

def validar_dni(dni, lista):
    """
    Función aux que se encarga de validar(Expresiones regulares) el DNI del cliente
    :param dni: DNI de cliente
    :param lista: Lista de clientes
    :return: Cliente validado
    """
    if not re.match('[0-9]{2}[A-Z]$', dni):
        print("DNI incorrecto, debe cumplir con el formato")
        return False
    for cliente in lista:
        if cliente.dni == dni:
            print("DNI en uso por otro cliente")
            return False
    return True
