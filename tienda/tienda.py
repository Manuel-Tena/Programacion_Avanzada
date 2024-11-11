from productos.producto import Producto
from typing import List, Optional

class Tienda():
    lista_productos: List[Producto] = []
    
    def registrar_producto(self, producto: Producto):
        self.lista_productos.append(producto)
        print("Se registro con exito el producto")

    def mostrar_info_producto(self, nombre:str):
        producto = self.buscar_producto_por_nombre(nombre=nombre)
        print(producto.mostrar_info())

    def mostrar_inventario(self):
        print("------------------------- INVENTARIO -------------------------")
        for producto in self.lista_productos:
            print(producto.mostrar_info_inventario())

    def buscar_producto_por_nombre(self, nombre:str):
        for producto in self.lista_productos:
            if producto.nombre == nombre:
                return producto
        print("Producto no encontrado")
        return None