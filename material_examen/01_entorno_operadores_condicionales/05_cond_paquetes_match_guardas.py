"""
TEMA 3 - Ejercicio 3: Clasificación de paquetes con guardas condicionales
=========================================================================
ENUNCIADO (literal del profesor):
    "Dada la variable peso = 12.5, clasificar con match peso:
    case p if p <= 0: 'Peso no válido.', case p if p <= 5: 'Paquete pequeño.',
    case p if 5 < p <= 20: 'Paquete mediano.', case p if p > 20:
    'Paquete grande.', case _: 'Entrada no reconocida.'"

FORMA QUE EXIGE EL PROFESOR:
    - match-case con GUARDAS explícitas:  case p if condición:
    - case _ al final.
    - En el rango, comparación encadenada (5 < p <= 20), no "and".

CONCEPTOS QUE PRACTICA:
    - Patrón de captura (p) + guarda (if ...), comparación encadenada, comodín.

CÓMO EJECUTARLO:  python 05_cond_paquetes_match_guardas.py   (en Linux/Docker: python3 ...)
"""


def clasificar_paquete(peso):
    """Devuelve la categoría del paquete según su peso en kg."""
    # -----------------------------------------------------------
    # ¿Cómo funciona "case p if ...":?
    #   1) "p" es un PATRÓN DE CAPTURA: siempre coincide y guarda el valor
    #      de peso en la variable p.
    #   2) "if ..." es la GUARDA: el case solo se elige si además la
    #      condición es True. Si es False, se pasa al siguiente case.
    # Así match puede trabajar con RANGOS (un case 5: solo valdría para 5 exacto).
    # -----------------------------------------------------------
    match peso:
        case p if p <= 0:
            return "Peso no válido."
        case p if p <= 5:
            return "Paquete pequeño."
        case p if 5 < p <= 20:
            # Comparación encadenada: equivale a 5 < p and p <= 20.
            # (El "5 <" es redundante porque el case anterior ya filtró p <= 5,
            # pero el enunciado lo escribe así: déjalo igual.)
            return "Paquete mediano."
        case p if p > 20:
            return "Paquete grande."
        case _:
            # Con números nunca se llega aquí, pero el profesor exige el comodín.
            return "Entrada no reconocida."


if __name__ == "__main__":
    peso = 12.5
    print(clasificar_paquete(peso))

    # Pruebas de los límites de cada rango:
    for prueba in [-1, 0, 5, 5.1, 20, 20.5]:
        print(f"{prueba} kg -> {clasificar_paquete(prueba)}")

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# Paquete mediano.
# -1 kg -> Peso no válido.
# 0 kg -> Peso no válido.
# 5 kg -> Paquete pequeño.
# 5.1 kg -> Paquete mediano.
# 20 kg -> Paquete mediano.
# 20.5 kg -> Paquete grande.
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - "case p <= 5:" SIN el "p if" es SyntaxError: la condición va SIEMPRE tras "if".
# - El orden importa: el primer case cuya guarda sea True gana.
# - Se puede usar cualquier nombre (p, n, x); no reutilices el nombre de la
#   variable evaluada (case peso if ...) porque la sobrescribe y confunde.
# EN JAVA SERÍA: switch con "case Double p when p <= 0 ->" (Java 21) o if-else.
# ALTERNATIVA (funciona, pero NO es lo que pide el enunciado):
#   if peso <= 0: ... elif peso <= 5: ... -> el enunciado exige match con guardas.
