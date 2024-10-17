from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from coordinador.coordinador import Coordinador
from usuario.usuario import Usuario
from materias.materia import Materia
from carrera.carrera import Carrera
from semestre.semestre import Semestre
from datetime import datetime
from random import randint

class Escuela:
    lista_usuarios: List[Usuario] = []
    lista_estudiantes: List[Estudiante] = []
    lista_maestros: List[Maestro] = []
    lista_grupos: List[Grupo] = []
    lista_materias: List[Materia] = []
    lista_carreras: List[Carrera] = []
    lista_semestres: List[Semestre] = []

    def __init__(self):
        coordinador = Coordinador(numero_control="12345", nombre="Alberto", apellido="Martinez", rfc="MARTINEZ123", sueldo= 10000, anios_antiguedad=10, contrasenia="123*456*")
        self.lista_usuarios.append(coordinador)

    ###ESTUDIANTE###
    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_usuarios.append(estudiante)
        self.lista_estudiantes.append(estudiante)
        print("\nSe registro con exito al estudiante con numero de control: ", estudiante.numero_control)

    def generar_numero_control(self):
        #L - 2024 - 09- longitud lsita estudiantes +1 + random (o-10000)
        ano = datetime.now().year
        mes = datetime.now().month
        longitud_mas_uno = len(self.lista_estudiantes)+1
        aleatorio = randint(0,10000)
        numero_control = f"l{ano}{mes}{longitud_mas_uno}{aleatorio}"
        return numero_control
    
    def listar_estudiantes(self):
        print("*************Estudiantes*************")
        for estudiante in self.lista_estudiantes:
            print(estudiante.mostrar_informacion())

    def eliminar_estudiante(self, numero_control: str):
        for estudiante in self.lista_estudiantes:
            if estudiante.numero_control == numero_control.strip():
                self.lista_estudiantes.remove(estudiante)
                print(f"El Estudiante {estudiante.nombre} {estudiante.apellido}, ha sido eliminado exitosamente.\n")
                return 
        print(f"No se encontro al estudiante con numero de control: {numero_control} \n")

    ###MAESTRO###
    def registrar_maestro(self, maestro: Maestro):
        self.lista_usuarios.append(maestro)
        self.lista_maestros.append(maestro)

    def generar_numero_control_maestros(self, maestro: Maestro):
        ano = maestro.fecha_nacimiento.year
        dia = datetime.now().day
        aleatorio = randint(500,5000)
        primeras_2_letras_nombre = maestro.nombre[:2].upper()
        ultimas_2_letras_rfc = maestro.rfc[-2:].upper()
        longitud_mas_uno = len(self.lista_maestros)+1
        numero_control = f"M{ano}{dia}{aleatorio}{primeras_2_letras_nombre}{ultimas_2_letras_rfc}{longitud_mas_uno}"
        return numero_control
    
    def listar_maestros(self):
        print("*************Maestros*************")
        for maestro in self.lista_maestros:
            print(maestro.mostrar_informacion())

    def eliminar_maestro(self, numero_control: str):
        for maestro in self.lista_maestros:
            if maestro.numero_control_maestro == numero_control.strip():
                self.lista_maestros.remove(maestro)
                print(f"El Maestro {maestro.nombre} {maestro.apellido}, ha sido eliminado exitosamente.\n")
                return 
        print(f"No se encontro el maestro con numero de control: {numero_control} \n")

    ###MATERIA###
    def registrar_materia(self, materia: Materia):
        self.lista_materias.append(materia)
    
    def listar_materias(self):
        print("*************Materias*************")
        for materia in self.lista_materias:
            print(materia.mostrar_informacion())

    def eliminar_materia(self, id_de_la_materia: str):
        for materia in self.lista_materias:
            if materia.id == id_de_la_materia.strip():
                self.lista_materias.remove(materia)
                print(f"La Materia {materia.nombre}, ha sido eliminada exitosamente.\n")
                return 
        print(f"No se encontro la materia con ID: {id_de_la_materia} \n")

    ###Carrera###
    def registrar_carrera(self, carrera: Carrera):
        self.lista_carreras.append(carrera)
    
    def listar_carreras(self):
        print("*************Carreras*************")
        for carrera in self.lista_carreras:
            print(carrera.mostrar_informacion())

    ###Semestre###
    def registrar_semestre(self, semestre: Semestre):
        id_carrera = semestre.id_carrera
        for carrera in self.lista_carreras:
            if carrera.matricula == id_carrera:
                carrera.registrar_semestre(semestre=semestre)
                break
        self.lista_semestres.append(semestre)

    def listar_semestres(self):
        print("*************Semestres*************")
        for semestre in self.lista_semestres:
            print(semestre.mostrar_informacion())
    
    ###Grupo###
    def registrar_grupo(self, grupo: Grupo):
        id_semestre = grupo.id_semestre
        for semestre in self.lista_semestres:
            if id_semestre == semestre.id:
                semestre.registrar_grupo_en_semestre(grupo=grupo)
                break
        self.lista_grupos.append(grupo)

    def listar_grupos(self):
        print("*************Grupos*************")
        for grupo in self.lista_grupos:
            print(grupo.mostrar_informacion())

    def registrar_estudiante_en_grupo(self, numero_control_estudiante: str, id_grupo: str):
        estudiante = self.buscar_estudiante_por_numero_control(numero_control_estudiante=numero_control_estudiante)
        if estudiante is None:
            print("No se encontro ningun estudiante con el numero de control ingresado")
            return
        grupo = self.buscar_grupo_por_id(id_grupo=id_grupo)
        if grupo is None:
            print("No se encontro ningun grupo con el ID ingresado")
            return
        grupo.registrar_estudiante(estudiante=estudiante)
        print("Estudiante asignado al grupo correctamente")

    def ver_grupos_asignados_a_estudiante(self, numero_control_estudiante: str):
        estudiante = self.buscar_estudiante_por_numero_control(numero_control_estudiante=numero_control_estudiante)
        if estudiante is None:
            print("No se encontro ningun estudiante con el numero de control ingresado")
            return
        for grupo in self.lista_grupos:
            grupo.mostrar_info_grupo_para_estudiante()

    ### Validar Usuarios ###
    def validar_inicio_sesion(self, numero_control: str, contrasenia: str):
        for usuario in self.lista_usuarios:
            if usuario.numero_control == numero_control:
                if usuario.contrasenia == contrasenia:
                    return usuario
        return None
    
    def buscar_estudiante_por_numero_control(self, numero_control_estudiante: str):
        for estudiante in self.lista_estudiantes:
            if estudiante.numero_control == numero_control_estudiante:
                return estudiante
        return None
    
    def buscar_maestro_por_numero_control(self, numero_control_maestro: str):
        for maestro in self.lista_maestros:
            if maestro.numero_control == numero_control_maestro:
                return maestro
        return None
    
    def buscar_grupo_por_id(self, id_grupo: str):
        for grupo in self.lista_grupos:
            if grupo.id == id_grupo:
                return grupo
        return None
    