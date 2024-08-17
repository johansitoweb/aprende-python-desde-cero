def cargar_tareas():
    try:
        with open("tareas.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def guardar_tareas(tareas):
    with open("tareas.txt", "w") as file:
        for tarea in tareas:
            file.write(tarea + "\n")

def agregar_tarea(tareas, tarea):
    tareas.append(tarea)
    print(f"Tarea '{tarea}' agregada.")

def mostrar_tareas(tareas):
    print("Lista de Tareas:")
    for tarea in tareas:
        print(f"- {tarea}")

def main():
    tareas = cargar_tareas()
    while True:
        tarea = input("Ingresa una tarea (o 'salir' para terminar): ")
        if tarea.lower() == 'salir':
            break
        agregar_tarea(tareas, tarea)
        mostrar_tareas(tareas)
        guardar_tareas(tareas)

main()
