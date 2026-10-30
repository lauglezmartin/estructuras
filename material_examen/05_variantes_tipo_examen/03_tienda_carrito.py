"""
TEMA 6 (integrador) - Variante 03: "La tienda online y su carrito"
==================================================================
ENUNCIADO (redactado al estilo del profesor, modelo Teletubbies):

    Objetivo: Programar el inventario de una tienda y un carrito de la compra
    que calcule el ticket con IVA y descuentos.

    Requisitos de la clase Producto:
    1. Atributo de clase: IVA = 0.21 (compartido por todos los productos).
    2. Atributos públicos: nombre, precio (float, sin IVA), categoria.
       Atributo privado: __stock (int).
    3. get_stock(): getter que devuelve el entero.
       ver_stock(): GETTER que devuelve un STRING del tipo
       "Teclado: 3 uds (stock bajo)" usando MATCH-CASE con guardas:
       0 -> "agotado"; 1 a 5 -> "stock bajo" (COMPARACIÓN ENCADENADA);
       resto -> "disponible".
    4. retirar(cantidad): resta del stock solo si hay suficiente;
       devuelve True o False (return, no print).
    5. precio_con_iva(): devuelve el precio con IVA redondeado a 2 decimales.
    6. __str__ y __repr__.

    Requisitos de la clase Carrito:
    7. Atributo privado __lineas: DICCIONARIO {nombre_producto: [producto, cantidad]}.
    8. agregar(producto, cantidad=1): cantidad debe ser 1 <= cantidad <= 10
       (comparación encadenada). Si no hay stock, no se añade. Devuelve string.
    9. agregar_varios(*pares): recibe un número variable de tuplas
       (producto, cantidad) con *args y llama a agregar para cada una.
    10. subtotal(): suma con una COMPRENSIÓN (sum([...])) recorriendo el
        diccionario con .items() o .values().
    11. descuento(codigo): MATCH-CASE con guardas sobre el código:
        "VERANO" -> 10 %; "VIP" solo si subtotal >= 100 -> 20 %;
        "VIP" con subtotal menor -> 0 % (mensaje); cualquier otro -> 0 %.
        Devuelve una tupla (porcentaje, mensaje).
    12. ticket(codigo=None): devuelve un STRING multilínea con las líneas
        numeradas con enumerate(start=1), subtotal, descuento, total.

    Funciones fuera de las clases:
    13. precios_con_iva(productos): MAP + LAMBDA -> lista de (nombre, precio_iva).
    14. bajo_stock(productos): FILTER + LAMBDA -> productos con stock <= 5.
    15. mas_caros(productos, n): SORTED + LAMBDA (de mayor a menor), los n primeros.
    16. inventario_por_categoria(productos): DICCIONARIO {categoria: [nombres]}.

    Bloque principal: crea 5 productos, prueba todas las funciones y dos
    tickets (uno con "VIP" válido y otro con un código que no aplica).

    Cuestión teórica: ¿Por qué IVA es atributo de clase y no de instancia?
    ¿Qué pasaría si mañana el IVA sube al 0.23?

FORMA QUE EXIGE EL PROFESOR:
    - Atributo de clase IVA usado como Producto.IVA.
    - Atributo privado __stock con getter.
    - match-case con guardas (2 veces) y comparación encadenada.
    - *args en agregar_varios, dict recorrido con .items(),
      comprensión en subtotal, map/filter/sorted con lambda,
      enumerate(start=1), return en vez de print.

CONCEPTOS QUE PRACTICA:
    - Diccionario cuyo valor es una lista [objeto, cantidad]
    - Tuplas como valor de retorno múltiple, f-strings con :.2f

CÓMO EJECUTARLO:  python 03_tienda_carrito.py   (en Linux: python3 ...)
"""


# ---------------------------------------------------------------
# PASO 1: Clase Producto.
# ---------------------------------------------------------------
class Producto:
    """Un producto del inventario."""

    IVA = 0.21  # atributo de clase: igual para todos los productos

    def __init__(self, nombre, precio, categoria, stock=0):
        """Constructor. stock es privado."""
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.__stock = stock

    def get_stock(self):
        """Getter numérico del stock."""
        return self.__stock

    def ver_stock(self):
        """GETTER que devuelve un string describiendo el stock."""
        match self.__stock:
            case 0:                           # patrón literal
                estado = "agotado"
            case s if 1 <= s <= 5:            # guarda + comparación encadenada
                estado = "stock bajo"
            case _:
                estado = "disponible"
        return f"{self.nombre}: {self.__stock} uds ({estado})"

    def retirar(self, cantidad):
        """Resta stock si hay suficiente. Devuelve True/False."""
        if cantidad > self.__stock:
            return False
        self.__stock -= cantidad
        return True

    def precio_con_iva(self):
        """Precio final con IVA. Se usa Producto.IVA (atributo de clase)."""
        return round(self.precio * (1 + Producto.IVA), 2)

    def __str__(self):
        """Texto amigable para el usuario (lo usa print)."""
        # :.2f -> 2 decimales en el f-string
        return f"{self.nombre} ({self.categoria}) - {self.precio_con_iva():.2f} € IVA incl."

    def __repr__(self):
        """Texto técnico: cómo se crearía este objeto."""
        return (f"Producto('{self.nombre}', {self.precio}, "
                f"'{self.categoria}', {self.__stock})")


# ---------------------------------------------------------------
# PASO 2: Clase Carrito.
# ---------------------------------------------------------------
class Carrito:
    """Carrito de la compra: guarda cada producto con su cantidad."""

    def __init__(self, cliente):
        """Constructor: guarda los datos iniciales del objeto."""
        self.cliente = cliente
        # Diccionario: clave = nombre del producto, valor = [producto, cantidad]
        self.__lineas = {}

    def agregar(self, producto, cantidad=1):
        """Añade un producto si la cantidad es válida y hay stock."""
        if not (1 <= cantidad <= 10):                # comparación encadenada
            return f"Error: cantidad {cantidad} no permitida (1-10)."
        if not producto.retirar(cantidad):
            return f"Error: no hay stock suficiente de {producto.nombre}."
        if producto.nombre in self.__lineas:
            # Ya estaba: sumamos a la cantidad (posición 1 de la lista).
            self.__lineas[producto.nombre][1] += cantidad
        else:
            self.__lineas[producto.nombre] = [producto, cantidad]
        return f"Añadido: {cantidad} x {producto.nombre}"

    def agregar_varios(self, *pares):
        """*args: cada argumento es una tupla (producto, cantidad).
        Devuelve una lista con el mensaje de cada intento."""
        mensajes = []
        for producto, cantidad in pares:   # desempaquetamos cada tupla
            mensajes.append(self.agregar(producto, cantidad))
        return mensajes

    def subtotal(self):
        """Suma de precio_con_iva * cantidad con una comprensión."""
        # .values() da cada [producto, cantidad]; lo desempaquetamos.
        return round(sum([prod.precio_con_iva() * cant
                          for prod, cant in self.__lineas.values()]), 2)

    def descuento(self, codigo):
        """Devuelve (porcentaje, mensaje) según el código. match-case con guardas."""
        total = self.subtotal()
        match codigo:
            case None:
                return 0, "Sin código"
            case "VERANO":
                return 10, "Código VERANO: 10 %"
            case "VIP" if total >= 100:       # guarda: solo si gasta 100 o más
                return 20, "Código VIP: 20 %"
            case "VIP":                        # llega aquí si la guarda falló
                return 0, "VIP requiere 100 € mínimo"
            case _:
                return 0, f"Código '{codigo}' no válido"

    def ticket(self, codigo=None):
        """Devuelve el ticket completo como string (NO lo imprime)."""
        lineas_texto = [f"TICKET de {self.cliente}"]
        # .items() da (clave, valor); el valor es [producto, cantidad].
        # enumerate añade el número delante: (1, ('Ratón', [prod, 2])).
        # Por eso desempaquetamos con paréntesis: num, (nombre, linea).
        # Formato: :<10 alinea a la izquierda en 10 huecos; :>7.2f a la
        # derecha en 7 huecos con 2 decimales (solo estética).
        for num, (nombre, linea) in enumerate(self.__lineas.items(), start=1):
            prod, cant = linea      # linea es la lista [producto, cantidad]
            importe = prod.precio_con_iva() * cant
            lineas_texto.append(f"{num}. {nombre:<10} {cant} x "
                                f"{prod.precio_con_iva():>7.2f} = {importe:>7.2f} €")
        subtotal = self.subtotal()
        porcentaje, mensaje = self.descuento(codigo)   # desempaquetar la tupla
        rebaja = round(subtotal * porcentaje / 100, 2)
        lineas_texto.append(f"Subtotal: {subtotal:.2f} €")
        lineas_texto.append(f"{mensaje} -> -{rebaja:.2f} €")
        lineas_texto.append(f"TOTAL: {subtotal - rebaja:.2f} €")
        return "\n".join(lineas_texto)   # une la lista con saltos de línea


# ---------------------------------------------------------------
# PASO 3: Funciones con lambda sobre la lista de productos.
# ---------------------------------------------------------------
def precios_con_iva(productos):
    """map + lambda: transforma cada producto en (nombre, precio con IVA)."""
    return list(map(lambda p: (p.nombre, p.precio_con_iva()), productos))


def bajo_stock(productos):
    """filter + lambda: se queda con los que tienen 5 o menos."""
    return list(filter(lambda p: p.get_stock() <= 5, productos))


def mas_caros(productos, n):
    """sorted + lambda (reverse=True) y slicing [:n] para quedarnos con n."""
    return sorted(productos, key=lambda p: p.precio, reverse=True)[:n]


def inventario_por_categoria(productos):
    """Diccionario {categoria: [nombres]}."""
    categorias = {}
    for p in productos:
        # setdefault crea la lista vacía si la clave no existe y la devuelve.
        # Equivale a (forma más básica, también válida):
        #     if p.categoria not in categorias:
        #         categorias[p.categoria] = []
        #     categorias[p.categoria].append(p.nombre)
        categorias.setdefault(p.categoria, []).append(p.nombre)
    return categorias


# ---------------------------------------------------------------
# PASO 4: Bloque principal.
# ---------------------------------------------------------------
if __name__ == "__main__":
    inventario = [
        Producto("Portátil", 650.0, "informática", 4),
        Producto("Ratón", 12.5, "informática", 30),
        Producto("Teclado", 25.0, "informática", 3),
        Producto("Silla", 89.9, "mobiliario", 0),
        Producto("Lámpara", 19.99, "mobiliario", 12),
    ]

    print("--- Inventario ---")
    for num, p in enumerate(inventario, start=1):
        print(f"{num}. {p} | {p.ver_stock()}")

    print("\nPrecios con IVA (map):", precios_con_iva(inventario))
    print("Bajo stock (filter):", [p.nombre for p in bajo_stock(inventario)])
    print("Los 2 más caros (sorted):", mas_caros(inventario, 2))

    print("\n--- Por categoría (.items()) ---")
    for categoria, nombres in inventario_por_categoria(inventario).items():
        print(f"{categoria}: {', '.join(nombres)}")

    portatil, raton, teclado, silla, lampara = inventario

    print("\n--- Carrito de Ana ---")
    carrito_ana = Carrito("Ana")
    for mensaje in carrito_ana.agregar_varios((portatil, 1), (raton, 2),
                                              (silla, 1), (raton, 15)):
        print(mensaje)
    print(carrito_ana.ticket("VIP"))

    print("\n--- Carrito de Luis ---")
    carrito_luis = Carrito("Luis")
    print(carrito_luis.agregar(teclado, 2))
    print(carrito_luis.agregar(teclado, 2))     # solo queda 1
    print(carrito_luis.agregar(lampara))         # cantidad por defecto = 1
    print(carrito_luis.ticket("VIP"))

    print("\n--- Stock tras las compras ---")
    for p in inventario:
        print(p.ver_stock())

# ---------------------------------------------------------------
# SALIDA ESPERADA (copiada de la ejecución real):
# --- Inventario ---
# 1. Portátil (informática) - 786.50 € IVA incl. | Portátil: 4 uds (stock bajo)
# 2. Ratón (informática) - 15.12 € IVA incl. | Ratón: 30 uds (disponible)
# 3. Teclado (informática) - 30.25 € IVA incl. | Teclado: 3 uds (stock bajo)
# 4. Silla (mobiliario) - 108.78 € IVA incl. | Silla: 0 uds (agotado)
# 5. Lámpara (mobiliario) - 24.19 € IVA incl. | Lámpara: 12 uds (disponible)
#
# Precios con IVA (map): [('Portátil', 786.5), ('Ratón', 15.12), ('Teclado', 30.25), ('Silla', 108.78), ('Lámpara', 24.19)]
# Bajo stock (filter): ['Portátil', 'Teclado', 'Silla']
# Los 2 más caros (sorted): [Producto('Portátil', 650.0, 'informática', 4), Producto('Silla', 89.9, 'mobiliario', 0)]
#
# --- Por categoría (.items()) ---
# informática: Portátil, Ratón, Teclado
# mobiliario: Silla, Lámpara
#
# --- Carrito de Ana ---
# Añadido: 1 x Portátil
# Añadido: 2 x Ratón
# Error: no hay stock suficiente de Silla.
# Error: cantidad 15 no permitida (1-10).
# TICKET de Ana
# 1. Portátil   1 x  786.50 =  786.50 €
# 2. Ratón      2 x   15.12 =   30.24 €
# Subtotal: 816.74 €
# Código VIP: 20 % -> -163.35 €
# TOTAL: 653.39 €
#
# --- Carrito de Luis ---
# Añadido: 2 x Teclado
# Error: no hay stock suficiente de Teclado.
# Añadido: 1 x Lámpara
# TICKET de Luis
# 1. Teclado    2 x   30.25 =   60.50 €
# 2. Lámpara    1 x   24.19 =   24.19 €
# Subtotal: 84.69 €
# VIP requiere 100 € mínimo -> -0.00 €
# TOTAL: 84.69 €
#
# --- Stock tras las compras ---
# Portátil: 3 uds (stock bajo)
# Ratón: 28 uds (disponible)
# Teclado: 1 uds (stock bajo)
# Silla: 0 uds (agotado)
# Lámpara: 11 uds (disponible)
# ---------------------------------------------------------------
# RESPUESTA A LA CUESTIÓN TEÓRICA:
# - El IVA es el mismo para todos los productos: guardarlo una vez en la
#   clase evita repetirlo en cada objeto. Si sube al 23 %, basta con
#   Producto.IVA = 0.23 y TODOS los productos lo usan al instante.
# - Si se hiciera portatil.IVA = 0.23, solo ese objeto tendría un
#   atributo de instancia nuevo que "tapa" al de la clase.
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - En un patrón de match, "case VIP:" sin comillas NO compara con un
#   texto: captura cualquier valor en una variable llamada VIP (y si no
#   es el último case, Python da SyntaxError).
# - El orden importa: "case 'VIP' if ..." tiene que ir ANTES de "case 'VIP'".
# - round(x, 2) para dinero; en el f-string :.2f solo cambia cómo se ve.
# EN JAVA SERÍA... static final double IVA = 0.21;
# ALTERNATIVA (funciona, pero NO es lo que pide el enunciado):
#   subtotal con un for y un acumulador total += ... -> pide comprensión.
#   [p for p in productos if p.get_stock() <= 5]     -> pide filter+lambda.
# ---------------------------------------------------------------
