from CLASES.estudiantes import Estudiante
from CLASES.profesores import Profesor
from CLASES.asignaturas import Asignatura

# === ALMACENAMIENTO GLOBAL (SIMULACIÓN EN MEMORIA) ===
estudiantes = []
profesores = []
asignaturas = []

# === FUNCIONES DE BÚSQUEDA ===
def buscarEstudiante(identificacion):
    #"""Busca un estudiante por su identificación y lo devuelve si existe."""
    for e in estudiantes:
        if e.identificacion == identificacion:
            return e
    return None

def buscarProfesor(identificacion):
    #"""Busca un profesor por su identificación y lo devuelve si existe."""
    for p in profesores:
        if p.identificacion == identificacion:
            return p
    return None

def buscarAsignatura(codigo):
    #"""Busca una asignatura por su código y la devuelve si existe."""
    for a in asignaturas:
        if a.codigo == codigo:
            return a
    return None

# === MENÚ PRINCIPAL ===
while True:
    print("\nMenu Principal")
    print("\n1. Registrar Estudiantes\n2. Registrar Profesor\n3. Crear asignatura\n4. Ingresar notas\n5. Ver promedio y estado de un estudiante\n6. Lista estudiantes\n7. Lista asignaturas\n0. Salir")
    opcion = input("\nSeleccione una opcion: ").strip()

    match opcion:
        # === CASO 1: REGISTRAR N ESTUDIANTES ===
        case "1":
            try:
                n = int(input("¿Cuantos estudiantes desea registrar? ").strip())
                if n <= 0:
                    print("El numero debe ser mayor que cero.")
                    continue
            except ValueError:
                print("Ingrese un numero valido.")
                continue
            creados = 0

            for i in range(n):
                print(f"\nEstudiante {i+1}")
                nombre = input("Nombre: ").strip()
                apellido = input("Apellido: ").strip()
                identificacion = input("Identificacion: ").strip()
                # --> Validar que no falten datos
                if not nombre or not apellido or not identificacion:
                    print(" Datos incompletos. Se omite este estudiante.")
                    continue
                # --> Evitar duplicados
                if buscarEstudiante(identificacion):
                    print(f"Ya existe un estudiante con ID {identificacion}. Se omitira.")
                    continue
                # --> Crear y registrar estudiante
                nuevoEstudiante = Estudiante(nombre, apellido, identificacion)
                estudiantes.append(nuevoEstudiante)
                # --> Vincular automáticamente a todas las asignaturas existentes
                for asignatura in asignaturas:
                    asignatura.inscribirEstudiante(nuevoEstudiante)
                creados += 1
                print(f"{nuevoEstudiante.nombre} registrado e inscrito en {len(asignaturas)} asignaturas.")
            print(f"\n¡{creados} de {n} estudiante(s) registrado(s) con exito!")

        # === CASO 2: REGISTRAR PROFESOR ===
        case "2":
            nombre = input("Nombre del profesor: ").strip()
            apellido = input("Apellido: ").strip()
            identificacion = input("Identificacion: ").strip()
            if not nombre or not apellido or not identificacion:
                print("Datos incompletos.")
                continue
            if buscarProfesor(identificacion):
                print("Ya existe un profesor con esa identificación.")
            else:
                profesores.append(Profesor(nombre, apellido, identificacion))
                print("Profesor registrado con exito.")

        # === CASO 3: CREAR ASIGNATURA Y ASIGNAR PROFESOR ===
        case "3":
            nombre = input("Nombre de la asignatura: ").strip()
            codigo = input("Código de la asignatura: ").strip()
            if not nombre or not codigo:
                print("Nombre o código invalidos.")
                continue
            if buscarAsignatura(codigo):
                print("Ya existe una asignatura con ese codigo.")
                continue
            idProfesor = input("Identificacion del profesor: ").strip()
            profesor = buscarProfesor(idProfesor)
            if not profesor:
                print("Profesor no encontrado. La asignatura no se creara.")
                continue
            # --> Crear asignatura con profesor asignado
            nuevaAsignatura = Asignatura(nombre, codigo, profesor=profesor)
            # --> Registrar que el profesor dicta esta asignatura
            profesor.agregarAsignatura(codigo)
            asignaturas.append(nuevaAsignatura)
            # --> Vincular automáticamente a todos los estudiantes existentes
            for estudiante in estudiantes:
                nuevaAsignatura.inscribirEstudiante(estudiante)
            print(f"Asignatura '{nombre}' creada con exito.")
            print(f"Profesor asignado: {profesor.nombre} {profesor.apellido}")
            print(f"Estudiantes inscritos automaticamente: {len(estudiantes)}")

        # === CASO 4: INGRESAR NOTAS (ESCALA 0-5) ===
        case "4":
            codigoAsignatura = input("Codigo de la asignatura: ").strip()
            asignatura = buscarAsignatura(codigoAsignatura)
            # --> Validar que la asignatura exista y tenga profesor
            if not asignatura or not asignatura.profesor:
                print("Asignatura no existe o no tiene profesor asignado.")
                continue
            idEstudiante = input("Identificación del estudiante: ").strip()
            estudiante = buscarEstudiante(idEstudiante)
            # --> Validar que el estudiante exista y esté inscrito
            if not estudiante or estudiante not in asignatura.estudiantes:
                print("Estudiante no encontrado o no inscrito en esta asignatura.")
                continue
            try:
                nota = float(input("Ingrese la nota (0-5): "))
                if 0 <= nota <= 5:
                    estudiante.agregarNota(codigoAsignatura, nota)
                    print("Nota registrada con exito.")
                else:
                    print("La nota debe estar entre 0 y 5.")
            except ValueError:
                print("Por favor, ingrese una nota válida.")

        # === CASO 5: CONSULTAR PROMEDIO Y ESTADO (APROBADO/REPROBADO) ===
        case "5":
            idEstudiante = input("Identificación del estudiante: ").strip()
            estudiante = buscarEstudiante(idEstudiante)
            if not estudiante:
                print("Estudiante no encontrado.")
                continue
            codigoAsignatura = input("Codigo de la asignatura: ").strip()
            promedio = estudiante.obtenerPromedio(codigoAsignatura)
            if promedio is None:
                print("El estudiante no tiene notas en esa asignatura.")
            else:
                estado = estudiante.estado(codigoAsignatura)  # Umbral: 3.0 (escala 0-5)
                print(f"\nEstudiante: {estudiante}")
                print(f"Asignatura: {codigoAsignatura}")
                print(f"Promedio: {promedio:.2f}")
                print(f"Estado: {estado}")

        # === CASO 6: LISTAR ESTUDIANTES ===
        case "6":
            if not estudiantes:
                print("No hay estudiantes registrados.")
            else:
                print("\nLista de estudiantes:")
                for estudiante in estudiantes:  # --> Corregido: variable "estudiante", no "eestudiante"
                    print(f"Nombre: {estudiante.nombre} Apellido: {estudiante.apellido} (ID: {estudiante.identificacion})")

        # === CASO 7: LISTAR ASIGNATURAS ===
        case "7":
            if not asignaturas:
                print("No hay asignaturas creadas.")
            else:
                print("\nLista de asignaturas:")
                for asignatura in asignaturas:
                    # --> Manejar caso en que el profesor sea None (aunque no debería pasar)
                    if asignatura.profesor:
                        prof_nombre = f"{asignatura.profesor.nombre} {asignatura.profesor.apellido}"
                    else:
                        prof_nombre = "Sin asignar"
                    print(f"Nombre: {asignatura.nombre} | Código: {asignatura.codigo} | Profesor: {prof_nombre}")

        # === CASO 0: SALIR ===
        case "0":
            print("\nHasta pronto!")
            break

        # === CASO POR DEFECTO ===
        case _:
            print("Opcion no válida.")