from typing import List
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materias

class Grupo:
    id: int
    estudiantes: List[Estudiante] = []
    maestros: List[Maestro] = []
    materias: List[Materias] = []
