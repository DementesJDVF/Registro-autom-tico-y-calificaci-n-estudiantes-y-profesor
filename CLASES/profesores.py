from CLASES.persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, apellido, identificacion):
        super().__init__(nombre, apellido, identificacion)
        self.asignaturas = []  # códigos de asignaturas que imparte
