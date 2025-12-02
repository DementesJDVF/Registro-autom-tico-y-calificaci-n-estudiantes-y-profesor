from CLASES.persona import Persona
class Estudiante(Persona):
    def __init__(self, nombre, apellido, identificacion):
        super().__init__(nombre, apellido, identificacion)
        self.notas = {}  # {codigo_asignatura: [notas]}

    def agregar_nota(self, codigo_asignatura, nota):
        if codigo_asignatura not in self.notas:
            self.notas[codigo_asignatura] = []
        self.notas[codigo_asignatura].append(nota)

    def obtener_promedio(self, codigo_asignatura):
        if codigo_asignatura in self.notas and self.notas[codigo_asignatura]:
            return sum(self.notas[codigo_asignatura]) / len(self.notas[codigo_asignatura])
        return None

    def estado(self, codigo_asignatura, nota_minima=60):
        prom = self.obtener_promedio(codigo_asignatura)
        if prom is None:
            return "Sin notas"
        return "Aprobado" if prom >= nota_minima else "Reprobado"