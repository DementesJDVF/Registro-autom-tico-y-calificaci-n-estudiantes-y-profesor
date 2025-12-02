class Persona:
    def __init__(self, nombre, apellido, identificacion):
        self.nombre = nombre
        self.apellido = apellido
        self.identificacion = identificacion

    def __str__(self):
        return f"{self.nombre} {self.apellido} (ID: {self.identificacion})"