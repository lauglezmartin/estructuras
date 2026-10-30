"""
TEMA 6 - Ejercicio 1: Práctica evaluada "La Galaxia de los Teletubbies"
=====================================================================
ENUNCIADO (literal del profesor):
    Objetivo: Diseñar e implementar en Python una clase que represente a un
    Teletubby, aplicando los conceptos fundamentales de la Programación
    Orientada a Objetos (POO): atributos de clase, atributos de instancia
    (públicos y privados), métodos de instancia y encapsulamiento.

    Requisitos de la Clase (PersonajeTeletubby):
    - Atributo de clase: Crea una variable de clase llamada saludo_oficial con
      el valor '¡Tubby abrazo!' (compartida por todos los personajes).
    - Atributos de instancia (en el constructor __init__):
        Públicos: nombre (cadena), color (cadena), antena (cadena),
                  objeto_favorito (cadena).
        Privados (__): __nivel_hambre (entero, por defecto 50),
                       __nivel_felicidad (entero, por defecto 100).
    - Métodos de instancia:
        saludar(): Muestra por pantalla una presentación con su nombre, color
                   y forma de antena.
        jugar(): Imprime un mensaje indicando que el Teletubby está jugando
                 con su objeto favorito. Incrementa __nivel_hambre en 20
                 unidades y __nivel_felicidad en 10.
        comer_tubby_papilla(): Imprime un mensaje de alimentación. Reduce
                 __nivel_hambre a 0 e incrementa __nivel_felicidad en 20.
        ver_estado(): Método tipo Getter que devuelve una cadena de texto
                 informando sobre el estado actual de los niveles de
                 felicidad y hambre del personaje.
    - Métodos Mágicos (Dunder Methods):
        __str__(self): Devuelve una cadena amigable e informal para el usuario
                 (ej. "Teletubby Tinky Winky (Morado) - Feliz: 100").
        __repr__(self): Devuelve una cadena técnica que representa cómo se
                 instanció el objeto
                 (ej. PersonajeTeletubby('Tinky Winky', 'Morado', 'Triángulo', 'Bolso')).

    Bloque Principal (main): En la sección if __name__ == "__main__":
    realiza las siguientes pruebas:
    1. Instancia al menos dos objetos de la clase PersonajeTeletubby con
       características distintas (por ejemplo, Tinky Winky y Po).
    2. Haz que ambos personajes ejecuten sus métodos saludar() y muestren por
       consola el saludo_oficial de la clase.
    3. Invoca el método jugar() en ambos personajes.
    4. Muestra el estado interno de cada uno usando ver_estado().
    5. Haz que solo uno de los Teletubbies coma usando comer_tubby_papilla().
    6. Muestra de nuevo el estado final de ambos para comprobar que solo ha
       variado el hambre del que ha comido.

    Cuestión Teórica: ¿Qué ocurriría si intentaras modificar po.__nivel_hambre
    directamente desde el bloque principal? Justifica por qué se utilizan
    atributos privados en este diseño.

FORMA QUE EXIGE EL PROFESOR:
    - Clase llamada EXACTAMENTE PersonajeTeletubby (PascalCase).
    - saludo_oficial como ATRIBUTO DE CLASE (fuera del __init__).
    - Privados con DOBLE guion bajo: self.__nivel_hambre, self.__nivel_felicidad
      (con valores 50 y 100 por defecto).
    - ver_estado() tiene que DEVOLVER (return) un string, NO imprimirlo.
      Quien imprime es el main: print(tinky.ver_estado()).
    - __str__ y __repr__ con el formato de los ejemplos del enunciado.
    - Las pruebas dentro de if __name__ == "__main__": y en el ORDEN pedido.
    - Docstrings con triple comilla en la clase y en cada método.

CONCEPTOS QUE PRACTICA:
    - class, __init__ (constructor), self.
    - Atributo de clase vs atributo de instancia.
    - Encapsulamiento: atributos privados (__) y name mangling.
    - Métodos de instancia; getter (return) frente a print.
    - __str__ (para el usuario) y __repr__ (para el programador).

CÓMO EJECUTARLO:  python 01_teletubbies.py   (en Linux/Docker: python3 01_teletubbies.py)
"""


# ---------------------------------------------------------------
# PASO 1: DEFINIR LA CLASE
# ---------------------------------------------------------------
# Una CLASE es el "molde" (plantilla). Un OBJETO (o instancia) es cada cosa
# concreta que fabricas con ese molde: tinky_winky y po son dos objetos
# distintos hechos con el mismo molde PersonajeTeletubby.
# EN JAVA SERÍA: public class PersonajeTeletubby { ... }  (aquí no hay llaves,
# manda la indentación de 4 espacios, y no se declaran tipos).
class PersonajeTeletubby:
    """Representa a un personaje Teletubby con sus niveles de hambre y felicidad."""

    # -----------------------------------------------------------
    # ATRIBUTO DE CLASE
    # -----------------------------------------------------------
    # Se escribe DENTRO de la clase pero FUERA de cualquier método (sin self).
    # Pertenece a la CLASE, no a cada objeto: hay UNA sola copia compartida
    # por todos los Teletubbies. Se lee así:
    #     PersonajeTeletubby.saludo_oficial   (forma recomendada)
    #     tinky_winky.saludo_oficial          (también funciona: si el objeto
    #                                          no lo tiene, Python lo busca
    #                                          en la clase)
    # EN JAVA SERÍA: public static String saludoOficial = "¡Tubby abrazo!";
    saludo_oficial = "¡Tubby abrazo!"

    # -----------------------------------------------------------
    # CONSTRUCTOR: __init__
    # -----------------------------------------------------------
    # __init__ se ejecuta SOLO cuando creas un objeto:
    #     po = PersonajeTeletubby("Po", "Rojo", "Círculo", "Patinete")
    # Python crea el objeto vacío y llama a __init__ pasándole ese objeto
    # como primer argumento (self). Por eso tú escribes 4 argumentos al crear
    # el objeto, pero el método tiene 5 parámetros (self + 4).
    #
    # ¿QUÉ ES self? Es "el objeto con el que estoy trabajando ahora mismo".
    # Equivale al "this" de Java, pero en Python es OBLIGATORIO escribirlo:
    #   - como primer parámetro de cada método de instancia, y
    #   - delante de cada atributo: self.nombre (si escribes solo "nombre"
    #     sería una variable local que desaparece al terminar el método).
    #
    # Los privados NO se piden como parámetro: el enunciado dice "por defecto
    # 50" y "por defecto 100", así que todos los Teletubbies nacen con esos
    # valores.
    def __init__(self, nombre, color, antena, objeto_favorito):
        """Crea un Teletubby con sus datos públicos y sus niveles privados por defecto."""
        # ATRIBUTOS DE INSTANCIA PÚBLICOS: cada objeto tiene su propia copia.
        # Se pueden leer y cambiar desde fuera: tinky_winky.nombre
        self.nombre = nombre
        self.color = color
        self.antena = antena
        self.objeto_favorito = objeto_favorito

        # ATRIBUTOS DE INSTANCIA PRIVADOS: empiezan por DOS guiones bajos.
        # Solo se deben usar DENTRO de la clase (desde los métodos).
        # Python les aplica "name mangling": internamente los renombra a
        # _PersonajeTeletubby__nivel_hambre y _PersonajeTeletubby__nivel_felicidad,
        # así que desde fuera "po.__nivel_hambre" NO los encuentra.
        # EN JAVA SERÍA: private int nivelHambre = 50;
        self.__nivel_hambre = 50
        self.__nivel_felicidad = 100

    # -----------------------------------------------------------
    # MÉTODOS DE INSTANCIA
    # -----------------------------------------------------------
    # Son funciones definidas dentro de la clase. Siempre reciben self para
    # poder leer/modificar los atributos de ESE objeto concreto.
    # Se llaman con el punto: po.saludar()  (Python pone self = po).

    def saludar(self):
        """Muestra por pantalla una presentación con nombre, color y forma de antena."""
        # El enunciado dice "muestra por pantalla" -> aquí SÍ va print.
        print(f"¡Hola! Soy {self.nombre}, soy de color {self.color} "
              f"y mi antena tiene forma de {self.antena}.")

    def jugar(self):
        """Juega con su objeto favorito: +20 de hambre y +10 de felicidad."""
        print(f"{self.nombre} está jugando con su {self.objeto_favorito}.")
        # Dentro de la clase SÍ podemos usar los privados con self.__
        self.__nivel_hambre += 20       # igual que: self.__nivel_hambre = self.__nivel_hambre + 20
        self.__nivel_felicidad += 10

    def comer_tubby_papilla(self):
        """Come Tubby Papilla: el hambre baja a 0 y la felicidad sube 20."""
        print(f"{self.nombre} se está comiendo su Tubby Papilla. ¡Ñam, ñam!")
        self.__nivel_hambre = 0         # "reduce A 0" -> se asigna 0 (no se resta)
        self.__nivel_felicidad += 20

    def ver_estado(self):
        """Getter: DEVUELVE un texto con los niveles de felicidad y hambre."""
        # ¿POR QUÉ UN GETTER? Los atributos privados no se leen desde fuera.
        # La forma controlada de consultarlos es un método público de la
        # clase que los devuelve. Así la clase decide QUÉ se enseña y CÓMO.
        #
        # OJO: return, NO print. El enunciado dice "devuelve una cadena".
        # Con return el main puede imprimirlo, guardarlo en una variable,
        # compararlo... Con print el método devolvería None.
        return (f"Estado de {self.nombre} -> Felicidad: {self.__nivel_felicidad}"
                f" | Hambre: {self.__nivel_hambre}")

    # -----------------------------------------------------------
    # MÉTODOS MÁGICOS (dunder = "double underscore")
    # -----------------------------------------------------------
    # Python los llama SOLO en ciertos momentos; tú no los llamas a mano.

    def __str__(self):
        """Texto amigable para el usuario. Lo usan print(objeto) y str(objeto)."""
        # Formato del ejemplo: Teletubby Tinky Winky (Morado) - Feliz: 100
        # EN JAVA SERÍA: public String toString()
        return f"Teletubby {self.nombre} ({self.color}) - Feliz: {self.__nivel_felicidad}"

    def __repr__(self):
        """Texto técnico: cómo se creó el objeto. Lo usan repr(objeto) y print(lista)."""
        # Formato del ejemplo:
        #   PersonajeTeletubby('Tinky Winky', 'Morado', 'Triángulo', 'Bolso')
        # Las comillas simples van DENTRO del f-string (que usa dobles).
        return (f"PersonajeTeletubby('{self.nombre}', '{self.color}', "
                f"'{self.antena}', '{self.objeto_favorito}')")


# ---------------------------------------------------------------
# PASO 2: BLOQUE PRINCIPAL CON LAS PRUEBAS (en el orden del enunciado)
# ---------------------------------------------------------------
# if __name__ == "__main__": significa "ejecuta esto SOLO si lanzo este
# archivo directamente" (python 01_teletubbies.py). Si otro archivo hace
# "import", la clase se carga pero las pruebas NO se ejecutan.
# EN JAVA SERÍA: public static void main(String[] args)
if __name__ == "__main__":

    # 1. Instanciar al menos dos objetos con características distintas.
    #    Al escribir NombreClase(...) se llama automáticamente a __init__.
    print("=== 1. Creamos los Teletubbies ===")
    tinky_winky = PersonajeTeletubby("Tinky Winky", "Morado", "Triángulo", "Bolso")
    po = PersonajeTeletubby("Po", "Rojo", "Círculo", "Patinete")
    print(tinky_winky)          # print usa __str__
    print(po)
    print(repr(tinky_winky))    # repr() usa __repr__
    print(repr(po))

    # 2. Ambos saludan y muestran el saludo_oficial DE LA CLASE.
    print("\n=== 2. Saludos ===")
    tinky_winky.saludar()
    print(PersonajeTeletubby.saludo_oficial)    # leído desde la clase
    po.saludar()
    print(po.saludo_oficial)                    # leído desde el objeto: es el mismo valor compartido

    # 3. Ambos juegan.
    print("\n=== 3. A jugar ===")
    tinky_winky.jugar()
    po.jugar()

    # 4. Estado de cada uno con ver_estado(). Como ver_estado() DEVUELVE el
    #    texto, aquí hay que meterlo en un print.
    print("\n=== 4. Estado después de jugar ===")
    print(tinky_winky.ver_estado())
    print(po.ver_estado())

    # 5. Solo uno come (Po).
    print("\n=== 5. Solo Po come ===")
    po.comer_tubby_papilla()

    # 6. Estado final de ambos: solo cambia el hambre (y la felicidad) de Po;
    #    Tinky Winky sigue igual porque cada objeto tiene SUS PROPIOS atributos.
    print("\n=== 6. Estado final ===")
    print(tinky_winky.ver_estado())
    print(po.ver_estado())

    # Extra (no lo pide, pero muestra __repr__ en acción): al imprimir una
    # LISTA de objetos, Python usa __repr__ de cada elemento.
    print("\n=== Extra: lista de Teletubbies (usa __repr__) ===")
    print([tinky_winky, po])

    # -----------------------------------------------------------
    # PASO 3: DEMOSTRACIÓN DE LA CUESTIÓN TEÓRICA
    # -----------------------------------------------------------
    print("\n=== Cuestión teórica: ¿y si toco po.__nivel_hambre? ===")

    # a) LEER desde fuera -> AttributeError (no existe con ese nombre).
    try:
        print(po.__nivel_hambre)
    except AttributeError as error:
        print("Al leer po.__nivel_hambre -> AttributeError:", error)

    # b) ASIGNAR desde fuera -> NO da error, pero crea un atributo NUEVO y
    #    público llamado literalmente "__nivel_hambre" (fuera de la clase no
    #    hay name mangling). El privado de verdad NO cambia.
    po.__nivel_hambre = 999
    print("He hecho po.__nivel_hambre = 999")
    print("po.__nivel_hambre (atributo nuevo):", po.__nivel_hambre)
    print("ver_estado() sigue igual ->", po.ver_estado())

    # c) Dónde está realmente el privado: vars() muestra el diccionario de
    #    atributos del objeto. Se ve el nombre "mangleado" y el nuevo falso.
    print("Atributos reales de po:", vars(po))

    # d) El nombre real es _PersonajeTeletubby__nivel_hambre. Se PUEDE
    #    acceder con él (Python no lo prohíbe del todo), pero es mala
    #    práctica: te saltas el encapsulamiento a propósito.
    print("po._PersonajeTeletubby__nivel_hambre =", po._PersonajeTeletubby__nivel_hambre)


# ---------------------------------------------------------------
# SALIDA ESPERADA:
# === 1. Creamos los Teletubbies ===
# Teletubby Tinky Winky (Morado) - Feliz: 100
# Teletubby Po (Rojo) - Feliz: 100
# PersonajeTeletubby('Tinky Winky', 'Morado', 'Triángulo', 'Bolso')
# PersonajeTeletubby('Po', 'Rojo', 'Círculo', 'Patinete')
#
# === 2. Saludos ===
# ¡Hola! Soy Tinky Winky, soy de color Morado y mi antena tiene forma de Triángulo.
# ¡Tubby abrazo!
# ¡Hola! Soy Po, soy de color Rojo y mi antena tiene forma de Círculo.
# ¡Tubby abrazo!
#
# === 3. A jugar ===
# Tinky Winky está jugando con su Bolso.
# Po está jugando con su Patinete.
#
# === 4. Estado después de jugar ===
# Estado de Tinky Winky -> Felicidad: 110 | Hambre: 70
# Estado de Po -> Felicidad: 110 | Hambre: 70
#
# === 5. Solo Po come ===
# Po se está comiendo su Tubby Papilla. ¡Ñam, ñam!
#
# === 6. Estado final ===
# Estado de Tinky Winky -> Felicidad: 110 | Hambre: 70
# Estado de Po -> Felicidad: 130 | Hambre: 0
#
# === Extra: lista de Teletubbies (usa __repr__) ===
# [PersonajeTeletubby('Tinky Winky', 'Morado', 'Triángulo', 'Bolso'), PersonajeTeletubby('Po', 'Rojo', 'Círculo', 'Patinete')]
#
# === Cuestión teórica: ¿y si toco po.__nivel_hambre? ===
# Al leer po.__nivel_hambre -> AttributeError: 'PersonajeTeletubby' object has no attribute '__nivel_hambre'
# He hecho po.__nivel_hambre = 999
# po.__nivel_hambre (atributo nuevo): 999
# ver_estado() sigue igual -> Estado de Po -> Felicidad: 130 | Hambre: 0
# Atributos reales de po: {'nombre': 'Po', 'color': 'Rojo', 'antena': 'Círculo', 'objeto_favorito': 'Patinete', '_PersonajeTeletubby__nivel_hambre': 0, '_PersonajeTeletubby__nivel_felicidad': 130, '__nivel_hambre': 999}
# po._PersonajeTeletubby__nivel_hambre = 0
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Olvidar self en la definición: def jugar():  -> TypeError al llamar po.jugar()
#   ("takes 0 positional arguments but 1 was given").
# - Escribir nivel_hambre += 20 sin self.__ -> UnboundLocalError / variable local.
# - Un solo guion bajo (_nivel_hambre) NO es privado para Python: es solo
#   una convención "no lo toques". El enunciado pide DOS (__).
# - ver_estado() con print en vez de return -> print(po.ver_estado())
#   imprimiría el texto y después "None". Pierdes puntos: pide "devuelve".
# - Poner saludo_oficial dentro de __init__ como self.saludo_oficial -> sería
#   de instancia, no de clase. El enunciado pide variable DE CLASE.
# - __str__ y __repr__ deben hacer return de un str; si haces print dentro,
#   da TypeError ("__str__ returned non-string").
# - Olvidar los paréntesis: po.jugar (sin ()) no ejecuta nada.
# - En comer_tubby_papilla, "reduce a 0" es = 0, no -= 0 ni -= 20.
# - El enunciado no pone límite a la felicidad, así que puede superar 100.
#
# ALTERNATIVA (funciona, pero NO es lo que pide el enunciado):
# - Poner los privados como parámetros con valor por defecto:
#     def __init__(self, nombre, color, antena, objeto_favorito,
#                  nivel_hambre=50, nivel_felicidad=100):
#   Es válido, pero el enunciado solo pide los 4 públicos en el constructor.
# - @property en lugar de ver_estado(): es más "pythónico", pero el
#   enunciado pide un MÉTODO tipo getter llamado ver_estado().
# - En los apuntes aparece otra versión de __str__:
#     f"Teletubby {self.nombre} (Color: {self.color}) - Estado actual: Hambre {...}"
#   Aquí se ha usado el formato del EJEMPLO del enunciado ("- Feliz: 100").
#   Si en el examen te dan otro ejemplo, copia EXACTAMENTE ese formato.
# ---------------------------------------------------------------


# ===============================================================
# RESPUESTA A LA CUESTIÓN TEÓRICA (lista para copiar)
# ===============================================================
# ¿Qué ocurriría si intentaras modificar po.__nivel_hambre directamente
# desde el bloque principal? Justifica por qué se utilizan atributos privados.
#
# Al definir self.__nivel_hambre dentro de la clase, Python aplica el
# mecanismo de "name mangling": el atributo se guarda internamente con el
# nombre _PersonajeTeletubby__nivel_hambre. Por eso, desde el bloque
# principal:
#
#   - Si intento LEER po.__nivel_hambre, se produce un AttributeError,
#     porque el objeto no tiene ningún atributo con ese nombre exacto.
#
#   - Si intento ASIGNAR po.__nivel_hambre = 999, no da error, pero no se
#     modifica el atributo privado: fuera de la clase no hay name mangling,
#     así que Python crea un atributo NUEVO y público llamado __nivel_hambre
#     en ese objeto. El valor real (_PersonajeTeletubby__nivel_hambre) sigue
#     intacto, y ver_estado() seguirá mostrando el hambre verdadera.
#
#   - Técnicamente se podría acceder con po._PersonajeTeletubby__nivel_hambre,
#     porque en Python la privacidad no es absoluta como en Java, pero hacerlo
#     es una mala práctica que rompe el encapsulamiento.
#
# Se usan atributos privados para aplicar el ENCAPSULAMIENTO: los niveles de
# hambre y felicidad son el estado interno del personaje y solo deben cambiar
# a través de sus métodos (jugar() suma 20 de hambre y 10 de felicidad,
# comer_tubby_papilla() pone el hambre a 0 y suma 20 de felicidad). Así se
# evita que desde fuera se pongan valores incoherentes (por ejemplo, hambre
# negativa o un texto), se protege la lógica del objeto y, si algún día
# cambia la forma de calcular estos niveles, solo hay que tocar la clase.
# Para consultarlos desde fuera se usa el método getter ver_estado(), que
# devuelve la información de forma controlada sin permitir modificarla.
# ===============================================================
