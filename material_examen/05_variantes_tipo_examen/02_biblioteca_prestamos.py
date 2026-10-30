"""
TEMA 6 (integrador) - Variante 02: "La biblioteca del instituto"
================================================================
ENUNCIADO (redactado al estilo del profesor, modelo Teletubbies):

    Objetivo: Gestionar los libros y los préstamos de una biblioteca usando
    dos clases que colaboran, una lista de objetos y un diccionario de socios.

    Requisitos de la clase Libro:
    1. Atributo de clase: total_libros (contador de libros creados).
    2. Atributos públicos: isbn, titulo, autor, anio (int).
       Atributo privado: __disponible (bool, True al crearse).
    3. esta_disponible(): getter que devuelve el booleano.
       marcar_prestado() y marcar_devuelto(): cambian __disponible.
    4. epoca(): MATCH-CASE con GUARDAS sobre el año:
       antes de 1900 -> "Clásico"; de 1900 a 1999 (COMPARACIÓN ENCADENADA)
       -> "Siglo XX"; 2000 en adelante -> "Contemporáneo".
    5. __str__ (amigable con estado) y __repr__ (técnico).

    Requisitos de la clase Socio:
    6. Atributo de clase: max_prestamos = 2.
    7. Atributos: nombre (público), __libros (lista privada de ISBN).
    8. puede_pedir(): devuelve True si aún no ha llegado al máximo.
       ver_prestamos(): GETTER que DEVUELVE un string con sus préstamos.

    Requisitos de la clase Biblioteca:
    9. Atributos: __catalogo (lista de Libro) y __socios (dict nombre -> Socio).
    10. alta_libro(**datos): crea el Libro con **kwargs y lo añade.
    11. buscar_libro(isbn): recorre con for ... ELSE (el else se ejecuta si
        el bucle no encontró nada y no hubo break). Devuelve el libro o None.
    12. prestar(isbn, nombre_socio): CLÁUSULAS DE GUARDA (return temprano)
        para: socio inexistente, libro inexistente, libro no disponible,
        socio con el máximo. Devuelve SIEMPRE un string (no print).
    13. devolver(isbn, nombre_socio): devuelve un string.
    14. disponibles(): COMPRENSIÓN DE LISTAS con los títulos disponibles.
    15. libros_de(autor): FILTER + LAMBDA.
    16. ordenados_por_anio(): SORTED + LAMBDA.
    17. libros_por_epoca(): DICCIONARIO {época: número de libros}.

    Bloque principal: alta de 5 libros con **kwargs, 2 socios, préstamos
    correctos y erróneos (todos los casos de guarda), devolución, listados
    con enumerate(start=1) y recorrido del diccionario con .items().

    Cuestión teórica: ¿Qué diferencia hay entre for-else y poner el else
    dentro del for? ¿Por qué __catalogo es privado?

FORMA QUE EXIGE EL PROFESOR:
    - **kwargs en alta_libro, for-else en buscar_libro.
    - Cláusulas de guarda con return temprano en prestar.
    - match-case con guardas + comparación encadenada en epoca.
    - Comprensión de listas, filter+lambda, sorted+lambda, dict con .items().

CONCEPTOS QUE PRACTICA:
    - Varias clases que colaboran (composición), atributos privados
    - Diccionario de objetos, lista de objetos, for-else, **kwargs

CÓMO EJECUTARLO:  python 02_biblioteca_prestamos.py   (en Linux: python3 ...)
"""


# ---------------------------------------------------------------
# PASO 1: Clase Libro.
# ---------------------------------------------------------------
class Libro:
    """Un libro del catálogo."""

    total_libros = 0  # atributo de clase (contador)

    def __init__(self, isbn, titulo, autor, anio):
        """Guarda los datos del libro. Al crearse está disponible."""
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.__disponible = True  # privado: solo lo cambian los métodos
        Libro.total_libros += 1

    def esta_disponible(self):
        """Getter: devuelve True si se puede prestar."""
        return self.__disponible

    def marcar_prestado(self):
        """Pone el libro como prestado."""
        self.__disponible = False

    def marcar_devuelto(self):
        """Pone el libro como disponible otra vez."""
        self.__disponible = True

    def epoca(self):
        """Clasifica el libro por su año con match-case y guardas."""
        # Aquí hacemos match sobre el propio año: "case a if ..." captura el
        # valor en la variable a y luego comprueba la guarda.
        match self.anio:
            case a if a < 1900:
                return "Clásico"
            case a if 1900 <= a <= 1999:   # comparación encadenada
                return "Siglo XX"
            case _:
                return "Contemporáneo"

    def __str__(self):
        """Texto amigable para el usuario."""
        # Expresión condicional (ternario de Python): VALOR_SI if COND else VALOR_NO
        estado = "disponible" if self.__disponible else "PRESTADO"
        return f"'{self.titulo}' de {self.autor} ({self.anio}) - {estado}"

    def __repr__(self):
        """Texto técnico: cómo se crearía este objeto."""
        return f"Libro('{self.isbn}', '{self.titulo}', '{self.autor}', {self.anio})"


# ---------------------------------------------------------------
# PASO 2: Clase Socio.
# ---------------------------------------------------------------
class Socio:
    """Un socio que puede tener libros prestados."""

    max_prestamos = 2  # atributo de clase: el límite es igual para todos

    def __init__(self, nombre):
        """Crea el socio sin préstamos."""
        self.nombre = nombre
        # Lista privada creada DENTRO de __init__: cada socio tiene la suya.
        # (Nunca pongas def __init__(self, nombre, libros=[]): se comparte.)
        self.__libros = []

    def puede_pedir(self):
        """Devuelve True si no ha llegado al máximo de préstamos."""
        return len(self.__libros) < Socio.max_prestamos

    def anotar(self, isbn):
        """Apunta un préstamo."""
        self.__libros.append(isbn)

    def tiene(self, isbn):
        """Devuelve True si el socio tiene ese libro."""
        return isbn in self.__libros

    def quitar(self, isbn):
        """Borra un préstamo."""
        self.__libros.remove(isbn)

    def ver_prestamos(self):
        """GETTER que devuelve un string con los préstamos del socio."""
        if not self.__libros:
            return f"{self.nombre} no tiene préstamos."
        return f"{self.nombre} tiene: {', '.join(self.__libros)}"

    def __str__(self):
        """Texto amigable para el usuario (lo usa print)."""
        return f"Socio {self.nombre} ({len(self.__libros)}/{Socio.max_prestamos})"

    def __repr__(self):
        """Texto técnico: cómo se crearía este objeto."""
        return f"Socio('{self.nombre}')"


# ---------------------------------------------------------------
# PASO 3: Clase Biblioteca: contiene la lista de libros y el dict de socios.
# ---------------------------------------------------------------
class Biblioteca:
    """Gestiona el catálogo y los préstamos."""

    def __init__(self, nombre):
        """Constructor: guarda los datos iniciales del objeto."""
        self.nombre = nombre
        self.__catalogo = []   # lista de objetos Libro
        self.__socios = {}     # diccionario: clave nombre -> valor objeto Socio

    def alta_libro(self, **datos):
        """Crea un libro a partir de argumentos con nombre (**kwargs)."""
        # datos es un diccionario: {'isbn': ..., 'titulo': ..., ...}
        # Libro(**datos) "desempaqueta" el dict en argumentos con nombre.
        libro = Libro(**datos)
        self.__catalogo.append(libro)
        return libro

    def alta_socio(self, nombre):
        """Añade un socio al diccionario."""
        self.__socios[nombre] = Socio(nombre)

    def obtener_socio(self, nombre):
        """Devuelve el socio o None (dict.get no da error si no existe)."""
        return self.__socios.get(nombre)

    def buscar_libro(self, isbn):
        """Busca un libro por ISBN con for-else."""
        for libro in self.__catalogo:
            if libro.isbn == isbn:
                encontrado = libro
                break             # al hacer break, el else NO se ejecuta
        else:
            encontrado = None     # solo llega aquí si el for terminó sin break
        return encontrado

    def prestar(self, isbn, nombre_socio):
        """Presta un libro. Usa cláusulas de guarda (return temprano)."""
        socio = self.obtener_socio(nombre_socio)
        # Cada "if ...: return" corta la función en cuanto algo falla.
        # Así evitamos if anidados y el caso bueno queda al final, limpio.
        if socio is None:
            return f"Error: el socio '{nombre_socio}' no existe."
        libro = self.buscar_libro(isbn)
        if libro is None:
            return f"Error: no hay ningún libro con ISBN {isbn}."
        if not libro.esta_disponible():
            return f"Error: '{libro.titulo}' ya está prestado."
        if not socio.puede_pedir():
            return f"Error: {socio.nombre} ya tiene {Socio.max_prestamos} libros."
        # Caso correcto:
        libro.marcar_prestado()
        socio.anotar(isbn)
        return f"Préstamo OK: '{libro.titulo}' para {socio.nombre}."

    def devolver(self, isbn, nombre_socio):
        """Devuelve un libro prestado."""
        socio = self.obtener_socio(nombre_socio)
        libro = self.buscar_libro(isbn)
        if socio is None or libro is None or not socio.tiene(isbn):
            return "Error: devolución no válida."
        socio.quitar(isbn)
        libro.marcar_devuelto()
        return f"Devolución OK: '{libro.titulo}'."

    def disponibles(self):
        """Comprensión de listas: títulos de los libros disponibles."""
        return [libro.titulo for libro in self.__catalogo if libro.esta_disponible()]

    def libros_de(self, autor):
        """filter + lambda: libros de un autor. filter devuelve un iterador,
        por eso lo convertimos con list()."""
        return list(filter(lambda libro: libro.autor == autor, self.__catalogo))

    def ordenados_por_anio(self):
        """sorted + lambda: copia del catálogo ordenada por año."""
        return sorted(self.__catalogo, key=lambda libro: libro.anio)

    def libros_por_epoca(self):
        """Diccionario {época: cantidad} contando con .get(clave, 0)."""
        conteo = {}
        for libro in self.__catalogo:
            epoca = libro.epoca()
            # get(epoca, 0): si la clave aún no existe empieza en 0.
            conteo[epoca] = conteo.get(epoca, 0) + 1
        return conteo


# ---------------------------------------------------------------
# PASO 4: Bloque principal con datos fijos (sin input).
# ---------------------------------------------------------------
if __name__ == "__main__":
    bib = Biblioteca("IES Las Galletas")

    # **kwargs: los argumentos van con nombre, en cualquier orden.
    bib.alta_libro(isbn="111", titulo="Don Quijote", autor="Cervantes", anio=1605)
    bib.alta_libro(isbn="222", titulo="Cien años de soledad",
                   autor="García Márquez", anio=1967)
    bib.alta_libro(isbn="333", titulo="Novelas ejemplares", autor="Cervantes", anio=1613)
    bib.alta_libro(titulo="Python para todos", autor="Severance",
                   anio=2016, isbn="444")
    bib.alta_libro(isbn="555", titulo="El túnel", autor="Sabato", anio=1948)

    bib.alta_socio("Ana")
    bib.alta_socio("Luis")

    print("--- Préstamos ---")
    print(bib.prestar("111", "Ana"))
    print(bib.prestar("444", "Ana"))
    print(bib.prestar("222", "Ana"))     # guarda: Ana ya tiene 2
    print(bib.prestar("111", "Luis"))    # guarda: ya prestado
    print(bib.prestar("999", "Luis"))    # guarda: ISBN inexistente
    print(bib.prestar("222", "Marta"))   # guarda: socio inexistente
    print(bib.prestar("222", "Luis"))

    print("\n--- Estado de los socios ---")
    for nombre in ("Ana", "Luis"):
        print(bib.obtener_socio(nombre).ver_prestamos())

    print("\n--- Devolución ---")
    print(bib.devolver("111", "Ana"))
    print(bib.devolver("111", "Ana"))    # ya no lo tiene
    print(bib.obtener_socio("Ana"))      # __str__ del socio

    print("\nDisponibles:", bib.disponibles())
    print("De Cervantes:", bib.libros_de("Cervantes"))   # lista -> __repr__

    print("\n--- Catálogo por año ---")
    for numero, libro in enumerate(bib.ordenados_por_anio(), start=1):
        print(f"{numero}. {libro} [{libro.epoca()}]")

    print("\n--- Libros por época ---")
    for epoca, cantidad in bib.libros_por_epoca().items():
        print(f"{epoca}: {cantidad}")

    print(f"\nTotal de libros creados: {Libro.total_libros}")

# ---------------------------------------------------------------
# SALIDA ESPERADA (copiada de la ejecución real):
# --- Préstamos ---
# Préstamo OK: 'Don Quijote' para Ana.
# Préstamo OK: 'Python para todos' para Ana.
# Error: Ana ya tiene 2 libros.
# Error: 'Don Quijote' ya está prestado.
# Error: no hay ningún libro con ISBN 999.
# Error: el socio 'Marta' no existe.
# Préstamo OK: 'Cien años de soledad' para Luis.
#
# --- Estado de los socios ---
# Ana tiene: 111, 444
# Luis tiene: 222
#
# --- Devolución ---
# Devolución OK: 'Don Quijote'.
# Error: devolución no válida.
# Socio Ana (1/2)
#
# Disponibles: ['Don Quijote', 'Novelas ejemplares', 'El túnel']
# De Cervantes: [Libro('111', 'Don Quijote', 'Cervantes', 1605), Libro('333', 'Novelas ejemplares', 'Cervantes', 1613)]
#
# --- Catálogo por año ---
# 1. 'Don Quijote' de Cervantes (1605) - disponible [Clásico]
# 2. 'Novelas ejemplares' de Cervantes (1613) - disponible [Clásico]
# 3. 'El túnel' de Sabato (1948) - disponible [Siglo XX]
# 4. 'Cien años de soledad' de García Márquez (1967) - PRESTADO [Siglo XX]
# 5. 'Python para todos' de Severance (2016) - PRESTADO [Contemporáneo]
#
# --- Libros por época ---
# Clásico: 2
# Siglo XX: 2
# Contemporáneo: 1
#
# Total de libros creados: 5
# ---------------------------------------------------------------
# RESPUESTA A LA CUESTIÓN TEÓRICA:
# - El else del for-else va al nivel del for (no del if) y se ejecuta UNA
#   vez, solo si el bucle acabó sin break: perfecto para "no encontrado".
#   Un else dentro del for (pegado al if) se ejecutaría en cada vuelta.
# - __catalogo es privado para que nadie haga bib.__catalogo.append(...)
#   saltándose alta_libro(); toda modificación pasa por los métodos.
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - filter() y map() devuelven iteradores: usa list(...) para verlos.
# - Libro(**datos) solo funciona si las claves coinciden con los
#   parámetros de __init__ (isbn, titulo, autor, anio).
# - Usar socios["Marta"] con una clave inexistente da KeyError;
#   socios.get("Marta") devuelve None.
# EN JAVA SERÍA... un HashMap<String, Socio> y un ArrayList<Libro>.
# ALTERNATIVA (funciona, pero NO es lo que pide el enunciado):
#   prestar con if/else anidados en vez de cláusulas de guarda, o
#   buscar con una variable bandera "encontrado = False" en vez de for-else.
# ---------------------------------------------------------------
