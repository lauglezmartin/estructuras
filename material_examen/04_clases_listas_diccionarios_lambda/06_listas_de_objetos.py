"""
TEMA 6 - Teoría-práctica 6: CRUD sobre una lista de objetos
===========================================================
ENUNCIADO: Archivo de consulta. Gestiona una lista de objetos Producto con
las operaciones típicas de examen: añadir (Create), listar y buscar (Read),
modificar (Update), eliminar (Delete), contar, sumar y sacar el máximo y el
mínimo con max/min(key=lambda).

FORMA QUE EXIGE EL PROFESOR:
    - Los objetos se guardan en una lista: inventario = [Producto(...), ...]
    - Recorrer con for (o enumerate(..., start=1) si se muestra numerado).
    - Filtrar/transformar en una línea con comprensión de listas.
    - Ordenar / máximo por un atributo con key=lambda p: p.atributo.
    - Funciones con docstring y pruebas en if __name__ == "__main__":

CONCEPTOS QUE PRACTICA:
    - Lista de objetos y acceso a sus atributos dentro de un for.
    - Funciones que reciben la lista y la modifican o devuelven resultados.
    - remove(), del, pop(); no borrar mientras recorres la lista.
    - sum(), len(), max()/min() con key, sorted() con key.

CÓMO EJECUTARLO:  python 06_listas_de_objetos.py   (en Linux/Docker: python3 06_listas_de_objetos.py)
"""


# ---------------------------------------------------------------
# PASO 1: LA CLASE DE LOS OBJETOS QUE VAMOS A GUARDAR
# ---------------------------------------------------------------
class Producto:
    """Producto de una tienda con nombre, precio, categoría y stock."""

    def __init__(self, nombre, precio, categoria, stock):
        """Crea el producto."""
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock

    def valor_stock(self):
        """Devuelve precio * stock (dinero que hay en el almacén de este producto)."""
        return self.precio * self.stock

    def __str__(self):
        """Texto para el usuario."""
        return f"{self.nombre} - {self.precio} € ({self.categoria}, stock {self.stock})"

    def __repr__(self):
        """Texto técnico."""
        return f"Producto('{self.nombre}', {self.precio}, '{self.categoria}', {self.stock})"


# ---------------------------------------------------------------
# PASO 2: FUNCIONES CRUD
# ---------------------------------------------------------------
# Las listas son MUTABLES: si una función hace lista.append(...) o
# lista.remove(...), el cambio se ve fuera (no hace falta devolver la lista).

def anadir_producto(lista, producto):
    """CREATE: añade el producto al final de la lista."""
    lista.append(producto)


def listar_productos(lista):
    """READ: muestra todos los productos numerados."""
    if not lista:                           # lista vacía -> False
        print("No hay productos.")
        return
    for numero, p in enumerate(lista, start=1):
        print(f"{numero}. {p}")


def buscar_producto(lista, nombre):
    """READ: devuelve el producto con ese nombre (sin mirar mayúsculas) o None."""
    for p in lista:
        if p.nombre.lower() == nombre.lower():
            return p
    return None


def modificar_precio(lista, nombre, nuevo_precio):
    """UPDATE: cambia el precio del producto. Devuelve True si lo encontró."""
    p = buscar_producto(lista, nombre)      # reutilizamos la búsqueda
    if p is None:
        return False
    p.precio = nuevo_precio                 # modificamos EL OBJETO que está en la lista
    return True


def eliminar_producto(lista, nombre):
    """DELETE: quita el producto de la lista. Devuelve True si lo encontró."""
    p = buscar_producto(lista, nombre)
    if p is None:
        return False
    lista.remove(p)                         # remove borra la PRIMERA coincidencia
    return True


# ---------------------------------------------------------------
# PASO 3: PRUEBAS
# ---------------------------------------------------------------
if __name__ == "__main__":

    inventario = []                         # empezamos con la lista vacía

    print("=== CREATE: añadir ===")
    anadir_producto(inventario, Producto("Portátil", 800, "electrónica", 5))
    anadir_producto(inventario, Producto("Ratón", 25, "electrónica", 50))
    anadir_producto(inventario, Producto("Mesa", 200, "muebles", 10))
    anadir_producto(inventario, Producto("Silla", 90, "muebles", 0))
    anadir_producto(inventario, Producto("Teclado", 45, "electrónica", 20))
    print("Productos añadidos:", len(inventario))

    print("\n=== READ: listar ===")
    listar_productos(inventario)

    print("\n=== READ: buscar ===")
    encontrado = buscar_producto(inventario, "mesa")
    print("Buscar 'mesa':", encontrado)
    print("Buscar 'Lámpara':", buscar_producto(inventario, "Lámpara"))

    print("\n=== UPDATE: modificar ===")
    if modificar_precio(inventario, "Ratón", 19.99):
        print("Precio cambiado:", buscar_producto(inventario, "Ratón"))
    if not modificar_precio(inventario, "Lámpara", 30):
        print("No se puede modificar 'Lámpara': no existe")
    # También se puede modificar directamente recorriendo:
    for p in inventario:
        if p.categoria == "muebles":
            p.stock += 5                    # reponemos todos los muebles

    print("\n=== DELETE: eliminar ===")
    print("Eliminar 'Teclado':", eliminar_producto(inventario, "Teclado"))
    print("Eliminar 'Lámpara':", eliminar_producto(inventario, "Lámpara"))
    # Otras formas de borrar por POSICIÓN:
    #   del inventario[0]          -> borra el primero
    #   ultimo = inventario.pop()  -> quita el último y lo devuelve
    listar_productos(inventario)

    print("\n=== Contar ===")
    print("Total de productos:", len(inventario))
    # Contar los que cumplen algo: con contador o con len() de una comprensión.
    contador = 0
    for p in inventario:
        if p.categoria == "electrónica":
            contador += 1
    print("De electrónica (for):", contador)
    print("De electrónica (comprensión):", len([p for p in inventario if p.categoria == "electrónica"]))

    print("\n=== Sumar ===")
    total = 0
    for p in inventario:
        total += p.valor_stock()
    print("Valor total del almacén (for):", total)
    print("Valor total del almacén (sum):", sum(p.valor_stock() for p in inventario))
    print("Unidades totales:", sum(p.stock for p in inventario))

    print("\n=== Máximo y mínimo con key=lambda ===")
    # max(lista) sin key no sabe comparar objetos -> TypeError.
    # key=lambda p: p.precio  -> "compara los productos por su precio".
    # Devuelve el OBJETO entero, no el número.
    mas_caro = max(inventario, key=lambda p: p.precio)
    mas_barato = min(inventario, key=lambda p: p.precio)
    print("Más caro:", mas_caro)
    print("Más barato:", mas_barato)
    print("Precio máximo (solo el número):", max(p.precio for p in inventario))

    print("\n=== Filtrar y ordenar ===")
    disponibles = [p for p in inventario if p.stock > 0]
    print("Disponibles:", [p.nombre for p in disponibles])
    ordenados = sorted(inventario, key=lambda p: p.precio, reverse=True)
    print("Por precio (mayor a menor):", [p.nombre for p in ordenados])

    print("\n=== Borrar varios cumpliendo una condición (forma segura) ===")
    # NO borres con remove dentro de "for p in inventario" (se salta elementos).
    # Crea una lista nueva con los que QUIERES CONSERVAR:
    inventario = [p for p in inventario if p.precio >= 50]
    print(inventario)


# ---------------------------------------------------------------
# SALIDA ESPERADA:
# === CREATE: añadir ===
# Productos añadidos: 5
#
# === READ: listar ===
# 1. Portátil - 800 € (electrónica, stock 5)
# 2. Ratón - 25 € (electrónica, stock 50)
# 3. Mesa - 200 € (muebles, stock 10)
# 4. Silla - 90 € (muebles, stock 0)
# 5. Teclado - 45 € (electrónica, stock 20)
#
# === READ: buscar ===
# Buscar 'mesa': Mesa - 200 € (muebles, stock 10)
# Buscar 'Lámpara': None
#
# === UPDATE: modificar ===
# Precio cambiado: Ratón - 19.99 € (electrónica, stock 50)
# No se puede modificar 'Lámpara': no existe
#
# === DELETE: eliminar ===
# Eliminar 'Teclado': True
# Eliminar 'Lámpara': False
# 1. Portátil - 800 € (electrónica, stock 5)
# 2. Ratón - 19.99 € (electrónica, stock 50)
# 3. Mesa - 200 € (muebles, stock 15)
# 4. Silla - 90 € (muebles, stock 5)
#
# === Contar ===
# Total de productos: 4
# De electrónica (for): 2
# De electrónica (comprensión): 2
#
# === Sumar ===
# Valor total del almacén (for): 8449.5
# Valor total del almacén (sum): 8449.5
# Unidades totales: 75
#
# === Máximo y mínimo con key=lambda ===
# Más caro: Portátil - 800 € (electrónica, stock 5)
# Más barato: Ratón - 19.99 € (electrónica, stock 50)
# Precio máximo (solo el número): 800
#
# === Filtrar y ordenar ===
# Disponibles: ['Portátil', 'Ratón', 'Mesa', 'Silla']
# Por precio (mayor a menor): ['Portátil', 'Mesa', 'Silla', 'Ratón']
#
# === Borrar varios cumpliendo una condición (forma segura) ===
# [Producto('Portátil', 800, 'electrónica', 5), Producto('Mesa', 200, 'muebles', 15), Producto('Silla', 90, 'muebles', 5)]
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - max(inventario) sin key -> TypeError ('>' not supported between Producto).
# - Confundir el objeto con un atributo: print(mas_caro) muestra el producto;
#   mas_caro.precio es el número.
# - remove() de algo que no está -> ValueError. Por eso primero se busca.
# - Borrar con remove DENTRO de un for sobre la misma lista se salta
#   elementos. Usa una comprensión (o recorre una copia: for p in lista[:]).
# - Comparar texto sin .lower(): "mesa" != "Mesa".
# EN JAVA SERÍA: ArrayList<Producto>; aquí la lista no tiene tipo y se
# recorre con "for p in lista" (como el for-each de Java).
# ---------------------------------------------------------------
