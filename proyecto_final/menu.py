import database as db
import helpers

"""
Módulo para crear el menú en terminal
"""

def iniciar():
    """
    Función para iniciar menú en terminal
    :return:
    """
    separador = "=" * 30
    helpers.limpiar_pantalla()
    while True:
        print(separador)
        print("\tEscoge una opción")
        print(separador)
        print()
        print("[1] Listar los clientes\n\n"
              "[2] buscar un cliente\n\n"
              "[3] Crear un cliente\n\n"
              "[4] Modificar un cliente\n\n"
              "[5] Borrar un cliente\n\n"
              "[6] Salir de la aplicación\n")
        print(separador)
        opcion = int(input())

        # Listar clientes
        if opcion == 1:
            helpers.limpiar_pantalla()
            print("******  CLIENTES  ******")
            for c in db.Clientes.lista_clientes:
                print(str(c).replace("(", "").replace(")", ""))
            print()
            input("Presiones tecla para continuar...")

        # Buscar por DNI
        elif opcion == 2:
            helpers.limpiar_pantalla()
            if len(db.Clientes.lista_clientes) > 0:
                print("\t****\t BUSCAR CLIENTE\t****\n")
                dni = helpers.leer_texto(3, 3, "DNI(2 num y una letra)").upper()
                if db.Clientes.buscar(dni) is not None:
                    print("*** Cliente ***")
                    print(str(db.Clientes.buscar(dni)).replace("(","").replace(")", ""))
                    print()
                    input("Presiones tecla para continuar...")
                else:
                    helpers.limpiar_pantalla()
                    print("No se ha encontrado el cliente")
                    print()
            else:
                print("No existe ningún cliente en Base de datos")
                print()
                input("Presiones tecla para continuar...")

        # Crear nuevo cliente
        elif opcion == 3:
            print("\t****\t NUEVO CLIENTE\t****\n")
            while True:
                dni = helpers.leer_texto(3, 3, "DNI (2 num y 1 letra)").upper()
                if helpers.validar_dni(dni, db.Clientes.lista_clientes):
                    break
            nombre = helpers.leer_texto(1, 20, "Nombre Cliente").capitalize()
            apellido = helpers.leer_texto(1, 30, "Apellido Cliente").capitalize()
            db.Clientes.crear(dni, nombre, apellido)
            helpers.limpiar_pantalla()
            print("Cliente creado con éxito")
            print()
            input("Presiones tecla para continuar...")

        # Modificar cliente
        elif opcion == 4:
            helpers.limpiar_pantalla()
            print("\t ****\t MODIFICAR CLIENTE\t****\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 num y 1 letra)").upper()
            for c in db.Clientes.lista_clientes:
                if c.dni == dni:
                    nuevo_nombre = helpers.leer_texto(1, 20, f"Nuevo nombre Cliente({c.nombre})").capitalize()
                    nuevo_apellido = helpers.leer_texto(1, 30, f"Nuevo apellido Cliente({c.apellido})").capitalize()
                    db.Clientes.modificar(dni,nuevo_nombre, nuevo_apellido)
                    helpers.limpiar_pantalla()
                    print("Cliente modificado con éxito")
                    print()
                    input("Presiones tecla para continuar...")
                else:
                    print("Cliente no encontrado")
                    print()
                    input("Presiones tecla para continuar...")

        # Borrar Cliente
        elif opcion == 5:
            helpers.limpiar_pantalla()
            if len(db.Clientes.lista_clientes) > 0:
                print("\t ****\t BORRAR CLIENTE\t****\n")
                dni = helpers.leer_texto(3, 3, "DNI(2 num y una letra)").upper()
                print("Cliente eliminado") if db.Clientes.borrar(dni) else print("No se ha encontrado el Cliente")
                print()
                input("Presiones tecla para continuar...")
            else:
                print("La lista de clientes está vacía")
                print()
                input("Presiones tecla para continuar...")

        # Salir de aplicación
        elif opcion == 6:
            helpers.limpiar_pantalla()
            print("Gracias por usar nuestros servicios\n")
            break


