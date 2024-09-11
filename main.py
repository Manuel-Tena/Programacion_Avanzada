from coche import Coche

coche_uno = Coche("Toyota", "Camry", 2021)
coche_dos = Coche("Ford", "Muytang", 2022)
coche_tres = Coche("Honda", "Civic", 2020)

print("\n ------------------------------- \n")
coche_uno.mostrar_informacion()
coche_uno.calcular_edad_coche()
print("\n ------------------------------- \n")
coche_dos.mostrar_informacion()
coche_dos.calcular_edad_coche()
print("\n ------------------------------- \n")
coche_tres.mostrar_informacion()
coche_tres.calcular_edad_coche()
print("\n ------------------------------- \n")