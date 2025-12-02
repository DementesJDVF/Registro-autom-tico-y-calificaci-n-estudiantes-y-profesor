from CLASES.estudiantes import Estudiante
from CLASES.profesores import Profesor
from CLASES.asignaturas import Asignatura

estudiantes = []
profesores = []
asignaturas = []

def buscarEstudiante(identificacion):
    for e in estudiantes:
        if e.identificacion == identificacion:
            return e
    return None

def buscarProfesor(identificacion):
    for p in profesores:
        if p.identificacion == identificacion:
            return p
    return None

def buscarAsignatura(codigo):
    for a in asignaturas:
        if a.codigo == codigo:
            return a
    return None

