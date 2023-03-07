import tkinter
import helpers
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel,WARNING

import database as db

"""
Módulo para la creación y la gestión de la interfaz gráfica (tkinter)
"""

class CenterWidgetMixin:
    def center(self):
        """
        Función encargada de dar tamaño y centrar las diferentes ventanas
        :return:
        """
        self.update()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        self.geometry(f"+{int(ws / 4)}+{int(hs / 4)}")

class Crear_toplevel(Toplevel, CenterWidgetMixin):
    """
    Clase para crear subventanas
    """
    def __init__(self, padre):
        """
        Constructor de la clase
        :param padre: Ventana que va a contener la misma
        """
        super().__init__(padre)
        self.center()
        self.transient(padre) # 1...
        self.grab_set() # 2...    Métodos para tener que interactuar con la ventana Top antes de pasar a la principal



class MainWindow(Tk, CenterWidgetMixin):
    """
    Clase para generar la ventana principal del proyecto
    """
    def __init__(self):
        """
        Constructor de ventana principal
        """
        super().__init__()
        self.boton_mod = None
        self.boton_nuevo = None
        self.treeview = None
        self.title("Gestor de clientes")
        self.center()
        self.build()
        self.validaciones = [False, False, False]

    def build(self):
        """
        Función para construir la ventana principal
        :return:
        """
        frame = Frame(self)
        frame.pack()
        treeview = ttk.Treeview(frame, columns=("DNI", "Nombre", "Apellido"))

        # Configuración de las columnas
        treeview.column("#0", width=0, stretch=NO)
        treeview.column("DNI", anchor=CENTER)
        treeview.column("Nombre", anchor=CENTER)
        treeview.column("Apellido", anchor=CENTER)

        # Configuración de las cabeceras
        treeview.heading("DNI", text="DNI", anchor=CENTER)
        treeview.heading("Nombre", text="Nombre", anchor=CENTER)
        treeview.heading("Apellido", text="Apellido", anchor=CENTER)

        # Scroll para treeview
        scrollbar = tkinter.Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Asignamos al treeView el scrollbar
        treeview['yscrollcommand'] = scrollbar.set

        # Llenar las columnas del treeview
        for indice, cliente in enumerate(db.Clientes.lista_clientes):
            treeview.insert(
                parent='',
                index=END,
                iid=cliente.dni,
                values=(cliente.dni, cliente.nombre, cliente.apellido))
            if indice == 0:  # Obligo a poner el focus en el primer elemento del treeview
                treeview.focus(cliente.dni)
                treeview.selection_set(cliente.dni)
        treeview.pack()

        frame = Frame(self)
        frame.pack(pady=20)

        Button(frame, text="Nuevo", command=self.crear).grid(row=0, column=0)
        Button(frame, text="Modificar", command=self.modificar).grid(row=0, column=1)
        Button(frame, text="Borrar", command=self.borrar).grid(row=0, column=2)

        self.treeview = treeview

    def borrar(self):
        """
        Función para borrar datos de treeview y sincronizar datos con dataBase
        :return:
        """
        cliente = self.treeview.focus()
        if cliente:
            campos = self.treeview.item(cliente, "values")
            confirmacion = askokcancel(
                title="Confirmar borrar",
                message=f"borrar {campos[1]} {campos[2]}",
                icon=WARNING)
            if confirmacion:
                self.treeview.delete(cliente)
                db.Clientes.borrar(campos[0])


    def validar(self, event, indice, boton):
        """
        Función encargada de validar datos que se introducen
        :param event: Evento que se envía
        :param indice: Índice
        :param boton: Botón que envía el evento
        :return:
        """
        valor = event.widget.get()
        # Cambiamos el estado botón en función de las validaciones
        if boton == "nuevo":
            valido = helpers.validar_dni(valor, db.Clientes.lista_clientes) if indice == 0 \
                else valor.isalpha() and 2 <= len(valor) <= 30
            event.widget.configure({"bg": "Green" if valido else "Red"})
            self.validaciones[indice] = valido
            self.boton_nuevo.config(state=NORMAL if self.validaciones == [True, True, True] else DISABLED)
        elif boton == "modificar":
            self.validaciones[0],self.validaciones[1],self.validaciones[2] = True, True, True
            valido =  True if indice > 0 and valor.isalpha() and 2 <= len(valor) <= 30 else False
            event.widget.configure({"bg": "Green" if valido else "Red"})
            self.validaciones[indice] = valido
            self.boton_mod.config(state=NORMAL if self.validaciones == [True, True, True] else DISABLED)


    def modificar(self):
        """
        Función para modificar datos de cliente
        :return:
        """
        form = Crear_toplevel(self)
        form.title("Modificar cliente")
        cliente = self.treeview.focus()
        dni = StringVar(None,"")
        nombre = StringVar(None,"")
        apellido = StringVar(None,"")
        if cliente:
            campos = self.treeview.item(cliente, "values") #Extrae valores seleccionados del treeview
            dni.set(campos[0])
            nombre.set(campos[1])
            apellido.set(campos[2])
            form.title("Modificar cliente")
            tkinter.Label(form, text="DNI").grid(column=0, row=0, pady=10, padx=10)
            entry_dni = tkinter.Entry(form, justify=CENTER, state=DISABLED)
            entry_dni.grid(column=1, row=0, pady=10, padx=10)
            entry_dni.config(textvariable=dni)
            tkinter.Label(form, text="Nombre").grid(column=0, row=1, pady=10, padx=10)
            entry_nombre = tkinter.Entry(form, justify=CENTER)
            entry_nombre.grid(column=1, row=1, pady=10, padx=10)
            entry_nombre.config(textvariable=nombre)
            entry_nombre.bind("<KeyRelease>", lambda event: self.validar(event, 1, "modificar"))
            tkinter.Label(form, text="Apellido").grid(column=0, row=2, pady=10, padx=10)
            entry_apellido = tkinter.Entry(form, justify=CENTER)
            entry_apellido.grid(column=1, row=2, pady=10, padx=10)
            entry_apellido.config(textvariable=apellido)
            entry_apellido.bind("<KeyRelease>", lambda event: self.validar(event, 2, "modificar"))
            def enviar():
                """
                Función insertada para enviar datos a database
                :return:
                """
                self.treeview.insert("", 0 , values=(campos[0], entry_nombre.get(), entry_apellido.get()))
                self.treeview.delete(cliente)
                db.Clientes.modificar(campos[0], entry_nombre.get(), entry_apellido.get())
                cerrar()

            def cerrar():
                """
                Función para cerrar subventana
                :return:
                """
                form.destroy()

            boton_mod = tkinter.Button(form, text="Modificar", justify=CENTER, command=enviar)
            boton_mod.grid(column=0, row=3, pady=10, padx=15)
            tkinter.Button(form, text="Cancelar", justify=CENTER, command=cerrar).grid(column=1, row=3)
            self.boton_mod = boton_mod


    def crear(self):
        """
        Función para crear un nuevo registro de Cliente
        :return:
        """
        form = Crear_toplevel(self)
        form.title("Crear cliente")
        tkinter.Label(form, text="DNI").grid(column=0, row=0, pady=10, padx=10)
        entry_dni = tkinter.Entry(form, justify=CENTER)
        entry_dni.grid(column=1, row=0, pady=10, padx=10)
        entry_dni.bind("<KeyRelease>", lambda event: self.validar(event, 0, "nuevo"))
        tkinter.Label(form, text="Nombre").grid(column=0, row=1, pady=10, padx=10)
        entry_nombre = tkinter.Entry(form, justify=CENTER)
        entry_nombre.grid(column=1, row=1, pady=10, padx=10)
        entry_nombre.bind("<KeyRelease>", lambda event: self.validar(event, 1, "nuevo"))
        tkinter.Label(form, text="Apellido").grid(column=0, row=2, pady=10, padx=10)
        entry_apellido = tkinter.Entry(form, justify=CENTER)
        entry_apellido.grid(column=1, row=2, pady=10, padx=10)
        entry_apellido.bind("<KeyRelease>", lambda event: self.validar(event, 2, "nuevo"))

        def enviar():
            """
            Función insertada para enviar datos a database(Sincronización)
            :return:
            """
            self.treeview.insert("", 0, values=(entry_dni.get(), entry_nombre.get(), entry_apellido.get()))
            db.Clientes.crear(entry_dni.get(), entry_nombre.get(), entry_apellido.get())
            cerrar()

        def cerrar():
            """
            Función para cerrar subventana
            :return:
            """
            form.destroy()

        boton_nuevo = tkinter.Button(form, text="Nuevo", justify=CENTER, command=enviar, state=DISABLED)
        boton_nuevo.grid(column=0, row=3, pady=10, padx=15)
        tkinter.Button(form, text="Cancelar", justify=CENTER, command=cerrar).grid(column=1, row=3)
        self.boton_nuevo = boton_nuevo



if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
