print("Bienvenido a tu gestor de tareas")

tareas = [None] * 100  
contador = 0
opcion = ""

def agregar_tarea(tareas, contador):
    nombre = input("Nombre de la tarea: ")
    prioridad = input("Prioridad (alta, media, baja): ")
    fecha = input("Fecha límite (dd/mm/yyyy): ")
    if prioridad == "alta" or prioridad == "media" or prioridad == "baja":
        tarea = [nombre, prioridad, fecha, "Pendiente"]
        tareas[contador] = tarea
        print("Tarea agregada.")
        return contador + 1
    else:
        print("Prioridad inválida. Usa alta, media o baja.")
        return contador

def mostrar_todas(tareas, contador):
    if contador == 0:
        print("No hay tareas.")
    else:
        i = 0
        while i < contador:
            tarea = tareas[i]
            print(str(i + 1) + ". " + tarea[0] + " | " + tarea[3] + " | Prioridad: " + tarea[1] + " | Fecha límite: " + tarea[2])
            i += 1

def buscar_tarea(tareas, contador):
    nombre = input("Nombre de la tarea a buscar: ")
    encontrada = False
    i = 0
    while i < contador:
        tarea = tareas[i]
        if tarea[0] == nombre:
            print(tarea[0] + " | " + tarea[3] + " | Prioridad: " + tarea[1] + " | Fecha límite: " + tarea[2])
            encontrada = True
        i += 1
    if not encontrada:
        print("No encontrada.")

def marcar_completada(tareas, contador):
    nombre = input("Nombre de la tarea a marcar como completada: ")
    marcado = False
    i = 0
    while i < contador:
        tarea = tareas[i]
        if tarea[0] == nombre:
            if tarea[3] == "Pendiente":
                tarea[3] = "Completada"
                print("Tarea marcada como completada.")
            else:
                print("La tarea ya está completada.")
            marcado = True
        i += 1
    if not marcado:
        print("No encontrada.")

def eliminar_tarea(tareas, contador):
    nombre = input("Nombre de la tarea a eliminar: ")
    eliminada = False
    i = 0
    while i < contador:
        tarea = tareas[i]
        if tarea[0] == nombre:
            print("Tarea eliminada.")
            j = i
            while j < contador - 1:
                tareas[j] = tareas[j + 1]
                j += 1
            tareas[contador - 1] = None
            contador -= 1
            eliminada = True
            
        else:
            i += 1
    if not eliminada:
        print("No encontrada.")
    return contador

def mostrar_por_prioridad(tareas, contador):
    prioridad = input("Prioridad a mostrar (alta, media, baja): ")
    if prioridad != "alta" and prioridad != "media" and prioridad != "baja":
        print("Prioridad inválida.")
        return
    hay = False
    i = 0
    while i < contador:
        tarea = tareas[i]
        if tarea[1] == prioridad:
            print(tarea[0] + " | " + tarea[3] + " | Prioridad: " + tarea[1] + " | Fecha límite: " + tarea[2])
            hay = True
        i += 1
    if not hay:
        print("No hay tareas con esa prioridad.")

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Agregar tarea")
    print("2. Mostrar todas las tareas")
    print("3. Buscar tarea por nombre")
    print("4. Marcar tarea como completada")
    print("5. Eliminar tarea")
    print("6. Mostrar tareas por prioridad")
    print("7. Mostrar tareas pendientes con fecha límite cercana")
    print("8. Salir")

while opcion != "8":
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        contador = agregar_tarea(tareas, contador)
    elif opcion == "2":
        mostrar_todas(tareas, contador)
    elif opcion == "3":
        buscar_tarea(tareas, contador)
    elif opcion == "4":
        marcar_completada(tareas, contador)
    elif opcion == "5":
        contador = eliminar_tarea(tareas, contador)
    elif opcion == "6":
        mostrar_por_prioridad(tareas, contador)
    elif opcion == "7":
        print("No disponible sin fechas automáticas.")
    elif opcion == "8":
        print("¡Hasta luego!")
    else:
        print("Opción no válida.")
