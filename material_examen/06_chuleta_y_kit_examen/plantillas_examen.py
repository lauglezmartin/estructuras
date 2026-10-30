"""
KIT DE EXAMEN - Plantillas listas para copiar y adaptar
========================================================
QUÉ ES:
    Esqueletos de las estructuras que más salen en el examen (temas 1-6).
    Copia el bloque que necesites, cambia los nombres y adapta la lógica.

ÍNDICE (busca con Ctrl+F el texto entre corchetes):
    [P1]  Leer un número validando (while + isdigit / try-except)
    [P2]  Menú con while True + match-case + opción salir
    [P3]  Clase con atributos privados + getters/setters + __str__/__repr__
    [P4]  Clase gestora con lista de objetos (añadir, listar, buscar,
          eliminar, filtrar con comprensión, ordenar con lambda)
    [P5]  Contador con diccionario
    [P6]  Función con *args y **kwargs
    [P7]  Decorador básico
    [P8]  Bloque main (demos con datos fijos, sin input())

CÓMO EJECUTARLO:  python plantillas_examen.py   (Linux/Docker: python3 ...)
    El main NO pide nada por teclado: usa datos fijos para que veas
    cómo funciona todo. Las funciones con input() están listas para usar
    en tu examen, pero aquí solo se llaman si quitas el comentario.
"""


# =====================================================================
# [P1] LEER UN NÚMERO VALIDANDO
# =====================================================================
# input() SIEMPRE devuelve str. Si haces int("hola") salta ValueError.
# Dos formas de validar. Usa la que pida el enunciado; si no pide
# ninguna, cualquiera vale.

def pedir_entero(mensaje):
    """Pide un entero >= 0 hasta que sea válido (forma while + isdigit).

    isdigit() es True solo si TODOS los caracteres son dígitos:
    "12" -> True, "-3" -> False, "3.5" -> False, "" -> False.
    Por eso sirve para enteros >= 0, no para negativos ni decimales.
    """
    texto = input(mensaje).strip()          # strip quita espacios sobrantes
    while not texto.isdigit():              # mientras NO sea válido...
        print("Error: escribe un número entero (0 o mayor), sin signo ni decimales.")
        texto = input(mensaje).strip()      # ...vuelvo a pedir (¡si no, bucle infinito!)
    return int(texto)                       # aquí ya es seguro convertir


def pedir_decimal(mensaje):
    """Pide un número (puede ser negativo o decimal) con try-except.

    Intenta convertir; si falla (ValueError) avisa y repite.
    """
    while True:
        try:
            return float(input(mensaje))    # si convierte bien, sale con return
        except ValueError:
            print("Error: eso no es un número. Ejemplo válido: 3.5")


def es_entero_valido(texto):
    """Versión SIN input() para probar la validación con datos fijos."""
    return texto.strip().isdigit()


# =====================================================================
# [P2] MENÚ CON while True + match-case + SALIR
# =====================================================================
# Estructura: bucle infinito -> mostrar opciones -> leer -> match -> break
# en la opción salir. case _ recoge cualquier opción no válida.

def mostrar_menu():
    """Imprime las opciones del menú."""
    print("\n--- MENÚ ---")
    print("1. Añadir")
    print("2. Listar")
    print("3. Buscar")
    print("0. Salir")


def ejecutar_opcion(opcion):
    """Ejecuta una opción. Devuelve False si hay que salir, True si no.

    Separar esto del input() permite probar el menú sin teclado.
    """
    match opcion:
        case "1":                            # comparo con str: input da str
            print("-> Has elegido AÑADIR")
        case "2":
            print("-> Has elegido LISTAR")
        case "3":
            print("-> Has elegido BUSCAR")
        case "0":
            print("-> ¡Hasta luego!")
            return False                     # señal de salir
        case _:                              # comodín: cualquier otra cosa
            print("-> Opción no válida")
    return True


def menu_interactivo():
    """Menú real del examen: while True + match-case + break."""
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()
        if not ejecutar_opcion(opcion):
            break                            # sale del while True


# =====================================================================
# [P3] CLASE CON ATRIBUTOS PRIVADOS + GETTERS/SETTERS + __str__/__repr__
# =====================================================================

class Producto:
    """Representa un producto de una tienda.

    Atributos:
        categoria_tienda (de CLASE): compartido por todos los productos.
        nombre (público), __precio y __stock (privados).
    """

    categoria_tienda = "Alimentación"        # atributo de CLASE (fuera de __init__)

    def __init__(self, nombre, precio, stock=0):
        """Constructor: crea los atributos de INSTANCIA de cada objeto."""
        self.nombre = nombre                 # público: se puede leer desde fuera
        self.__precio = precio               # privado: __ activa el name mangling
        self.__stock = stock                 # (por fuera se llama _Producto__stock)

    # ---- getters: DEVUELVEN el valor (return, no print) ----
    def get_precio(self):
        """Devuelve el precio."""
        return self.__precio

    def get_stock(self):
        """Devuelve las unidades disponibles."""
        return self.__stock

    # ---- setters: cambian el valor VALIDANDO (cláusula de guarda) ----
    def set_precio(self, nuevo_precio):
        """Cambia el precio solo si es positivo. Devuelve True si lo cambia."""
        if nuevo_precio <= 0:                # guarda: error -> salgo ya
            print(f"Error: precio no válido ({nuevo_precio})")
            return False
        self.__precio = nuevo_precio
        return True

    def vender(self, unidades):
        """Resta unidades del stock si hay suficientes."""
        if unidades > self.__stock:
            print(f"No hay stock suficiente de {self.nombre}")
            return False
        self.__stock -= unidades
        return True

    # ---- métodos mágicos ----
    def __str__(self):
        """Texto amigable para el usuario: lo usa print(objeto)."""
        return f"{self.nombre} - {self.__precio:.2f} € ({self.__stock} uds.)"

    def __repr__(self):
        """Texto técnico: cómo se creó el objeto. Lo usa print(lista)."""
        return f"Producto('{self.nombre}', {self.__precio}, {self.__stock})"


# =====================================================================
# [P4] CLASE GESTORA CON LISTA DE OBJETOS
# =====================================================================

class Tienda:
    """Gestiona una lista de objetos Producto."""

    def __init__(self, nombre):
        """Crea la tienda con una lista VACÍA propia (en __init__, no en la clase)."""
        self.nombre = nombre
        self.productos = []

    def anadir(self, producto):
        """Añade un producto si no existe otro con el mismo nombre."""
        if self.buscar(producto.nombre) is not None:
            print(f"Ya existe {producto.nombre}")
            return False
        self.productos.append(producto)
        return True

    def listar(self):
        """Muestra los productos numerados desde 1."""
        if not self.productos:               # lista vacía = False
            print("(no hay productos)")
            return
        for i, producto in enumerate(self.productos, start=1):
            print(f"{i}. {producto}")        # usa __str__

    def buscar(self, nombre):
        """Devuelve el producto con ese nombre o None si no está."""
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():   # sin distinguir mayúsculas
                return producto
        return None                          # FUERA del for: ya miré todos

    def eliminar(self, nombre):
        """Elimina el producto con ese nombre. Devuelve True si lo borra."""
        producto = self.buscar(nombre)
        if producto is None:
            return False
        self.productos.remove(producto)
        return True

    def filtrar_baratos(self, precio_max):
        """Devuelve una lista NUEVA con los productos de precio <= precio_max."""
        return [p for p in self.productos if p.get_precio() <= precio_max]

    def ordenados_por_precio(self, descendente=False):
        """Devuelve una lista NUEVA ordenada por precio (la original no cambia)."""
        return sorted(self.productos, key=lambda p: p.get_precio(),
                      reverse=descendente)

    def valor_total(self):
        """Devuelve la suma de precio * stock de todos los productos."""
        total = 0
        for p in self.productos:             # acumulador clásico
            total += p.get_precio() * p.get_stock()
        return total

    def mas_caro(self):
        """Devuelve el producto más caro (o None si no hay)."""
        if not self.productos:
            return None
        return max(self.productos, key=lambda p: p.get_precio())


# =====================================================================
# [P5] CONTADOR CON DICCIONARIO
# =====================================================================

def contar_palabras(texto):
    """Devuelve un dict {palabra: veces} sin distinguir mayúsculas."""
    conteo = {}
    for palabra in texto.lower().split():
        conteo[palabra] = conteo.get(palabra, 0) + 1   # get evita KeyError
    return conteo


def contar_vocales(texto):
    """Devuelve un dict con cuántas veces aparece cada vocal."""
    conteo = {v: 0 for v in "aeiou"}         # comprensión de diccionario
    for letra in texto.lower():
        if letra in conteo:                  # ojo: "é" NO cuenta como "e"
            conteo[letra] += 1
    return conteo


# =====================================================================
# [P6] FUNCIÓN CON *args Y **kwargs
# =====================================================================

def calcular_promedio(*args):
    """Devuelve la media de los números recibidos (args es una TUPLA)."""
    if not args:                             # guarda: evita dividir entre 0
        return 0
    return sum(args) / len(args)


def crear_perfil_usuario(nombre, apellido, **kwargs):
    """Devuelve un dict con nombre, apellido y los datos extra (kwargs es un DICT)."""
    perfil = {"nombre": nombre, "apellido": apellido}
    for clave, valor in kwargs.items():
        perfil[clave] = valor
    return perfil


def mostrar_datos(**kwargs):
    """Imprime cada dato como 'Clave: valor' con la clave capitalizada."""
    for clave, valor in kwargs.items():
        print(f"{clave.capitalize()}: {valor}")


# =====================================================================
# [P7] DECORADOR BÁSICO
# =====================================================================
# Un decorador es una función que recibe una función y devuelve otra
# (la "envoltura") que añade algo antes y/o después.

def anunciar_ejecucion(funcion):
    """Decorador: imprime un mensaje antes y otro después de la función."""
    def envoltura(*args, **kwargs):          # *args/**kwargs: vale para cualquier función
        """Función que sustituye a la original: añade los mensajes."""
        print("--- Iniciando función ---")
        resultado = funcion(*args, **kwargs) # ejecuto la función original
        print("--- Función terminada ---")
        return resultado                     # no pierdo lo que devuelva
    return envoltura                         # devuelvo la función SIN ()


@anunciar_ejecucion                          # = tarea_importante = anunciar_ejecucion(tarea_importante)
def tarea_importante():
    """Función de ejemplo decorada."""
    print("Procesando datos en la base de datos...")


@anunciar_ejecucion
def sumar(a, b):
    """Suma dos números (decorada, con parámetros y return)."""
    return a + b


# =====================================================================
# [P8] BLOQUE MAIN: pruebas con datos fijos
# =====================================================================

def main():
    """Ejecuta una demo de cada plantilla sin pedir nada por teclado."""
    print("=== [P1] Validación de números ===")
    for dato in ["25", "-3", "3.5", "hola", ""]:
        print(f"{dato!r:8} -> ¿entero válido? {es_entero_valido(dato)}")

    print("\n=== [P2] Menú (opciones simuladas) ===")
    for opcion in ["1", "2", "9", "0"]:      # simulo lo que escribiría el usuario
        print(f"Usuario escribe: {opcion}")
        if not ejecutar_opcion(opcion):
            break

    print("\n=== [P3] Clase con privados ===")
    leche = Producto("Leche", 1.15, 20)
    print(leche)                             # __str__
    print(repr(leche))                       # __repr__
    leche.set_precio(-5)                     # setter rechaza
    leche.set_precio(1.25)
    print("Precio nuevo:", leche.get_precio())
    print("Categoría (atributo de clase):", Producto.categoria_tienda)
    try:
        print(leche.__precio)                # NO se puede: es privado
    except AttributeError as error:
        print("AttributeError:", error)

    print("\n=== [P4] Tienda con lista de objetos ===")
    tienda = Tienda("Super DAW")
    tienda.anadir(leche)
    tienda.anadir(Producto("Pan", 0.90, 50))
    tienda.anadir(Producto("Aceite", 8.50, 5))
    tienda.anadir(Producto("Café", 4.20, 12))
    tienda.anadir(Producto("pan", 1.00, 1))  # repetido -> lo rechaza
    tienda.listar()
    print("Buscar 'café':", tienda.buscar("café"))
    print("Buscar 'sal':", tienda.buscar("sal"))
    print("Baratos (<= 2 €):", tienda.filtrar_baratos(2))     # usa __repr__
    print("Ordenados por precio desc.:")
    for p in tienda.ordenados_por_precio(descendente=True):
        print("  ", p)
    print("Más caro:", tienda.mas_caro())
    print(f"Valor total del stock: {tienda.valor_total():.2f} €")
    print("¿Eliminado Pan?", tienda.eliminar("Pan"))
    print("¿Eliminado Sal?", tienda.eliminar("Sal"))
    tienda.listar()

    print("\n=== [P5] Contadores con diccionario ===")
    print(contar_palabras("el sol y el mar y EL cielo"))
    print(contar_vocales("Murciélago estudia Python"))

    print("\n=== [P6] *args y **kwargs ===")
    print("Promedio:", calcular_promedio(4, 6, 8))
    print("Promedio vacío:", calcular_promedio())
    print(crear_perfil_usuario("Ana", "Ruiz", edad=20, ciudad="Adeje"))
    mostrar_datos(nombre="Luis", edad=19, ciudad="Arona")

    print("\n=== [P7] Decorador ===")
    tarea_importante()
    print("Resultado de sumar:", sumar(2, 3))

    # Para probar las versiones con teclado, quita el # de estas líneas:
    # numero = pedir_entero("Dame un entero: ")
    # precio = pedir_decimal("Dame un precio: ")
    # menu_interactivo()


if __name__ == "__main__":
    main()

# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - return None DENTRO del for de buscar(): solo miraría el primero.
# - sort() cambia la lista y devuelve None; sorted() devuelve una nueva.
# - __str__ y __repr__ DEVUELVEN un str (return), no imprimen.
# - En el menú compara con "1" (str), porque input() devuelve str.
# - Lista de objetos en __init__ (self.productos = []), nunca como
#   atributo de clase: la compartirían todas las tiendas.
# EN JAVA SERÍA: private double precio; + getPrecio(); aquí self.__precio.
# ---------------------------------------------------------------
