"""
TEMA 6 (integrador) - Variante 04: "El cuaderno del profesor"
=============================================================
ENUNCIADO (redactado al estilo del profesor, modelo Teletubbies):

    Objetivo: Gestionar las notas de un grupo de alumnos con una clase,
    una lista de objetos y diccionarios, calculando medias y calificaciones.

    Requisitos de la clase Alumno:
    1. Atributos de clase: nota_aprobado = 5.0 y centro = "IES Las Galletas".
    2. Atributos de instancia: nombre (público) y __notas (privado): un
       DICCIONARIO {asignatura: nota}.
    3. poner_nota(asignatura, nota): solo acepta 0 <= nota <= 10
       (COMPARACIÓN ENCADENADA). Devuelve True/False (return temprano).
    4. media(): devuelve la media redondeada a 2 decimales (0.0 si no hay
       notas). Debe usar sum() y len() sobre .values().
    5. calificacion(): MATCH-CASE con GUARDAS sobre la media:
       < 5 "Insuficiente", < 6 "Suficiente", < 7 "Bien",
       < 9 "Notable", resto "Sobresaliente".
    6. suspensas(): COMPRENSIÓN DE LISTAS con las asignaturas < nota_aprobado,
       recorriendo el diccionario con .items().
    7. ver_boletin(): GETTER que devuelve un STRING multilínea con cada
       asignatura y su nota, la media y la calificación.
    8. get_notas(): devuelve una COPIA del diccionario (no el original).
    9. __str__ y __repr__.

    Funciones (con type hints):
    10. crear_alumno(nombre: str, **notas: float) -> Alumno: usa **kwargs
        para recibir las notas como argumentos con nombre.
    11. aprobados(alumnos) -> list[str]: comprensión de listas con los
        nombres de los alumnos sin ninguna suspensa.
    12. ranking(alumnos): SORTED + LAMBDA por media de mayor a menor.
    13. medias_por_asignatura(alumnos) -> dict[str, float]: diccionario
        con la media de cada asignatura de todo el grupo.
    14. nombres_en_mayusculas(alumnos): MAP + LAMBDA.
    15. dieces_necesarios(alumno, objetivo) -> int: con un WHILE, calcula
        cuántos 10 adicionales necesitaría para alcanzar la media objetivo
        (sin modificar al alumno original). Si objetivo no está entre 0 y 10,
        devuelve -1.

    Bloque principal: crea 4 alumnos con **kwargs, muestra los boletines,
    aprobados, ranking con enumerate(start=1), medias por asignatura con
    .items(), una nota inválida y el cálculo de dieces necesarios.

    Cuestión teórica: ¿Por qué get_notas() devuelve una copia? ¿Qué pasa
    si devuelve self.__notas directamente?

FORMA QUE EXIGE EL PROFESOR:
    - match-case con guardas para la calificación (NO if/elif).
    - **kwargs en crear_alumno y type hints en las funciones.
    - Comprensiones para suspensas y aprobados, sorted/map con lambda.
    - while en dieces_necesarios, .items() al recorrer diccionarios.

CONCEPTOS QUE PRACTICA:
    - Diccionario como atributo privado, copia de diccionarios
    - Funciones que devuelven objetos, listas y diccionarios

CÓMO EJECUTARLO:  python 04_gestor_alumnos_notas.py   (en Linux: python3 ...)
"""


# ---------------------------------------------------------------
# PASO 1: Clase Alumno.
# ---------------------------------------------------------------
class Alumno:
    """Un alumno con sus notas por asignatura."""

    nota_aprobado = 5.0
    centro = "IES Las Galletas"

    def __init__(self, nombre: str):
        """Crea el alumno con el diccionario de notas vacío."""
        self.nombre = nombre
        self.__notas = {}   # {asignatura: nota}

    def poner_nota(self, asignatura: str, nota: float) -> bool:
        """Guarda la nota si es válida (0-10). Devuelve True si la guardó."""
        if not (0 <= nota <= 10):    # comparación encadenada
            return False             # return temprano: nota inválida
        self.__notas[asignatura] = nota  # añade o sobrescribe la clave
        return True

    def media(self) -> float:
        """Media de las notas (0.0 si no tiene ninguna)."""
        if not self.__notas:          # diccionario vacío -> False
            return 0.0                # evita dividir entre 0
        return round(sum(self.__notas.values()) / len(self.__notas), 2)

    def calificacion(self) -> str:
        """Calificación textual con match-case y guardas."""
        # Las guardas se comprueban en orden: basta con "< 6" en la segunda
        # porque si fuera < 5 ya habría entrado en la primera.
        match self.media():
            case m if m < 5:
                return "Insuficiente"
            case m if m < 6:
                return "Suficiente"
            case m if m < 7:
                return "Bien"
            case m if m < 9:
                return "Notable"
            case _:
                return "Sobresaliente"

    def suspensas(self) -> list[str]:
        """Comprensión de listas recorriendo el diccionario con .items()."""
        return [asig for asig, nota in self.__notas.items()
                if nota < Alumno.nota_aprobado]

    def get_notas(self) -> dict[str, float]:
        """Devuelve una COPIA para que desde fuera no se pueda modificar el original."""
        return self.__notas.copy()   # también valdría dict(self.__notas)

    def ver_boletin(self) -> str:
        """GETTER: devuelve el boletín como string multilínea."""
        lineas = [f"Boletín de {self.nombre} ({Alumno.centro})"]
        for asignatura, nota in self.__notas.items():
            # Ternario para marcar las suspensas
            marca = " <- suspensa" if nota < Alumno.nota_aprobado else ""
            lineas.append(f"  {asignatura:<12}{nota:>5}{marca}")
        lineas.append(f"  Media: {self.media()} - {self.calificacion()}")
        return "\n".join(lineas)

    def __str__(self):
        """Texto amigable para el usuario (lo usa print)."""
        return f"{self.nombre}: media {self.media()} ({self.calificacion()})"

    def __repr__(self):
        """Texto técnico: cómo se crearía este objeto."""
        return f"Alumno('{self.nombre}')"


# ---------------------------------------------------------------
# PASO 2: Funciones sobre la lista de alumnos (con type hints).
# ---------------------------------------------------------------
def crear_alumno(nombre: str, **notas: float) -> Alumno:
    """Crea un alumno y le pone las notas recibidas con **kwargs.

    Ejemplo: crear_alumno("Ana", Mates=7, Lengua=8)
    -> notas = {'Mates': 7, 'Lengua': 8}
    """
    alumno = Alumno(nombre)
    for asignatura, nota in notas.items():   # notas es un diccionario
        alumno.poner_nota(asignatura, nota)
    return alumno


def aprobados(alumnos: list[Alumno]) -> list[str]:
    """Nombres de los alumnos sin suspensas (lista vacía = False)."""
    return [a.nombre for a in alumnos if not a.suspensas()]


def ranking(alumnos: list[Alumno]) -> list[Alumno]:
    """Ordena por media de mayor a menor con sorted + lambda."""
    return sorted(alumnos, key=lambda a: a.media(), reverse=True)


def medias_por_asignatura(alumnos: list[Alumno]) -> dict[str, float]:
    """Diccionario {asignatura: media del grupo}."""
    acumulado = {}   # {asignatura: [nota1, nota2, ...]}
    for alumno in alumnos:
        for asignatura, nota in alumno.get_notas().items():
            acumulado.setdefault(asignatura, []).append(nota)
    # Comprensión de DICCIONARIO: {clave: valor for ... in ...}
    return {asig: round(sum(notas) / len(notas), 2)
            for asig, notas in acumulado.items()}


def nombres_en_mayusculas(alumnos: list[Alumno]) -> list[str]:
    """map + lambda: transforma cada alumno en su nombre en mayúsculas."""
    return list(map(lambda a: a.nombre.upper(), alumnos))


def dieces_necesarios(alumno: Alumno, objetivo: float) -> int:
    """Cuántos 10 extra harían falta para llegar a la media objetivo."""
    if not (0 <= objetivo <= 10):
        return -1
    # Trabajamos con una copia de las notas (lista) para no tocar al alumno.
    notas = list(alumno.get_notas().values())
    dieces = 0
    # while: repetimos MIENTRAS no se alcance el objetivo.
    # Con objetivo 10 y alguna nota < 10 nunca se llegaría: lo limitamos a 100
    # vueltas para evitar un bucle infinito.
    while sum(notas) / len(notas) < objetivo and dieces < 100:
        notas.append(10)
        dieces += 1
    return dieces


# ---------------------------------------------------------------
# PASO 3: Bloque principal.
# ---------------------------------------------------------------
if __name__ == "__main__":
    grupo = [
        crear_alumno("Ana", Mates=7.5, Lengua=8, Python=9.5),
        crear_alumno("Luis", Mates=4, Lengua=6, Python=5.5),
        crear_alumno("Marta", Mates=9, Lengua=9.5, Python=10),
        crear_alumno("Pablo", Mates=3, Lengua=4.5, Python=6),
    ]

    print("--- Boletines ---")
    for alumno in grupo:
        print(alumno.ver_boletin())

    print("\nNota inválida (11):", grupo[0].poner_nota("Inglés", 11))
    print("Nota válida (6):", grupo[0].poner_nota("Inglés", 6))
    print(grupo[0])                                   # __str__

    print("\nAprobados:", aprobados(grupo))
    print("Suspensas de Pablo:", grupo[3].suspensas())
    print("En mayúsculas:", nombres_en_mayusculas(grupo))

    print("\n--- Ranking ---")
    for puesto, alumno in enumerate(ranking(grupo), start=1):
        print(f"{puesto}. {alumno}")

    print("\n--- Media por asignatura ---")
    for asignatura, media in medias_por_asignatura(grupo).items():
        print(f"{asignatura}: {media}")

    print("\n--- Dieces necesarios ---")
    print("Pablo para llegar a 6:", dieces_necesarios(grupo[3], 6))
    print("Marta para llegar a 9:", dieces_necesarios(grupo[2], 9))
    print("Objetivo imposible (12):", dieces_necesarios(grupo[1], 12))

    # Demostración de la copia: modificarla NO cambia al alumno.
    copia = grupo[1].get_notas()
    copia["Mates"] = 10
    print("\nCopia modificada:", copia)
    print("Original intacto:", grupo[1].get_notas())
    print("Repr del grupo:", grupo)

# ---------------------------------------------------------------
# SALIDA ESPERADA (copiada de la ejecución real):
# --- Boletines ---
# Boletín de Ana (IES Las Galletas)
#   Mates         7.5
#   Lengua          8
#   Python        9.5
#   Media: 8.33 - Notable
# Boletín de Luis (IES Las Galletas)
#   Mates           4 <- suspensa
#   Lengua          6
#   Python        5.5
#   Media: 5.17 - Suficiente
# Boletín de Marta (IES Las Galletas)
#   Mates           9
#   Lengua        9.5
#   Python         10
#   Media: 9.5 - Sobresaliente
# Boletín de Pablo (IES Las Galletas)
#   Mates           3 <- suspensa
#   Lengua        4.5 <- suspensa
#   Python          6
#   Media: 4.5 - Insuficiente
#
# Nota inválida (11): False
# Nota válida (6): True
# Ana: media 7.75 (Notable)
#
# Aprobados: ['Ana', 'Marta']
# Suspensas de Pablo: ['Mates', 'Lengua']
# En mayúsculas: ['ANA', 'LUIS', 'MARTA', 'PABLO']
#
# --- Ranking ---
# 1. Marta: media 9.5 (Sobresaliente)
# 2. Ana: media 7.75 (Notable)
# 3. Luis: media 5.17 (Suficiente)
# 4. Pablo: media 4.5 (Insuficiente)
#
# --- Media por asignatura ---
# Mates: 5.88
# Lengua: 7.0
# Python: 7.75
# Inglés: 6.0
#
# --- Dieces necesarios ---
# Pablo para llegar a 6: 2
# Marta para llegar a 9: 0
# Objetivo imposible (12): -1
#
# Copia modificada: {'Mates': 10, 'Lengua': 6, 'Python': 5.5}
# Original intacto: {'Mates': 4, 'Lengua': 6, 'Python': 5.5}
# Repr del grupo: [Alumno('Ana'), Alumno('Luis'), Alumno('Marta'), Alumno('Pablo')]
# ---------------------------------------------------------------
# RESPUESTA A LA CUESTIÓN TEÓRICA:
# - Los diccionarios son MUTABLES y se pasan por referencia: si
#   get_notas() devolviera self.__notas, quien lo recibe podría hacer
#   notas["Mates"] = 10 y cambiaría la nota "privada" del alumno sin pasar
#   por poner_nota() (que valida 0-10). La copia protege el encapsulamiento.
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - match-case: "case m if m < 5" captura la media en m; "case < 5" NO existe.
# - sum(dic) suma las CLAVES; para sumar notas hay que usar dic.values().
# - Dividir entre len() de un diccionario vacío -> ZeroDivisionError.
# - En **notas las claves son nombres válidos de variable: Mates=7 vale,
#   "Educación Física"=7 no (por eso las asignaturas son de una palabra).
# EN JAVA SERÍA... switch no admite rangos; aquí las guardas lo resuelven.
# ALTERNATIVA (funciona, pero NO es lo que pide el enunciado):
#   if media < 5: ... elif media < 6: ...  -> pide match-case con guardas.
#   for + append para aprobados            -> pide comprensión de listas.
# ---------------------------------------------------------------
