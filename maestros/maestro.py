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

    def mostrar_informacion(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        informacion = f"Numero de control: {self.numero_control_maestro} \nNombre completo: {nombre_completo} \nRFC: {self.rfc} \nSueldo: {self.sueldo} \nFecha de nacimiento: {self.fecha_nacimiento} \n------------------------------------------"
        return informacion
    