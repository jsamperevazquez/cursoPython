import unittest
import database as db


class TestDatabase(unittest.TestCase):
    def setUp(self):
            db.Clientes.lista_clientes = [
            db.Cliente('36x', 'Ángel', 'Sampere'),
            db.Cliente('35p', 'María', 'Vázquez'),
            db.Cliente('43v', 'Ramón', 'López')
        ]

    def test_buscar_clientes(self):
        cliente_correcto = db.Clientes.buscar('36x')
        cliente_incorrecto = db.Clientes.buscar('67u')
        self.assertIsNotNone(cliente_correcto)
        self.assertIsNone(cliente_incorrecto)

    def crear_cliente_test(self):
        nuevo_cliente = db.Clientes.crear("41B","Marta","Pérez")
        self.assertEqual(len(db.Clientes.lista_clientes), 4)
        self.assertEqual(nuevo_cliente.dni, "41B")
        self.assertEqual(nuevo_cliente.nombre, "Marta")
        self.assertEqual(nuevo_cliente.apellido, "Pérez")





