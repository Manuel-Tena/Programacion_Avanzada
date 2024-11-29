from tkinter import messagebox, ttk
from tkinter import *
import tkinter as tk
import mysql.connector

def login():
    root = tk.Tk()
    root.title("Login")
    root.geometry("400x250")
    
    label_usuario = tk.Label(root, text="Usuario:", font=("Times New Roman", 14, "roman"))
    label_usuario.pack(pady=8)
    entry_usuario = tk.Entry(root, width=30)
    entry_usuario.pack(pady=8)
    
    label_contraseña = tk.Label(root, text="Contraseña:", font=("Times New Roman", 14, "roman"))
    label_contraseña.pack(pady=8)
    entry_contraseña = tk.Entry(root, width=30, show="*")
    entry_contraseña.pack(pady=8)
    
    def verificar_login():
        usuario = entry_usuario.get()
        contraseña = entry_contraseña.get()

        try:
            inicio = mysql.connector.connect(host='localhost', user='root', password='', database='proyecto_final')
            cursor = inicio.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE usuario = %s AND contraseña = %s ", (usuario, contraseña))
            usuario = cursor.fetchone()

            if usuario:
                
                if usuario[5] == "Administrador":
                    messagebox.showinfo("Sesion Iniciada con exito", f"Bienvenido al menu de Administrador {usuario[1]}")
                    root.withdraw()
                    gestion_de_empleados()
                elif usuario[5] == "Empleado":
                    messagebox.showinfo("Sesion Iniciada con exito", f"Bienvenido al menu de Empleado {usuario[1]}")
                    root.withdraw()
                    gestion_de_libros()
            else:
                messagebox.showerror("Error", "El Usuario o contraseña no fueron encontrados.")
                entry_usuario.delete(0, END)
                entry_contraseña.delete(0, END)
    
        except mysql.connector.Error as err:
            messagebox.showerror("Error de conexión", f"Error: {err}")
    
        finally:
            if inicio.is_connected():
                inicio.close()  

    bttn_login = tk.Button(root, text="Iniciar Sesion", font=("Times New Roman", 12), command=verificar_login)
    bttn_login.pack(pady=30)

    root.mainloop()

def gestion_de_empleados():
    ventana_administrador = tk.Toplevel()
    ventana_administrador.title("Gestion de Empleados")
    ventana_administrador.destroy()

    def mostrar():
        mysqlC = mysql.connector.connect(host="localhost", user="root", password="", database="proyecto_final")
        micursor =mysqlC.cursor()
        micursor .execute("select * from usuarios")
        lista = micursor.fetchall()

        for i,(id, nombre, apellido, usuario, contraseña, rol) in enumerate(lista,start=1):
            listbox.insert("","end",values=(id, nombre, apellido, usuario, contraseña, rol))
            mysqlC.close()
    
    def add():
        idAdd = identificador.get()
        nameadd = name.get()
        lastnameadd = lastname.get()
        useradd = user.get()
        passwordAdd = password.get()
        rolAdd = role.get()
        
        if rolAdd == "":
            messagebox.showerror("Error", "El campo 'Rol' no puede estar vacío. Seleccione un rol para continuar.")
            return

        mysqlC = mysql.connector.connect(host="localhost", user="root", password="", database="proyecto_final")
        micursor = mysqlC.cursor()
        try: 
            micursor.execute(f"insert into usuarios (id, nombre, apellido, usuario, contraseña, rol) values('{idAdd}','{nameadd}','{lastnameadd}','{useradd}','{passwordAdd}','{rolAdd}')")
            mysqlC.commit()
            identificador.delete(0,END)
            name.delete(0,END)
            lastname.delete(0,END)
            user.delete(0,END)
            password.delete(0,END)
            role.delete(0,END)
            messagebox.showinfo("informacion","usuario registrado con exito")
            actualizar()
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()

    def actualizar():
        for i in listbox.get_children():
            listbox.delete(i)
        mostrar()
    
    def edit():
        idAdd = identificador.get()
        nameadd = name.get()
        lastnameadd = lastname.get()
        useradd = user.get()
        passwordAdd = password.get()
        rolAdd = role.get()

        mysqlC = mysql.connector.connect(host="localhost",user="root",password="",database="proyecto_final")
        micursor=mysqlC.cursor()
        try:
            micursor.execute(f"UPDATE usuarios set nombre='{nameadd}', apellido = '{lastnameadd}', usuario = '{useradd}', contraseña = '{passwordAdd}', rol = '{rolAdd}' where id = {idAdd}")
            mysqlC.commit()
            identificador.delete(0,END)
            name.delete(0,END)
            lastname.delete(0,END)
            user.delete(0,END)
            password.delete(0,END)
            role.delete(0,END)
            messagebox.showinfo("informacion","datos del empleado editados correctamente")
            actualizar()
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()
    
    def delete():
        idAdd = identificador.get()
        mysqlC = mysql.connector.connect(host="localhost", user="root", password="", database="proyecto_final")
        micursor = mysqlC.cursor()
        try:
            micursor.execute(f"DELETE FROM USUARIOS WHERE id = {idAdd}")
            mysqlC.commit()
            identificador.delete(0,END)
            name.delete(0,END)
            lastname.delete(0,END)
            user.delete(0,END)
            password.delete(0,END)
            role.delete(0,END)
            messagebox.showinfo("informacion","empleado eliminado correctamente")
            actualizar()
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()

    def obtener(event):
        identificador.delete(0,END)
        name.delete(0,END)
        lastname.delete(0,END)
        user.delete(0,END)
        password.delete(0,END)
        role.delete(0,END)

        renglon = listbox.selection()[0]
        print(renglon)
        seleccion = listbox.set(renglon)
        print(seleccion)
        identificador.insert(0, seleccion["Id"])
        name.insert(0, seleccion["Nombre"])
        lastname.insert(0, seleccion["Apellido"])
        user.insert(0, seleccion["Usuario"])
        password.insert(0, seleccion["Contraseña"])
        role.insert(0, seleccion["Rol"])

    
    def regresar():
        ventana_administrador.destroy()
        login()

    ventana_administrador = tk.Tk()
    ventana_administrador.geometry("1200x600")
    
    label1 = tk.Label(ventana_administrador, text="Registro de empleados", fg="blue",font=("Times New Roman",24)).place(x=170,y=0)
    
    global identificador
    global name
    global lastname
    global user
    global password
    global role
    
    labelid = tk.Label(ventana_administrador, text="ID", font=("Times New Roman", 12))
    labelid.place(x=100, y=50)
    labelnombre = tk.Label(ventana_administrador, text="Nombre", font=("Times New Roman", 12))
    labelnombre.place(x=100, y=80)
    labelapellido = tk.Label(ventana_administrador, text="Apellido", font=("Times New Roman", 12))
    labelapellido.place(x=100, y=110)
    labelusuario = tk.Label(ventana_administrador, text="Usuario", font=("Times New Roman", 12))
    labelusuario.place(x=100, y=140)
    labelcontrasena = tk.Label(ventana_administrador, text="Contraseña", font=("Times New Roman", 12))
    labelcontrasena.place(x=100, y=170)
    labelrol = tk.Label(ventana_administrador, text="Rol", font=("Times New Roman", 12))
    labelrol.place(x=100, y=200)
    
    identificador = tk.Entry(ventana_administrador)
    identificador.place(x=270, y=50)
    name = tk.Entry(ventana_administrador)
    name.place(x=270, y=80)
    lastname = tk.Entry(ventana_administrador)
    lastname.place(x=270, y=110)
    user = tk.Entry(ventana_administrador)
    user.place(x=270, y=140)
    password = tk.Entry(ventana_administrador)
    password.place(x=270, y=170)
    role = ttk.Combobox(ventana_administrador, values=["", "Empleado", "Administrador"], state="readonly")
    role.place(x=270, y=200)
    
    tk.Button(ventana_administrador,text="Crear",command=add, height=5, width=10, font=("Times New Roman",12)).place(x=100,y=230)
    tk.Button(ventana_administrador,text="Editar",command=edit, height=5, width=10, font=("Times New Roman",12)).place(x=250,y=230)
    tk.Button(ventana_administrador,text="Eliminar",command=delete, height=5, width=10, font=("Times New Roman",12)).place(x=400,y=230)
    tk.Button(ventana_administrador,text="Regresar",command=regresar, height=5, width=10, font=("Times New Roman",12)).place(x=550,y=230)
    
    columnas = ("Id","Nombre","Apellido","Usuario","Contraseña","Rol")
    listbox = ttk.Treeview(ventana_administrador,columns=columnas,show="headings")
    
    for col in columnas:
        listbox.heading(col, text=col)
        listbox.grid(row=1, column=0, columnspan=1)
        listbox.place(x=0, y=350)
    
    mostrar()
    listbox.bind("<Double-Button-1>", obtener)
    ventana_administrador.mainloop()

def gestion_de_libros():
    ventana_empleado = tk.Toplevel()
    ventana_empleado.title("Gestion de Libros")
    ventana_empleado.destroy()

    def mostrar():
        mysqlC = mysql.connector.connect(host="localhost", user="root", password="", database="proyecto_final")
        micursor =mysqlC.cursor()
        micursor .execute("select * from libros")
        lista = micursor.fetchall()

        for i,(id, titulo, autor, editorial, publicacion, precio) in enumerate(lista,start=1):
            listbox.insert("","end",values=(id, titulo, autor, editorial, publicacion, precio))
            mysqlC.close()
    
    def add():
        idAdd = identificador.get()
        titleadd = title.get()
        autoradd = autor.get()
        editorialadd = editorial.get()
        releasedateAdd = releasedate.get()
        priceAdd = price.get()

        mysqlC = mysql.connector.connect(host="localhost", user="root", password="", database="proyecto_final")
        micursor = mysqlC.cursor()
        try: 
            micursor.execute(f"insert into libros (id, titulo, autor, editorial, año_publicación, precio) values('{idAdd}','{titleadd}','{autoradd}','{editorialadd}','{releasedateAdd}','{priceAdd}')")
            mysqlC.commit()
            identificador.delete(0,END)
            title.delete(0, END)
            autor.delete(0, END)
            editorial.delete(0, END)
            releasedate.delete(0, END)
            price.delete(0, END)
            messagebox.showinfo("informacion","libro registrado con exito")
            actualizar()
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()

    def actualizar():
        for i in listbox.get_children():
            listbox.delete(i)
        mostrar()

    def actualizar_sinmostrar():
        for i in listbox.get_children():
                listbox.delete(i)

    def reiniciar():
        actualizar()
        messagebox.showinfo("Información", "El filtro fue eliminado")
    
    def edit():
        idAdd = identificador.get()
        titleadd = title.get()
        autoradd = autor.get()
        editorialadd = editorial.get()
        releasedateAdd = releasedate.get()
        priceAdd = price.get()

        mysqlC = mysql.connector.connect(host="localhost",user="root",password="",database="proyecto_final")
        micursor=mysqlC.cursor()
        try:
            micursor.execute(f"UPDATE libros set titulo = '{titleadd}', autor = '{autoradd}', editorial = '{editorialadd}', año_publicación = '{releasedateAdd}', precio = '{priceAdd}' where id = {idAdd}")
            mysqlC.commit()
            identificador.delete(0,END)
            title.delete(0, END)
            autor.delete(0, END)
            editorial.delete(0, END)
            releasedate.delete(0, END)
            price.delete(0, END)
            messagebox.showinfo("informacion","datos del libro editados correctamente")
            actualizar()
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()
    
    def delete():
        idAdd = identificador.get()
        mysqlC = mysql.connector.connect(host="localhost", user="root", password="", database="proyecto_final")
        micursor = mysqlC.cursor()
        try:
            micursor.execute(f"DELETE FROM LIBROS WHERE id = {idAdd}")
            mysqlC.commit()
            identificador.delete(0,END)
            title.delete(0, END)
            autor.delete(0, END)
            editorial.delete(0, END)
            releasedate.delete(0, END)
            price.delete(0, END)
            messagebox.showinfo("informacion","libro eliminado correctamente")
            actualizar()
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()

    def obtener(event):
        identificador.delete(0,END)
        title.delete(0, END)
        autor.delete(0, END)
        editorial.delete(0, END)
        releasedate.delete(0, END)
        price.delete(0, END)

        renglon = listbox.selection()[0]
        print(renglon)
        seleccion = listbox.set(renglon)
        print(seleccion)
        identificador.insert(0, seleccion["Id"])
        name.insert(0, seleccion["Titulo"])
        lastname.insert(0, seleccion["Autor"])
        user.insert(0, seleccion["Editorial"])
        password.insert(0, seleccion["Año de publicación"])
        role.insert(0, seleccion["Precio"])

    def filtrar_por_editorial():
        filtrar_por_editorial = filtrareditorial.get()
        
        mysqlC = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "proyecto_final")
        micursor = mysqlC.cursor()
        
        try:
            micursor.execute("SELECT DISTINCT editorial FROM libros")
            lista = [row[0] for row in micursor.fetchall()]

            if filtrar_por_editorial not in lista:
                messagebox.showerror("Error", f"La editorial '{filtrar_por_editorial}' no existe, vuelve a intentar")
                return

            micursor.execute(f"SELECT * FROM libros WHERE editorial = '{filtrar_por_editorial}'")
            lista = micursor.fetchall()
            actualizar_sinmostrar()

            if lista:
                for id, titulo, autor, editorial, año_de_publicacion, precio in lista:
                    listbox.insert("", "end", values=(id, titulo, autor, editorial, año_de_publicacion, precio))
                messagebox.showinfo("Información", "Datos filtrados con exito.")
            else:
                messagebox.showinfo("Información", "No se encontraron libros de esa editorial")
        
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()
            
    def regresar():
        ventana_empleado.destroy()
        login()

    ventana_empleado = tk.Tk()
    ventana_empleado.geometry("1200x650")
    
    label1 = tk.Label(ventana_empleado, text="Registro de libros", fg="blue",font=("Times New Roman",24)).place(x=500,y=0)
    
    global identificador
    global title
    global autor
    global editorial
    global releasedate
    global price
    
    labelid = tk.Label(ventana_empleado, text="ID", font=("Times New Roman", 12))
    labelid.place(x=460, y=50)
    labeltitulo = tk.Label(ventana_empleado, text="Titulo", font=("Times New Roman", 12))
    labeltitulo.place(x=460, y=80)
    labelautor = tk.Label(ventana_empleado, text="Autor", font=("Times New Roman", 12))
    labelautor.place(x=460, y=110)
    labeleditorial = tk.Label(ventana_empleado, text="Editorial", font=("Times New Roman", 12))
    labeleditorial.place(x=460, y=140)
    labelañodepublicacion = tk.Label(ventana_empleado, text="Año de Publicación", font=("Times New Roman", 12))
    labelañodepublicacion.place(x=460, y=170)
    labelprecio = tk.Label(ventana_empleado, text="Precio", font=("Times New Roman", 12))
    labelprecio.place(x=460, y=200)
    labelfiltrareditorial = tk.Label(ventana_empleado, text="Filtrar por Editorial", font=("Times New Roman", 12))
    labelfiltrareditorial.place(x=460, y=230)
    
    identificador = tk.Entry(ventana_empleado)
    identificador.place(x=640, y=50)
    title = tk.Entry(ventana_empleado)
    title.place(x=640, y=80)
    autor = tk.Entry(ventana_empleado)
    autor.place(x=640, y=110)
    editorial = tk.Entry(ventana_empleado)
    editorial.place(x=640, y=140)
    releasedate = tk.Entry(ventana_empleado)
    releasedate.place(x=640, y=170)
    price = tk.Entry(ventana_empleado)
    price.place(x=640, y=200)
    filtrareditorial = tk.Entry(ventana_empleado)
    filtrareditorial.place(x=640, y=230)
    
    tk.Button(ventana_empleado, text="Crear", command=add, height=5, width=10, font=("Times New Roman",12)).place(x=100,y=260)
    tk.Button(ventana_empleado, text="Editar", command=edit, height=5, width=10, font=("Times New Roman",12)).place(x=280,y=260)
    tk.Button(ventana_empleado, text="Filtrar", command=filtrar_por_editorial, height=5, width=10, font=("Times New Roman",12)).place(x=460,y=260)
    tk.Button(ventana_empleado, text="Eliminar", command=delete, height=5, width=10, font=("Times New Roman",12)).place(x=640,y=260)
    tk.Button(ventana_empleado, text="Reiniciar", command=reiniciar, height=5, width=10, font=("Times New Roman",12)).place(x=820,y=260)
    tk.Button(ventana_empleado, text="Regresar", command=regresar, height=5, width=10, font=("Times New Roman",12)).place(x=1000,y=260)
    
    columnas = ("Id","Titulo","Autor","Editorial","Año de Publicación","Precio")
    listbox = ttk.Treeview(ventana_empleado,columns=columnas,show="headings")
    
    for col in columnas:
        listbox.heading(col, text=col)
        listbox.grid(row=1, column=0, columnspan=1)
        listbox.place(x=0, y=400)
    
    mostrar()
    listbox.bind("<Double-Button-1>", obtener)
    ventana_empleado.mainloop()

login()