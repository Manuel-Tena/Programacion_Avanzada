from usuario.usuario import Usuario
from datetime import datetime
from usuario.utils.roles import Rol

class Maestro(Usuario):
    rfc : str
    sueldo : float
    fecha_nacimiento : datetime

    def __init__(self, numero_control: str, nombre: str,apellido: str,  fecha_nacimiento: datetime, rfc: str, sueldo: float, contrasenia: str):
        super().__init__(numero_control=numero_control, nombre=nombre, apellido=apellido, contrasenia=contrasenia, rol=Rol.MAESTRO)
        self.fecha_nacimiento = fecha_nacimiento
        self.rfc = rfc
        self.sueldo = sueldo

    def mostrar_informacion(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        informacion = f"Numero de control: {self.numero_control} \nNombre completo: {nombre_completo} \nRFC: {self.rfc} \nSueldo: {self.sueldo} \nFecha de nacimiento: {self.fecha_nacimiento} \nRol: {self.rol.value} \n------------------------------------------"
        return informacion