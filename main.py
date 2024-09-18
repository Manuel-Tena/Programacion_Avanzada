"""
- Pacientes
- Médicos
- Consultas
- Medicamentos
"""

from paciente.paciente import Paciente
from medico.medico import Medico
from hospital.hospital import Hospital

hospital = Hospital()

while True:
    print ("\n ----------------- Bienvenido al sistema del hospital ----------------- \n")
    print ("1. Registrar paciente")
    print ("2. Registrar medico")
    print ("3. Mostrar pacientes")
    print ("4. Mostrar medicos")
    print ("5. Eliminar paciente")
    print ("6. Eliminar medico")
    print ("7. Mostrar pacientes menores de edad")
    print ("8. Mostrar pacientes mayores de edad")
    print ("9. Salir")

    opcion_usuario= input("Selecione lo deseado: ")
    if opcion_usuario == "1": #Registrar Usuario
        nombre = input ("\nIngrese el nombre: ")
        ano_nacimiento = int(input("Ingrese el año de nacimiento: "))
        peso = input ("Ingrese el peso: ")
        estatura = input ("Ingrese la estatura: ")
        direccion = input ("Ingrese la direccion: ")

        paciente = Paciente(nombre=nombre, ano_nacimiento=ano_nacimiento, peso=peso, estatura=estatura, direccion=direccion)
        hospital.registrar_paciente(paciente=paciente)
        print("\n Paciente registrado")
        
    elif opcion_usuario == "2": #Registrar Medico
        nombre = input ("\nIngrese el nombre: ")
        ano_nacimiento = int(input("Ingrese el año de nacimiento: "))
        rfc = input ("Ingrese el rfc: ")
        direccion = input ("Ingrese la direccion: ")

        medico = Medico(nombre=nombre, ano_nacimiento=ano_nacimiento, rfc=rfc, direccion=direccion)
        hospital.registrar_medico(medico=medico)
        print("\n Medico registrado")

    elif opcion_usuario == "3":
        hospital.mostrar_pacientes()
    
    elif opcion_usuario == "4":
        hospital.mostrar_medicos()

    elif opcion_usuario == "5": #eliminar paciente
        id_paciente = int(input("Ingresa el ID del paciente: "))
        hospital.eliminar_paciente(id_paciente=id_paciente)

    elif opcion_usuario == "6": #eliminar medicos
        id_medico = int(input("Ingresa el ID del medico: "))
        hospital.eliminar_medico(id_medico=id_medico)    

    elif opcion_usuario == "7": #mostrar pacientes menores
        hospital.mostrar_pacientes_menores()
        pass

    elif opcion_usuario == "8": #mostrar pacientes mayores
        hospital.mostrar_pacientes_mayores()
        pass

    elif opcion_usuario == "9":
        print("Que tengas buen dia")
        break
    
   