# Pedir al usuario que ingrese la fecha actual en formato "día, DD/MM"
fecha_actual = input("Ingrese la fecha actual en formato 'día, DD/MM': ").strip().lower()

# Dividir la entrada en día y fecha
dia_semana, fecha = fecha_actual.split(", ")
dia, mes = fecha.split("/")

# Listas para asociar los días de la semana con los niveles de clases
dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes"]
niveles_clases = ["nivel inicial", "nivel intermedio", "nivel avanzado", "práctica hablada", "inglés para viajeros"]

# Verificar si el día de la semana es válido
if dia_semana not in dias_semana:
    print("Error: Día de la semana no válido.")
else:
    indice_dia = dias_semana.index(dia_semana)
    nivel_clase = niveles_clases[indice_dia]

    # Procesar según el nivel de clase
    if nivel_clase in ["nivel inicial", "nivel intermedio", "nivel avanzado"]:
        # Preguntar si hubo exámenes
        hubo_examenes = input("¿Hubo exámenes? (Sí/No): ").strip().lower()

        if hubo_examenes == "sí":
            aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
            no_aprobados = int(input("Ingrese la cantidad de alumnos no aprobados: "))
            porcentaje_aprobados = (aprobados / (aprobados + no_aprobados)) * 100
            print(f"El porcentaje de aprobados fue: {porcentaje_aprobados}%")

    elif nivel_clase == "práctica hablada":
        # Preguntar por el porcentaje de asistencia
        porcentaje_asistencia = float(input("Ingrese el porcentaje de asistencia a clase: "))
        if porcentaje_asistencia > 50:
            print("Asistió la mayoría.")
        else:
            print("No asistió la mayoría.")

    elif nivel_clase == "inglés para viajeros":
        # Verificar si es el comienzo de un nuevo ciclo
        if (mes == "01" and dia == "01") or (mes == "07" and dia == "01"):
            print("Comienzo de nuevo ciclo")
            cantidad_alumnos = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
            arancel_por_alumno = float(input("Ingrese el arancel en $ por cada alumno: "))
            ingreso_total = cantidad_alumnos * arancel_por_alumno
            print(f"Ingreso total en $: {ingreso_total}")
