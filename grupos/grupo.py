from typing import List
from estudiantes.estudiante import Estudiante
from materias.materia import Materia
from random import randint

class Grupo:
    id: str
    estudiantes: List[Estudiante] = []
    materias: List[Materia] = []
    tipo: chr
    id_semestre: str

    def __init__(self, tipo: chr, id_semestre: str):
        self.id = self.generar_id(tipo=tipo)
        self.tipo = tipo
        self.id_semestre = id_semestre

    def generar_id(self, tipo:chr) -> str:
        return f"{tipo}-{randint(0,1000000)}-{randint(0,1000000)}"
    
    def registrar_estudiante(self, estudiante: Estudiante):
        self.estudiantes.append(estudiante)
    
    def registrar_materia(self, materia: Materia):
        self.materias.append(materia)
    
    def mostrar_informacion(self):
        informacion = f"ID: {self.id} \nTipo: {self.tipo} \nID del semestre: {self.id_semestre} \n------------------------------------------"
        return informacion  
      
    def mostrar_info_grupo_para_estudiante(self):
        print(f"\nInformacion del Grupo {self.tipo}, del semestre {self.id_semestre}")
        ##Mostrar materias##
        for materia in self.materias:
            print(materia.mostrar_informacion())