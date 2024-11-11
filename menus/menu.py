from productos.producto import Producto
from tienda.tienda import Tienda
from excepciones.excepcion import PrecioInvalidoException, CantidadInvalidaException, ProductoInvalidoException

class Menu():
    
    tienda = Tienda()
    
    def mostrar_menu(self):
        
        while True:
            try:
                print("************** Tienda **************")
                print("1. Agregar Producto")
                print("2. Modificar Existencia de un Producto")
                print("3. Mostrar Detalles de Producto")
                print("4. Mostrar Inventario")
                print("5. Salir")
                opcion = int(input("Ingresa una opcion: "))
                
                if 1<= opcion <= 5:
                    
                    if opcion == 1:
                        nombre = input("Ingresa el nombre del producto: ")
                        precio = float(input("Ingresa el precio del producto: "))
                        cantidad = int(input("Ingresa la cantidad de productos: "))
                        
                        try:
                            producto = Producto(nombre=nombre, precio=precio, cantidad=cantidad)
                            self.tienda.registrar_producto(producto=producto)
                        except ProductoInvalidoException as e:
                            print(e)
                        except PrecioInvalidoException as e:
                            print(e)
                        except CantidadInvalidaException as e:
                            print(e)
                    
                    elif opcion == 2:
                        nombre = input("Ingresa el nombre del producto a modificar: ")
                        producto = self.tienda.buscar_producto_por_nombre(nombre)
                        while True:
                            try:
                                print("************** Modificar Producto **************")
                                print("1. Agregar ")
                                print("2. Eliminar cantidad de producto")
                                print("3. Salir")
                                opcion = int(input("Ingresa una opcion: "))

                                if 1<=opcion<=3:
                                    if opcion == 1:
                                        cantidad = int(input("Ingresa la cantidad que se va a agregar: "))
                                        nueva_cantidad = producto.cantidad + cantidad
                                        producto.cantidad = nueva_cantidad
                                        break
                                        
                                    elif opcion == 2:
                                        cantidad = int(input("Ingresa la cantidad que se va a eliminar: "))
                                        nueva_cantidad = producto.cantidad - cantidad
                                        try:
                                            producto.cantidad = nueva_cantidad
                                            break
                                        except CantidadInvalidaException as e:
                                            print(e)

                                    elif opcion == 3:
                                        break 
  
                                else:
                                    print("Opcion no válida. Por favor, elige un numero entre 1 y 3")
                                    
                            except ValueError:
                                print("Entrada no válida. Por favor, ingresa un número entero")

                    elif opcion == 3:
                        nombre = input("Ingresa el nombre del producto: ")
                        producto = self.tienda.buscar_producto_por_nombre(nombre)
                        if producto is None:
                            return
                        self.tienda.mostrar_info_producto(nombre=nombre)                       

                    elif opcion == 4:
                        self.tienda.mostrar_inventario()
                        
                    else:
                        print("Hasta luego")
                        break
                
                else:
                    print("Opcion no válida. Por favor, elige un numero entre 1 y 4")
                     
            except ValueError:
                print("Entrada no válida. Por favor, ingresa un número entero")
 