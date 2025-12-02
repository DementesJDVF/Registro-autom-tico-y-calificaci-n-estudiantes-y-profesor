from CLASES.persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, apellido, identificacion):
        super().__init__(nombre, apellido, identificacion)
        self.asignaturas = []  # códigos de asignaturas que imparte

    def agregarAsignatura(self, codigoAsignatura):
        """Agrega una asignatura si no está ya asignada."""
        if codigoAsignatura not in self.asignaturas:
            self.asignaturas.append(codigoAsignatura)
        else:
            print(f"El profesor {self.nombre} ya imparte la asignatura {codigoAsignatura}.")