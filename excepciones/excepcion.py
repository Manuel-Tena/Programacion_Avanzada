class ProductoInvalidoException(Exception):
    def __init__(self, message="El nombre del producto no puede estar vacío"):
        self.message = message
        super().__init__(self.message)

class PrecioInvalidoException(Exception):
    def __init__(self, message="El precio debe ser un valor positivo y mayor que cero"):
        self.message = message
        super().__init__(self.message)

class CantidadInvalidaException(Exception):
    def __init__(self, message="La cantidad debe ser un número positivo"):
        self.message = message
        super().__init__(self.message)
 