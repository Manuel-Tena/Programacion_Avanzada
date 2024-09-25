from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime

escuela = Escuela()

while True:
    print("** MINDBOX **")
    print("1. Registrar estudiante")
    print("2. Registrar maestro")
    print("3. Registrar materia")
    print("4. Registrar grupo")
    print("5. Registrar horario")
    print("6. Mostrar estudiantes")
    print("7. Mostrar maestros")
    print("8. Mostrar materias")
    print("9. Mostrar grupos")
    print("10. Eliminar estudiante")
    print("11. Eliminar maestro")
    print("12. Eliminar materia")
    print("13. Salir")
    opcion = input("Ingrese una opcion para continuar: ")
    
    if opcion == "1":
        print("\nSeleccionaste agregar un estudiante \n")
        nombre = input("Ingresa el nombre del estudiante: ")
        apellido = input("Ingresa el apellido del estudiante: ")
        curp = input("Ingresa la curp del estudiante: ")
        ano = int(input("Ingresa el año de nacimiento del estudiante: "))
        mes = int(input("Ingresa el mes de nacimiento del estudiante: "))
        dia = int(input("Ingresa el dia de nacimiento del estudiante: "))
        fecha_nacimiento = datetime(ano, mes, dia)

        estudiante = Estudiante("", nombre=nombre, apellido=apellido, curp=curp, fecha_nacimiento=fecha_nacimiento)
        numero_control = escuela.generar_numero_control()
        estudiante.numero_control = numero_control
        print("numero de control es: ", numero_control)
        escuela.registrar_estudiante(estudiante=estudiante)        

    elif opcion == "2":
        print("\nSeleccionaste agregar un maestro \n")
        nombre = input("Ingresa el nombre del maestro: ")
        apellido = input("Ingresa el apellido del maestro: ")
        ano = int(input("Ingresa el año de nacimiento del maestro: "))
        mes = int(input("Ingresa el mes de nacimiento del maestro: "))
        dia = int(input("Ingresa el dia de nacimiento del maestro: "))
        fecha_nacimiento = datetime(ano, mes, dia)
        rfc = input("Ingresa el rfc del maestro: ")
        sueldo = input("Ingresa el sueldo del maestro: ")
        
        maestro = Maestro("", nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, rfc=rfc, sueldo=sueldo)      
        numero_control_maestro = escuela.generar_numero_control_maestros(maestro)
        maestro.numero_control_maestro = numero_control_maestro
        print("El numero de control del maestro es: ", numero_control_maestro)
        escuela.registrar_maestro(maestro=maestro)

    elif opcion == "3":
        print("\nSeleccionaste agregar una materia \n")
        nombre = input("Ingresa el nombre de la materia: ")
        descripcion = input("Ingresa la descripcion de la materia: ")
        semestre = int(input("Ingresa el semestre al que corresponde la materia: "))
        credito = int(input("Ingresa los creditos que otorga la materia: "))
        
        materia = Materia("", nombre=nombre, descripcion=descripcion, semestre=semestre, credito=credito)      
        id_materia = escuela.generar_id_materia(materia)
        materia.id = id_materia
        print("El id de la materia es: ", materia.id)
        escuela.registrar_materia(materia=materia)

    elif opcion == "4":
        print("\nSeleccionaste agregar un grupo \n")
    
    elif opcion == "5":
        print("\nSeleccionaste agregar un horario \n")
        
    elif opcion == "6":
        escuela.listar_estudiantes()
    
    elif opcion == "7":
        escuela.listar_maestros()
    
    elif opcion == "8":
        escuela.listar_materias()
    
    elif opcion == "9":
        print("\nSeleccionaste agregar un horario \n")
    
    elif opcion == "10":
        print("\nSeleccionaste la opcion de eliminar estudiante")
        numero_control = input("\nIngresa el numero de control del estudiante: ")
        escuela.eliminar_estudiante(numero_control=numero_control)
    
    elif opcion == "11":
        print("\nSeleccionaste la opcion de eliminar maestro")
        numero_control = input("\nIngresa el numero de control del maestro: ")
        escuela.eliminar_maestro(numero_control=numero_control)
    
    elif opcion == "12":
        print("\nSeleccionaste la opcion de eliminar materia")
        id_de_la_materia = input("\nIngresa el ID de la materia: ")
        escuela.eliminar_materia(id_de_la_materia=id_de_la_materia)

    else:
        print("\nHasta luego")
        break
