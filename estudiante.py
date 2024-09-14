from curso import Curso
import random

curso_uno = Curso(1, "Analisis de Fluidos", "MTC-1003", "Eli Chagolla Inzunza")
curso_dos = Curso(2, "Programacion Avanzada", "MTG-1023", "Eder Rivera Cisneros")
curso_tres = Curso(3, "Mecanismos", "AED-1043", "Fernando Saldaña Salas")

class Estudiante:
    nombre = ""
    edad = 0
    id_estudiante = 0
    cursos = 0

    def __init__(self, nombre, edad, id_estudiante):
        self.nombre = nombre
        self.edad = edad
        self.id_estudiante = id_estudiante
        self.cursos = random.randint(1,3)
        self.numcursos = random.randint(2,3)

    def agregar_curso(self):
        if self.numcursos == 2: 
            if self.cursos == 1:
                curso_uno.mostrar_info_curso()
                curso_dos.mostrar_info_curso()
            elif self.cursos == 2:
                curso_tres.mostrar_info_curso()
                curso_dos.mostrar_info_curso()
            elif self.cursos == 3:
                curso_uno.mostrar_info_curso()
                curso_tres.mostrar_info_curso()
            return
        elif self.numcursos == 3:
            curso_uno.mostrar_info_curso()
            curso_dos.mostrar_info_curso()
            curso_tres.mostrar_info_curso()
        return      
    def mostrar_informacion(self):
        print("\n Nombre: ", self.nombre)
        print("\n Edad: ", self.edad)
        print("\n Id del estudiante: ", self.id_estudiante)
        print("\n ------------- Cursos --------------")
        self.agregar_curso()

        