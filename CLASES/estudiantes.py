from CLASES.persona import Persona
class Estudiante(Persona):
    def __init__(self, nombre, apellido, identificacion):
        super().__init__(nombre, apellido, identificacion)
        self.notas = {}  # {codigo_asignatura: [notas]}

    def agregarNota(self, codigoAsignatura, nota):
        if codigoAsignatura not in self.notas:
            self.notas[codigoAsignatura] = []
        self.notas[codigoAsignatura].append(nota)

    def obtenerPromedio(self, codigoAsignatura):
        if codigoAsignatura in self.notas and self.notas[codigoAsignatura]:
            return sum(self.notas[codigoAsignatura]) / len(self.notas[codigoAsignatura])
        return None

    def estado(self, codigoAsignatura, notaMinima=3):
        prom = self.obtenerPromedio(codigoAsignatura)
        if prom is None:
            return "Sin notas"
        return "Aprobado" if prom >= notaMinima else "Reprobado"