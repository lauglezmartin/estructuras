"""
TEMA 6 - Teoría-práctica 7: Diccionarios
========================================
ENUNCIADO: Archivo de consulta. Todo lo que se hace con diccionarios en el
examen: crear, acceder ([] vs get), añadir, modificar, borrar (del / pop),
comprobar con in, recorrer (items / keys / values), diccionario de listas,
lista de diccionarios y contar apariciones.

FORMA QUE EXIGE EL PROFESOR:
    - Recorrer diccionarios con .items() (clave y valor) o .values().
    - Acceso seguro con .get(clave, valor_por_defecto) cuando la clave puede
      no existir (evita KeyError).

CONCEPTOS QUE PRACTICA:
    - Pares clave: valor; las claves no se repiten.
    - dic[clave] (lanza KeyError si no existe) vs dic.get(clave).
    - del, pop, in, len, items, keys, values.
    - Estructuras anidadas: dict de listas y lista de dicts.
    - Contar apariciones (con for + get y con dict).

CÓMO EJECUTARLO:  python 07_diccionarios.py   (en Linux/Docker: python3 07_diccionarios.py)
"""

# ---------------------------------------------------------------
# PASO 1: CREAR Y ACCEDER
# ---------------------------------------------------------------
# Un diccionario guarda pares clave: valor entre llaves.
# EN JAVA SERÍA: HashMap<String, Object>  (pero aquí mantiene el orden de inserción).
pelicula = {
    "titulo": "Inception",
    "year": 2010,
    "director": "Nolan",
    "rating": 8.8,
}
vacio = {}                                  # diccionario vacío (dict() también vale)

print("=== Crear y acceder ===")
print(pelicula)
print(pelicula["titulo"])                   # [] -> si la clave no existe: KeyError
print(pelicula.get("genero"))               # get -> si no existe: None
print(pelicula.get("genero", "n/a"))        # get con valor por defecto
try:
    print(pelicula["genero"])
except KeyError as error:
    print("KeyError con []:", error)
print("Número de claves:", len(pelicula), "| vacío:", len(vacio))

# ---------------------------------------------------------------
# PASO 2: AÑADIR, MODIFICAR, BORRAR
# ---------------------------------------------------------------
print("\n=== Añadir y modificar (misma sintaxis) ===")
pelicula["genero"] = "Ciencia ficción"      # la clave NO existía -> se AÑADE
pelicula["rating"] = 9.0                    # la clave SÍ existía -> se MODIFICA
print(pelicula)

print("\n=== Borrar ===")
del pelicula["year"]                        # borra la clave (KeyError si no existe)
director = pelicula.pop("director")         # borra y DEVUELVE el valor
print("Valor quitado con pop:", director)
print(pelicula.pop("oscar", "no tenía"))    # pop con defecto: no da error
print(pelicula)

# ---------------------------------------------------------------
# PASO 3: COMPROBAR CON in (mira las CLAVES, no los valores)
# ---------------------------------------------------------------
print("\n=== in ===")
print("titulo" in pelicula)                 # True
print("Inception" in pelicula)              # False: es un valor, no una clave
print("Inception" in pelicula.values())     # True: buscando en los valores
if "year" not in pelicula:
    print("Ya no tiene 'year'")

# ---------------------------------------------------------------
# PASO 4: RECORRER
# ---------------------------------------------------------------
precios = {"portátil": 800, "móvil": 500, "tableta": 300}

print("\n=== Recorrer ===")
for producto in precios:                    # por defecto recorre las CLAVES
    print("Clave:", producto)
for producto in precios.keys():             # igual que lo anterior, más explícito
    print("keys():", producto)
total = 0
for precio in precios.values():             # solo los VALORES
    total += precio
print("Total con values():", total)
for producto, precio in precios.items():    # CLAVE y VALOR a la vez (forma pedida)
    print(f"{producto}: {precio} €")

# Modificar todos los valores recorriendo:
for producto in precios:
    precios[producto] = precios[producto] * 0.9     # 10 % de descuento
print("Con descuento:", precios)

# ---------------------------------------------------------------
# PASO 5: DICCIONARIO DE LISTAS (valor = lista)
# ---------------------------------------------------------------
print("\n=== Diccionario de listas ===")
notas = {
    "Ana": [7, 8, 9],
    "Luis": [5, 4, 6],
}
notas["Eva"] = []                           # nuevo alumno sin notas
notas["Eva"].append(10)                     # añadir a la LISTA de Eva
notas["Ana"].append(10)
for alumno, lista_notas in notas.items():
    media = sum(lista_notas) / len(lista_notas)
    print(f"{alumno}: {lista_notas} -> media {media:.2f}")

# ---------------------------------------------------------------
# PASO 6: LISTA DE DICCIONARIOS (cada elemento = un "registro")
# ---------------------------------------------------------------
print("\n=== Lista de diccionarios ===")
productos = [
    {"name": "Laptop", "price": 800, "category": "electronics", "stock": 5},
    {"name": "Mouse", "price": 25, "category": "electronics", "stock": 50},
    {"name": "Desk", "price": 200, "category": "furniture", "stock": 10},
]
# Filtrar con for (ejemplo de los apuntes):
search_category = "electronics"
available_products = []
for product in productos:
    if product["category"] == search_category and product["stock"] > 0:
        available_products.append(product)
print("Disponibles:", [p["name"] for p in available_products])
# Ordenar por una clave con lambda (como en los apuntes con peliculas.sort):
productos.sort(key=lambda p: p["price"], reverse=True)
print("Por precio desc:", [p["name"] for p in productos])
# El más barato:
barato = min(productos, key=lambda p: p["price"])
print("Más barato:", barato["name"], barato["price"])

# ---------------------------------------------------------------
# PASO 7: CONTAR APARICIONES
# ---------------------------------------------------------------
print("\n=== Contar apariciones ===")
frutas = ["manzana", "pera", "manzana", "uva", "pera", "manzana"]
# Forma 1: if/else
conteo = {}
for fruta in frutas:
    if fruta in conteo:
        conteo[fruta] += 1                  # ya estaba: sumamos 1
    else:
        conteo[fruta] = 1                   # primera vez: empieza en 1
print(conteo)
# Forma 2: get con 0 por defecto (más corta)
conteo2 = {}
for fruta in frutas:
    conteo2[fruta] = conteo2.get(fruta, 0) + 1
print(conteo2)
# Contar letras de una palabra:
letras = {}
for letra in "banana":
    letras[letra] = letras.get(letra, 0) + 1
print(letras)
# La más repetida: max sobre las claves usando el valor como criterio.
print("Fruta más repetida:", max(conteo, key=lambda f: conteo[f]))


# ---------------------------------------------------------------
# SALIDA ESPERADA:
# === Crear y acceder ===
# {'titulo': 'Inception', 'year': 2010, 'director': 'Nolan', 'rating': 8.8}
# Inception
# None
# n/a
# KeyError con []: 'genero'
# Número de claves: 4 | vacío: 0
#
# === Añadir y modificar (misma sintaxis) ===
# {'titulo': 'Inception', 'year': 2010, 'director': 'Nolan', 'rating': 9.0, 'genero': 'Ciencia ficción'}
#
# === Borrar ===
# Valor quitado con pop: Nolan
# no tenía
# {'titulo': 'Inception', 'rating': 9.0, 'genero': 'Ciencia ficción'}
#
# === in ===
# True
# False
# True
# Ya no tiene 'year'
#
# === Recorrer ===
# Clave: portátil
# Clave: móvil
# Clave: tableta
# keys(): portátil
# keys(): móvil
# keys(): tableta
# Total con values(): 1600
# portátil: 800 €
# móvil: 500 €
# tableta: 300 €
# Con descuento: {'portátil': 720.0, 'móvil': 450.0, 'tableta': 270.0}
#
# === Diccionario de listas ===
# Ana: [7, 8, 9, 10] -> media 8.50
# Luis: [5, 4, 6] -> media 5.00
# Eva: [10] -> media 10.00
#
# === Lista de diccionarios ===
# Disponibles: ['Laptop', 'Mouse']
# Por precio desc: ['Laptop', 'Desk', 'Mouse']
# Más barato: Mouse 25
#
# === Contar apariciones ===
# {'manzana': 3, 'pera': 2, 'uva': 1}
# {'manzana': 3, 'pera': 2, 'uva': 1}
# {'b': 1, 'a': 3, 'n': 2}
# Fruta más repetida: manzana
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - dic["clave"] con una clave que no existe -> KeyError. Usa get() o "in".
# - "valor" in dic busca en las CLAVES; para valores: in dic.values().
# - for k, v in dic:  (sin .items()) recorre solo las CLAVES e intenta
#   partir cada una en dos -> normalmente ValueError. Lleva .items().
# - No añadas ni borres claves MIENTRAS recorres el mismo diccionario
#   (RuntimeError). Cambiar el VALOR de claves existentes sí se puede.
# - Las claves deben ser inmutables (str, int, tupla); una lista no vale.
# - Asignar a una clave que ya existe la SOBRESCRIBE (no hay duplicados).
# ---------------------------------------------------------------
