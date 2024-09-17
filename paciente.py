import random

class Paciente:
    id = 0
    nombre = ""
    ano_nacimiento = 0
    peso = 0
    estatura = 0
    direccion = ""

    def __init__(self, nombre, ano_nacimiento, peso, estatura, direccion):
        self.id = random.randint(1, 10001)
        self.nombre = nombre
        self.ano_nacimiento = ano_nacimiento
        self.peso = peso
        self.estatura = estatura
        self.direccion = direccion

    def mostrar_informacion(self):
        print(f"\nId: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Año de nacimiento: {self.ano_nacimiento}")
        print(f"Peso: {self.peso}")
        print(f"Estatura: {self.estatura}")
        print(f"Dirección: {self.direccion}")

    def mostrar_mayores_de_edad(self):
        if self.ano_nacimiento < 2007:
            print(f"\nId: {self.id}")
            print(f"Nombre: {self.nombre}")
            print(f"Año de nacimiento: {self.ano_nacimiento}")
            print(f"Peso: {self.peso}")
            print(f"Estatura: {self.estatura}")
            print(f"Dirección: {self.direccion}")
             
    def mostrar_menores_de_edad(self):
        if self.ano_nacimiento >= 2007:
            print(f"\nId: {self.id}")
            print(f"Nombre: {self.nombre}")
            print(f"Año de nacimiento: {self.ano_nacimiento}")
            print(f"Peso: {self.peso}")
            print(f"Estatura: {self.estatura}")
            print(f"Dirección: {self.direccion}")
