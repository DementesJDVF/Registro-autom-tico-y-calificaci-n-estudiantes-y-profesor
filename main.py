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
    print("\n1. Registrar Estudiantes\n2. Registrar Profesor\n3. Crear asignatura\n4. Ingresar notas\n5. Ver promedio y estado de un estudiante\n6. Lista estudiantes\n7. Lista asignaturas\n0. Salir")
    opcion = input("\nSeleccione una opción: ").strip()

    match opcion:
        case "1":
            try:
                n = int(input("¿Cuántos estudiantes desea registrar? ").strip())
                if n <= 0:
                    print("El número debe ser mayor que cero.")
                    continue
            except ValueError:
                print("Por favor, ingrese un número válido.")
                continue
            creados = 0
            for i in range(n):
                print(f"\n--- Estudiante #{i+1} ---")
                nombre = input("Nombre: ").strip()
                apellido = input("Apellido: ").strip()
                identificacion = input("Identificación: ").strip()
                if not nombre or not apellido or not identificacion:
                    print(" Datos incompletos. Se omitirá este estudiante.")
                    continue
                if buscarEstudiante(identificacion):
                    print(f"Ya existe un estudiante con ID {identificacion}. Se omitirá.")
                    continue
                nuevoEstudiante = Estudiante(nombre, apellido, identificacion)
                estudiantes.append(nuevoEstudiante)
                for asignatura in asignaturas:
                    asignatura.inscribirEstudiante(nuevoEstudiante)
                creados += 1
                print(f"{nuevoEstudiante.nombre} registrado e inscrito en {len(asignaturas)} asignaturas.")
            print(f"\n¡{creados} de {n} estudiante(s) registrado(s) con éxito!")
        case "2":
            nombre = input("Nombre del profesor: ").strip()
            apellido = input("Apellido: ").strip()
            identificacion = input("Identificación: ").strip()
            if not nombre or not apellido or not identificacion:
                print("Datos incompletos.")
                continue
            if buscarProfesor(identificacion):
                print("Ya existe un profesor con esa identificación.")
            else:
                profesores.append(Profesor(nombre, apellido, identificacion))
                print("Profesor registrado con éxito.")
        case "3":
            nombre = input("Nombre de la asignatura: ").strip()
            codigo = input("Código de la asignatura: ").strip()
            if not nombre or not codigo:
                print("Nombre o código inválidos.")
                continue
            if buscarAsignatura(codigo):
                print("Ya existe una asignatura con ese código.")
                continue
            idProfesor = input("Identificación del profesor que la impartirá: ").strip()
            profesor = buscarProfesor(idProfesor)
            if not profesor:
                print("Profesor no encontrado. La asignatura no se creará.")
                continue
            nuevaAsignatura = Asignatura(nombre, codigo, profesor=profesor)
            profesor.agregarAsignatura(codigo)
            asignaturas.append(nuevaAsignatura)
            for estudiante in estudiantes:
                nuevaAsignatura.inscribirEstudiante(estudiante)
            print(f"Asignatura '{nombre}' creada con éxito.")
            print(f"Profesor asignado: {profesor.nombre} {profesor.apellido}")
            print(f"Estudiantes inscritos automáticamente: {len(estudiantes)}")
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

        