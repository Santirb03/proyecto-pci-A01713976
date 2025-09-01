print("Bienvenido a tu gestor de tareas")

tareas = []
opcion = ""

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
        nombre = input("Nombre de la tarea: ")
        prioridad = input("Prioridad (alta, media, baja): ")
        fecha = input("Fecha límite (dd/mm/yyyy): ")
        tarea = [nombre, prioridad, fecha, "Pendiente"]
        tareas.append(tarea)
        print("Tarea agregada.")

    elif opcion == "2":
        if len(tareas) == 0:
            print("No hay tareas.")
        else:
            num = 1
            for tarea in tareas:
                print(str(num) + ". " + tarea[0] + " | " + tarea[3] + " | Prioridad: " + tarea[1] + " | Fecha límite: " + tarea[2])
                num = num + 1

    elif opcion == "3":
        nombre = input("Nombre de la tarea a buscar: ")
        encontrada = False
        for tarea in tareas:
            if tarea[0] == nombre:
                print(tarea[0] + " | " + tarea[3] + " | Prioridad: " + tarea[1] + " | Fecha límite: " + tarea[2])
                encontrada = True
        if not encontrada:
            print("No encontrada.")

    elif opcion == "4":
        nombre = input("Nombre de la tarea a marcar como completada: ")
        marcado = False
        for tarea in tareas:
            if tarea[0] == nombre:
                tarea[3] = "Completada"
                print("Tarea marcada como completada.")
                marcado = True
        if not marcado:
            print("No encontrada.")

    elif opcion == "5":
        nombre = input("Nombre de la tarea a eliminar: ")
        nueva_lista = []
        eliminada = False
        for tarea in tareas:
            if tarea[0] == nombre:
                print("Tarea eliminada.")
                eliminada = True
            else:
                nueva_lista.append(tarea)
        tareas = nueva_lista
        if not eliminada:
            print("No encontrada.")

    elif opcion == "6":
        prioridad = input("Prioridad a mostrar (alta, media, baja): ")
        hay = False
        for tarea in tareas:
            if tarea[1] == prioridad:
                print(tarea[0] + " | " + tarea[3] + " | Prioridad: " + tarea[1] + " | Fecha límite: " + tarea[2])
                hay = True
        if not hay:
            print("No hay tareas con esa prioridad.")

    elif opcion == "7":
        print("No disponible sin fechas automáticas.")

    elif opcion == "8":
        print("¡Hasta luego!")

    else:
        print("Opción no válida.")
