from datetime import datetime

class Maestro:
    numero_control_maestro : str
    nombre : str
    apellido : str
    rfc : str
    sueldo : float
    fecha_nacimiento : datetime

    def __init__(self, numero_control_maestro: str, nombre: str,apellido: str,  fecha_nacimiento: datetime, rfc: str, sueldo: float):
        self.numero_control_maestro = numero_control_maestro
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.rfc = rfc
        self.sueldo = sueldo
    