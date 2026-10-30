"""
TEMA 4 - Ejercicio 10: Contador y acumulador en while
======================================================
ENUNCIADO (literal del profesor):
    Escribe un programa que pida números al usuario sin parar y los vaya sumando.
    El bucle debe terminar cuando la suma total (acumulador) supere el valor de 50.
    Muestra cuántos números se ingresaron (contador).

FORMA QUE EXIGE EL PROFESOR:
    - Bucle while con una variable CONTADOR y otra ACUMULADOR.

CONCEPTOS QUE PRACTICA:
    - CONTADOR: cuenta CUÁNTAS veces pasa algo -> siempre suma 1   (contador += 1)
    - ACUMULADOR: guarda la SUMA de valores    -> suma el valor     (suma += numero)
    - Los dos se inicializan a 0 ANTES del bucle.
    - "supere 50" significa > 50, así que el bucle sigue MIENTRAS suma <= 50.

CÓMO EJECUTARLO:  python 10_contador_acumulador_while.py   (en Linux/Docker: python3 10_contador_acumulador_while.py)
"""

# ---------------------------------------------------------------
# PASO 1: inicializar contador y acumulador
# Van FUERA (antes) del bucle. Si estuvieran dentro, se pondrían a 0
# en cada vuelta y nunca llegaríamos a 50 -> bucle infinito.
# ---------------------------------------------------------------
LIMITE = 50
suma = 0       # ACUMULADOR: la suma de todos los números
contador = 0   # CONTADOR: cuántos números se han escrito

# ---------------------------------------------------------------
# PASO 2: el bucle
# Condición: seguir MIENTRAS la suma NO supere 50  ->  suma <= 50.
# (Pensar al revés es lo que más cuesta: el enunciado dice cuándo
#  PARAR -> suma > 50; el while necesita cuándo SEGUIR -> lo contrario.)
#
# ¿CÓMO EVITO EL BUCLE INFINITO? La variable de la condición (suma)
# cambia dentro del bucle en cada vuelta. Ojo: si el usuario solo
# mete ceros o negativos, la suma nunca supera 50 y el bucle sigue:
# es lo que pide el enunciado ("sin parar"), no es un fallo del código.
# ---------------------------------------------------------------
while suma <= LIMITE:
    # int() convierte el texto de input() en número entero.
    # Si quieres admitir decimales (2.5), usa float() en su lugar.
    numero = int(input("Introduce un número: "))
    suma += numero      # acumulador: suma el VALOR
    contador += 1       # contador: suma 1, da igual qué número fuera
    print(f"  Suma parcial: {suma}")

# ---------------------------------------------------------------
# PASO 3: resultados (fuera del bucle)
# ---------------------------------------------------------------
print(f"La suma ({suma}) ha superado {LIMITE}.")
print(f"Has introducido {contador} números.")

# ---------------------------------------------------------------
# SALIDA ESPERADA (escribiendo 20, 15, 10, 8):
# Introduce un número:   Suma parcial: 20
# Introduce un número:   Suma parcial: 35
# Introduce un número:   Suma parcial: 45
# Introduce un número:   Suma parcial: 53
# La suma (53) ha superado 50.
# Has introducido 4 números.
# Caso límite: si la suma llega EXACTAMENTE a 50, sigue pidiendo (50 no "supera" 50).
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Confundir contador y acumulador: contador += numero estaría MAL.
# - while suma < 50 pararía al llegar a 50 justo, y el enunciado dice "supere".
# - Si escriben letras, int() da ValueError (ver ejercicio 12 para controlarlo).
