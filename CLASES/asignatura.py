class Asignatura:
    def __init__(self, nombre, codigo, profesor=None):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        self.estudiantes = []
