def agregar_tarea(tareas, tarea):
    tareas.append(tarea)
    print("Tarea agregada con éxito.")

def eliminar_tarea(tareas, tarea):
    if tarea in tareas:
        tareas.remove(tarea)
        print("Tarea eliminada con éxito.")
    else:
        print("La tarea especificada no existe en la lista.")

def mostrar_tareas(tareas):
    if tareas:
        print("Tareas pendientes:")
        for idx, tarea in enumerate(tareas, start=1):
            print(f"{idx}. {tarea}")
    else:
        print("No hay tareas pendientes.")

tareas_pendientes = []

while True:
    print("\n--- Lista de Tareas Pendientes ---")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Mostrar tareas")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nueva_tarea = input("Ingrese la nueva tarea: ")
        agregar_tarea(tareas_pendientes, nueva_tarea)
    elif opcion == "2":
        tarea_eliminar = input("Ingrese la tarea a eliminar: ")
        eliminar_tarea(tareas_pendientes, tarea_eliminar)
    elif opcion == "3":
        mostrar_tareas(tareas_pendientes)
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
