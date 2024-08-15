# HAY 1 ERROR INTENCIONAL, PUESTO PARA PROBAR EL PYTEST Y SU FUNCIONAMIENTO
# EN EL ERROR DE LA LINEA 35 POR FAVOR DESCOMENTAR PARA QUE EL TEST VERIQUE 
# UNA VEZ VERIFICADO EL ERROR VOLVER A COMENTAR POR FAVOR



class Tarea:
    def __init__(self, id_tarea, descripcion, prioridad):
        self.id_tarea = id_tarea
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.completada = False

def agregar_tarea(tareas, id_tarea, descripcion, prioridad):
    """Agrega una nueva tarea al sistema."""
    if id_tarea in tareas:
        raise ValueError(f"Una tarea con ID '{id_tarea}' ya existe.")
    tareas[id_tarea] = Tarea(id_tarea, descripcion, prioridad)


def actualizar_tarea(tareas, id_tarea, nueva_descripcion, nueva_prioridad):
    """Actualiza la descripción y prioridad de una tarea existente."""
    if id_tarea not in tareas:
        raise KeyError(f"Tarea con ID '{id_tarea}' no existe.")
    tarea = tareas[id_tarea]
    tarea.descripcion = nueva_descripcion
    tarea.prioridad = nueva_prioridad

def marcar_completada(tareas, id_tarea):
    """Marca una tarea como completada."""
    if id_tarea not in tareas:
        raise KeyError(f"Tarea con ID '{id_tarea}' no existe.")
    tareas[id_tarea].completada = True
    ######3# Error intencional: Marcado incorrecto de completada (comentado)#######
    #tareas[id_tarea].completada = False

def eliminar_tarea(tareas, id_tarea):
    """Elimina una tarea del sistema."""
    if id_tarea not in tareas:
        raise KeyError(f"Tarea con ID '{id_tarea}' no existe.")
    del tareas[id_tarea]

def listar_tareas(tareas, completadas=False):
    """Lista las tareas pendientes o completadas."""
    for tarea in tareas.values():
        if tarea.completada == completadas:
            estado = "Completada" if tarea.completada else "Pendiente"
            print(f"ID: {tarea.id_tarea}, Descripción: {tarea.descripcion}, Prioridad: {tarea.prioridad}, Estado: {estado}")

def main():
    tareas = {}

    while True:
        print("\n1. AGREGAR TAREA")
        print("2. ACTUALIZAR TAREA")
        print("3. MARCAR TAREA COMO COMPLETADA")
        print("4. ELIMINAR TAREA")
        print("5. LISTAR TAREAS PENDIENTES")
        print("6. LISTAR TAREAS COMPLETADAS")
        print("7. SALIR")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_tarea = input("Ingrese el ID de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea: ")
            prioridad = input("Ingrese la prioridad de la tarea: ")
            try:
                agregar_tarea(tareas, id_tarea, descripcion, prioridad)
                print("Tarea agregada correctamente.")
            except ValueError as e:
                print(e)

        elif opcion == '2':
            id_tarea = input("Ingrese el ID de la tarea que desea actualizar: ")
            nueva_descripcion = input("Ingrese la nueva descripción: ")
            nueva_prioridad = input("Ingrese la nueva prioridad: ")
            try:
                actualizar_tarea(tareas, id_tarea, nueva_descripcion, nueva_prioridad)
                print("Tarea actualizada correctamente.")
            except KeyError as e:
                print(e)

        elif opcion == '3':
            id_tarea = input("Ingrese el ID de la tarea que desea marcar como completada: ")
            try:
                marcar_completada(tareas, id_tarea)
                print("Tarea marcada como completada.")
            except KeyError as e:
                print(e)

        elif opcion == '4':
            id_tarea = input("Ingrese el ID de la tarea que desea eliminar: ")
            try:
                eliminar_tarea(tareas, id_tarea)
                print("Tarea eliminada correctamente.")
            except KeyError as e:
                print(e)

        elif opcion == '5':
            print("\nTareas Pendientes:")
            listar_tareas(tareas, completadas=False)

        elif opcion == '6':
            print("\nTareas Completadas:")
            listar_tareas(tareas, completadas=True)

        elif opcion == '7':
            print("Usted salió del programa.")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
