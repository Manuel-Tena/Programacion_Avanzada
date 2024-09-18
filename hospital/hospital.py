class Hospital:
    pacientes = []
    medicos = []
    consultas = []
    

    def registrar_consulta(self, id_paciente, id_medico):
        if not self.validar_cantidad_usuarios():
            return
        
        if not self.validar_existencia_paciente(id_paciente) or not self.validar_existencia_medico(id_medico):
            print("No se puede registrar la consulta, no existe el médico o el paciente")
            return
        
        print("Continuamos con el registro")

    def registrar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def registrar_medico(self, medico):
        self.medicos.append(medico)

    def mostrar_pacientes(self):
        print()  # Línea en blanco para espacio
        print("*** Pacientes en el Sistema ***")
        for paciente in self.pacientes:
            paciente.mostrar_informacion()

    def validar_existencia_paciente(self, id_paciente):
        for paciente in self.pacientes:
            if paciente.id == id_paciente:
                return True
        return False
    
#nuevo edad
    def mostrar_pacientes_menores(self):
        menores = [p for p in self.pacientes if self.calcular_edad(p) < 18]
        if not menores:
            print("No hay pacientes menores de edad en el sistema.")
        else:
            print()  # Línea en blanco para espacio
            print("*** Pacientes Menores de Edad ***")
            for paciente in menores:
                paciente.mostrar_informacion()

    def mostrar_pacientes_mayores(self):                                                #nuevo mayor
        mayores = [p for p in self.pacientes if self.calcular_edad(p) >= 18]
        if not mayores:
            print("No hay pacientes mayores de edad en el sistema.")
        else:
            print()  # Línea en blanco para espacio
            print("*** Pacientes Mayores de Edad ***")
            for paciente in mayores:
                paciente.mostrar_informacion()

    def calcular_edad(self, paciente):
        from datetime import datetime #para mostrar la edad
        anio_actual = datetime.now().year
        return anio_actual - paciente.ano_nacimiento
    
    #Medicos 
    def validar_existencia_medico(self, id_medico): #nuevo
        for medico in self.medicos:
            if medico.id == id_medico:
                return True
        return False
        
    def validar_cantidad_usuarios(self):
        if len(self.pacientes) == 0:
            print("No puedes registrar una consulta, no existen pacientes")
            return False
        
        if len(self.medicos) == 0:              #nuevo
            print("No puedes registrar una consulta, no existen médicos")
            return False
        
        return True
    
    def mostrar_medicos(self):
        if not self.medicos:
            print("No hay médicos registrados en el sistema.")
        else:
            print()  # Línea en blanco para espacio
            print("*** Médicos Registrados ***")                #nuevo
            for medico in self.medicos:
                print(f"\nId: {medico.id}")
                print(f"Nombre: {medico.nombre}")
                print(f"Año de nacimiento: {medico.ano_nacimiento}")
                print(f"RFC: {medico.rfc}")
                print(f"Dirección: {medico.direccion}")

#Eliminar pacientes
    def eliminar_paciente(self, id_paciente):
        paciente_a_eliminar = None
        for paciente in self.pacientes:
            if paciente.id == id_paciente:
                paciente_a_eliminar = paciente
                break
        
        if paciente_a_eliminar:
            self.pacientes.remove(paciente_a_eliminar)
            print()  # Línea en blanco para espacio
            print(f"Paciente con la ID {id_paciente} ha se elimino xd.")
        else:
            print(f"No se encontró un paciente con ID {id_paciente} xd.")

#Eliminar medicos
    def eliminar_medico(self, id_medico):
        medico_a_eliminar = None
        for medico in self.medicos:
            if medico.id == id_medico:
                medico_a_eliminar = medico
                break
        
        if medico_a_eliminar:
            self.medicos.remove(medico_a_eliminar)
            print()  # Línea en blanco para espacio
            print(f"Médico con ID {id_medico} se ha sido eliminado.")
        else:
            print()  # Línea en blanco para espacio
            print(f"No se existe un médico con ID {id_medico}.")


   

