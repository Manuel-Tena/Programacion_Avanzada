import tkinter as tk
from tkinter import messagebox
 
def sumar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        suma = num1 + num2
        messagebox.showinfo("Resultado", f"El resultado de la suma es: {suma}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

def resta():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resta = num1 - num2
        messagebox.showinfo("Resultado", f"El resultado de la resta es: {resta}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
 
def division():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        division = num1/num2
        messagebox.showinfo("Resultado", f"El resultado de la division es: {division}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

def multiplicacion():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        multiplicacion = num1*num2
        messagebox.showinfo("Resultado", f"El resultado de la multiplicacion es: {multiplicacion}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

ventana = tk.Tk()
ventana.title("Calculadora de Suma")
ventana.geometry("584x200")
 
label_num1 = tk.Label(ventana, text="Número 1:", bg="gray", fg="white", font=("Times New Roman", 16, "bold"), relief="sunken", padx=10, pady=10)
label_num1.grid(row = 1, column = 3)
entry_num1 = tk.Entry(ventana, font=("Times New Roman", 14), bd=1, relief="solid")
entry_num1.grid(row = 3, column = 3)
 
label_num2 = tk.Label(ventana, text="Número 2:", bg="gray", fg="white", font=("Times New Roman", 16, "bold"), relief="sunken", padx=10, pady=10)
label_num2.grid(row = 1, column = 5)
entry_num2 = tk.Entry(ventana, font=("Times New Roman", 14), bd=1, relief="solid")
entry_num2.grid(row = 3, column = 5)
 
label = tk.Label(text = "    ")
label.grid(row = 3, column = 4)

label = tk.Label(text = "")
label.grid(row = 4, column = 2)

label = tk.Label(text = "")
label.grid(row = 2, column = 0)

label = tk.Label(text = "")
label.grid(row = 0, column = 0)
 
boton_sumar = tk.Button(ventana, text="Sumar", bg="gray", fg="white", font=("Times New Roman", 12), command=sumar)
boton_sumar.grid(row = 5, column = 1)

boton_restar = tk.Button(ventana, text="Restar", bg="gray", fg="white", font=("Times New Roman", 12), command=resta)
boton_restar.grid(row = 5, column = 3)

boton_multiplicar = tk.Button(ventana, text="Multiplicar", bg="gray", fg="white", font=("Times New Roman", 12), command=multiplicacion)
boton_multiplicar.grid(row = 5, column = 5)

boton_dividir = tk.Button(ventana, text="Dividir", bg="gray", fg="white", font=("Times New Roman", 12), command=division)
boton_dividir.grid(row = 5, column = 7)
 
ventana.mainloop()