from excepciones.excepcion import ProductoInvalidoException, PrecioInvalidoException, CantidadInvalidaException

class Producto():
    nombre: str
    precio: float
    cantidad: int

    def __init__(self, nombre: str, precio: float, cantidad: int):
        if not nombre:
            raise ProductoInvalidoException()
        self.nombre = nombre
        if precio <= 0:
            raise PrecioInvalidoException()
        self.precio = precio
        if cantidad < 0:
            raise CantidadInvalidaException
        self.cantidad = cantidad

    def calcular_valor_total(self):
        return (self.precio * self.cantidad)

    def mostrar_info(self):
        valor_total = self.calcular_valor_total()
        info = f"Nombre: {self.nombre} \nPrecio Individual: {self.precio} \nProductos en Existencia: {self.cantidad} \nValor total del producto: {valor_total}"
        return info

    def mostrar_info_inventario(self):
        info = f"Nombre del producto: {self.nombre} \nProductos en Existencia: {self.cantidad} \n------------------------------\n"
        return info