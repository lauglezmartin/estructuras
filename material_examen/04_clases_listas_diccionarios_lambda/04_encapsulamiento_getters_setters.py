"""
TEMA 6 - Teoría-práctica 4: Encapsulamiento, getters y setters
==============================================================
ENUNCIADO: Archivo de consulta. Muestra atributos públicos, "protegidos" (_)
y privados (__), el name mangling, getters y setters con validación (la forma
de los apuntes) y @property como alternativa más moderna.

FORMA QUE EXIGE EL PROFESOR:
    - Privados con DOBLE guion bajo: self.__atributo (name mangling).
    - Getters y setters como MÉTODOS normales (como ver_estado() de la
      práctica de los Teletubbies): get_x() devuelve, set_x(valor) valida y
      cambia. Es lo que aparece en los apuntes.
    - @property: funciona y es muy pythónico, pero NO es lo que muestran los
      apuntes. Úsalo solo si el enunciado lo pide.

CONCEPTOS QUE PRACTICA:
    - Público / _protegido (convención) / __privado (name mangling).
    - Getter = método que DEVUELVE un privado.
    - Setter = método que VALIDA y cambia un privado.
    - @property y @x.setter.

CÓMO EJECUTARLO:  python 04_encapsulamiento_getters_setters.py   (en Linux/Docker: python3 ...)
"""


# ---------------------------------------------------------------
# PASO 1: LOS TRES NIVELES DE "VISIBILIDAD"
# ---------------------------------------------------------------
# En Python NO existen public/private como palabras clave. Se usan nombres:
#   nombre       -> público: se usa libremente desde fuera.
#   _nombre      -> "protegido": SOLO una convención ("no lo toques").
#                   Python no hace nada especial; se puede leer desde fuera.
#   __nombre     -> privado: Python lo renombra a _Clase__nombre (name
#                   mangling), así que obj.__nombre desde fuera no existe.
class Alumno:
    """Alumno con nota privada, accesible mediante getter y setter (forma de los apuntes)."""

    def __init__(self, nombre, nota):
        """Crea el alumno. La nota pasa por el setter para validarla."""
        self.nombre = nombre        # público
        self._curso = "2º DAW"      # protegido (convención)
        self.__nota = 0             # privado: valor seguro inicial
        self.set_nota(nota)         # validamos también al crear

    # GETTER: devuelve el valor privado. Sin él, no podríamos leer la nota.
    def get_nota(self):
        """Devuelve la nota del alumno."""
        return self.__nota

    # SETTER: solo cambia la nota si es válida. Esta es la ventaja de tener
    # el atributo privado: NADIE puede poner una nota de 15 o "hola".
    def set_nota(self, nueva_nota):
        """Cambia la nota si es un número entre 0 y 10."""
        if isinstance(nueva_nota, (int, float)) and 0 <= nueva_nota <= 10:
            self.__nota = nueva_nota
        else:
            print(f"Nota no válida: {nueva_nota!r}. Se mantiene {self.__nota}.")

    # Un método puede usar el privado para CALCULAR algo (getter "derivado").
    def esta_aprobado(self):
        """Devuelve True si la nota es 5 o más."""
        return self.__nota >= 5

    def __str__(self):
        """Texto para el usuario."""
        return f"{self.nombre} ({self._curso}): {self.__nota}"


# ---------------------------------------------------------------
# PASO 2: ALTERNATIVA CON @property (NO es la forma de los apuntes)
# ---------------------------------------------------------------
# @property convierte un método en algo que se USA COMO UN ATRIBUTO:
#     alumno.nota        -> llama al getter (sin paréntesis)
#     alumno.nota = 7    -> llama al setter (con su validación)
# Por dentro sigue habiendo un privado (self.__nota).
class AlumnoProperty:
    """Igual que Alumno, pero con @property en vez de get_/set_."""

    def __init__(self, nombre, nota):
        """Crea el alumno; la asignación self.nota = nota pasa por el setter."""
        self.nombre = nombre
        self.__nota = 0
        self.nota = nota            # OJO: esto llama al setter de abajo

    @property
    def nota(self):
        """Getter: se usa como alumno.nota (sin paréntesis)."""
        return self.__nota

    @nota.setter
    def nota(self, nueva_nota):
        """Setter: se usa como alumno.nota = valor."""
        if isinstance(nueva_nota, (int, float)) and 0 <= nueva_nota <= 10:
            self.__nota = nueva_nota
        else:
            print(f"Nota no válida: {nueva_nota!r}. Se mantiene {self.__nota}.")


# ---------------------------------------------------------------
# PASO 3: PRUEBAS
# ---------------------------------------------------------------
if __name__ == "__main__":

    print("=== Getters y setters (forma de los apuntes) ===")
    ana = Alumno("Ana", 8)
    print(ana)
    print("Nota con getter:", ana.get_nota())
    ana.set_nota(9.5)                   # válida
    print("Tras set_nota(9.5):", ana.get_nota())
    ana.set_nota(15)                    # no válida
    ana.set_nota("diez")                # no válida
    print("¿Aprobada?", ana.esta_aprobado())

    print("\n=== Validación también en el constructor ===")
    luis = Alumno("Luis", -3)           # no válida -> se queda en 0
    print(luis, "| ¿Aprobado?", luis.esta_aprobado())

    print("\n=== Protegido (_): se puede leer, es solo convención ===")
    print(ana._curso)

    print("\n=== Privado (__): name mangling ===")
    try:
        print(ana.__nota)
    except AttributeError as error:
        print("AttributeError:", error)
    ana.__nota = 0                      # crea un atributo NUEVO, no toca el privado
    print("Tras ana.__nota = 0, get_nota() sigue dando:", ana.get_nota())
    print(vars(ana))
    print("Nombre real:", ana._Alumno__nota, "(se puede, pero NO se debe)")

    print("\n=== Alternativa con @property ===")
    eva = AlumnoProperty("Eva", 6)
    print("eva.nota:", eva.nota)        # getter sin paréntesis
    eva.nota = 7                        # setter con validación
    print("eva.nota:", eva.nota)
    eva.nota = 11                       # rechazado por el setter
    print("eva.nota:", eva.nota)


# ---------------------------------------------------------------
# SALIDA ESPERADA:
# === Getters y setters (forma de los apuntes) ===
# Ana (2º DAW): 8
# Nota con getter: 8
# Tras set_nota(9.5): 9.5
# Nota no válida: 15. Se mantiene 9.5.
# Nota no válida: 'diez'. Se mantiene 9.5.
# ¿Aprobada? True
#
# === Validación también en el constructor ===
# Nota no válida: -3. Se mantiene 0.
# Luis (2º DAW): 0 | ¿Aprobado? False
#
# === Protegido (_): se puede leer, es solo convención ===
# 2º DAW
#
# === Privado (__): name mangling ===
# AttributeError: 'Alumno' object has no attribute '__nota'
# Tras ana.__nota = 0, get_nota() sigue dando: 9.5
# {'nombre': 'Ana', '_curso': '2º DAW', '_Alumno__nota': 9.5, '__nota': 0}
# Nombre real: 9.5 (se puede, pero NO se debe)
#
# === Alternativa con @property ===
# eva.nota: 6
# eva.nota: 7
# Nota no válida: 11. Se mantiene 7.
# eva.nota: 7
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Getter con print en vez de return -> no puedes usar el valor fuera.
# - Llamar al getter sin paréntesis: ana.get_nota  -> muestra
#   <bound method ...>, no la nota. Con @property es al revés: eva.nota()
#   da TypeError porque ya devuelve el número.
# - En @property, si el atributo interno se llama igual que la propiedad
#   (self.nota = ... dentro del setter) -> recursión infinita. Por eso el
#   interno es self.__nota.
# - Un solo guion bajo NO protege nada: es una convención.
# ¿POR QUÉ ENCAPSULAR? La clase controla sus datos: valida lo que entra,
# evita estados incoherentes y puedes cambiar la implementación interna sin
# romper el código que usa la clase.
# EN JAVA SERÍA: private double nota; public double getNota(); public void setNota(double n)
# ---------------------------------------------------------------
