"""
TEMA 6 - Teoría-práctica 3: Clases básicas
==========================================
ENUNCIADO: Archivo de consulta (no es un ejercicio del profesor). Muestra con
un ejemplo sencillo (CuentaBancaria y el Dog de los apuntes) todo lo básico:
clase, constructor, self, atributos de clase y de instancia, métodos,
__str__ y __repr__.

FORMA QUE EXIGE EL PROFESOR:
    - Clases en PascalCase (CuentaBancaria), métodos y atributos en snake_case.
    - Docstring con triple comilla en la clase y en cada método.
    - Pruebas dentro de if __name__ == "__main__":

CONCEPTOS QUE PRACTICA:
    - class, __init__, self, instanciar objetos.
    - Atributo de clase (compartido) vs atributo de instancia (de cada objeto).
    - Métodos de instancia que modifican el objeto o devuelven datos.
    - __str__ (usuario, print) vs __repr__ (programador, listas, repr()).

CÓMO EJECUTARLO:  python 03_clases_basico.py   (en Linux/Docker: python3 03_clases_basico.py)
"""


# ---------------------------------------------------------------
# PASO 1: LA CLASE MÍNIMA
# ---------------------------------------------------------------
# class Nombre:  -> define un tipo nuevo. Dentro van atributos y métodos.
class CuentaBancaria:
    """Cuenta bancaria sencilla con titular y saldo."""

    # ATRIBUTO DE CLASE: uno solo para todas las cuentas.
    # Útil para constantes o contadores comunes.
    banco = "Banco Python"
    total_cuentas = 0           # contador de cuentas creadas

    # CONSTRUCTOR: se ejecuta al hacer CuentaBancaria("Ana", 100).
    # saldo=0 es un parámetro con valor por defecto (opcional al crear).
    def __init__(self, titular, saldo=0):
        """Crea la cuenta con su titular y su saldo inicial."""
        self.titular = titular  # ATRIBUTO DE INSTANCIA: cada cuenta el suyo
        self.saldo = saldo
        # Para cambiar un atributo de CLASE se usa el nombre de la clase.
        # Si hicieras self.total_cuentas += 1 crearías uno de instancia.
        CuentaBancaria.total_cuentas += 1

    # MÉTODO que MODIFICA el objeto.
    def ingresar(self, cantidad):
        """Suma la cantidad al saldo si es positiva."""
        if cantidad > 0:
            self.saldo += cantidad
        else:
            print("La cantidad debe ser positiva.")

    # MÉTODO que DEVUELVE un dato (return), útil para usarlo fuera.
    def retirar(self, cantidad):
        """Resta la cantidad si hay saldo suficiente. Devuelve True/False."""
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        return False

    # __str__: lo llama print(objeto) y str(objeto). Para el USUARIO.
    def __str__(self):
        """Texto legible para el usuario."""
        return f"Cuenta de {self.titular}: {self.saldo} €"

    # __repr__: lo llama repr(objeto) y print(lista_de_objetos). Para el
    # PROGRAMADOR: idealmente, el código para volver a crear el objeto.
    def __repr__(self):
        """Texto técnico que muestra cómo se creó el objeto."""
        return f"CuentaBancaria('{self.titular}', {self.saldo})"


# ---------------------------------------------------------------
# PASO 2: EJEMPLO DE LOS APUNTES (Dog) y el ERROR CLÁSICO
# ---------------------------------------------------------------
class Dog:
    """Perro de los apuntes: kind es de clase, name y tricks de instancia."""

    kind = "canine"             # de clase: todos los perros son 'canine'

    def __init__(self, name):
        """Crea el perro con su nombre y su lista de trucos vacía."""
        self.name = name        # de instancia: cada perro su nombre
        self.tricks = []        # de instancia: cada perro SU PROPIA lista

    def add_trick(self, trick):
        """Añade un truco a la lista de este perro."""
        self.tricks.append(trick)


class DogMal:
    """ERROR CLÁSICO: lista mutable como atributo de CLASE (la comparten todos)."""

    tricks = []                 # MAL: una sola lista para TODOS los perros

    def __init__(self, name):
        """Crea el perro (pero tricks no es suyo, es de la clase)."""
        self.name = name

    def add_trick(self, trick):
        """Añade el truco... a la lista compartida."""
        self.tricks.append(trick)


# ---------------------------------------------------------------
# PASO 3: PRUEBAS
# ---------------------------------------------------------------
if __name__ == "__main__":

    print("=== Crear objetos (instanciar) ===")
    # No se escribe "new" como en Java: se llama a la clase como a una función.
    cuenta_ana = CuentaBancaria("Ana", 100)
    cuenta_luis = CuentaBancaria("Luis")       # saldo por defecto: 0
    print(cuenta_ana)                          # __str__
    print(cuenta_luis)
    print(repr(cuenta_ana))                    # __repr__
    print([cuenta_ana, cuenta_luis])           # lista -> __repr__ de cada uno

    print("\n=== Usar métodos ===")
    cuenta_ana.ingresar(50)
    cuenta_luis.ingresar(-10)                  # mensaje de error
    if cuenta_ana.retirar(500):                # usamos lo que devuelve
        print("Retirada hecha")
    else:
        print("Saldo insuficiente")
    print(cuenta_ana)

    print("\n=== Atributos de instancia: cada objeto el suyo ===")
    cuenta_luis.saldo = 20                     # público: se puede cambiar
    print(cuenta_ana.saldo, cuenta_luis.saldo)

    print("\n=== Atributos de clase: compartidos ===")
    print(CuentaBancaria.banco)                # desde la clase
    print(cuenta_ana.banco, cuenta_luis.banco) # desde los objetos (mismo valor)
    print("Cuentas creadas:", CuentaBancaria.total_cuentas)
    CuentaBancaria.banco = "Nuevo Banco"       # cambia para TODOS
    print(cuenta_ana.banco, "|", cuenta_luis.banco)
    # Si se asigna desde un objeto, se crea uno de INSTANCIA que tapa al de clase:
    cuenta_ana.banco = "Banco de Ana"
    print(cuenta_ana.banco, "|", cuenta_luis.banco, "|", CuentaBancaria.banco)

    print("\n=== vars(): atributos de instancia de un objeto ===")
    print(vars(cuenta_luis))

    print("\n=== Dog (bien) vs DogMal (lista de clase) ===")
    d = Dog("Fido")
    e = Dog("Buddy")
    d.add_trick("rodar")
    e.add_trick("hacerse el muerto")
    print(d.name, d.kind, d.tricks)
    print(e.name, e.kind, e.tricks)
    m1 = DogMal("Rex")
    m2 = DogMal("Toby")
    m1.add_trick("rodar")
    m2.add_trick("sentarse")
    print(m1.name, m1.tricks)                  # ¡tiene también el truco de Toby!
    print(m2.name, m2.tricks)


# ---------------------------------------------------------------
# SALIDA ESPERADA:
# === Crear objetos (instanciar) ===
# Cuenta de Ana: 100 €
# Cuenta de Luis: 0 €
# CuentaBancaria('Ana', 100)
# [CuentaBancaria('Ana', 100), CuentaBancaria('Luis', 0)]
#
# === Usar métodos ===
# La cantidad debe ser positiva.
# Saldo insuficiente
# Cuenta de Ana: 150 €
#
# === Atributos de instancia: cada objeto el suyo ===
# 150 20
#
# === Atributos de clase: compartidos ===
# Banco Python
# Banco Python Banco Python
# Cuentas creadas: 2
# Nuevo Banco | Nuevo Banco
# Banco de Ana | Nuevo Banco | Nuevo Banco
#
# === vars(): atributos de instancia de un objeto ===
# {'titular': 'Luis', 'saldo': 20}
#
# === Dog (bien) vs DogMal (lista de clase) ===
# Fido canine ['rodar']
# Buddy canine ['hacerse el muerto']
# Rex ['rodar', 'sentarse']
# Toby ['rodar', 'sentarse']
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Olvidar self como primer parámetro -> TypeError al llamar al método.
# - Olvidar self. delante del atributo -> se crea una variable local y el
#   objeto no guarda nada.
# - __init__ con UN guion bajo a cada lado (_init_) -> no es el constructor;
#   al crear el objeto con argumentos da TypeError.
# - Listas/diccionarios como atributo de CLASE -> los comparten todos (DogMal).
#   Créalos en __init__ con self.lista = [].
# - __str__ / __repr__ deben DEVOLVER un str (return), no imprimir.
# EN JAVA SERÍA: constructor = __init__, this = self, static = atributo de
# clase, toString() = __str__. No hay new ni tipos declarados.
# ---------------------------------------------------------------
