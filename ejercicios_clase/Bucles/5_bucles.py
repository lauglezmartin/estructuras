# Bucle for con enumerate()
# Enunciado: Tienes una lista de tareas pendientes: ["Comprar leche", "Llamar al médico",
# "Estudiar Python"]. Imprímelas numeradas empezando desde el 1 para mostrarlas como una
# lista ordenada. 

# Definimos la lista de tareas originales
tareas = ["Comprar leche", "Llamar al médico", "Estudiar Python"]

# Usamos enumerate con start=1 para obtener una numeración automática que empiece en 1
for index, tarea in enumerate(tareas, start=1):
    # Imprimimos el índice y la tarea de forma ordenada
    print(f"{index}. {tarea}")