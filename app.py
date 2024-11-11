import tkinter as tk
from tkinter import messagebox
from productos.producto import Producto
from tienda.tienda import Tienda
from excepciones.excepcion import PrecioInvalidoException, CantidadInvalidaException, ProductoInvalidoException

class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Tienda")
        
        self.tienda = Tienda()
        
        # Sección para agregar un producto
        tk.Label(ventana, text="Nombre del Producto:", bg="blue", fg="white", font=("Times New Roman", 10)).grid(row=0, column=0, padx=10, pady=5)
        self.nombre_entry = tk.Entry(ventana)
        self.nombre_entry.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(ventana, text="Precio:", bg="blue", fg="white", font=("Times New Roman", 10)).grid(row=1, column=0, padx=10, pady=5)
        self.precio_entry = tk.Entry(ventana)
        self.precio_entry.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(ventana, text="Cantidad:", bg="blue", fg="white", font=("Times New Roman", 10)).grid(row=2, column=0, padx=10, pady=5)
        self.cantidad_entry = tk.Entry(ventana)
        self.cantidad_entry.grid(row=2, column=1, padx=10, pady=5)
        
        tk.Button(ventana, text="Agregar Producto", font=("Times New Roman", 10), command=self.agregar_producto).grid(row=3, column=0, columnspan=2, pady=10)
        
        # Sección para modificar inventario
        tk.Label(ventana, text="Nombre del Producto a Modificar:", bg="blue", fg="white", font=("Times New Roman", 10)).grid(row=4, column=0, padx=10, pady=5)
        self.nombre_modificar_entry = tk.Entry(ventana)
        self.nombre_modificar_entry.grid(row=4, column=1, padx=10, pady=5)
        
        tk.Label(ventana, text="Cantidad a Modificar:", bg="blue", fg="white", font=("Times New Roman", 10)).grid(row=5, column=0, padx=10, pady=5)
        self.cantidad_modificar_entry = tk.Entry(ventana)
        self.cantidad_modificar_entry.grid(row=5, column=1, padx=10, pady=5)
        
        tk.Button(ventana, text="Agregar Cantidad", font=("Times New Roman", 10), command=lambda: self.modificar_inventario_de_producto("agregar")).grid(row=6, column=0, pady=10)
        tk.Button(ventana, text="Eliminar Cantidad", font=("Times New Roman", 10), command=lambda: self.modificar_inventario_de_producto("eliminar")).grid(row=6, column=1, pady=10)

        # Sección para buscar un producto
        tk.Label(ventana, text="Buscar Producto:", bg="blue", fg="white", font=("Times New Roman", 10)).grid(row=7, column=0, padx=10, pady=5)
        self.buscar_entry = tk.Entry(ventana)
        self.buscar_entry.grid(row=7, column=1, padx=10, pady=5)
        
        tk.Button(ventana, text="Buscar Producto", font=("Times New Roman", 10), command=self.buscar_producto).grid(row=8, column=0, columnspan=2, pady=10)
        
        # Botones para mostrar detalles y el inventario completo
        tk.Button(ventana, text="Mostrar Inventario Completo", font=("Times New Roman", 10), command=self.mostrar_inventario).grid(row=9, column=0, columnspan=2, pady=5)
        
        # Área de salida
        self.output_text = tk.Text(ventana, height=10, width=40)
        self.output_text.grid(row=10, column=0, columnspan=2, padx=10, pady=10)
    
    def agregar_producto(self):
        nombre = self.nombre_entry.get()
        try:
            precio = float(self.precio_entry.get())
            cantidad = int(self.cantidad_entry.get())
            
            producto = Producto(nombre=nombre, precio=precio, cantidad=cantidad)
            self.tienda.registrar_producto(producto)
            
            messagebox.showinfo("Éxito", "Producto registrado con éxito")
            self.limpiar_entradas()
            
        except (ProductoInvalidoException, PrecioInvalidoException, CantidadInvalidaException) as e:
            messagebox.showerror("Error", str(e))
        except ValueError:
            messagebox.showerror("Error", "Precio y cantidad deben ser valores numéricos")
    
    def modificar_inventario_de_producto(self, accion):
        nombre = self.nombre_modificar_entry.get()
        try:
            cantidad_modificar = int(self.cantidad_modificar_entry.get())
            producto = self.tienda.buscar_producto_por_nombre(nombre)
            
            self.output_text.delete(1.0, tk.END)
            
            if producto:
                if accion == "agregar":
                    producto.cantidad += cantidad_modificar
                elif accion == "eliminar":
                    producto.cantidad -= cantidad_modificar
                
                messagebox.showinfo("Éxito", f"Inventario actualizado para '{nombre}'")
                detalles = producto.mostrar_info()
                self.output_text.insert(tk.END, detalles)

            else:
                messagebox.showerror("Error", "Producto no encontrado")
                
        except CantidadInvalidaException as e:
            messagebox.showerror("Error", str(e))
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número entero")
    
    def buscar_producto(self):
        nombre = self.buscar_entry.get()
        producto = self.tienda.buscar_producto_por_nombre(nombre)
        
        self.output_text.delete(1.0, tk.END)
        
        if producto:
            detalles = producto.mostrar_info()
            self.output_text.insert(tk.END, detalles)
        else:
            self.output_text.insert(tk.END, "Producto no encontrado\n")
    
    def mostrar_inventario(self):
        self.output_text.delete(1.0, tk.END)
        
        if not self.tienda.lista_productos:
            self.output_text.insert(tk.END, "No hay productos registrados\n")
        else:
            for producto in self.tienda.lista_productos:
                detalles = producto.mostrar_info_inventario()
                self.output_text.insert(tk.END, detalles)
    
    def limpiar_entradas(self):
        self.nombre_entry.delete(0, tk.END)
        self.precio_entry.delete(0, tk.END)
        self.cantidad_entry.delete(0, tk.END)
        self.nombre_modificar_entry.delete(0, tk.END)
        self.cantidad_modificar_entry.delete(0, tk.END)
        self.buscar_entry.delete(0, tk.END)