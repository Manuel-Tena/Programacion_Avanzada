class Curso:
    id= 0
    nombre_curso = ""
    codigo_curso = ""
    instructor = ""

    def __init__(self, id, nombre_curso, codigo_curso, instructor):
        self.id = id
        self.nombre_curso = nombre_curso
        self.codigo_curso = codigo_curso
        self.instructor = instructor

    def mostrar_info_curso(self):
        print("\n Nombre del curso: ", self.nombre_curso)
        print("\n Codigo del curso: ", self.codigo_curso)
        print("\n Instructor: ", self.instructor)
        print("\n ------------------------------------ \n")