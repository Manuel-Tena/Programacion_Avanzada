from menus.menu import Menu
from app import App
import tkinter as tk

if __name__ == "__main__":
    while True:
        try:
            print("Modo de ejecución \n1.- Interfaz gráfica(usuario) \n2.- Consola(Desarrollador)")
            opcion = int(input("Elige el modo de ejecución: "))

            if 1<=opcion<=2:
                if opcion == 1:
                    ventana = tk.Tk()
                    app = App(ventana)
                    ventana.mainloop()

                if opcion == 2:
                    menu = Menu()
                    menu.mostrar_menu()
            else:
                print("Opcion no válida. Por favor, elige un numero entre 1 y 2")

        except ValueError:
                print("Entrada no válida. Por favor, ingresa un número entero")