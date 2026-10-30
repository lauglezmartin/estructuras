"""
TEMA 6 - Ejercicio 2: Teletubbies ampliado (lista de objetos, diccionarios y lambda)
==================================================================================
ENUNCIADO (ampliación para practicar el tema 6 completo; no es literal del profesor):
    Partiendo de la clase PersonajeTeletubby de la práctica evaluada:
    - Añade getters (get_nivel_hambre, get_nivel_felicidad) y un setter con
      validación (set_nivel_hambre: solo enteros entre 0 y 100).
    - Crea una LISTA con los cuatro Teletubbies (lista de objetos).
    - Recórrela con for, busca uno por nombre, filtra con una comprensión de
      listas los que tienen hambre > 50 y ordénalos con sorted(key=lambda ...).
    - Crea un diccionario nombre -> objeto y otro {nombre: color} con una
      comprensión de diccionario.

FORMA QUE EXIGE EL PROFESOR:
    - Clase PersonajeTeletubby igual que en la práctica (atributo de clase,
      privados con __, ver_estado() que DEVUELVE un str, __str__ y __repr__).
    - Para filtrar/transformar en una línea: COMPRENSIÓN DE LISTAS.
    - Para ordenar por un atributo: sorted(lista, key=lambda t: t.atributo).
    - Recorrer diccionarios con .items() / .values().
    - Pruebas dentro de if __name__ == "__main__":

CONCEPTOS QUE PRACTICA:
    - Lista de objetos: añadir, recorrer, buscar, filtrar, ordenar.
    - Getters y setters con validación (los privados solo se tocan desde la clase).
    - Diccionario de objetos y comprensión de diccionario.
    - lambda como "key" de sorted y max.

CÓMO EJECUTARLO:  python 02_teletubbies_ampliado.py   (en Linux/Docker: python3 02_teletubbies_ampliado.py)
"""


# ---------------------------------------------------------------
# PASO 1: LA CLASE (la misma de la práctica + getters y setter)
# ---------------------------------------------------------------
class PersonajeTeletubby:
    """Representa a un personaje Teletubby con sus niveles de hambre y felicidad."""

    saludo_oficial = "¡Tubby abrazo!"       # atributo de CLASE (compartido)

    def __init__(self, nombre, color, antena, objeto_favorito):
        """Crea un Teletubby con datos públicos y niveles privados por defecto."""
        self.nombre = nombre                # públicos
        self.color = color
        self.antena = antena
        self.objeto_favorito = objeto_favorito
        self.__nivel_hambre = 50            # privados (name mangling)
        self.__nivel_felicidad = 100

    # ---- Métodos de la práctica ----
    def saludar(self):
        """Muestra una presentación con nombre, color y forma de antena."""
        print(f"¡Hola! Soy {self.nombre}, soy de color {self.color} "
              f"y mi antena tiene forma de {self.antena}.")

    def jugar(self):
        """Juega con su objeto favorito: +20 de hambre y +10 de felicidad."""
        print(f"{self.nombre} está jugando con su {self.objeto_favorito}.")
        self.__nivel_hambre += 20
        self.__nivel_felicidad += 10

    def comer_tubby_papilla(self):
        """Come Tubby Papilla: hambre a 0 y +20 de felicidad."""
        print(f"{self.nombre} se está comiendo su Tubby Papilla. ¡Ñam, ñam!")
        self.__nivel_hambre = 0
        self.__nivel_felicidad += 20

    def ver_estado(self):
        """Getter: devuelve un texto con los niveles de felicidad y hambre."""
        return (f"Estado de {self.nombre} -> Felicidad: {self.__nivel_felicidad}"
                f" | Hambre: {self.__nivel_hambre}")

    # ---- GETTERS nuevos ----
    # Un getter DEVUELVE el valor de un privado. Hacen falta porque desde
    # fuera no se puede escribir t.__nivel_hambre (AttributeError) y para
    # filtrar u ordenar por hambre necesitamos el NÚMERO, no un texto.
    def get_nivel_hambre(self):
        """Devuelve el nivel de hambre (int)."""
        return self.__nivel_hambre

    def get_nivel_felicidad(self):
        """Devuelve el nivel de felicidad (int)."""
        return self.__nivel_felicidad

    # ---- SETTER con validación ----
    # Un setter CAMBIA un privado, pero solo si el valor es correcto.
    # Esa es la gracia del encapsulamiento: la clase controla qué entra.
    def set_nivel_hambre(self, nuevo_nivel):
        """Cambia el nivel de hambre si es un entero entre 0 y 100.

        Devuelve True si lo cambia y False si el valor no es válido.
        """
        # isinstance(x, int) comprueba que sea un entero.
        # 0 <= x <= 100 es una comparación encadenada (en Java: x >= 0 && x <= 100).
        if isinstance(nuevo_nivel, int) and 0 <= nuevo_nivel <= 100:
            self.__nivel_hambre = nuevo_nivel
            return True
        print(f"Valor no válido para el hambre de {self.nombre}: {nuevo_nivel!r} "
              f"(debe ser un entero de 0 a 100).")
        return False

    # ---- Métodos mágicos ----
    def __str__(self):
        """Texto amigable para el usuario (print)."""
        return f"Teletubby {self.nombre} ({self.color}) - Feliz: {self.__nivel_felicidad}"

    def __repr__(self):
        """Texto técnico: cómo se creó el objeto (repr y print de listas)."""
        return (f"PersonajeTeletubby('{self.nombre}', '{self.color}', "
                f"'{self.antena}', '{self.objeto_favorito}')")


# ---------------------------------------------------------------
# PASO 2: FUNCIÓN DE BÚSQUEDA EN UNA LISTA DE OBJETOS
# ---------------------------------------------------------------
def buscar_por_nombre(lista, nombre):
    """Devuelve el Teletubby cuyo nombre coincide (sin mirar mayúsculas) o None."""
    for teletubby in lista:
        # .lower() en los dos lados para que "po" encuentre a "Po".
        if teletubby.nombre.lower() == nombre.lower():
            return teletubby        # en cuanto lo encuentra, sale de la función
    return None                     # si el for termina sin encontrarlo


# ---------------------------------------------------------------
# PASO 3: PRUEBAS
# ---------------------------------------------------------------
if __name__ == "__main__":

    # 3.1 LISTA DE OBJETOS: cada elemento es un objeto PersonajeTeletubby.
    print("=== Lista de Teletubbies ===")
    teletubbies = [
        PersonajeTeletubby("Tinky Winky", "Morado", "Triángulo", "Bolso"),
        PersonajeTeletubby("Dipsy", "Verde", "Palo", "Sombrero"),
        PersonajeTeletubby("Laa-Laa", "Amarillo", "Rizo", "Pelota"),
    ]
    # append() añade un objeto al final de la lista.
    teletubbies.append(PersonajeTeletubby("Po", "Rojo", "Círculo", "Patinete"))
    print(teletubbies)              # print de una lista -> usa __repr__ de cada uno
    print("Hay", len(teletubbies), "Teletubbies")

    # 3.2 RECORRER con for (cada vuelta, t es UN objeto -> t.nombre, t.saludar()...)
    print("\n=== Recorrer con for (usa __str__) ===")
    for t in teletubbies:
        print(t)                    # print de UN objeto -> usa __str__

    # enumerate(..., start=1) da posición y objeto a la vez (forma pedida en bucles).
    print("\n=== Recorrer con enumerate ===")
    for posicion, t in enumerate(teletubbies, start=1):
        print(f"{posicion}. {t.nombre} - antena: {t.antena}")

    # 3.3 Modificar estados para tener datos variados.
    print("\n=== Jugamos un poco ===")
    teletubbies[0].jugar()          # Tinky Winky: hambre 70
    teletubbies[0].jugar()          # Tinky Winky: hambre 90
    teletubbies[1].jugar()          # Dipsy: hambre 70
    teletubbies[3].comer_tubby_papilla()    # Po: hambre 0
    for t in teletubbies:
        print(t.ver_estado())

    # 3.4 GETTERS y SETTER con validación.
    print("\n=== Getters y setter ===")
    laa_laa = teletubbies[2]
    print("Hambre de Laa-Laa (getter):", laa_laa.get_nivel_hambre())
    laa_laa.set_nivel_hambre(60)            # válido -> cambia
    print("Tras set_nivel_hambre(60):", laa_laa.get_nivel_hambre())
    laa_laa.set_nivel_hambre(150)           # fuera de rango -> no cambia
    laa_laa.set_nivel_hambre("mucha")       # no es int -> no cambia
    print("Sigue en:", laa_laa.get_nivel_hambre())

    # 3.5 BUSCAR por nombre.
    print("\n=== Buscar por nombre ===")
    encontrado = buscar_por_nombre(teletubbies, "dipsy")
    if encontrado:                  # None se evalúa como False
        print("Encontrado:", encontrado)
    else:
        print("No encontrado")
    if buscar_por_nombre(teletubbies, "Noo-Noo") is None:
        print("Noo-Noo no está en la lista")

    # 3.6 FILTRAR con comprensión de listas: los que tienen hambre > 50.
    #     Forma: [expresión for elemento in lista if condición]
    #     OJO: hay que usar el getter; t.__nivel_hambre daría AttributeError.
    print("\n=== Filtrar: hambre > 50 ===")
    hambrientos = [t for t in teletubbies if t.get_nivel_hambre() > 50]
    print(hambrientos)
    # Solo los nombres (la expresión puede ser cualquier cosa, no solo t):
    nombres_hambrientos = [t.nombre for t in hambrientos]
    print(nombres_hambrientos)
    # El for equivalente (funciona, pero el profesor pide comprensión para esto):
    #   hambrientos = []
    #   for t in teletubbies:
    #       if t.get_nivel_hambre() > 50:
    #           hambrientos.append(t)

    # 3.7 ORDENAR con sorted(key=lambda ...).
    #     key recibe una función que dice POR QUÉ ordenar. La lambda recibe un
    #     Teletubby (t) y devuelve el dato por el que se compara.
    #     sorted() devuelve una lista NUEVA; la original no cambia.
    print("\n=== Ordenar ===")
    por_hambre = sorted(teletubbies, key=lambda t: t.get_nivel_hambre())
    print("Por hambre (menor a mayor):", [t.nombre for t in por_hambre])
    por_hambre_desc = sorted(teletubbies, key=lambda t: t.get_nivel_hambre(), reverse=True)
    print("Por hambre (mayor a menor):", [t.nombre for t in por_hambre_desc])
    por_nombre = sorted(teletubbies, key=lambda t: t.nombre)
    print("Por nombre:", [t.nombre for t in por_nombre])

    # max / min con key: el MÁS hambriento y el MÁS feliz.
    mas_hambriento = max(teletubbies, key=lambda t: t.get_nivel_hambre())
    mas_feliz = max(teletubbies, key=lambda t: t.get_nivel_felicidad())
    print("Más hambriento:", mas_hambriento.nombre)
    print("Más feliz:", mas_feliz.nombre)

    # 3.8 DICCIONARIO nombre -> objeto (buscar por clave es directo, sin for).
    print("\n=== Diccionario nombre -> objeto ===")
    por_nombre_dic = {}
    for t in teletubbies:
        por_nombre_dic[t.nombre] = t       # añadir clave: valor
    print(por_nombre_dic["Po"])            # acceso directo por clave (__str__)
    print(por_nombre_dic.get("Noo-Noo", "No existe"))   # get evita KeyError
    # Recorrer con .items(): clave y valor a la vez.
    for nombre, t in por_nombre_dic.items():
        print(f"{nombre}: {t.get_nivel_hambre()} de hambre")

    # 3.9 COMPRENSIÓN DE DICCIONARIO: {clave: valor for elemento in lista}
    print("\n=== Comprensión de diccionario ===")
    colores = {t.nombre: t.color for t in teletubbies}
    print(colores)
    # Con if: solo los que tienen hambre > 50, nombre -> hambre.
    hambre_alta = {t.nombre: t.get_nivel_hambre() for t in teletubbies if t.get_nivel_hambre() > 50}
    print(hambre_alta)

    # 3.10 Contar y sumar con la lista de objetos.
    print("\n=== Contar y sumar ===")
    total_hambre = sum(t.get_nivel_hambre() for t in teletubbies)
    print("Hambre total:", total_hambre)
    print("Media de hambre:", total_hambre / len(teletubbies))
    print("Cuántos tienen hambre > 50:", len(hambrientos))


# ---------------------------------------------------------------
# SALIDA ESPERADA:
# === Lista de Teletubbies ===
# [PersonajeTeletubby('Tinky Winky', 'Morado', 'Triángulo', 'Bolso'), PersonajeTeletubby('Dipsy', 'Verde', 'Palo', 'Sombrero'), PersonajeTeletubby('Laa-Laa', 'Amarillo', 'Rizo', 'Pelota'), PersonajeTeletubby('Po', 'Rojo', 'Círculo', 'Patinete')]
# Hay 4 Teletubbies
#
# === Recorrer con for (usa __str__) ===
# Teletubby Tinky Winky (Morado) - Feliz: 100
# Teletubby Dipsy (Verde) - Feliz: 100
# Teletubby Laa-Laa (Amarillo) - Feliz: 100
# Teletubby Po (Rojo) - Feliz: 100
#
# === Recorrer con enumerate ===
# 1. Tinky Winky - antena: Triángulo
# 2. Dipsy - antena: Palo
# 3. Laa-Laa - antena: Rizo
# 4. Po - antena: Círculo
#
# === Jugamos un poco ===
# Tinky Winky está jugando con su Bolso.
# Tinky Winky está jugando con su Bolso.
# Dipsy está jugando con su Sombrero.
# Po se está comiendo su Tubby Papilla. ¡Ñam, ñam!
# Estado de Tinky Winky -> Felicidad: 120 | Hambre: 90
# Estado de Dipsy -> Felicidad: 110 | Hambre: 70
# Estado de Laa-Laa -> Felicidad: 100 | Hambre: 50
# Estado de Po -> Felicidad: 120 | Hambre: 0
#
# === Getters y setter ===
# Hambre de Laa-Laa (getter): 50
# Tras set_nivel_hambre(60): 60
# Valor no válido para el hambre de Laa-Laa: 150 (debe ser un entero de 0 a 100).
# Valor no válido para el hambre de Laa-Laa: 'mucha' (debe ser un entero de 0 a 100).
# Sigue en: 60
#
# === Buscar por nombre ===
# Encontrado: Teletubby Dipsy (Verde) - Feliz: 110
# Noo-Noo no está en la lista
#
# === Filtrar: hambre > 50 ===
# [PersonajeTeletubby('Tinky Winky', 'Morado', 'Triángulo', 'Bolso'), PersonajeTeletubby('Dipsy', 'Verde', 'Palo', 'Sombrero'), PersonajeTeletubby('Laa-Laa', 'Amarillo', 'Rizo', 'Pelota')]
# ['Tinky Winky', 'Dipsy', 'Laa-Laa']
#
# === Ordenar ===
# Por hambre (menor a mayor): ['Po', 'Laa-Laa', 'Dipsy', 'Tinky Winky']
# Por hambre (mayor a menor): ['Tinky Winky', 'Dipsy', 'Laa-Laa', 'Po']
# Por nombre: ['Dipsy', 'Laa-Laa', 'Po', 'Tinky Winky']
# Más hambriento: Tinky Winky
# Más feliz: Tinky Winky
#
# === Diccionario nombre -> objeto ===
# Teletubby Po (Rojo) - Feliz: 120
# No existe
# Tinky Winky: 90 de hambre
# Dipsy: 70 de hambre
# Laa-Laa: 60 de hambre
# Po: 0 de hambre
#
# === Comprensión de diccionario ===
# {'Tinky Winky': 'Morado', 'Dipsy': 'Verde', 'Laa-Laa': 'Amarillo', 'Po': 'Rojo'}
# {'Tinky Winky': 90, 'Dipsy': 70, 'Laa-Laa': 60}
#
# === Contar y sumar ===
# Hambre total: 220
# Media de hambre: 55.0
# Cuántos tienen hambre > 50: 3
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Filtrar u ordenar con t.__nivel_hambre desde fuera -> AttributeError.
#   Usa el getter: t.get_nivel_hambre()  (¡con paréntesis!).
# - key=lambda t: t.get_nivel_hambre   (sin paréntesis) compara MÉTODOS, no
#   números -> TypeError. Lleva ().
# - sorted() devuelve una lista nueva; lista.sort() ordena la misma lista y
#   devuelve None (no hagas lista = lista.sort()).
# - Empate en max(): devuelve el PRIMERO que encuentra con el valor máximo
#   (Tinky Winky y Po tienen felicidad 120 -> sale Tinky Winky).
# - Si dos objetos tienen el mismo nombre, en el diccionario nombre -> objeto
#   el segundo SOBRESCRIBE al primero (las claves no se repiten).
#
# ALTERNATIVA (funciona, pero NO es lo que pide el tema):
# - Filtrar con filter(lambda t: t.get_nivel_hambre() > 50, teletubbies)
#   -> hay que envolverlo en list(...). Para filtrar el profesor pide
#   comprensión de listas.
# - Buscar con next((t for t in teletubbies if t.nombre == "Po"), None):
#   correcto pero menos legible que el for con return.
# ---------------------------------------------------------------
