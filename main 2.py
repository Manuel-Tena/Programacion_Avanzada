"""
- Pacientes
- Médicos
- Consultas
- Medicamentos
"""

from paciente import Paciente
from medico import Medico
from hospital import Hospital

hospital = Hospital()

paciente_uno = Paciente("Juan", 2004, 76, 1.78, "Avenida Madero") # 5
paciente_dos = Paciente("Jonathan", 2005, 70, 1.90, "Avenida Madero") # 5
paciente_tres = Paciente("Carlos", 2010, 62, 1.65, "Avenida Michoacan") # 5
paciente_cuatro = Paciente("Francisco", 2008, 72, 1.73, "Avenida Michoacan") # 5

medico_uno = Medico("Alberto", 1989, "ALB4817BNDDDF", "Av. Periodismo") # 8
medico_dos = Medico("Esteban", 1965, "EST7184TNRRAM", "Av. Lazaro CArdenas") # 8

hospital.registrar_paciente(paciente=paciente_uno)
hospital.registrar_paciente(paciente=paciente_dos)
hospital.registrar_paciente(paciente=paciente_tres)
hospital.registrar_paciente(paciente=paciente_cuatro)

hospital.registrar_medico(medico=medico_uno)
hospital.registrar_medico(medico=medico_dos)

while True: 
    print("\n ------------------ Bienvenido ------------------ \n ")
    print(" \n ------------ Opciones en el Sistema ------------ \n ")
    print("1. Pacientes")
    print("2. Medicos")
    print("3. Salir")
    opcion = input("\n Ingresa la opcion que deseas: ")
    if opcion == "1":
        while True:
            print("\n Opciones en la seccion Pacientes \n ")
            print("1. Mostrar todos los Pacientes")
            print("2. Mostrar Pacientes Mayores de edad")
            print("3. Mostrar Pacientes Menores de edad")
            print("4. Eliminar paciente")
            print("5. Regresar")
            opcion_1 = input("\n Ingresa la opcion que deseas: ")
            if opcion_1 == "1":
                hospital.mostrar_pacientes()
            elif opcion_1 == "2":
                hospital.mostrar_pacientes_mayores_de_edad()
            elif opcion_1 == "3":
                hospital.mostrar_pacientes_menores_de_edad()
            elif opcion_1 == "4":
                id_paciente = int(input("Ingresa el ID del paciente: "))
                hospital.eliminar_paciente(id_paciente=id_paciente)
            else:
                break
    elif opcion == "2":
        while True:
            print("\n Opciones en la seccion Medicos \n ")
            print("1. Mostrar todos los Medicos")
            print("2. Eliminar Medico")
            print("3. Regresar")
            opcion_2 = input("\n Ingresa la opcion que deseas: ")
            if opcion_2 == "1":
                hospital.mostrar_medicos()
            elif opcion_2 == "2":
                id_medico = int(input("Ingresa el ID del medico: "))
                hospital.eliminar_medico(id_medico=id_medico)
            else:
                break
    else:
        print("\n Hasta luego")
        break

    #hospital.registrar_consulta(id_paciente=1, id_medico=1)

