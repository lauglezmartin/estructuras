"""
TEMA 6 - Teoría-práctica 5: Herencia, super() y herencia múltiple (MRO)
======================================================================
ENUNCIADO (parte final, literal del profesor - ejercicio integrador):
    "Implementar la herencia múltiple cooperativa utilizando **kwargs, lo que
    permite que super() propague la llamada a través de toda la cadena del MRO
    (Cyborg -> Humano -> Robot) sin perder los argumentos. Definir la clase
    Humano con ejecutar_tarea(...), la clase Robot con ejecutar_tarea(...) y
    la subclase Cyborg(Humano, Robot) probando la ejecución en cascada con
    super(), llamadas explícitas aisladas (Humano.ejecutar_tarea(self, ...)) y
    la consulta del orden MRO mediante Cyborg.mro()."

FORMA QUE EXIGE EL PROFESOR:
    - Herencia: class Hija(Padre):
    - Reutilizar el constructor del padre con super().__init__(...).
    - Herencia múltiple cooperativa: cada clase llama a super() pasando
      **kwargs; consultar el orden con Cyborg.mro().

CONCEPTOS QUE PRACTICA:
    - Herencia simple, super().__init__, añadir atributos propios.
    - Sobrescribir métodos (override) y ampliar el del padre con super().
    - isinstance() / issubclass().
    - Herencia múltiple, MRO (de izquierda a derecha), **kwargs.

CÓMO EJECUTARLO:  python 05_herencia_super.py   (en Linux/Docker: python3 05_herencia_super.py)
"""


# ---------------------------------------------------------------
# PASO 1: HERENCIA SIMPLE
# ---------------------------------------------------------------
# La clase PADRE (base) tiene lo común a todos.
class Animal:
    """Clase base: todo animal tiene nombre y edad, y puede hablar."""

    def __init__(self, nombre, edad):
        """Guarda nombre y edad."""
        self.nombre = nombre
        self.edad = edad

    def hablar(self):
        """Sonido genérico (las hijas lo sobrescriben)."""
        return "..."

    def presentarse(self):
        """Devuelve una presentación usando hablar() (polimorfismo)."""
        # self.hablar() llamará a la versión de la clase HIJA si la tiene.
        return f"Soy {self.nombre}, tengo {self.edad} años y digo {self.hablar()}"

    def __str__(self):
        """Texto para el usuario."""
        return f"{type(self).__name__}: {self.nombre}"


# class Hija(Padre): -> Perro HEREDA todo lo de Animal.
# EN JAVA SERÍA: class Perro extends Animal
class Perro(Animal):
    """Perro: añade raza y sobrescribe hablar()."""

    def __init__(self, nombre, edad, raza):
        """Reutiliza el constructor de Animal y añade la raza."""
        # super().__init__(...) llama al __init__ del PADRE para que guarde
        # nombre y edad. Sin esta línea, el perro NO tendría self.nombre.
        # (En Java: super(nombre, edad);) Aquí NO se pasa self.
        super().__init__(nombre, edad)
        self.raza = raza                    # atributo propio de Perro

    # SOBRESCRIBIR (override): mismo nombre que en el padre -> manda este.
    def hablar(self):
        """Sonido del perro."""
        return "¡Guau!"


class Gato(Animal):
    """Gato: no tiene __init__ propio -> usa el de Animal directamente."""

    def hablar(self):
        """Sonido del gato."""
        return "¡Miau!"

    # AMPLIAR un método del padre: llamo a su versión con super() y añado algo.
    def presentarse(self):
        """Presentación del padre + una frase extra."""
        return super().presentarse() + " (y paso de ti)"


# ---------------------------------------------------------------
# PASO 2: HERENCIA MÚLTIPLE COOPERATIVA (ejemplo de los apuntes)
# ---------------------------------------------------------------
# class Cyborg(Humano, Robot): hereda de DOS clases.
# MRO (Method Resolution Order) = orden en que Python busca un método:
#   Cyborg -> Humano -> Robot -> object   (de izquierda a derecha)
# super() NO significa "mi padre", sino "la SIGUIENTE clase en el MRO".
# Por eso, dentro de Humano, super() apunta a Robot cuando el objeto es un Cyborg.
# **kwargs recoge argumentos con nombre extra y los pasa a lo largo de la
# cadena sin perderlos.
class Humano:
    """Parte humana del Cyborg."""

    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        """Ejecuta la tarea y, si hay otra clase después en el MRO, le pasa la llamada."""
        print(f"[Humano] Intentando '{tarea}' con prioridad {prioridad}.")
        # hasattr comprueba si la siguiente clase del MRO tiene ese método.
        # (Si el objeto es un Humano solo, la siguiente es object y no lo tiene.)
        if hasattr(super(), 'ejecutar_tarea'):
            super().ejecutar_tarea(tarea, prioridad, **kwargs)


class Robot:
    """Parte robótica del Cyborg (última de la cadena)."""

    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        """Procesa la tarea; muestra los kwargs que han llegado hasta aquí."""
        print(f"[Robot] Procesando '{tarea}' a nivel {prioridad}.")
        if kwargs:
            print(f"[Robot] Datos extra recibidos: {kwargs}")


class Cyborg(Humano, Robot):
    """Hereda de Humano y de Robot; super() recorre toda la cadena."""

    def ejecutar_tarea(self, tarea, prioridad, **kwargs):
        """Inicia la directiva y delega en la siguiente clase del MRO (Humano)."""
        print("[Cyborg] Iniciando directiva principal...")
        super().ejecutar_tarea(tarea, prioridad, **kwargs)


# ---------------------------------------------------------------
# PASO 3: PRUEBAS
# ---------------------------------------------------------------
if __name__ == "__main__":

    print("=== Herencia simple ===")
    toby = Perro("Toby", 3, "Beagle")
    misi = Gato("Misi", 5)                  # usa el __init__ de Animal
    print(toby, "| raza:", toby.raza)
    print(misi)
    print(toby.presentarse())               # método heredado + hablar() sobrescrito
    print(misi.presentarse())               # método ampliado con super()

    print("\n=== Polimorfismo con una lista de objetos ===")
    animales = [toby, misi, Animal("Genérico", 1)]
    for a in animales:
        print(f"{a.nombre}: {a.hablar()}")  # cada uno usa SU versión

    print("\n=== isinstance / issubclass ===")
    print(isinstance(toby, Perro), isinstance(toby, Animal), isinstance(toby, Gato))
    print(issubclass(Perro, Animal))

    print("\n=== Herencia múltiple: ejecución en cascada con super() ===")
    c = Cyborg()
    c.ejecutar_tarea("Reparar nave", 1, zona="motor")

    print("\n=== Llamadas explícitas aisladas ===")
    # Llamar al método de UNA clase concreta: Clase.metodo(self, ...)
    Robot.ejecutar_tarea(c, "Escanear", 2)  # solo Robot
    print("--")
    Humano.ejecutar_tarea(Humano(), "Leer", 3)   # Humano solo: no hay Robot después

    print("\n=== Orden MRO ===")
    print(Cyborg.mro())
    print([clase.__name__ for clase in Cyborg.mro()])


# ---------------------------------------------------------------
# SALIDA ESPERADA:
# === Herencia simple ===
# Perro: Toby | raza: Beagle
# Gato: Misi
# Soy Toby, tengo 3 años y digo ¡Guau!
# Soy Misi, tengo 5 años y digo ¡Miau! (y paso de ti)
#
# === Polimorfismo con una lista de objetos ===
# Toby: ¡Guau!
# Misi: ¡Miau!
# Genérico: ...
#
# === isinstance / issubclass ===
# True True False
# True
#
# === Herencia múltiple: ejecución en cascada con super() ===
# [Cyborg] Iniciando directiva principal...
# [Humano] Intentando 'Reparar nave' con prioridad 1.
# [Robot] Procesando 'Reparar nave' a nivel 1.
# [Robot] Datos extra recibidos: {'zona': 'motor'}
#
# === Llamadas explícitas aisladas ===
# [Robot] Procesando 'Escanear' a nivel 2.
# --
# [Humano] Intentando 'Leer' con prioridad 3.
#
# === Orden MRO ===
# [<class '__main__.Cyborg'>, <class '__main__.Humano'>, <class '__main__.Robot'>, <class 'object'>]
# ['Cyborg', 'Humano', 'Robot', 'object']
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Olvidar super().__init__(...) en la hija -> AttributeError al usar
#   self.nombre (el padre nunca lo guardó).
# - Escribir super().__init__(self, nombre, edad) -> sobra self: TypeError.
# - Si la hija no define __init__, se usa el del padre (caso Gato).
# - En herencia múltiple el ORDEN de los padres importa:
#   Cyborg(Humano, Robot) busca primero en Humano. Cyborg(Robot, Humano)
#   llamaría primero a Robot (y como Robot no llama a super(), Humano no
#   se ejecutaría).
# - Si quitas **kwargs de alguna clase de la cadena, el argumento zona="motor"
#   provoca TypeError (unexpected keyword argument).
# EN JAVA SERÍA: extends + super(...). Java NO permite herencia múltiple de
# clases (usa interfaces); Python sí, y resuelve el orden con el MRO.
# ---------------------------------------------------------------
