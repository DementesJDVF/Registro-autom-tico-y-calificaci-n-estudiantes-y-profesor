class Asignatura:
    def __init__(self, nombre, codigo, profesor=None):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        self.estudiantes = []  # lista de objetos Estudiante

    def inscribirEstudiante(self, estudiante):
        if estudiante not in self.estudiantes:
            self.estudiantes.append(estudiante)

    def __str__(self):
        prof = self.profesor.nombre if self.profesor else "Sin asignar"
        return f"{self.nombre} ({self.codigo}) - Profesor: {prof}"
    
    