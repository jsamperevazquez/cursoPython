import sys
import menu
import ui

"""
Launcher de la aplicación. En función de argumentos recibidos en terminal se ejecuta en
terminal o en ventana.
"""
if __name__== "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        menu.iniciar()
    else:
        ui.MainWindow().mainloop()
