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

while True:
    print("\nMenú Principal")
    print("\n1. Registrar Estudiantes\n2. Registrar Profesor\n3. Crear asignatur\n4. Ingresar notas\n5. Ver promedio y estado de un estudiante\n6. Lista estudiantes\n7. Lista asignaturas\n0. Salir")
    opcion = input("\nSeleccione una opción: ").strip()

    match opcion:
        case "1":
            break  # Código para registrar estudiantes
        case "2":
            break  # Código para registrar profesores
        case "3":
            break  # Código para crear asignaturas
        case "4":
            break  # Código para ingresar notas
        case "5":
            break  # Código para ver promedio y estado de un estudiante
        case "6":
            break  # Código para listar estudiantes
        case "7":
            break  # Código para listar asignaturas
        case "0":
            break  # Salir del programa