print("Bienvenido a tu gestor de tareas")

tareas = []
opcion = ""

def agregar_tarea(tareas):
    nombre = input("Nombre de la tarea: ")
    prioridad = input("Prioridad (alta, media, baja): ")
    fecha = input("Fecha límite (dd/mm/yyyy): ")
    tarea = [nombre, prioridad, fecha, "Pendiente"]
    tareas.append(tarea)
    print("Tarea agregada.")

def mostrar_todas(tareas):
    if len(tareas) == 0:
        print("No hay tareas.")
    else:
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea[0]} | {tarea[3]} | Prioridad: {tarea[1]} | Fecha límite: {tarea[2]}")

def buscar_tarea(tareas):
    nombre = input("Nombre de la tarea a buscar: ")
    encontrada = False
    for tarea in tareas:
        if tarea[0] == nombre:
            print(f"{tarea[0]} | {tarea[3]} | Prioridad: {tarea[1]} | Fecha límite: {tarea[2]}")
            encontrada = True
    if not encontrada:
        print("No encontrada.")

def marcar_completada(tareas):
    nombre = input("Nombre de la tarea a marcar como completada: ")
    marcado = False
    for tarea in tareas:
        if tarea[0] == nombre:
            tarea[3] = "Completada"
            print("Tarea marcada como completada.")
            marcado = True
    if not marcado:
        print("No encontrada.")

def eliminar_tarea(tareas):
    nombre = input("Nombre de la tarea a eliminar: ")
    nueva_lista = []
    eliminada = False
    for tarea in tareas:
        if tarea[0] == nombre:
            print("Tarea eliminada.")
            eliminada = True
        else:
            nueva_lista.append(tarea)
    tareas[:] = nueva_lista
    if not eliminada:
        print("No encontrada.")

def mostrar_por_prioridad(tareas):
    prioridad = input("Prioridad a mostrar (alta, media, baja): ")
    hay = False
    for tarea in tareas:
        if tarea[1] == prioridad:
            print(f"{tarea[0]} | {tarea[3]} | Prioridad: {tarea[1]} | Fecha límite: {tarea[2]}")
            hay = True
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

print("Bienvenido a tu gestor de tareas")
tareas = []
opcion = ""

while opcion != "8":
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_tarea(tareas)
    elif opcion == "2":
        mostrar_todas(tareas)
    elif opcion == "3":
        buscar_tarea(tareas)
    elif opcion == "4":
        marcar_completada(tareas)
    elif opcion == "5":
        eliminar_tarea(tareas)
    elif opcion == "6":
        mostrar_por_prioridad(tareas)
    elif opcion == "7":
        print("No disponible sin fechas automáticas.")
    elif opcion == "8":
        print("¡Hasta luego!")
    else:
        print("Opción no válida.")
