# proyecto-pci-A01713976
Proyecto pci santiago rodrigurez

Contexto:
En nuesto dia a dia es fácil olvidar tareas importantes, especialmente para estudiantes que tenemos múltiples actividades. 
Este proyecto busca craer un sistema sencillo donde el usuario pueda registrar, consultar y marcar tareas como completadas. 

Algoritmo:
Inicio
    Crear lista vacía de tareas
    Cada tarea tendrá:
        - Nombre
        - Estado (pendiente / completada)
        - Prioridad (alta, media, baja)
        - Fecha límite (opcional)

    Mostrar menú con opciones:
        1. Agregar tarea
        2. Mostrar todas las tareas
        3. Buscar tarea por nombre
        4. Marcar tarea como completada
        5. Eliminar tarea
        6. Mostrar tareas por prioridad
        7. Mostrar tareas pendientes con fecha límite cercana
        8. Salir

    Mientras el usuario no seleccione "Salir":
        Leer opción elegida

        Si opción = 1:
            Solicitar nombre, prioridad y fecha límite
            Crear tarea y agregarla a la lista

        Si opción = 2:
            Mostrar todas las tareas con sus propiedades (nombre, estado, prioridad, fecha)

        Si opción = 3:
            Solicitar nombre de tarea
            Buscar en la lista
            Si se encuentra:
                Mostrar detalles de la tarea
            Sino:
                Mostrar mensaje "No encontrada"

        Si opción = 4:
            Solicitar número o nombre de tarea
            Cambiar estado de "pendiente" a "completada"

        Si opción = 5:
            Solicitar número o nombre de tarea
            Eliminar de la lista

        Si opción = 6:
            Solicitar nivel de prioridad (alta, media, baja)
            Mostrar solo las tareas con esa prioridad

        Si opción = 7:
            Revisar todas las tareas
            Mostrar las que tengan fecha límite cercana (ejemplo: dentro de 3 días)

        Si opción = 8:
            Terminar programa

Fin

