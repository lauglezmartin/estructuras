"""
TEMA 6 (integrador) - Variante 01: "El refugio de mascotas virtuales" (tipo Tamagotchi)
=====================================================================================
ENUNCIADO (redactado al estilo del profesor, modelo Teletubbies):

    Objetivo: Diseñar una clase que represente una mascota virtual y gestionar
    un refugio (lista de objetos) aplicando POO, condicionales, bucles,
    funciones, diccionarios, comprensiones de listas y lambda.

    Requisitos de la clase MascotaVirtual:
    1. Atributo de clase: nombre_app = "TamaPy" y un contador total_mascotas
       que se incremente cada vez que se crea una mascota.
    2. Atributos de instancia:
       - Públicos: nombre (str), especie (str).
       - Privados (__): __hambre (int, por defecto 50), __energia (int, por
         defecto 80), __felicidad (int, por defecto 60).
       Los niveles siempre deben quedar entre 0 y 100.
    3. alimentar(*comidas): recibe un número variable de comidas (*args).
       Cada comida reduce __hambre en 15. Devuelve (return) un mensaje.
    4. jugar(minutos): solo acepta minutos entre 1 y 60 usando una
       COMPARACIÓN ENCADENADA. Si no es válido, devuelve un mensaje de error
       (return temprano). Si es válido: felicidad += minutos // 2,
       energia -= minutos, hambre += minutos // 3.
    5. dormir(): energía a 100 y hambre += 10. Devuelve un mensaje.
    6. ver_estado(): GETTER que DEVUELVE un string con los tres niveles.
    7. estado_animo(): usa MATCH-CASE con GUARDAS para devolver:
       "Hambrienta" si hambre >= 80, "Agotada" si energía <= 20,
       "Feliz" si felicidad >= 70, "Normal" en cualquier otro caso (case _).
    8. get_felicidad(): getter que devuelve el entero (se usará con lambda).
    9. __str__ (amigable) y __repr__ (técnico, como se instanció).

    Funciones fuera de la clase:
    10. resumen_refugio(mascotas): devuelve un DICCIONARIO {nombre: ánimo}.
    11. mascotas_que_necesitan_cuidado(mascotas): devuelve con una
        COMPRENSIÓN DE LISTAS los nombres de las que NO están "Feliz" ni "Normal".

    Bloque principal (if __name__ == "__main__"):
    12. Crea al menos 3 mascotas en una lista y recórrela con enumerate(start=1).
    13. Haz que interactúen (alimentar con varias comidas, jugar, dormir,
        y un jugar con minutos inválidos).
    14. Recorre el diccionario del resumen con .items().
    15. Ordena las mascotas por felicidad (de mayor a menor) con sorted + lambda.
    16. Muestra total_mascotas y el atributo de clase.
    17. (Opcional) Menú interactivo con while + input en una función aparte.

    Cuestión teórica: ¿Por qué alimentar() usa *args? ¿Qué diferencia hay
    entre que ver_estado() devuelva el texto o lo imprima?

FORMA QUE EXIGE EL PROFESOR:
    - Atributo de clase + contador de clase (MascotaVirtual.total_mascotas += 1).
    - Atributos privados con doble guion bajo (__).
    - Getter que DEVUELVE string (return, no print).
    - *args en alimentar.
    - Comparación encadenada 1 <= minutos <= 60.
    - match-case con guardas (case _ if ...) y case _ final.
    - Diccionario recorrido con .items(), enumerate(start=1),
      comprensión de listas, sorted con key=lambda.

CONCEPTOS QUE PRACTICA:
    - Clases, atributos de clase/instancia, privados, __str__/__repr__
    - *args, return temprano, comparación encadenada, match-case
    - Lista de objetos, diccionario, comprensión, lambda, while (menú)

CÓMO EJECUTARLO:  python 01_tamagotchi_mascotas.py   (en Linux/Docker: python3 ...)
"""


# ---------------------------------------------------------------
# PASO 1: La clase. Atributos de CLASE arriba (compartidos por todas
# las mascotas) y atributos de INSTANCIA en __init__ (uno por mascota).
# ---------------------------------------------------------------
class MascotaVirtual:
    """Representa una mascota virtual con niveles de hambre, energía y felicidad."""

    # Atributos de clase: se escriben FUERA de __init__ y SIN self.
    nombre_app = "TamaPy"
    total_mascotas = 0  # contador compartido por toda la clase

    def __init__(self, nombre, especie, hambre=50, energia=80, felicidad=60):
        """Constructor: guarda los datos públicos y los niveles privados."""
        # Públicos: se pueden leer/cambiar desde fuera (mascota.nombre).
        self.nombre = nombre
        self.especie = especie
        # Privados: el doble guion bajo activa el "name mangling"
        # (Python lo renombra a _MascotaVirtual__hambre).
        # Pasan por __limitar para que también al crearla queden entre 0 y 100.
        self.__hambre = self.__limitar(hambre)
        self.__energia = self.__limitar(energia)
        self.__felicidad = self.__limitar(felicidad)
        # Para tocar el contador de CLASE se usa el nombre de la clase.
        # OJO: self.total_mascotas += 1 crearía un atributo de instancia nuevo.
        MascotaVirtual.total_mascotas += 1

    # Método auxiliar privado: mantiene un valor entre 0 y 100.
    # Se llama __limitar para que no se use desde fuera de la clase.
    def __limitar(self, valor):
        """Devuelve el valor recortado al rango 0-100."""
        return max(0, min(100, valor))

    def alimentar(self, *comidas):
        """Da de comer. *comidas recoge todas las comidas en una TUPLA."""
        # Cláusula de guarda: si no pasan ninguna comida, salimos ya.
        if not comidas:
            return f"{self.nombre} no ha recibido nada de comer."
        # len(comidas) = cuántos argumentos llegaron.
        self.__hambre = self.__limitar(self.__hambre - 15 * len(comidas))
        # ", ".join(...) une la tupla de strings con comas.
        return f"{self.nombre} come: {', '.join(comidas)}. Hambre: {self.__hambre}"

    def jugar(self, minutos):
        """Juega unos minutos (solo entre 1 y 60)."""
        # Comparación ENCADENADA: equivale a 1 <= minutos and minutos <= 60.
        # Usamos "not (...)" para hacer el return temprano del caso inválido.
        if not (1 <= minutos <= 60):
            return f"Error: {minutos} minutos no es válido (1-60)."
        self.__felicidad = self.__limitar(self.__felicidad + minutos // 2)
        self.__energia = self.__limitar(self.__energia - minutos)
        self.__hambre = self.__limitar(self.__hambre + minutos // 3)
        return f"{self.nombre} ha jugado {minutos} min."

    def dormir(self):
        """Recupera toda la energía, pero se despierta con algo de hambre."""
        self.__energia = 100
        self.__hambre = self.__limitar(self.__hambre + 10)
        return f"{self.nombre} ha dormido. Energía al máximo."

    def ver_estado(self):
        """GETTER: devuelve (no imprime) un texto con el estado interno."""
        return (f"Estado de {self.nombre} -> Hambre: {self.__hambre} | "
                f"Energía: {self.__energia} | Felicidad: {self.__felicidad}")

    def get_felicidad(self):
        """Getter numérico: necesario para ordenar desde fuera con lambda."""
        return self.__felicidad

    def estado_animo(self):
        """Devuelve el ánimo usando match-case con guardas."""
        # Truco típico: hacemos match sobre algo cualquiera (aquí self) y
        # decidimos con las GUARDAS "if". El orden de los case importa:
        # se ejecuta el PRIMERO que cumpla.
        match self:
            case _ if self.__hambre >= 80:
                return "Hambrienta"
            case _ if self.__energia <= 20:
                return "Agotada"
            case _ if self.__felicidad >= 70:
                return "Feliz"
            case _:  # comodín: equivale al "else"/"default"
                return "Normal"

    def __str__(self):
        """Texto amigable: lo usa print(mascota) y str(mascota)."""
        return f"{self.especie} {self.nombre} - Ánimo: {self.estado_animo()}"

    def __repr__(self):
        """Texto técnico: cómo se instanció. Lo usa print(lista_de_mascotas)."""
        return (f"MascotaVirtual('{self.nombre}', '{self.especie}', "
                f"{self.__hambre}, {self.__energia}, {self.__felicidad})")


# ---------------------------------------------------------------
# PASO 2: Funciones que trabajan con la LISTA de objetos.
# Devuelven datos (return): quien las llama decide si los imprime.
# ---------------------------------------------------------------
def resumen_refugio(mascotas):
    """Devuelve un diccionario {nombre: ánimo} de todas las mascotas."""
    resumen = {}
    for mascota in mascotas:
        resumen[mascota.nombre] = mascota.estado_animo()
    return resumen
    # Versión en una línea (comprensión de diccionario):
    # return {m.nombre: m.estado_animo() for m in mascotas}


def mascotas_que_necesitan_cuidado(mascotas):
    """Devuelve (comprensión de listas) los nombres que necesitan atención."""
    # Estructura: [EXPRESIÓN for ELEMENTO in LISTA if CONDICIÓN]
    return [m.nombre for m in mascotas
            if m.estado_animo() not in ("Feliz", "Normal")]


# ---------------------------------------------------------------
# PASO 3 (opcional): menú interactivo con while + input.
# Está en una función aparte para que el main se ejecute sin pedir datos.
# Para probarlo, descomenta la llamada al final del main.
# ---------------------------------------------------------------
def menu_interactivo(mascota):
    """Menú con while: se repite hasta que el usuario elige salir."""
    opcion = ""
    while opcion != "0":
        print("\n1) Alimentar  2) Jugar  3) Dormir  4) Ver estado  0) Salir")
        opcion = input("Elige opción: ")
        match opcion:
            case "1":
                print(mascota.alimentar("pienso"))
            case "2":
                minutos = int(input("¿Cuántos minutos? "))
                print(mascota.jugar(minutos))
            case "3":
                print(mascota.dormir())
            case "4":
                print(mascota.ver_estado())
            case "0":
                print("¡Hasta pronto!")
            case _:
                print("Opción no válida.")


# ---------------------------------------------------------------
# PASO 4: Bloque principal con datos de prueba fijos.
# ---------------------------------------------------------------
if __name__ == "__main__":
    print(f"=== Bienvenida a {MascotaVirtual.nombre_app} ===")

    # Lista de objetos: cada elemento es una instancia.
    refugio = [
        MascotaVirtual("Pelusa", "Gato"),
        MascotaVirtual("Rex", "Dinosaurio", hambre=70, energia=30),
        MascotaVirtual("Burbuja", "Pez", felicidad=90),
    ]

    # enumerate(..., start=1) da el número de orden empezando en 1.
    print("\n--- Mascotas del refugio ---")
    for numero, mascota in enumerate(refugio, start=1):
        print(f"{numero}. {mascota}")  # print llama a __str__

    print("\n--- Interacciones ---")
    pelusa, rex, burbuja = refugio  # desempaquetado de la lista
    print(pelusa.alimentar("pienso", "atún"))     # *args: 2 comidas
    print(pelusa.jugar(40))
    print(rex.jugar(25))
    print(rex.jugar(90))                         # inválido -> mensaje de error
    print(burbuja.alimentar())                    # *args vacío
    print(burbuja.dormir())

    print("\n--- Estados (getter que devuelve string) ---")
    for mascota in refugio:
        print(mascota.ver_estado())

    print("\n--- Resumen del refugio (dict con .items()) ---")
    for nombre, animo in resumen_refugio(refugio).items():
        print(f"{nombre}: {animo}")

    print("\nNecesitan cuidado:", mascotas_que_necesitan_cuidado(refugio))

    # sorted NO modifica la lista original; key=lambda dice POR QUÉ ordenar.
    # reverse=True -> de mayor a menor.
    ranking = sorted(refugio, key=lambda m: m.get_felicidad(), reverse=True)
    print("\n--- Ranking de felicidad ---")
    for posicion, mascota in enumerate(ranking, start=1):
        print(f"{posicion}º {mascota.nombre} ({mascota.get_felicidad()})")

    print("\nRepr de la lista:", refugio)  # print de una lista usa __repr__
    print(f"Total de mascotas creadas: {MascotaVirtual.total_mascotas}")

    # Cuestión típica: acceder al privado desde fuera da AttributeError.
    try:
        print(pelusa.__hambre)
    except AttributeError as error:
        print("AttributeError:", error)

    # menu_interactivo(pelusa)   # <- descomenta para probar el menú con input()

# ---------------------------------------------------------------
# SALIDA ESPERADA (copiada de la ejecución real):
# === Bienvenida a TamaPy ===
#
# --- Mascotas del refugio ---
# 1. Gato Pelusa - Ánimo: Normal
# 2. Dinosaurio Rex - Ánimo: Normal
# 3. Pez Burbuja - Ánimo: Feliz
#
# --- Interacciones ---
# Pelusa come: pienso, atún. Hambre: 20
# Pelusa ha jugado 40 min.
# Rex ha jugado 25 min.
# Error: 90 minutos no es válido (1-60).
# Burbuja no ha recibido nada de comer.
# Burbuja ha dormido. Energía al máximo.
#
# --- Estados (getter que devuelve string) ---
# Estado de Pelusa -> Hambre: 33 | Energía: 40 | Felicidad: 80
# Estado de Rex -> Hambre: 78 | Energía: 5 | Felicidad: 72
# Estado de Burbuja -> Hambre: 60 | Energía: 100 | Felicidad: 90
#
# --- Resumen del refugio (dict con .items()) ---
# Pelusa: Feliz
# Rex: Agotada
# Burbuja: Feliz
#
# Necesitan cuidado: ['Rex']
#
# --- Ranking de felicidad ---
# 1º Burbuja (90)
# 2º Pelusa (80)
# 3º Rex (72)
#
# Repr de la lista: [MascotaVirtual('Pelusa', 'Gato', 33, 40, 80), MascotaVirtual('Rex', 'Dinosaurio', 78, 5, 72), MascotaVirtual('Burbuja', 'Pez', 60, 100, 90)]
# Total de mascotas creadas: 3
# AttributeError: 'MascotaVirtual' object has no attribute '__hambre'
# ---------------------------------------------------------------
# RESPUESTA A LA CUESTIÓN TEÓRICA:
# - *args permite llamar a alimentar() con 0, 1 o muchas comidas; dentro
#   llegan como una tupla (comidas). Sin *args habría que pasar una lista.
# - Si ver_estado() hace return, el texto se puede guardar, comparar o
#   imprimir donde quieras. Si hiciera print, devolvería None y
#   print(m.ver_estado()) mostraría el texto y luego "None".
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Olvidar self en los métodos: def jugar(minutos) -> TypeError al llamarlo.
# - Escribir self.total_mascotas += 1: NO cambia el contador de la clase.
# - En match-case, "case _:" (sin if) tiene que ir el ÚLTIMO: si lo pones
#   antes que otros, Python da SyntaxError ("wildcard makes remaining
#   patterns unreachable"). Con guarda ("case _ if ...") sí puede ir antes.
# - Desde fuera NO existe mascota.__hambre (name mangling); existe
#   mascota._MascotaVirtual__hambre, pero usarlo rompe el encapsulamiento.
# EN JAVA SERÍA... private int hambre; y static int totalMascotas;
# ALTERNATIVA (funciona, pero NO es lo que pide el enunciado):
#   if 1 <= minutos and minutos <= 60  -> pide comparación ENCADENADA.
#   un if/elif/else en estado_animo    -> pide match-case con guardas.
# ---------------------------------------------------------------
