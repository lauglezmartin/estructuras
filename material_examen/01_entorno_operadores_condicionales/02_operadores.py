"""
TEMA 2 - Operadores y expresiones lógicas (3 ejercicios + demo)
===============================================================
ENUNCIADO EJERCICIO 1 (literal): Verificación de mayoría de edad (Entrada-Proceso-Salida)
    "Entrada: El usuario ingresa su edad en años. Proceso: El programa compara
    la edad con el número 18. Salida: Se muestra el mensaje 'Sos mayor de edad'
    o 'Sos menor de edad'."

ENUNCIADO EJERCICIO 2 (literal): Comprobación de paridad y acceso (verificar_acceso)
    "Evaluación de mayoría de edad (Plan A vs Plan B): si la edad es mayor o
    igual a 18, imprimir 'Acceso concedido: Eres mayor de edad.', de lo
    contrario 'Acceso denegado: Eres menor de edad.'. Evaluación de paridad
    utilizando el operador módulo: si numero_verificacion % 2 == 0, imprimir
    'El código {numero_verificacion} es PAR.', si no, 'El código
    {numero_verificacion} es IMPAR.'"

ENUNCIADO EJERCICIO 3 (literal): Valor vs. identidad en memoria
    lista1 = [1, 15, 16]
    lista2 = [1, 15, 16]
    lista3 = lista1
    print(lista1 == lista2)  # True (Tienen el mismo valor)
    print(lista1 is lista2)  # False (Son objetos distintos en memoria)
    print(lista1 is lista3)  # True (Ambas variables apuntan al mismo objeto)

FORMA QUE EXIGE EL PROFESOR:
    - Ej. 1: modelo Entrada (input + int) -> Proceso (comparar con 18) -> Salida (print).
    - Ej. 2: la paridad se comprueba con el operador MÓDULO: numero % 2 == 0.
    - Ej. 3: == compara CONTENIDO; is / is not comparan IDENTIDAD (mismo objeto).
      En Python NO existe === (eso es de JavaScript/PHP).

CONCEPTOS QUE PRACTICA:
    - input(), int(), if/else, %, ==, is, f-strings.
    - Demo final: aritméticos, relacionales, lógicos, truthy/falsy, in/not in,
      ternario, conversión de tipos y round().

CÓMO EJECUTARLO:  python 02_operadores.py   (en Linux/Docker: python3 02_operadores.py)
    Pide una edad por teclado (ejercicio 1).
"""


# ===============================================================
# EJERCICIO 1: mayoría de edad con modelo Entrada-Proceso-Salida
# ===============================================================
def ejercicio_1():
    """Pide la edad y dice si es mayor o menor de edad (EPS)."""
    # ENTRADA: input() devuelve SIEMPRE un str ("17"), aunque escribas números.
    # Por eso lo convertimos con int(); si no, "17" >= 18 da TypeError.
    edad = int(input("Introduce tu edad en años: "))

    # PROCESO: comparamos con 18 usando el operador relacional >=.
    # SALIDA: un print según el resultado (textos literales del enunciado).
    if edad >= 18:
        print("Sos mayor de edad")
    else:
        print("Sos menor de edad")


# ===============================================================
# EJERCICIO 2: verificar_acceso (edad + paridad con %)
# ===============================================================
def verificar_acceso(edad, numero_verificacion):
    """Comprueba la mayoría de edad y si el código de verificación es par."""
    # Plan A (if) vs Plan B (else): solo se ejecuta una de las dos ramas.
    if edad >= 18:
        print("Acceso concedido: Eres mayor de edad.")
    else:
        print("Acceso denegado: Eres menor de edad.")

    # % es el operador MÓDULO: devuelve el RESTO de la división entera.
    # Un número es par si al dividirlo entre 2 el resto es 0.
    #   8 % 2 -> 0 (par)      7 % 2 -> 1 (impar)
    if numero_verificacion % 2 == 0:
        print(f"El código {numero_verificacion} es PAR.")
    else:
        print(f"El código {numero_verificacion} es IMPAR.")


# ===============================================================
# EJERCICIO 3: == (valor) frente a is (identidad)
# ===============================================================
def ejercicio_3():
    """Muestra la diferencia entre == e is con listas."""
    lista1 = [1, 15, 16]
    lista2 = [1, 15, 16]   # otra lista NUEVA con el mismo contenido
    lista3 = lista1        # NO copia: lista3 es otro nombre para el MISMO objeto

    print(lista1 == lista2)  # True  -> mismo contenido
    print(lista1 is lista2)  # False -> son dos objetos distintos en memoria
    print(lista1 is lista3)  # True  -> apuntan al mismo objeto

    # id() devuelve la "dirección" del objeto: is equivale a id(a) == id(b).
    print(id(lista1) == id(lista3))  # True

    # Consecuencia práctica: si modificas lista3, también cambia lista1.
    lista3.append(99)
    print(lista1)  # [1, 15, 16, 99]

    # El uso correcto de is: comparar con None (es un objeto único).
    valor = None
    print(valor is None)       # True  (forma recomendada, NO "valor == None")
    print(valor is not None)   # False


# ===============================================================
# DEMO COMENTADA DE OPERADORES (para consultar)
# ===============================================================
def demo_operadores():
    """Ejemplos de todos los operadores del tema 2."""
    print("\n--- Aritméticos ---")
    print(7 / 2)    # 3.5  -> / SIEMPRE da float (en Java 7/2 da 3; aquí NO)
    print(7 // 2)   # 3    -> // división entera (redondea hacia abajo)
    print(-7 // 2)  # -4   -> ¡hacia abajo (suelo), no hacia el cero como Java!
    print(7 % 2)    # 1    -> % resto (módulo)
    print(2 ** 3)   # 8    -> ** potencia (en Java: Math.pow(2, 3))
    print(9 ** 0.5)  # 3.0 -> raíz cuadrada con ** 0.5

    print("\n--- Relacionales (devuelven True/False) ---")
    a, b = 5, 10
    print(a == b, a != b, a < b, a <= b, a > b, a >= b)  # False True True True False False
    print(1 < a < 10)  # True -> comparación ENCADENADA (equivale a 1 < a and a < 10)
    print("Ana" < "ana")  # True -> los str se comparan por código Unicode: 'A'(65) < 'a'(97)

    print("\n--- Lógicos: and, or, not (en Java: &&, ||, !) ---")
    print(True and False)  # False -> and: True solo si AMBOS son True
    print(True or False)   # True  -> or: True si ALGUNO es True
    print(not True)        # False -> not: invierte
    # Cortocircuito: si el primer operando ya decide, el segundo no se evalúa.
    x = 0
    print(x != 0 and 10 / x > 1)  # False, y NO da ZeroDivisionError

    print("\n--- Truthy / Falsy ---")
    # Son FALSY (cuentan como False en un if): 0, 0.0, "", [], {}, (), set(), None, False
    # TODO lo demás es TRUTHY (" " con un espacio, [0], "0", -1...)
    for valor in [0, 0.0, "", [], {}, None, "0", " ", [0], -1]:
        print(repr(valor), "->", bool(valor))
    nombre = ""
    if not nombre:  # forma pythónica de comprobar "está vacío"
        print("El nombre está vacío")

    print("\n--- Pertenencia: in / not in ---")
    print(3 in [1, 2, 3])          # True
    print("py" in "python")        # True  -> busca subcadenas
    print("x" not in "python")     # True
    print("edad" in {"edad": 20})  # True  -> en diccionarios busca en las CLAVES

    print("\n--- Operador ternario (expresión condicional) ---")
    # valor_si_true if condición else valor_si_false   (en Java: cond ? a : b)
    edad = 20
    mensaje = "mayor" if edad >= 18 else "menor"
    print(mensaje)  # mayor

    print("\n--- Conversión de tipos ---")
    print(int("42") + 1)     # 43    -> str a int
    print(float("3.5") * 2)  # 7.0   -> str a float
    print(int(3.99))         # 3     -> int() TRUNCA (corta decimales), no redondea
    print(str(10) + " años")  # "10 años" -> int a str para concatenar con +
    print(type(3.0))         # <class 'float'>
    # int("3.5") -> ValueError: primero float() y luego int(): int(float("3.5")) = 3

    print("\n--- round() ---")
    print(round(3.14159, 2))  # 3.14 -> redondea a 2 decimales
    print(round(2.5))         # 2    -> ¡OJO! redondeo "del banquero": a par
    print(round(3.5))         # 4
    print(f"{3.14159:.2f}")   # 3.14 -> alternativa: formatear solo al mostrar


if __name__ == "__main__":
    print("=== Ejercicio 1 ===")
    ejercicio_1()

    print("\n=== Ejercicio 2 ===")
    verificar_acceso(20, 8)
    verificar_acceso(15, 7)

    print("\n=== Ejercicio 3 ===")
    ejercicio_3()

    demo_operadores()

# ---------------------------------------------------------------
# SALIDA ESPERADA (introduciendo 18):
# === Ejercicio 1 ===
# Introduce tu edad en años: Sos mayor de edad
#
# === Ejercicio 2 ===
# Acceso concedido: Eres mayor de edad.
# El código 8 es PAR.
# Acceso denegado: Eres menor de edad.
# El código 7 es IMPAR.
#
# === Ejercicio 3 ===
# True
# False
# True
# True
# [1, 15, 16, 99]
# True
# False
# ... (después, la demo de operadores con los valores comentados en cada línea)
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Olvidar int() en input(): comparar str con int da TypeError.
# - Usar = (asignación) en vez de == (comparación) dentro de un if: SyntaxError.
# - Usar is para comparar números o textos: usa ==. is solo para None/identidad.
# - 18 es MAYOR de edad: la condición es >= 18, no > 18.
# EN JAVA SERÍA: == en objetos compara referencias (como is); .equals() compara contenido (como ==).
# ALTERNATIVA (funciona, pero NO es lo que pide el ej. 2): comprobar par con
#   numero_verificacion / 2 == numero_verificacion // 2  -> el enunciado exige %.
