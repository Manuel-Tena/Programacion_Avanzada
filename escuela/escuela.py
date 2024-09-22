from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime
from random import randint

class Escuela:
    lista_estudiantes: List[Estudiante] = []
    lista_maestros: List[Maestro] = []
    lista_grupos: List[Grupo] = []
    lista_materias: List[Materia] = []

    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)

    def generar_numero_control(self):
        #L - 2024 - 09- longitud lsita estudiantes +1 + random (o-10000)
        ano = datetime.now().year
        mes = datetime.now().month
        longitud_mas_uno = len(self.lista_estudiantes)+1
        aleatorio = randint(0,10000)
        numero_control = f"l{ano}{mes}{longitud_mas_uno}{aleatorio}"
        return numero_control

    def registrar_maestro(self, maestro: Maestro):
        self.lista_maestros.append(maestro)

    def generar_numero_control_maestros(self, maestro: Maestro):
        ano = maestro.fecha_nacimiento.year
        dia = datetime.now().day
        aleatorio = randint(500,5000)
        primeras_2_letras_nombre = maestro.nombre[:2].upper()
        ultimas_2_letras_rfc = maestro.rfc[-2:].upper()
        longitud_mas_uno = len(self.lista_maestros)+1
        numero_control_maestro = f"M{ano}{dia}{aleatorio}{primeras_2_letras_nombre}{ultimas_2_letras_rfc}{longitud_mas_uno}"
        return numero_control_maestro

    def registrar_materia(self, materia: Materia):
        self.lista_materias.append(materia)
    
    def generar_id_materia(self, materia: Materia):
        Ultimas_2_letras_nombre = materia.nombre[-2:].upper()
        semestre = materia.semestre
        creditos = materia.credito
        aleatorio = randint(0,1000)  
        id_materia = f"MT{Ultimas_2_letras_nombre}{semestre}{creditos}{aleatorio}"
        return id_materia
       