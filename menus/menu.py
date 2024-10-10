from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from coordinador.coordinador import Coordinador
from materias.materia import Materia
from carrera.carrera import Carrera
from semestre.semestre import Semestre
from usuario.utils.roles import Rol
from grupos.grupo import Grupo
from datetime import datetime

class Menu:
    escuela = Escuela()

    def login(self):
        intentos = 0
        print("*** BIENVENIDO ***")
        while intentos < 5:
            print("Inicia Sesión para continuar")
            numero_control = input("Ingresa tu numero de control: ")
            contrasenia_usuario = input("Ingresa tu contraseña: ")
            usuario = self.escuela.validar_inicio_sesion(numero_control=numero_control, contrasenia=contrasenia_usuario)
            
            if usuario is None:
                intentos = self.mostrar_intento_sesion_fallido(intentos_usuarios=intentos)
            else: 
                if usuario.rol == Rol.ESTUDIANTE:
                    self.mostrar_menu_estudiante(usuario)
                    intentos = 0
                elif usuario.rol == Rol.MAESTRO:
                    self.mostrar_menu_maestro(usuario)
                    intentos = 0
                else: 
                    self.mostrar_menu_coordinador(usuario)
                    intentos = 0

        print("Máximos intentos de inicio de sesion alcanzados. Intente mas tarde")

    def mostrar_intento_sesion_fallido(self, intentos_usuarios):
        print("\nUsuario o contraseña incorrectos. Intente de nuevo")
        return intentos_usuarios + 1

    def mostrar_menu_estudiante(self, usuario: Estudiante):
        opcion = 0
        while opcion != 6:
            print("\n*** MINDBOX ***")
            print("1. Ver horario")
            print("2. Ver grupos")
            print("3. Ver materias")
            print("4. Ver semestres")
            print("5. Ver mi informacion")
            print("6. Salir")
            opcion = int(input("Ingresa una opción: "))
            
            if opcion == 1:
                print("\nSeleccionaste mostrar un horario \n")

            elif opcion == 2:
                self.escuela.listar_grupos()

            elif opcion == 3:
                self.escuela.listar_materias()

            elif opcion == 4:
                self.escuela.listar_semestres()
            
            elif opcion == 5:
                print("************* INFORMACION DE USUARIO *************")
                print(usuario.mostrar_informacion())
            
            else:
                print("\nHasta luego")
                break            

    def mostrar_menu_maestro(self, usuario: Maestro):
        opcion = 0
        while opcion != 8:
            print("\n*** MINDBOX ***")
            print("1. Ver horarios")
            print("2. Ver grupos")
            print("3. Ver materias")
            print("4. Ver alumnos")
            print("5. Ver carreras")
            print("6. Ver semestres")
            print("7. Ver mi informacion")
            print("8. Salir")
            opcion = int(input("Ingresa una opción: "))
            
            if opcion == 1:
                print("\nSeleccionaste mostrar un horario \n")

            elif opcion == 2:
                self.escuela.listar_grupos()

            elif opcion == 3:
                self.escuela.listar_materias()

            elif opcion == 4:
                self.escuela.listar_estudiantes()

            elif opcion == 5:
                self.escuela.listar_carreras()
            
            elif opcion == 6:
                self.escuela.listar_semestres()
            
            elif opcion == 7:
                print("************* INFORMACION DE USUARIO *************")
                print(usuario.mostrar_informacion())
            
            else:
                print("\nHasta luego")
                break            

    def mostrar_menu_coordinador(self, usuario: Coordinador):
        while True:
            print("*** MINDBOX ***")
            print("1. Registrar estudiante")
            print("2. Registrar maestro")
            print("3. Registrar materia")
            print("4. Registrar grupo")
            print("5. Registrar horario")
            print("6. Registrar carrera")
            print("7. Registrar semestre")
            print("8. Mostrar estudiantes")
            print("9. Mostrar maestros")
            print("10. Mostrar materias")
            print("11. Mostrar grupos")
            print("12. Mostrar horarios")
            print("13. Mostrar carreras")
            print("14. Mostrar semestres")
            print("15. Eliminar estudiante")
            print("16. Eliminar maestro")
            print("17. Eliminar materia")
            print("18. Ver mi informacion")
            print("19. Salir")
            opcion = int(input("Ingrese una opcion para continuar: "))
            
            if opcion == 1:
                print("\nSeleccionaste agregar un estudiante \n")
                nombre = input("Ingresa el nombre del estudiante: ")
                apellido = input("Ingresa el apellido del estudiante: ")
                curp = input("Ingresa la curp del estudiante: ")
                ano = int(input("Ingresa el año de nacimiento del estudiante: "))
                mes = int(input("Ingresa el mes de nacimiento del estudiante: "))
                dia = int(input("Ingresa el dia de nacimiento del estudiante: "))
                fecha_nacimiento = datetime(ano, mes, dia)
                contrasenia = input("Ingresa la contraseña del estudiante: ")

                estudiante = Estudiante("", nombre=nombre, apellido=apellido, curp=curp, fecha_nacimiento=fecha_nacimiento, contrasenia=contrasenia)
                numero_control = self.escuela.generar_numero_control()
                estudiante.numero_control = numero_control
                print("numero de control es: ", numero_control)
                self.escuela.registrar_estudiante(estudiante=estudiante)        

            elif opcion == 2:
                print("\nSeleccionaste agregar un maestro \n")
                nombre = input("Ingresa el nombre del maestro: ")
                apellido = input("Ingresa el apellido del maestro: ")
                ano = int(input("Ingresa el año de nacimiento del maestro: "))
                mes = int(input("Ingresa el mes de nacimiento del maestro: "))
                dia = int(input("Ingresa el dia de nacimiento del maestro: "))
                fecha_nacimiento = datetime(ano, mes, dia)
                rfc = input("Ingresa el rfc del maestro: ")
                sueldo = input("Ingresa el sueldo del maestro: ")
                contrasenia = input("Ingresa la contraseña del maestro: ")
                
                maestro = Maestro("", nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, rfc=rfc, sueldo=sueldo, contrasenia=contrasenia)      
                numero_control = self.escuela.generar_numero_control_maestros(maestro)
                maestro.numero_control = numero_control
                print("El numero de control del maestro es: ", numero_control)
                self.escuela.registrar_maestro(maestro=maestro)

            elif opcion == 3:
                print("\nSeleccionaste agregar una materia \n")
                nombre = input("Ingresa el nombre de la materia: ")
                descripcion = input("Ingresa la descripcion de la materia: ")
                semestre = input("Ingresa el id del semestre al que corresponde la materia: ")
                credito = int(input("Ingresa los creditos que otorga la materia: "))
                
                materia = Materia(nombre=nombre, descripcion=descripcion, id_semestre=semestre, creditos=credito)      
                print("El id de la materia es: ", materia.numero_control)
                self.escuela.registrar_materia(materia=materia)

            elif opcion == 4:
                print("\nSeleccionaste agregar un grupo \n")
                tipo = input("Ingresa el tipo de grupo (A/B): ")
                id_semestre = input("Ingresa el ID del semestre al que pertenece el grupo: ")
                grupo = Grupo(tipo=tipo, id_semestre=id_semestre)
                self.escuela.registrar_grupo(grupo=grupo)

            elif opcion == 5:
                print("\nSeleccionaste agregar un horario \n")
            
            elif opcion == 6:
                print("\nSeleccionaste registrar una carrera")
                nombre  = input("Ingresa el nombre de la carrera: ")
                carrera = Carrera(nombre=nombre)
                self.escuela.registrar_carrera(carrera=carrera)

            elif opcion == 7:
                print("\nSeleccionaste registrar un semestre")
                numero = input("Ingresa el numero del semestre: ")
                id_carrera = input("Ingresa el ID de la carrera: ")
                semestre = Semestre(numero=numero, id_carrera=id_carrera)
                self.escuela.registrar_semestre(semestre=semestre) 

            elif opcion == 8:
                self.escuela.listar_estudiantes()
            
            elif opcion == 9:
                self.escuela.listar_maestros()
            
            elif opcion == 10:
                self.escuela.listar_materias()
            
            elif opcion == 11:
                self.escuela.listar_grupos()
            
            elif opcion == 12:
                print("\nSeleccionaste mostrar un horario \n")
            
            elif opcion == 13:
                print("\nSeleccionaste mostrar carreras \n")
                self.escuela.listar_carreras()
            
            elif opcion == 14:
                print("\nSeleccionaste mostrar semestres \n")
                self.escuela.listar_semestres()

            elif opcion == 15:
                print("\nSeleccionaste la opcion de eliminar estudiante")
                numero_control = input("\nIngresa el numero de control del estudiante: ")
                self.escuela.eliminar_estudiante(numero_control=numero_control)
            
            elif opcion == 16:
                print("\nSeleccionaste la opcion de eliminar maestro")
                numero_control = input("\nIngresa el numero de control del maestro: ")
                self.escuela.eliminar_maestro(numero_control=numero_control)
            
            elif opcion == 17:
                print("\nSeleccionaste la opcion de eliminar materia")
                id_de_la_materia = input("\nIngresa el ID de la materia: ")
                self.escuela.eliminar_materia(id_de_la_materia=id_de_la_materia)
            
            elif opcion == 18:
                print("************* INFORMACION DE USUARIO *************")
                print(usuario.mostrar_informacion())

            else:
                print("\nHasta luego")
                break

