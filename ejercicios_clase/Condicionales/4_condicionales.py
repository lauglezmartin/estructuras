# Ejercicio 4: Manejador de Respuestas HTTP con match-case
# Conceptos aplicados: Estructura match-case (Python 3.10+), patrones literales, patrones agrupados (|), comodín por defecto.

# Enunciado:
# Diseña un controlador de API REST que 
# reciba un código de estado HTTP entero (por ejemplo: 200, 201, 400, 401, 403, 404, 500, 503) y devuelva una categoría estándar.

# Requisitos:
# Usa una estructura match-case.
# Agrupa en una sola rama (case 200 | 201:) las respuestas exitosas.
# Agrupa en una sola rama los errores de cliente conocidos (400, 401, 403, 404).
# Agrupa en una rama los errores de servidor (500, 503).
# Usa el comodín “_” para capturar cualquier otro código no contemplado e informar de "Código de estado no reconocido".


# Solicito el código por teclado y lo convierto a entero (int)
# Uso int() porque input() siempre devuelve texto y los códigos son números.
entrada = input("Introduce un código de estado HTTP (ej. 200, 404, 500): ")
codigo_http = int(entrada)


# Estructura match-case: evalúa el valor de la variable de forma limpia y permite agrupar múltiples casos en una sola rama.
match codigo_http:
    
    # Patrón agrupado (|): si es 200 ó 201, se considera una respuesta exitosa
    case 200 | 201:
        print("Éxito: La solicitud se ha completado correctamente.")
        
    # Patrón agrupado para errores de cliente (solicitudes incorrectas, no autorizado, prohibido o no encontrado)
    case 400 | 401 | 403 | 404:
        print("Error del cliente: Revise los datos o permisos enviados.")
        
    # Patrón agrupado para errores internos o servicio no disponible en el servidor
    case 500 | 503:
        print("Error del servidor: Hubo un fallo en el sistema remoto.")
        
    # Comodín (_): Funciona como un 'else' por defecto para cualquier otro código numérico no previsto
    case _:
        print("Código de estado no reconocido.")