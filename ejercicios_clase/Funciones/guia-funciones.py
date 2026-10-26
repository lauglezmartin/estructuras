"""
=============================================================================
MASTER CLASS DE PYTHON: GUÍA DEFINITIVA DE FUNCIONES
Estructura, sintaxis, parámetros avanzados, ámbitos y errores comunes.
=============================================================================
"""

# =============================================================================
# SECCIÓN 1: ¿QUÉ ES UNA FUNCIÓN Y SU SINTAXIS BÁSICA?
# =============================================================================
# Las funciones son bloques de código reutilizables que realizan una tarea 
# específica, permitiendo organizar el código y evitar repeticiones[cite: 1].

print("--- 1. SINTAXIS BÁSICA ---")

def saludar():
    """Función simple que imprime un saludo en pantalla[cite: 1]."""
    print("¡Hola, mundo!")

# Llamada obligatoria a la función usando paréntesis ()
# Si omites los paréntesis, Python devuelve la referencia del objeto en memoria.
saludar()  # Salida: ¡Hola, mundo![cite: 1]
print()


# =============================================================================
# SECCIÓN 2: ANATOMÍA DE UNA FUNCIÓN
# =============================================================================
# Una función estándar se compone de: 'def', nombre en snake_case, parámetros, 
# un Docstring opcional, el cuerpo indentado y la sentencia 'return'[cite: 1].

print("=== 2. ANATOMÍA DE UNA FUNCIÓN ===")

def nombre_funcion(parametro1, parametro2):
    """
    Docstring explicativo: describe el propósito de la función.
    Aquí realizamos una operación lógica básica con los parámetros de entrada[cite: 1].
    """
    resultado = parametro1 + parametro2
    return resultado  # Devuelve el resultado calculado hacia el programa principal[cite: 1]

print("Resultado de anatomía (5 + 3):", nombre_funcion(5, 3))
print()


# =============================================================================
# SECCIÓN 3: EL SISTEMA DE ENTRADAS (PARÁMETROS Y ARGUMENTOS)
# =============================================================================
# Los parámetros permiten que las funciones reciban datos dinámicos[cite: 1].

print("=== 3. SISTEMA DE PARÁMETROS ===")

# A. Parámetros posicionales: Los datos se asignan estrictamente en orden[cite: 1].
def calcular_area_rectangulo(ancho, alto):
    """Calcula el área multiplicando ancho por alto."""
    return ancho * alto

print("Área posicional (5, 10):", calcular_area_rectangulo(5, 10))  # Salida: 50[cite: 1]


# B. Parámetros con nombre (keyword arguments): Permiten alterar el orden de los datos[cite: 1].
def crear_usuario(nombre, edad, ciudad):
    return f"{nombre}, {edad} años, de {ciudad}"

usuario_a = crear_usuario("Ana", 25, "Madrid")  # Posicional clásico[cite: 1]
usuario_b = crear_usuario(nombre="Carlos", edad=30, ciudad="Barcelona")  # Con nombre[cite: 1]
usuario_c = crear_usuario(ciudad="Valencia", nombre="Laura", edad=28)  # Orden alterado con éxito[cite: 1]

print("Usuario 1:", usuario_a)
print("Usuario 2:", usuario_b)
print("Usuario 3:", usuario_c)


# C. Parámetros con valores por defecto: Son opcionales si no se especifican en la llamada[cite: 1].
# REGLA: Los parámetros por defecto deben ir siempre DESPUÉS de los obligatorios.
def saludar_personalizado(nombre, saludo="Hola"):
    """Saluda a una persona utilizando un saludo predeterminado opcional[cite: 1]."""
    return f"{saludo}, {nombre}!"

print(saludar_personalizado("María"))                 # Usa el valor por defecto: Hola, María![cite: 1]
print(saludar_personalizado("Pedro", "Buenos días"))  # Sobrescribe el valor: Buenos días, Pedro![cite: 1]
print()


# =============================================================================
# SECCIÓN 4: EL SISTEMA DE SALIDAS (LA SENTENCIA RETURN)
# =============================================================================
# 'return' finaliza la ejecución de la función de inmediato y entrega un valor[cite: 1].

print("=== 4. LA SENTENCIA RETURN ===")

# A. Return simple: Devuelve un único resultado[cite: 1].
def sumar(a, b):
    return a + b

print("Return simple (5 + 3):", sumar(5, 3))  # Salida: 8[cite: 1]


# B. Return múltiple: Python permite empaquetar múltiples valores en una tupla[cite: 1].
def calcular_estadisticas(numeros):
    """Calcula suma, promedio y máximo, retornando múltiples valores[cite: 1]."""
    total = sum(numeros)
    promedio = total / len(numeros)
    maximo = max(numeros)
    return total, promedio, maximo  # Devuelve una tupla[cite: 1]

# Desempaquetado directo de la tupla retornada:
suma_tot, prom_val, max_val = calcular_estadisticas([10, 20, 30, 40, 50])
print(f"Estadísticas -> Suma: {suma_tot}, Promedio: {prom_val}, Máximo: {max_val}[cite: 1]")


# C. Funciones sin return: Si se omite, devuelven 'None' implícitamente de forma silenciosa[cite: 1].
def imprimir_mensaje(mensaje):
    print(f"Mensaje en consola: {mensaje}")
    # Sin sentencia return

retorno_vacio = imprimir_mensaje("Hola")
print(f"Valor devuelto por función sin return: {retorno_vacio}")  # Salida: None[cite: 1]


# D. Return anticipado (Cortocircuito lógico): Sale de la función antes de llegar al final[cite: 1].
def es_par(numero):
    """Verifica si un número es par utilizando un retorno temprano[cite: 1]."""
    if numero % 2 == 0:
        return True   # Cortocircuito: sale aquí si es par[cite: 1]
    return False      # Solo se ejecuta si la condición anterior falló[cite: 1]

print("¿El número 4 es par?:", es_par(4))   # True[cite: 1]
print("¿El número 7 es par?:", es_par(7))   # False[cite: 1]
print()


# =============================================================================
# SECCIÓN 5: ÁMBITO DE VARIABLES (SCOPE)
# =============================================================================
# Define en qué partes del código tus variables están vivas y son accesibles[cite: 1].

print("=== 5. ÁMBITO DE VARIABLES (SCOPE) ===")

tasa_iva = 0.21  # Variable global: accesible desde cualquier parte del archivo[cite: 1]

def calcular_precio_final(precio_neto):
    """Las funciones pueden leer variables globales libremente[cite: 1]."""
    impuesto = precio_neto * tasa_iva  # Variable local: solo existe dentro de esta función[cite: 1]
    return precio_neto + impuesto

print("Precio con IVA aplicado:", calcular_precio_final(100))  # Salida: 121.0[cite: 1]

# Modificación de variables globales usando la palabra clave 'global'[cite: 1]
contador_visitas = 0

def incrementar_contador():
    global contador_visitas  # Indica que vamos a modificar la variable global original[cite: 1]
    contador_visitas += 1

incrementar_contador()
print("Contador global tras 1 llamada:", contador_visitas)  # 1[cite: 1]
print()


# =============================================================================
# SECCIÓN 6: FLEXIBILIDAD EXTREMA CON *ARGS Y **KWARGS
# =============================================================================
# Permiten recibir un número indeterminado de argumentos posicionales o con nombre[cite: 1].

print("=== 6. *ARGS Y **KWARGS ===")

# A. *args: Recoge argumentos posicionales variables y los agrupa en una tupla[cite: 1].
def sumar_ilimitado(*numeros):
    """Suma cualquier cantidad indefinida de números[cite: 1]."""
    total = 0
    for num in numeros:
        total += num
    return total

print("Suma ilimitada (1, 2, 3):", sumar_ilimitado(1, 2, 3))             # 6[cite: 1]
print("Suma ilimitada (10, 20, 30, 40):", sumar_ilimitado(10, 20, 30, 40))  # 100[cite: 1]


# B. **kwargs: Recoge argumentos con nombre variables y los agrupa en un diccionario[cite: 1].
def crear_perfil_usuario(**datos):
    """Crea un perfil dinámico procesando pares de clave-valor[cite: 1]."""
    print("Datos del perfil de usuario:")
    for clave, valor in datos.items():
        print(f"  - {clave}: {valor}")

crear_perfil_usuario(nombre="Ana", edad=25, ciudad="Madrid")  #[cite: 1]
print()


# =============================================================================
# SECCIÓN 7: FUNCIONES ANIDADAS Y CLOSURES
# =============================================================================
# Funciones declaradas dentro de otras funciones para encapsular lógica auxiliar[cite: 1].

print("=== 7. FUNCIONES ANIDADAS Y CLOSURES ===")

def calcular_precio_con_descuento(precio, porcentaje_descuento):
    """Función principal que utiliza funciones internas auxiliares[cite: 1]."""
    
    def aplicar_descuento(p, desc):
        return p * (1 - desc / 100)

    def aplicar_iva(p):
        return p * 1.21

    # Ejecución interna de las subfunciones
    precio_rebajado = aplicar_descuento(precio, porcentaje_descuento)
    return aplicar_iva(precio_rebajado)

print("Precio final con descuento e IVA anidados:", calcular_precio_con_descuento(100, 10))  # 108.9[cite: 1]


# Closures: Funciones internas que recuerdan el entorno de su función externa[cite: 1].
def crear_multiplicador(factor):
    """Retorna una función personalizada que multiplica por un factor fijo[cite: 1]."""
    def multiplicar(numero):
        return numero * factor  # Accede a la variable 'factor' de la función externa[cite: 1]
    return multiplicar

duplicar = crear_multiplicador(2)
triplicar = crear_multiplicador(3)
print("Duplicar el número 10:", duplicar(10))   # 20[cite: 1]
print("Triplicar el número 10:", triplicar(10)) # 30[cite: 1]
print()


# =============================================================================
# SECCIÓN 8: DOCUMENTACIÓN CON DOCSTRINGS
# =============================================================================
# El estándar de oro para documentar código profesionalmente mediante triple comilla[cite: 1].

print("=== 8. DOCUMENTACIÓN CON DOCSTRINGS ===")

def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC).

    Args:
        peso (float): Peso en kilogramos[cite: 1].
        altura (float): Altura en metros[cite: 1].

    Returns:
        float: El IMC calculado[cite: 1].
    """
    return peso / (altura ** 2)

# Acceso al Docstring integrado de la función mediante '__doc__'[cite: 1]
print(calcular_imc.__doc__)
print()


# =============================================================================
# SECCIÓN 9: FUNCIONES COMO OBJETOS DE PRIMERA CLASE
# =============================================================================
# En Python, las funciones son tratadas exactamente igual que cualquier otro dato[cite: 1].

print("=== 9. OBJETOS DE PRIMERA CLASE ===")

def saludar_formal(nombre):
    return f"Estimado/a {nombre}"

# 1. Asignar funciones a variables[cite: 1]
mi_variable_funcion = saludar_formal
print("Llamada usando variable asignada:", mi_variable_funcion("Carlos"))

# 2. Pasar funciones como argumentos a otras funciones[cite: 1]
def aplicar_operacion(a, b, operacion):
    return operacion(a, b)

def sumar_valores(x, y):
    return x + y

print("Función pasada como argumento (5 + 3):", aplicar_operacion(5, 3, sumar_valores))  # 8[cite: 1]
print()


# =============================================================================
# SECCIÓN 10: CASOS DE USO PRÁCTICOS
# =============================================================================
print("=== 10. CASOS DE USO PRÁCTICOS ===")

# A. Validación básica de correos electrónicos[cite: 1]
def validar_email(email):
    """Verifica si un email contiene '@' y un punto posterior válido[cite: 1]."""
    if "@" not in email:
        return False
    if "." not in email.split("@")[1]:
        return False
    return True

print("¿'usuario@ejemplo.com' es válido?:", validar_email("usuario@ejemplo.com"))  # True[cite: 1]
print("¿'usuario@ejemplo' es válido?:", validar_email("usuario@ejemplo"))          # False[cite: 1]


# B. Procesamiento y filtrado de listas[cite: 1]
def filtrar_pares(numeros):
    """Recorre una lista y extrae únicamente los números pares[cite: 1]."""
    pares = []
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
    return pares

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Números pares filtrados:", filtrar_pares(lista_numeros))  # [2, 4, 6, 8, 10][cite: 1]
print()


# =============================================================================
# SECCIÓN 11: ERRORES COMUNES Y CÓMO EVITARLOS
# =============================================================================
print("=== 11. ERRORES COMUNES Y BUENAS PRÁCTICAS ===")

# ERROR 1: Modificar tipos mutables (como listas) como valores por defecto en parámetros.
# MALO: def agregar_item(item, lista=[]): ... (Acumula datos entre llamadas).
# BUENO: Usar 'None' y declarar la lista vacía dentro de la función[cite: 1].

def agregar_item_seguro(item, lista=None):
    """Evita el error crítico de mutación de listas por defecto en parámetros[cite: 1]."""
    if lista is None:
        lista = []  # Crea una lista nueva y limpia en cada llamada sin argumentos previos[cite: 1]
    lista.append(item)
    return lista

print("Primer uso seguro de lista:", agregar_item_seguro(1))  # [1][cite: 1]
print("Segundo uso seguro de lista:", agregar_item_seguro(2)) # [2] (¡Lista nueva, sin rastro del anterior!)[cite: 1]