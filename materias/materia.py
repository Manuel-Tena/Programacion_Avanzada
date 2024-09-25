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

    def mostrar_informacion(self):
        informacion = f"Id de la Materia: {self.id} \nNombre de la materia: {self.nombre} \nDescripcion: {self.descripcion} \nSemetre: {self.semestre} \nCreditos: {self.credito} \n------------------------------------------"
        return informacion