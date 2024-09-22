class Materia:
    id: str
    nombre: str
    descripcion:str
    semestre: int
    credito: int

    def __init__(self, id: str, nombre: str, descripcion:str, semestre: int, credito: int):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.semestre = semestre
        self.credito = credito