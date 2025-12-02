from CLASES.persona import Persona
class Estudiante(Persona):
    def __init__(self, nombre, apellido, identificacion):
        super().__init__(nombre, apellido, identificacion)
        self.notas = {}  # {codigo_asignatura: [notas]}

