"""
TEMA 6 (integrador) - Variante 06: "Arena Pythonia" (herencia y polimorfismo)
=============================================================================
ENUNCIADO (redactado al estilo del profesor, modelo Teletubbies):

    Objetivo: Diseñar una jerarquía de clases para un videojuego de combate
    por turnos: una clase base y dos clases hijas que la amplían con super().

    Requisitos de la clase base Personaje:
    1. Atributos de clase: mundo = "Pythonia" y total_personajes (contador).
    2. Atributos públicos: nombre, nivel (int, por defecto 1).
       Privados: __vida y __vida_max (100 + 10 * nivel).
    3. get_vida(): getter numérico. esta_vivo(): devuelve bool.
    4. recibir_danio(cantidad): resta vida sin bajar de 0 y DEVUELVE un string.
    5. curar(cantidad): sube vida sin pasar de __vida_max. Devuelve string.
    6. calcular_danio(): daño base = nivel * 3.
    7. atacar(objetivo): el objetivo recibe calcular_danio(). Devuelve string.
    8. ver_estado(): GETTER que DEVUELVE un string con nombre, clase, vida
       y una barra de vida hecha con "#" (una por cada 10 %).
    9. __str__ y __repr__.

    Requisitos de la clase hija Guerrero(Personaje):
    10. Atributos extra: fuerza y armadura. El constructor llama a
        super().__init__(...) para reutilizar el del padre.
    11. Sobrescribe calcular_danio(): daño base del padre (super()) + fuerza.
    12. Sobrescribe recibir_danio(): la armadura reduce el daño (mínimo 1)
        y luego llama a super().recibir_danio(...).

    Requisitos de la clase hija Mago(Personaje):
    13. Atributo extra: privado __mana (por defecto 30).
    14. Sobrescribe calcular_danio(): si tiene 10 de maná o más, lanza un
        hechizo (gasta 10, daño = nivel * 6); si no, golpe de bastón (2).
    15. __str__ de las hijas reutiliza super().__str__() y añade sus datos.

    Funciones:
    16. crear_personaje(tipo, **datos): fábrica con MATCH-CASE sobre el tipo
        ("guerrero", "mago", case _ -> None), usando **kwargs.
    17. describir(p): IF/ELIF con ISINSTANCE() para saber de qué clase es:
        Guerrero con fuerza >= 15 -> "Guerrero pesado", Guerrero -> "Guerrero",
        Mago -> "Mago", resto -> "Aventurero".
    18. combate(a, b, max_turnos=10): WHILE que alterna ataques mientras los
        dos sigan vivos y no se pase de max_turnos. Devuelve el ganador
        (o None si empatan por turnos) y una lista con el registro.
    19. clasificacion(personajes): SORTED + LAMBDA por vida (desc).
    20. vivos(personajes): COMPRENSIÓN DE LISTAS con los nombres vivos.
    21. contar_por_clase(personajes): DICCIONARIO {nombre_clase: cantidad}.

    Bloque principal: crea al menos 4 personajes (con la fábrica), muestra
    POLIMORFISMO (el mismo bucle llama a atacar() de cada clase),
    un combate completo, la clasificación con enumerate(start=1), el
    diccionario con .items(), isinstance() e issubclass().

    Cuestión teórica: ¿Por qué Guerrero NO puede escribir self.__vida
    aunque herede de Personaje? ¿Qué hace exactamente super()?

FORMA QUE EXIGE EL PROFESOR:
    - Herencia class Hija(Padre) y super().__init__ en las hijas.
    - Sobrescritura de métodos reutilizando super().metodo().
    - Atributos de clase, privados con __, getter que devuelve string.
    - match-case sobre el texto del tipo (con case _) y **kwargs en la fábrica.
    - if/elif con isinstance() para comprobar la clase de un objeto.
    - while con condición compuesta, comprensión, sorted+lambda,
      dict con .items(), enumerate(start=1), return y no print.

CONCEPTOS QUE PRACTICA:
    - Herencia, polimorfismo, name mangling en herencia, isinstance
    - type(obj).__name__ para obtener el nombre de la clase

CÓMO EJECUTARLO:  python 06_videojuego_herencia.py   (en Linux: python3 ...)
"""


# ---------------------------------------------------------------
# PASO 1: Clase base (padre).
# ---------------------------------------------------------------
class Personaje:
    """Clase base de todos los personajes del juego."""

    mundo = "Pythonia"
    total_personajes = 0

    def __init__(self, nombre, nivel=1):
        """Constructor del padre: lo reutilizan las hijas con super()."""
        self.nombre = nombre
        self.nivel = nivel
        self.__vida_max = 100 + 10 * nivel
        self.__vida = self.__vida_max
        Personaje.total_personajes += 1

    def get_vida(self):
        """Getter numérico de la vida."""
        return self.__vida

    def esta_vivo(self):
        """True si le queda vida."""
        return self.__vida > 0

    def recibir_danio(self, cantidad):
        """Resta vida (sin bajar de 0). Devuelve un string."""
        self.__vida = max(0, self.__vida - cantidad)
        texto = f"{self.nombre} recibe {cantidad} de daño (vida {self.__vida})"
        if not self.esta_vivo():
            texto += " y cae derrotado"
        return texto

    def curar(self, cantidad):
        """Sube vida sin pasar del máximo."""
        if not self.esta_vivo():
            return f"{self.nombre} no puede curarse: está derrotado."
        self.__vida = min(self.__vida_max, self.__vida + cantidad)
        return f"{self.nombre} se cura hasta {self.__vida}."

    def calcular_danio(self):
        """Daño base. Las hijas lo sobrescriben."""
        return self.nivel * 3

    def atacar(self, objetivo):
        """Ataca a otro personaje. Gracias al POLIMORFISMO, self.calcular_danio()
        y objetivo.recibir_danio() ejecutan la versión de la clase real."""
        danio = self.calcular_danio()
        return f"{self.nombre} ataca -> " + objetivo.recibir_danio(danio)

    def ver_estado(self):
        """GETTER que devuelve un string con barra de vida."""
        # Porcentaje de vida -> número de '#' (cada uno es un 10 %).
        bloques = round(self.__vida / self.__vida_max * 10)
        barra = "#" * bloques + "." * (10 - bloques)   # repetir strings con *
        # type(self).__name__ da "Guerrero" o "Mago" aunque estemos en el padre.
        return (f"{self.nombre:<8} {type(self).__name__:<9} "
                f"[{barra}] {self.__vida}/{self.__vida_max}")

    def __str__(self):
        """Texto amigable para el usuario (lo usa print)."""
        return f"{self.nombre} (nivel {self.nivel}) de {Personaje.mundo}"

    def __repr__(self):
        """Texto técnico: cómo se crearía este objeto."""
        return f"Personaje('{self.nombre}', {self.nivel})"


# ---------------------------------------------------------------
# PASO 2: Clases hijas. class Hija(Padre): hereda TODO lo público.
# ---------------------------------------------------------------
class Guerrero(Personaje):
    """Personaje cuerpo a cuerpo con fuerza y armadura."""

    def __init__(self, nombre, nivel=1, fuerza=10, armadura=2):
        """Llama al constructor del padre y añade sus propios atributos."""
        super().__init__(nombre, nivel)   # crea nombre, nivel, vida...
        self.fuerza = fuerza
        self.armadura = armadura

    def calcular_danio(self):
        """Sobrescribe: daño del padre + fuerza."""
        return super().calcular_danio() + self.fuerza

    def recibir_danio(self, cantidad):
        """Sobrescribe: la armadura reduce el daño y luego actúa el padre."""
        reducido = max(1, cantidad - self.armadura)
        # NO podemos hacer self.__vida -= reducido: dentro de Guerrero eso
        # sería self._Guerrero__vida (otro nombre). Delegamos en el padre.
        return super().recibir_danio(reducido)

    def __str__(self):
        """Texto amigable para el usuario (lo usa print)."""
        return f"{super().__str__()} | Guerrero F{self.fuerza} A{self.armadura}"

    def __repr__(self):
        """Texto técnico: cómo se crearía este objeto."""
        return (f"Guerrero('{self.nombre}', {self.nivel}, "
                f"{self.fuerza}, {self.armadura})")


class Mago(Personaje):
    """Personaje a distancia que gasta maná en hechizos."""

    coste_hechizo = 10   # atributo de clase propio de Mago

    def __init__(self, nombre, nivel=1, mana=30):
        """Constructor: guarda los datos iniciales del objeto."""
        super().__init__(nombre, nivel)
        self.__mana = mana   # privado de Mago: _Mago__mana

    def get_mana(self):
        """Getter: devuelve el maná que le queda."""
        return self.__mana

    def calcular_danio(self):
        """Sobrescribe: hechizo si hay maná, si no golpe de bastón."""
        if self.__mana >= Mago.coste_hechizo:
            self.__mana -= Mago.coste_hechizo
            return self.nivel * 6
        return 2

    def __str__(self):
        """Texto amigable para el usuario (lo usa print)."""
        return f"{super().__str__()} | Mago maná {self.__mana}"

    def __repr__(self):
        """Texto técnico: cómo se crearía este objeto."""
        return f"Mago('{self.nombre}', {self.nivel}, {self.__mana})"


# ---------------------------------------------------------------
# PASO 3: Funciones.
# ---------------------------------------------------------------
def crear_personaje(tipo, **datos):
    """Fábrica: crea el personaje según el tipo. **datos va al constructor."""
    match tipo.lower():
        case "guerrero":
            return Guerrero(**datos)
        case "mago":
            return Mago(**datos)
        case _:
            return None


def describir(p):
    """Devuelve el tipo de aventurero usando if/elif con isinstance().

    isinstance(p, Guerrero) devuelve True si p es un Guerrero (o de una
    clase hija de Guerrero). El orden importa: el caso más concreto
    ("Guerrero pesado") va ANTES que el general ("Guerrero").
    """
    if isinstance(p, Guerrero) and p.fuerza >= 15:
        return "Guerrero pesado"
    elif isinstance(p, Guerrero):
        return "Guerrero"
    elif isinstance(p, Mago):
        return "Mago"
    else:
        return "Aventurero"
    # Si te lo pidieran con MATCH-CASE, se puede hacer con lo visto en clase
    # (match sobre un texto + guardas), usando el nombre de la clase:
    #     match type(p).__name__:
    #         case "Guerrero" if p.fuerza >= 15:
    #             return "Guerrero pesado"
    #         case "Guerrero":
    #             return "Guerrero"
    #         case "Mago":
    #             return "Mago"
    #         case _:
    #             return "Aventurero"


def combate(a, b, max_turnos=10):
    """Combate por turnos con while. Devuelve (ganador o None, registro)."""
    registro = []
    turno = 1
    atacante, defensor = a, b
    # Condición compuesta: los dos vivos Y sin pasarnos de turnos.
    while a.esta_vivo() and b.esta_vivo() and turno <= max_turnos:
        registro.append(f"T{turno}: {atacante.atacar(defensor)}")
        atacante, defensor = defensor, atacante   # intercambio de turnos
        turno += 1
    if a.esta_vivo() and b.esta_vivo():
        return None, registro          # nadie cayó: empate
    ganador = a if a.esta_vivo() else b
    return ganador, registro           # return de dos valores = tupla


def clasificacion(personajes):
    """sorted + lambda por vida, de mayor a menor."""
    return sorted(personajes, key=lambda p: p.get_vida(), reverse=True)


def vivos(personajes):
    """Comprensión de listas: nombres de los que siguen en pie."""
    return [p.nombre for p in personajes if p.esta_vivo()]


def contar_por_clase(personajes):
    """Diccionario {nombre de la clase: cuántos hay}."""
    conteo = {}
    for p in personajes:
        clase = type(p).__name__
        conteo[clase] = conteo.get(clase, 0) + 1
    return conteo


# ---------------------------------------------------------------
# PASO 4: Bloque principal.
# ---------------------------------------------------------------
if __name__ == "__main__":
    personajes = [
        crear_personaje("guerrero", nombre="Brok", nivel=3, fuerza=16, armadura=4),
        crear_personaje("mago", nombre="Elora", nivel=4, mana=40),
        crear_personaje("Guerrero", nombre="Tess", nivel=2),
        crear_personaje("mago", nombre="Fizz", nivel=1, mana=10),
        Personaje("Aldeano"),                    # objeto de la clase base
    ]
    print("Tipo desconocido ->", crear_personaje("dragón", nombre="X"))

    print(f"\n--- Personajes de {Personaje.mundo} ---")
    for num, p in enumerate(personajes, start=1):
        print(f"{num}. {p}  <{describir(p)}>")

    print("\n--- Polimorfismo: todos atacan al Aldeano ---")
    aldeano = personajes[-1]                     # último elemento
    for p in personajes[:-1]:                    # todos menos el último
        print(p.atacar(aldeano))                 # cada uno usa SU calcular_danio

    print("\n--- Combate: Brok vs Elora ---")
    brok, elora = personajes[0], personajes[1]
    ganador, registro = combate(brok, elora, max_turnos=20)
    for linea in registro:
        print(linea)
    print("Ganador:", ganador.nombre if ganador else "empate")

    print("\n--- Curaciones ---")
    print(brok.curar(50))
    print(elora.curar(50))

    print("\n--- Clasificación por vida ---")
    for puesto, p in enumerate(clasificacion(personajes), start=1):
        print(f"{puesto}. {p.ver_estado()}")

    print("\nSiguen vivos:", vivos(personajes))
    print("\n--- Personajes por clase ---")
    for clase, cantidad in contar_por_clase(personajes).items():
        print(f"{clase}: {cantidad}")

    print("\nisinstance(brok, Personaje):", isinstance(brok, Personaje))
    print("isinstance(brok, Mago):", isinstance(brok, Mago))
    print("issubclass(Mago, Personaje):", issubclass(Mago, Personaje))
    print("Repr:", personajes)
    print("Total personajes:", Personaje.total_personajes)

# ---------------------------------------------------------------
# SALIDA ESPERADA (copiada de la ejecución real):
# Tipo desconocido -> None
#
# --- Personajes de Pythonia ---
# 1. Brok (nivel 3) de Pythonia | Guerrero F16 A4  <Guerrero pesado>
# 2. Elora (nivel 4) de Pythonia | Mago maná 40  <Mago>
# 3. Tess (nivel 2) de Pythonia | Guerrero F10 A2  <Guerrero>
# 4. Fizz (nivel 1) de Pythonia | Mago maná 10  <Mago>
# 5. Aldeano (nivel 1) de Pythonia  <Aventurero>
#
# --- Polimorfismo: todos atacan al Aldeano ---
# Brok ataca -> Aldeano recibe 25 de daño (vida 85)
# Elora ataca -> Aldeano recibe 24 de daño (vida 61)
# Tess ataca -> Aldeano recibe 16 de daño (vida 45)
# Fizz ataca -> Aldeano recibe 6 de daño (vida 39)
#
# --- Combate: Brok vs Elora ---
# T1: Brok ataca -> Elora recibe 25 de daño (vida 115)
# T2: Elora ataca -> Brok recibe 20 de daño (vida 110)
# T3: Brok ataca -> Elora recibe 25 de daño (vida 90)
# T4: Elora ataca -> Brok recibe 20 de daño (vida 90)
# T5: Brok ataca -> Elora recibe 25 de daño (vida 65)
# T6: Elora ataca -> Brok recibe 20 de daño (vida 70)
# T7: Brok ataca -> Elora recibe 25 de daño (vida 40)
# T8: Elora ataca -> Brok recibe 1 de daño (vida 69)
# T9: Brok ataca -> Elora recibe 25 de daño (vida 15)
# T10: Elora ataca -> Brok recibe 1 de daño (vida 68)
# T11: Brok ataca -> Elora recibe 25 de daño (vida 0) y cae derrotado
# Ganador: Brok
#
# --- Curaciones ---
# Brok se cura hasta 118.
# Elora no puede curarse: está derrotado.
#
# --- Clasificación por vida ---
# 1. Tess     Guerrero  [##########] 120/120
# 2. Brok     Guerrero  [#########.] 118/130
# 3. Fizz     Mago      [##########] 110/110
# 4. Aldeano  Personaje [####......] 39/110
# 5. Elora    Mago      [..........] 0/140
#
# Siguen vivos: ['Brok', 'Tess', 'Fizz', 'Aldeano']
#
# --- Personajes por clase ---
# Guerrero: 2
# Mago: 2
# Personaje: 1
#
# isinstance(brok, Personaje): True
# isinstance(brok, Mago): False
# issubclass(Mago, Personaje): True
# Repr: [Guerrero('Brok', 3, 16, 4), Mago('Elora', 4, 0), Guerrero('Tess', 2, 10, 2), Mago('Fizz', 1, 0), Personaje('Aldeano', 1)]
# Total personajes: 5
# ---------------------------------------------------------------
# RESPUESTA A LA CUESTIÓN TEÓRICA:
# - Por el name mangling: self.__vida escrito dentro de Personaje se
#   convierte en self._Personaje__vida; escrito dentro de Guerrero sería
#   self._Guerrero__vida, que NO existe. Los privados con __ no se
#   heredan "visibles": la hija usa los métodos del padre (get_vida,
#   super().recibir_danio...). En Java pasa lo mismo con private
#   (lo parecido a protected en Python sería un solo guion: _vida).
# - super() permite llamar a los métodos de la clase padre desde la hija
#   (en herencia simple, "el padre"; en herencia múltiple, la siguiente
#   clase del MRO): super().__init__(...) reutiliza el constructor del
#   padre y super().calcular_danio() reutiliza su cálculo para ampliarlo.
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Olvidar super().__init__ en la hija: el objeto no tendrá nombre,
#   nivel ni vida -> AttributeError al usarlos.
# - isinstance(objeto, Clase): primero el OBJETO y luego la CLASE (sin
#   comillas y sin paréntesis): isinstance(p, Guerrero), no isinstance(Guerrero, p).
# - El orden de los if importa: "Guerrero pesado" antes que "Guerrero";
#   si no, todos los guerreros entrarían en el primero.
# EN JAVA SERÍA... class Guerrero extends Personaje { super(nombre, nivel); }
# ALTERNATIVA (funciona, pero NO es lo que pide el enunciado):
#   type(p) == Guerrero en vez de isinstance(p, Guerrero): funciona aquí,
#   pero no acepta clases hijas; lo habitual es isinstance().
#   Copiar el código del constructor del padre en cada hija -> pide super().
# ---------------------------------------------------------------
