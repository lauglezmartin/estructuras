"""
TEMA 4 - Resumen: CHULETA DE BUCLES (ejecutable)
=================================================
Cada bloque es un ejemplo mínimo y comentado. Ejecuta el archivo y compara
lo que sale con lo que pone en el comentario "->".

CÓMO EJECUTARLO:  python 16_resumen_bucles.py   (en Linux/Docker: python3 16_resumen_bucles.py)

=====================================================================
TABLA "SI ME PIDEN X  ->  USO Y"
=====================================================================
 Si me piden...                                  -> Uso...
 ------------------------------------------------------------------
 Recorrer una lista / string elemento a elemento -> for x in lista:
 Repetir N veces / números de A a B              -> for i in range(A, B + 1):
 Contar hacia atrás o saltando (pares, de 5 en 5) -> range(inicio, fin, paso)  (paso negativo = atrás)
 Numerar elementos empezando en 1                -> for n, x in enumerate(lista, start=1):
 Recorrer dos listas a la vez (en paralelo)      -> for a, b in zip(lista1, lista2):
 Clave y valor de un diccionario                 -> for k, v in d.items():
 Solo claves / solo valores                      -> d.keys()  /  d.values()
 Todas las combinaciones de dos listas           -> for anidados (for dentro de for)
 Sumar sin sum()                                 -> acumulador: total = 0 ; total += x
 Contar cuántos cumplen algo                     -> contador: c = 0 ; c += 1
 Repetir sin saber cuántas veces (hasta que...)  -> while condicion:
 Repetir "para siempre" hasta que escriban algo  -> while True: ... if ...: break
 Salir del bucle antes de tiempo                 -> break
 Saltarse un elemento y seguir                   -> continue
 "Si no se encuentra..." al acabar de buscar     -> else del bucle (for/while ... else)
 Crear lista nueva en UNA línea                  -> [expr for x in lista]
 ... filtrando                                   -> [expr for x in lista if cond]        (if al FINAL)
 ... transformando según condición               -> [a if cond else b for x in lista]    (if-else DELANTE)
 Crear diccionario en UNA línea                  -> {clave: valor for x in lista}
=====================================================================
CONTADOR vs ACUMULADOR
 - Contador:   cuenta CUÁNTAS veces pasa algo -> suma siempre 1.
 - Acumulador: guarda la SUMA de valores      -> suma el valor.
 - Los dos se inicializan (normalmente a 0) ANTES del bucle.
EVITAR BUCLES INFINITOS EN WHILE
 - La variable de la condición tiene que CAMBIAR dentro del bucle.
 - En while True tiene que haber un break alcanzable.
 - Si se cuelga: Ctrl + C en la terminal.
=====================================================================
"""

# =====================================================================
# 1. FOR SOBRE UNA LISTA
# =====================================================================
frutas = ["manzana", "pera", "uva"]
for fruta in frutas:
    print(fruta)                      # -> manzana / pera / uva (una por línea)

# =====================================================================
# 2. FOR SOBRE UN STRING (letra a letra)
# =====================================================================
for letra in "hola":
    print(letra, end=" ")             # end=" " -> no salta de línea: h o l a
print()                               # salto de línea final

# =====================================================================
# 3. FOR CON RANGE
#    range(fin)             -> 0 .. fin-1
#    range(inicio, fin)     -> inicio .. fin-1   (el fin NUNCA se incluye)
#    range(inicio, fin, paso)
# =====================================================================
print(list(range(5)))                 # -> [0, 1, 2, 3, 4]
print(list(range(1, 6)))              # -> [1, 2, 3, 4, 5]
print(list(range(0, 11, 5)))          # -> [0, 5, 10]
print(list(range(10, 0, -3)))         # -> [10, 7, 4, 1]   (hacia atrás)

# =====================================================================
# 4. ENUMERATE (posición + elemento)
# =====================================================================
for numero, fruta in enumerate(frutas, start=1):
    print(f"{numero}. {fruta}")       # -> 1. manzana / 2. pera / 3. uva

# =====================================================================
# 5. ZIP (dos listas en paralelo; para en la más corta)
# =====================================================================
nombres = ["Ana", "Luis"]
notas = [8, 6]
for nombre, nota in zip(nombres, notas):
    print(f"{nombre}: {nota}")        # -> Ana: 8 / Luis: 6

# =====================================================================
# 6. DICCIONARIOS
# =====================================================================
stock = {"peras": 30, "uvas": 12}
for clave, valor in stock.items():    # clave y valor
    print(f"{clave} -> {valor}")      # -> peras -> 30 / uvas -> 12
for clave in stock.keys():            # solo claves (igual que: for clave in stock)
    print(clave)                      # -> peras / uvas
total_stock = 0
for valor in stock.values():          # solo valores
    total_stock += valor              # ACUMULADOR
print(total_stock)                    # -> 42

# =====================================================================
# 7. WHILE (se repite MIENTRAS la condición sea True)
# =====================================================================
contador = 3
while contador > 0:
    print(contador, end=" ")
    contador -= 1                     # ¡la condición cambia! si no, bucle infinito
print("¡Ya!")                         # -> 3 2 1 ¡Ya!

# =====================================================================
# 8. BREAK (salir del bucle) -- típico con while True
# =====================================================================
n = 0
while True:                           # infinito a propósito...
    n += 1
    if n == 4:
        break                         # ...la única salida es el break
print(f"Salí con n = {n}")            # -> Salí con n = 4

# =====================================================================
# 9. CONTINUE (saltar a la siguiente vuelta)
# =====================================================================
for i in range(1, 6):
    if i % 2 == 0:
        continue                      # los pares no se imprimen
    print(i, end=" ")                 # -> 1 3 5
print()

# =====================================================================
# 10. ELSE DEL BUCLE (solo se ejecuta si NO hubo break)
#     El else va a la altura del FOR, no del if.
# =====================================================================
for x in [1, 3, 5]:
    if x == 4:
        print("Encontrado")
        break
else:
    print("No encontrado")            # -> No encontrado (no hubo break)

# =====================================================================
# 11. BUCLES ANIDADOS (por cada vuelta de fuera, todas las de dentro)
# =====================================================================
for fila in range(1, 3):
    for col in ["A", "B"]:
        print(f"{fila}{col}", end=" ")  # -> 1A 1B 2A 2B
print()

# =====================================================================
# 12. COMPRENSIONES (bucle + lista nueva en UNA línea)
# =====================================================================
numeros = [1, 2, 3, 4, 5]
# a) Básica:  [expresion for x in iterable]
cuadrados = [x ** 2 for x in numeros]
print(cuadrados)                      # -> [1, 4, 9, 16, 25]
# b) Con if (FILTRO, va al FINAL):  [x for x in iterable if cond]
pares = [x for x in numeros if x % 2 == 0]
print(pares)                          # -> [2, 4]
# c) Con if-else (TRANSFORMA, va DELANTE del for):  [a if cond else b for x in iterable]
etiquetas = ["par" if x % 2 == 0 else "impar" for x in numeros]
print(etiquetas)                      # -> ['impar', 'par', 'impar', 'par', 'impar']
# d) De diccionario:  {clave: valor for x in iterable}
dobles = {x: x * 2 for x in numeros}
print(dobles)                         # -> {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}
#    ...o a partir de otro diccionario con .items():
stock_doble = {fruta: cant * 2 for fruta, cant in stock.items()}
print(stock_doble)                    # -> {'peras': 60, 'uvas': 24}

# =====================================================================
# 13. CONTADOR y ACUMULADOR juntos (sin sum() ni len())
# =====================================================================
precios = [10, 25, 5, 40]
total = 0          # acumulador
caros = 0          # contador
for p in precios:
    total += p                        # suma el VALOR
    if p > 20:
        caros += 1                    # suma 1
print(f"Total: {total}, caros: {caros}")  # -> Total: 80, caros: 2
