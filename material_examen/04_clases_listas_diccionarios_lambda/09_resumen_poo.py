"""
TEMA 6 - 9: CHULETA EJECUTABLE (clases, listas de objetos, dicts, comprensiones, lambda)
=======================================================================================
Lo mínimo de cada cosa, para copiar y adaptar en el examen.
Detalle y explicaciones: archivos 01 a 08 de esta carpeta.

CÓMO EJECUTARLO:  python 09_resumen_poo.py   (en Linux/Docker: python3 09_resumen_poo.py)
"""


# ===================== CLASE COMPLETA =====================
class Personaje:
    """Plantilla mínima: clase, instancia, privado, getter, setter, dunder."""

    especie = "Teletubby"                       # atributo de CLASE (compartido)

    def __init__(self, nombre, energia=50):     # constructor; self = el objeto
        """Crea el personaje."""
        self.nombre = nombre                    # público (de instancia)
        self.__energia = energia                # privado -> _Personaje__energia

    def get_energia(self):                      # GETTER: return, no print
        """Devuelve la energía."""
        return self.__energia

    def set_energia(self, valor):               # SETTER con validación
        """Cambia la energía si está entre 0 y 100."""
        if 0 <= valor <= 100:
            self.__energia = valor
        else:
            print("Valor no válido")

    def jugar(self):                            # método que modifica el estado
        """Gasta 10 de energía."""
        self.__energia -= 10

    def __str__(self):                          # print(obj) -> usuario
        """Texto para el usuario."""
        return f"{self.nombre} ({self.__energia})"

    def __repr__(self):                         # repr(obj) / print(lista) -> técnico
        """Texto técnico."""
        return f"Personaje('{self.nombre}', {self.__energia})"


# ===================== HERENCIA =====================
class Heroe(Personaje):                         # Heroe hereda de Personaje
    """Personaje con poder."""

    def __init__(self, nombre, poder, energia=50):
        """Reutiliza el constructor del padre."""
        super().__init__(nombre, energia)       # SIN self
        self.poder = poder

    def jugar(self):                            # sobrescribe y amplía
        """Juega como el padre y además usa su poder."""
        super().jugar()
        print(f"{self.nombre} usa {self.poder}")


if __name__ == "__main__":
    # ---- Objetos ----
    a = Personaje("Po", 80)
    b = Heroe("Dipsy", "rayo")
    print(a, "|", repr(a), "|", Personaje.especie)
    a.jugar()
    b.jugar()
    a.set_energia(500)                          # rechazado
    print(a.get_energia(), b.get_energia())
    try:
        a.__energia                             # privado desde fuera
    except AttributeError:
        print("AttributeError: el privado no se ve desde fuera")

    # ---- Lista de objetos ----
    grupo = [a, b, Personaje("Laa-Laa", 90)]
    grupo.append(Personaje("Tinky", 30))
    print(grupo)                                # usa __repr__
    for p in grupo:
        print(p.nombre, p.get_energia())
    encontrado = None
    for p in grupo:                             # buscar
        if p.nombre == "Laa-Laa":
            encontrado = p
            break
    print("Buscado:", encontrado)
    grupo.remove(encontrado)                    # eliminar
    print("Quedan:", len(grupo))
    print("Suma energía:", sum(p.get_energia() for p in grupo))
    print("Más energía:", max(grupo, key=lambda p: p.get_energia()))
    print("Ordenados:", sorted(grupo, key=lambda p: p.get_energia()))

    # ---- Diccionarios ----
    d = {"Po": "Rojo", "Dipsy": "Verde"}
    d["Tinky"] = "Morado"                       # añadir / modificar
    print(d["Po"], d.get("Noo", "no está"), "Po" in d)
    del d["Dipsy"]                              # borrar (o d.pop("Dipsy"))
    for clave, valor in d.items():
        print(clave, "->", valor)
    conteo = {}
    for letra in "papa":                        # contar apariciones
        conteo[letra] = conteo.get(letra, 0) + 1
    print(conteo)

    # ---- Comprensiones ----
    nums = [1, 2, 3, 4, 5]
    print([n * 2 for n in nums])                            # transformar
    print([n for n in nums if n % 2 == 0])                  # filtrar (if al final)
    print(["par" if n % 2 == 0 else "impar" for n in nums]) # if-else delante
    print({p.nombre: p.get_energia() for p in grupo})       # de diccionario

    # ---- lambda ----
    print(list(map(lambda x: x ** 2, nums)))                # aplicar a todos
    print(list(filter(lambda x: x > 2, nums)))              # filtrar
    print(sorted(["sol", "mar", "elefante"], key=lambda s: len(s), reverse=True))


# ---------------------------------------------------------------
# SALIDA ESPERADA:
# Po (80) | Personaje('Po', 80) | Teletubby
# Dipsy usa rayo
# Valor no válido
# 70 40
# AttributeError: el privado no se ve desde fuera
# [Personaje('Po', 70), Personaje('Dipsy', 40), Personaje('Laa-Laa', 90), Personaje('Tinky', 30)]
# Po 70
# Dipsy 40
# Laa-Laa 90
# Tinky 30
# Buscado: Laa-Laa (90)
# Quedan: 3
# Suma energía: 140
# Más energía: Po (70)
# Ordenados: [Personaje('Tinky', 30), Personaje('Dipsy', 40), Personaje('Po', 70)]
# Rojo no está True
# Po -> Rojo
# Tinky -> Morado
# {'p': 2, 'a': 2}
# [2, 4, 6, 8, 10]
# [2, 4]
# ['impar', 'par', 'impar', 'par', 'impar']
# {'Po': 70, 'Dipsy': 40, 'Tinky': 30}
# [1, 4, 9, 16, 25]
# [3, 4, 5]
# ['elefante', 'sol', 'mar']
# ---------------------------------------------------------------
# RECORDATORIOS RÁPIDOS:
# - self primero en cada método; self.atributo para guardar en el objeto.
# - Atributo de clase: fuera de __init__; se cambia con Clase.atributo.
# - __privado: AttributeError al leer desde fuera; asignar crea otro atributo.
# - Getter = return. print(obj.ver_estado()).
# - __str__ -> print(obj); __repr__ -> repr(obj) y print(lista).
# - super().__init__(...) sin self.
# - dic[k] da KeyError si no existe; dic.get(k, defecto) no.
# - for k, v in dic.items():
# - max/min/sorted con key=lambda x: x.atributo  (devuelven el objeto).
# - map/filter -> list(...).  lista.sort() devuelve None.
# ---------------------------------------------------------------
