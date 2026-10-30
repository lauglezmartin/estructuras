"""
=============================================================================
 PLANTILLA DE EXAMEN EXPLICADA PASO A PASO
=============================================================================
CÓMO USAR ESTE ARCHIVO EN EL EXAMEN
-----------------------------------
Casi todos los ejercicios del profesor (Teletubbies, cafetería...) tienen
SIEMPRE las mismas 3 partes:

    PARTE A -> UNA CLASE      (el "molde" de cada cosa: un producto, un
                                Teletubby, un alumno...)
    PARTE B -> FUNCIONES      (fuera de la clase, reciben objetos o datos
                                y DEVUELVEN algo con return)
    PARTE C -> BLOQUE MAIN    (if __name__ == "__main__": aquí se crean los
                                objetos, se meten en una lista y se prueba
                                todo)

Este archivo resuelve el ejercicio de la CAFETERÍA, explicado línea a línea.
Para tu ejercicio del examen:
    1. Lee el enunciado y subraya cada requisito numerado.
    2. Busca aquí el bloque que se parece (Ctrl+F con la palabra clave:
       "privado", "getter", "match", "enumerate", "lambda", "diccionario"...).
    3. Copia el bloque y cambia SOLO lo marcado con   # <-- CAMBIA
    4. Ejecuta después de cada parte. No lo dejes todo para el final.

Ejecutar:  python PLANTILLA_EXAMEN_EXPLICADA.py   (Linux/Docker: python3 ...)
"""


# =============================================================================
# PARTE A - LA CLASE
# =============================================================================
# Una clase es un MOLDE. Con el molde "Producto" fabricas muchos productos
# (café, zumo...). Cada producto fabricado se llama OBJETO o INSTANCIA.
# En Java sería:  public class Producto { ... }
# Nombre de la clase: SIEMPRE en PascalCase (cada palabra con mayúscula).

class Producto:                                   # <-- CAMBIA el nombre
    """Representa un producto de la cafetería."""  # docstring: el profe lo exige

    # -------------------------------------------------------------------------
    # A.1 ATRIBUTO DE CLASE
    # -------------------------------------------------------------------------
    # Va AQUÍ, dentro de la clase pero FUERA de cualquier método, sin self.
    # Es UNO solo y lo COMPARTEN todos los objetos (como "static" en Java).
    # Se usa así:  Producto.iva   o   self.iva
    # Enunciado típico: "Crea una variable de clase llamada X con valor Y".
    iva = 0.07                                    # <-- CAMBIA nombre y valor

    # -------------------------------------------------------------------------
    # A.2 CONSTRUCTOR  __init__
    # -------------------------------------------------------------------------
    # Se ejecuta SOLO al crear un objeto:  cafe = Producto("Café", "bebida", 1.2)
    # - self = "este objeto" (como this en Java). SIEMPRE es el 1.er parámetro
    #   de todos los métodos, pero al LLAMAR al método no se escribe.
    # - Los parámetros con "= valor" son OPCIONALES y van SIEMPRE al final.
    def __init__(self, nombre, categoria, precio, stock=10):  # <-- CAMBIA
        """Crea un producto con su nombre, categoría, precio y stock."""
        # ATRIBUTOS PÚBLICOS: self.nombre -> se puede leer desde fuera.
        self.nombre = nombre
        self.categoria = categoria
        # ATRIBUTOS PRIVADOS: empiezan por DOS guiones bajos  __
        # Desde fuera de la clase NO se pueden usar (como "private" en Java).
        self.__precio = precio
        self.__stock = stock
        # OJO: si el enunciado dice "privado con valor por defecto 50" y NO
        # lo pasa como parámetro, se escribe directamente:
        #     self.__nivel_hambre = 50

    # -------------------------------------------------------------------------
    # A.3 GETTER  (método que DEVUELVE un atributo privado)
    # -------------------------------------------------------------------------
    # Como desde fuera no se puede leer self.__precio, creamos un método que
    # lo DEVUELVE con return. Enunciado típico: "getter que devuelve...".
    def get_precio(self):                         # <-- CAMBIA el nombre
        """Devuelve el precio sin IVA."""
        return self.__precio

    def get_stock(self):
        """Devuelve el stock actual."""
        return self.__stock

    # -------------------------------------------------------------------------
    # A.4 SETTER  (método que CAMBIA un atributo privado, validando)
    # -------------------------------------------------------------------------
    # Solo si lo piden. Sirve para no dejar meter valores absurdos.
    def set_precio(self, nuevo_precio):
        """Cambia el precio solo si es mayor que 0."""
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Precio no válido")

    # -------------------------------------------------------------------------
    # A.5 MÉTODO QUE CALCULA Y DEVUELVE  (return, NO print)
    # -------------------------------------------------------------------------
    # Si el enunciado dice "DEVUELVE" -> return.  Si dice "IMPRIME" -> print.
    # round(numero, 2) redondea a 2 decimales.
    def precio_con_iva(self):
        """Devuelve el precio con IVA redondeado a 2 decimales."""
        return round(self.__precio * (1 + Producto.iva), 2)

    # -------------------------------------------------------------------------
    # A.6 MÉTODO QUE MODIFICA EL OBJETO + CLÁUSULA DE GUARDA
    # -------------------------------------------------------------------------
    # CLÁUSULA DE GUARDA = comprobar PRIMERO lo que está mal y salir con
    # return. Así el resto del código no queda metido dentro de muchos if.
    def vender(self, cantidad):
        """Resta del stock la cantidad vendida si es posible."""
        # 1) Guarda: si el dato es malo, aviso y salgo.
        if cantidad <= 0:
            print("Cantidad no válida")
            return                    # return solo = "sal del método ya"
        # 2) Otra guarda: no hay suficiente.
        if cantidad > self.__stock:
            print(f"No hay stock de {self.nombre}")
            return
        # 3) Caso bueno: ya sé que todo está bien.
        self.__stock -= cantidad      # igual que: self.__stock = self.__stock - cantidad
        print(f"Vendidos {cantidad} de {self.nombre}")

    # -------------------------------------------------------------------------
    # A.7 __str__  (lo que sale al hacer print(objeto))
    # -------------------------------------------------------------------------
    # SIEMPRE con return de un texto (si haces print dentro -> error).
    # Copia EXACTAMENTE el formato del ejemplo del enunciado.
    # {numero:.2f} = mostrar SIEMPRE 2 decimales (1.2 -> "1.20").
    # En Java sería:  public String toString()
    def __str__(self):
        """Texto amigable: Café (bebida) - 1.20 €"""
        return f"{self.nombre} ({self.categoria}) - {self.__precio:.2f} €"

    # -------------------------------------------------------------------------
    # A.8 __repr__  (texto "técnico": cómo se creó el objeto)
    # -------------------------------------------------------------------------
    # Sale al imprimir una LISTA de objetos:  print(lista)
    # !r pone comillas a los textos: 'Café'
    def __repr__(self):
        """Texto técnico: Producto('Café', 'bebida', 1.2)"""
        return f"Producto({self.nombre!r}, {self.categoria!r}, {self.__precio})"


# =============================================================================
# PARTE B - FUNCIONES (fuera de la clase, SIN sangría, SIN self)
# =============================================================================

# -----------------------------------------------------------------------------
# B.1 match-case CON GUARDAS + COMPARACIÓN ENCADENADA, que DEVUELVE un texto
# -----------------------------------------------------------------------------
# match = el "switch" de Java.  "case p if condición:" = caso con condición.
# Se comprueban EN ORDEN, de arriba abajo; entra en el PRIMERO que se cumpla.
# case _  = "cualquier otro caso" (como default). SIEMPRE el último.
# Comparación encadenada: 1.5 <= p < 3   (el profe NO quiere: p >= 1.5 and p < 3)
def valorar_precio(producto):
    """Devuelve 'barato', 'normal' o 'caro' según el precio sin IVA."""
    precio = producto.get_precio()     # el precio es privado -> uso el getter
    match precio:
        case p if p < 1.5:
            return "barato"
        case p if 1.5 <= p < 3:
            return "normal"
        case _:
            return "caro"


# -----------------------------------------------------------------------------
# B.2 *args (número variable de argumentos) + acumulador SIN sum()
# -----------------------------------------------------------------------------
# *productos recoge TODOS los argumentos en una tupla (como una lista).
# Se llama así:  total_carta(cafe, zumo)   o con una lista:  total_carta(*lista)
def total_carta(*productos):
    """Devuelve la suma de los precios con IVA (sin usar sum)."""
    total = 0                          # 1) acumulador empieza en 0 ANTES del for
    for producto in productos:         # 2) recorro uno a uno
        total += producto.precio_con_iva()   # 3) voy sumando
    return round(total, 2)             # 4) return FUERA del for (¡sin sangría extra!)


# -----------------------------------------------------------------------------
# B.3 **kwargs (argumentos con nombre variables) -> llegan como DICCIONARIO
# -----------------------------------------------------------------------------
# Se llama así:  crear_ficha("Ana", edad=20, ciudad="Adeje")
def crear_ficha(nombre, **datos):
    """Devuelve un diccionario con el nombre y todos los datos extra."""
    ficha = {"nombre": nombre}
    for clave, valor in datos.items():      # .items() da (clave, valor)
        ficha[clave] = valor
    return ficha


# -----------------------------------------------------------------------------
# B.4 BUSCAR un objeto en una lista por su nombre
# -----------------------------------------------------------------------------
def buscar_producto(lista, nombre):
    """Devuelve el producto con ese nombre, o None si no está."""
    for producto in lista:
        if producto.nombre.lower() == nombre.lower():   # ignora mayúsculas
            return producto            # lo encontré -> salgo devolviéndolo
    return None                        # terminé el for y no estaba


# -----------------------------------------------------------------------------
# B.5 PEDIR UN NÚMERO AL USUARIO SIN QUE EL PROGRAMA PETE
# -----------------------------------------------------------------------------
# input() SIEMPRE devuelve texto (str). Para números hay que convertir.
# Si escriben letras, int("hola") da ValueError -> lo capturamos.
def pedir_entero(mensaje):
    """Pide un número entero hasta que el usuario escriba uno válido."""
    while True:                         # repite para siempre...
        texto = input(mensaje)
        try:
            return int(texto)           # ...hasta que la conversión funcione
        except ValueError:
            print("Eso no es un número, prueba otra vez")


# -----------------------------------------------------------------------------
# B.6 MENÚ con while True + match-case (solo si piden un menú)
# -----------------------------------------------------------------------------
def menu(lista):
    """Menú interactivo para listar y vender productos."""
    while True:
        print("\n1. Listar  2. Vender  0. Salir")
        opcion = input("Opción: ").strip()     # strip() quita espacios
        match opcion:                          # opcion es TEXTO -> case "1"
            case "1":
                for producto in lista:
                    print(producto)
            case "2":
                nombre = input("¿Qué producto? ")
                producto = buscar_producto(lista, nombre)
                if producto is None:
                    print("No existe ese producto")
                else:
                    producto.vender(pedir_entero("¿Cuántos? "))
            case "0":
                print("¡Adiós!")
                break                          # break = salir del while
            case _:
                print("Opción no válida")


# =============================================================================
# PARTE C - BLOQUE PRINCIPAL
# =============================================================================
# Todo lo que va aquí dentro se ejecuta al lanzar el archivo.
# Es como el "public static void main" de Java. El profe lo exige.
if __name__ == "__main__":

    # -------------------------------------------------------------------------
    # C.1 CREAR OBJETOS y meterlos en una LISTA
    # -------------------------------------------------------------------------
    # NombreClase(parámetros en el MISMO orden que el __init__, SIN self)
    productos = [
        Producto("Café", "bebida", 1.20),
        Producto("Zumo", "bebida", 2.10),
        Producto("Bocadillo", "comida", 3.50),
        Producto("Donut", "comida", 1.40),
        Producto("Batido", "bebida", 2.80),
    ]
    # También vale uno a uno:  cafe = Producto("Café", "bebida", 1.20)
    #                          productos.append(cafe)

    # -------------------------------------------------------------------------
    # C.2 RECORRER la lista NUMERADA desde 1  -> enumerate(lista, start=1)
    # -------------------------------------------------------------------------
    # enumerate da DOS cosas en cada vuelta: el número y el objeto.
    print("=== Carta ===")
    for numero, producto in enumerate(productos, start=1):
        # print(producto) dentro de un f-string usa automáticamente __str__
        print(f"{numero}. {producto} -> {valorar_precio(producto)}")

    # -------------------------------------------------------------------------
    # C.3 COMPRENSIÓN DE LISTAS  [qué_guardo  for x in lista  if condición]
    # -------------------------------------------------------------------------
    # Léelo así: "guarda p.nombre, para cada p de productos, si es bebida".
    bebidas = [p.nombre for p in productos if p.categoria == "bebida"]
    print("\nBebidas:", bebidas)
    # Lo mismo con for normal (funciona, pero si piden comprensión NO vale):
    #   bebidas = []
    #   for p in productos:
    #       if p.categoria == "bebida":
    #           bebidas.append(p.nombre)

    # Comprensión que TRANSFORMA (sin if): precios con IVA de todos
    precios_iva = [p.precio_con_iva() for p in productos]
    print("Precios con IVA:", precios_iva)

    # -------------------------------------------------------------------------
    # C.4 ORDENAR con sorted + lambda
    # -------------------------------------------------------------------------
    # lambda p: p.get_precio()  = "función mini: dado p, devuelve su precio".
    # key = por qué se ordena.   reverse=True = de MAYOR a menor.
    # sorted() devuelve una lista NUEVA; la original no cambia.
    ordenados = sorted(productos, key=lambda p: p.get_precio(), reverse=True)
    print("\nDe más caro a más barato:", [p.nombre for p in ordenados])

    # Ordenar alfabéticamente por nombre:
    por_nombre = sorted(productos, key=lambda p: p.nombre)
    print("Por nombre:", [p.nombre for p in por_nombre])

    # -------------------------------------------------------------------------
    # C.5 MÁXIMO / MÍNIMO con lambda
    # -------------------------------------------------------------------------
    mas_caro = max(productos, key=lambda p: p.get_precio())
    mas_barato = min(productos, key=lambda p: p.get_precio())
    print(f"\nMás caro: {mas_caro.nombre} | Más barato: {mas_barato.nombre}")

    # -------------------------------------------------------------------------
    # C.6 filter y map con lambda (si los piden expresamente)
    # -------------------------------------------------------------------------
    # filter: se queda con los que cumplen.  map: transforma cada uno.
    # Hay que envolverlos en list(...) para ver el resultado.
    comidas = list(filter(lambda p: p.categoria == "comida", productos))
    nombres_mayus = list(map(lambda p: p.nombre.upper(), productos))
    print("Comidas:", [p.nombre for p in comidas])
    print("En mayúsculas:", nombres_mayus)

    # -------------------------------------------------------------------------
    # C.7 DICCIONARIO con comprensión + recorrerlo con .items()
    # -------------------------------------------------------------------------
    # {clave: valor  for x in lista}
    carta = {p.nombre: p.precio_con_iva() for p in productos}
    print("\n=== Precios con IVA ===")
    for nombre, precio in carta.items():          # .items() -> (clave, valor)
        print(f"{nombre}: {precio:.2f} €")

    # Operaciones típicas de diccionario:
    print("Precio del zumo:", carta["Zumo"])            # leer (error si no existe)
    print("¿Hay té?:", carta.get("Té", "no hay"))        # leer seguro con get
    carta["Té"] = 1.50                                   # añadir o modificar
    del carta["Té"]                                      # borrar
    print("¿Está el Café?:", "Café" in carta)            # comprobar si existe

    # Contar cuántos hay de cada categoría (patrón CONTADOR con diccionario)
    por_categoria = {}
    for p in productos:
        if p.categoria in por_categoria:
            por_categoria[p.categoria] += 1
        else:
            por_categoria[p.categoria] = 1
    print("Productos por categoría:", por_categoria)

    # -------------------------------------------------------------------------
    # C.8 LLAMAR A MÉTODOS que modifican y comprobar el resultado
    # -------------------------------------------------------------------------
    print("\n=== Ventas ===")
    donut = buscar_producto(productos, "donut")
    donut.vender(3)       # bien
    donut.vender(20)      # no hay stock
    donut.vender(-1)      # cantidad no válida
    print("Stock de donuts:", donut.get_stock())

    # -------------------------------------------------------------------------
    # C.9 LLAMAR a una función con *args pasándole una lista entera
    # -------------------------------------------------------------------------
    # El * "desempaqueta" la lista: es como escribir cada producto separado.
    print("\nTotal carta:", total_carta(*productos), "€")

    # -------------------------------------------------------------------------
    # C.10 **kwargs, atributo de clase, __repr__
    # -------------------------------------------------------------------------
    print("\nFicha:", crear_ficha("Laura", edad=20, ciudad="Adeje"))
    print("IVA de todos los productos:", Producto.iva)
    print("Lista con __repr__:", productos[:2])

    # -------------------------------------------------------------------------
    # C.11 DEMOSTRAR que lo privado es privado (pregunta teórica típica)
    # -------------------------------------------------------------------------
    try:
        print(donut.__precio)
    except AttributeError as error:
        print("\nError al leer el privado:", error)

    # Menú interactivo: quita el # de la línea siguiente para probarlo.
    # menu(productos)


# =============================================================================
# RESPUESTA A LA PREGUNTA TEÓRICA (cópiala adaptando el nombre del atributo)
# =============================================================================
# ¿Por qué __precio es privado y qué pasa si hago print(cafe.__precio)?
#
# El atributo es privado (empieza por __) para ENCAPSULAR el dato: así nadie
# puede cambiarlo desde fuera con valores incorrectos y solo se modifica a
# través de los métodos de la clase (getters, setters, vender...), que
# controlan que el cambio sea válido.
# Si escribo print(cafe.__precio) desde el bloque principal, Python da
# AttributeError, porque internamente renombra el atributo a
# _Producto__precio (esto se llama "name mangling"). Y si hiciera
# cafe.__precio = 5, NO cambiaría el precio privado: crearía un atributo
# nuevo distinto. Por eso se usa el getter get_precio().
# =============================================================================

# =============================================================================
# SALIDA AL EJECUTAR
# =============================================================================
# === Carta ===
# 1. Café (bebida) - 1.20 € -> barato
# 2. Zumo (bebida) - 2.10 € -> normal
# 3. Bocadillo (comida) - 3.50 € -> caro
# 4. Donut (comida) - 1.40 € -> barato
# 5. Batido (bebida) - 2.80 € -> normal
#
# Bebidas: ['Café', 'Zumo', 'Batido']
# Precios con IVA: [1.28, 2.25, 3.75, 1.5, 3.0]
#
# De más caro a más barato: ['Bocadillo', 'Batido', 'Zumo', 'Donut', 'Café']
# Por nombre: ['Batido', 'Bocadillo', 'Café', 'Donut', 'Zumo']
#
# Más caro: Bocadillo | Más barato: Café
# Comidas: ['Bocadillo', 'Donut']
# En mayúsculas: ['CAFÉ', 'ZUMO', 'BOCADILLO', 'DONUT', 'BATIDO']
#
# === Precios con IVA ===
# Café: 1.28 €
# Zumo: 2.25 €
# Bocadillo: 3.75 €
# Donut: 1.50 €
# Batido: 3.00 €
# Precio del zumo: 2.25
# ¿Hay té?: no hay
# ¿Está el Café?: True
# Productos por categoría: {'bebida': 3, 'comida': 2}
#
# === Ventas ===
# Vendidos 3 de Donut
# No hay stock de Donut
# Cantidad no válida
# Stock de donuts: 7
#
# Total carta: 11.78 €
#
# Ficha: {'nombre': 'Laura', 'edad': 20, 'ciudad': 'Adeje'}
# IVA de todos los productos: 0.07
# Lista con __repr__: [Producto('Café', 'bebida', 1.2), Producto('Zumo', 'bebida', 2.1)]
#
# Error al leer el privado: 'Producto' object has no attribute '__precio'
# =============================================================================


# =============================================================================
# CHULETA EXPRÉS: "SI EL ENUNCIADO DICE... -> ESCRIBO..."
# =============================================================================
# "variable/atributo de clase"        -> debajo de class, sin self: iva = 0.07
# "atributo privado"                  -> self.__nombre
# "por defecto X" (sin parámetro)     -> self.__hambre = 50 dentro de __init__
# "getter" / "devuelve el estado"     -> def get_x(self): return self.__x
# "devuelve" / "retorna"              -> return   (NO print)
# "muestra" / "imprime"               -> print
# "numerados desde 1"                 -> for i, x in enumerate(lista, start=1):
# "en una línea" / "comprensión"      -> [x.algo for x in lista if ...]
# "diccionario por comprensión"       -> {x.nombre: x.valor for x in lista}
# "recorre el diccionario"            -> for clave, valor in dic.items():
# "ordena" + "lambda"                 -> sorted(lista, key=lambda x: x.campo)
# "de mayor a menor"                  -> reverse=True
# "el mayor/menor"                    -> max(lista, key=lambda x: x.campo)
# "map con lambda"                    -> list(map(lambda x: ..., lista))
# "filter con lambda"                 -> list(filter(lambda x: ..., lista))
# "match-case" / "con guardas"        -> case p if condicion:  + case _:
# "rango" / "entre X e Y"             -> X <= valor <= Y   (NO and)
# "cláusula de guarda"                -> if malo: print(...); return  al principio
# "número variable de argumentos"     -> def f(*args):
# "argumentos con nombre variables"   -> def f(**kwargs):   -> kwargs.items()
# "sin usar sum()"                    -> total = 0; for...: total += ...
# "hasta que" / "repetir mientras"    -> while condición:   /   while True + break
# "salta" / "no imprimas los X"       -> continue
# "si no lo encuentra" (tras buscar)  -> for ... else:
# __str__                             -> return f"..." con el formato EXACTO
# Bloque principal                    -> if __name__ == "__main__":
# =============================================================================
