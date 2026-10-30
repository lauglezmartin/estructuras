"""
TEMA 5 - CHULETA EJECUTABLE DE FUNCIONES
========================================
Todo lo del tema en un solo archivo. Cada sección imprime un ejemplo.
Busca por número de sección (Ctrl+F "== 7" por ejemplo).

 1. def y llamada               10. Ámbito (local / global)
 2. Parámetros posicionales     11. Type hints
 3. Argumentos nombrados        12. Docstring
 4. Valores por defecto         13. lambda + map / filter / sorted(key=)
 5. return vs print (None)      14. Función como argumento
 6. Retorno múltiple            15. Decorador
 7. *args                       16. Recursividad
 8. **kwargs                    17. ERROR: parámetro mutable por defecto
 9. Orden correcto de parámetros

CÓMO EJECUTARLO:  python 16_resumen_funciones.py   (en Linux/Docker: python3 16_resumen_funciones.py)
"""

# =============================================================================
# 1. def Y LLAMADA
# =============================================================================
def saludar():
    """Definir NO ejecuta. Se ejecuta al llamarla con ()."""
    print("Hola")


# =============================================================================
# 2-4. POSICIONALES, NOMBRADOS Y POR DEFECTO
# =============================================================================
def presentar(nombre, edad, ciudad="Tenerife"):   # ciudad es opcional
    """Los parámetros con valor por defecto van SIEMPRE al final."""
    print(f"{nombre}, {edad} años, de {ciudad}")


# =============================================================================
# 5. return vs print
# =============================================================================
def doble_con_return(x):
    """Devuelve el doble de x."""
    return x * 2          # DEVUELVE: el valor se puede guardar y reutilizar


def doble_con_print(x):
    """Imprime el doble de x (no devuelve nada -> None)."""
    print(x * 2)          # Solo MUESTRA. Sin return la función devuelve None


# =============================================================================
# 6. RETORNO MÚLTIPLE (devuelve una tupla)
# =============================================================================
def min_max(lista):
    """Devuelve la tupla (mínimo, máximo) de la lista."""
    return min(lista), max(lista)     # equivale a return (min(...), max(...))


# =============================================================================
# 7. *args -> tupla con todos los posicionales sobrantes
# =============================================================================
def sumar_todo(*args):
    """Devuelve la suma de todos los números recibidos."""
    return sum(args)


# =============================================================================
# 8. **kwargs -> diccionario con todos los nombrados sobrantes
# =============================================================================
def mostrar_datos(**kwargs):
    """Imprime cada pareja clave: valor recibida."""
    for clave, valor in kwargs.items():
        print(f"  {clave}: {valor}")


# =============================================================================
# 9. ORDEN CORRECTO: normales, por defecto, *args, **kwargs
# =============================================================================
def orden_completo(a, b=2, *args, **kwargs):
    """Muestra qué valor llega a cada tipo de parámetro."""
    print(f"  a={a} b={b} args={args} kwargs={kwargs}")


# =============================================================================
# 10. ÁMBITO: local vs global
# =============================================================================
contador = 0              # Variable GLOBAL (fuera de cualquier función)


def incrementar():
    """Suma 1 a la variable global contador."""
    global contador       # Sin esto, "contador += 1" da UnboundLocalError
    contador += 1


def solo_local():
    """Crea una variable local con el mismo nombre que la global."""
    contador = 100        # Esto crea una variable LOCAL nueva; la global no cambia
    return contador


# =============================================================================
# 11-12. TYPE HINTS Y DOCSTRING
# =============================================================================
def area_rectangulo(ancho: float, alto: float) -> float:
    """
    Calcula el área de un rectángulo.

    Args:
        ancho (float): base del rectángulo.
        alto (float): altura del rectángulo.

    Returns:
        float: ancho * alto.
    """
    return ancho * alto   # Los hints son informativos: Python NO los comprueba


# =============================================================================
# 14. FUNCIÓN COMO ARGUMENTO (orden superior)
# =============================================================================
def aplicar(funcion, valor):
    """Llama a funcion(valor) y devuelve su resultado."""
    return funcion(valor)     # Se pasa la función SIN () y aquí se llama


# =============================================================================
# 15. DECORADOR
# =============================================================================
def con_marco(funcion):
    """Decorador: imprime un mensaje antes y otro después."""
    def envoltura(*args, **kwargs):
        print("  >>> antes")
        resultado = funcion(*args, **kwargs)
        print("  <<< después")
        return resultado
    return envoltura          # SIN paréntesis


@con_marco                     # = decorada = con_marco(decorada)
def decorada():
    """Función de ejemplo a la que se aplica el decorador."""
    print("  dentro de la función")


# =============================================================================
# 16. RECURSIVIDAD (caso base + llamada más pequeña)
# =============================================================================
def factorial(n):
    """Devuelve n! de forma recursiva."""
    if n <= 1:                # CASO BASE: para la recursión
        return 1
    return n * factorial(n - 1)


# =============================================================================
# 17. ERROR TÍPICO: lista (mutable) como valor por defecto
# =============================================================================
# MAL: la lista por defecto se crea UNA sola vez y se comparte entre llamadas.
def anadir_mal(elemento, lista=[]):
    """Ejemplo de lo que NO hay que hacer."""
    lista.append(elemento)
    return lista


# BIEN: usar None como valor por defecto y crear la lista dentro.
def anadir_bien(elemento, lista=None):
    """Añade elemento a lista (crea una lista nueva si no se pasa)."""
    if lista is None:
        lista = []
    lista.append(elemento)
    return lista


if __name__ == "__main__":
    print("== 1. def y llamada")
    saludar()

    print("== 2-4. Posicionales, nombrados, por defecto")
    presentar("Laura", 26)                         # posicionales (por orden)
    presentar(edad=30, nombre="Ana")               # nombrados (da igual el orden)
    presentar("Luis", 40, "Madrid")                # sustituye el valor por defecto

    print("== 5. return vs print")
    a = doble_con_return(5)
    print("  con return ->", a)                    # 10
    b = doble_con_print(5)                         # imprime 10...
    print("  con print  ->", b)                    # ...pero b vale None

    print("== 6. Retorno múltiple")
    minimo, maximo = min_max([3, 9, 1, 7])         # desempaquetado
    print(f"  min={minimo} max={maximo}")

    print("== 7. *args")
    print("  ", sumar_todo(1, 2, 3, 4))            # args = (1, 2, 3, 4)

    print("== 8. **kwargs")
    mostrar_datos(nombre="Laura", ciudad="Tenerife")

    print("== 9. Orden de parámetros")
    orden_completo(1)
    orden_completo(1, 5, 6, 7, x=8)

    print("== 10. Ámbito")
    incrementar()
    incrementar()
    print("  global contador =", contador)        # 2
    print("  local  contador =", solo_local())    # 100
    print("  global sigue    =", contador)        # 2

    print("== 11-12. Type hints y docstring")
    print("  área:", area_rectangulo(3, 4.5))
    print("  doc :", area_rectangulo.__doc__.strip().splitlines()[0])

    print("== 13. lambda con map / filter / sorted")
    nums = [5, 2, 8, 1]
    print("  map    :", list(map(lambda x: x * 10, nums)))        # transforma
    print("  filter :", list(filter(lambda x: x > 2, nums)))      # filtra
    palabras = ["kiwi", "uva", "manzana"]
    print("  sorted :", sorted(palabras, key=lambda p: len(p)))   # ordena por longitud
    alumnos = [("Ana", 7), ("Luis", 9), ("Eva", 5)]
    print("  sorted :", sorted(alumnos, key=lambda t: t[1], reverse=True))

    print("== 14. Función como argumento")
    print("  ", aplicar(abs, -7), aplicar(lambda x: x ** 2, 4))

    print("== 15. Decorador")
    decorada()

    print("== 16. Recursividad")
    print("  5! =", factorial(5))

    print("== 17. Parámetro mutable por defecto")
    print("  mal :", anadir_mal(1), anadir_mal(2))     # [1, 2] [1, 2] ¡se acumula!
    print("  bien:", anadir_bien(1), anadir_bien(2))   # [1] [2]

# -----------------------------------------------------------------------------
# SALIDA ESPERADA:
# == 1. def y llamada
# Hola
# == 2-4. Posicionales, nombrados, por defecto
# Laura, 26 años, de Tenerife
# Ana, 30 años, de Tenerife
# Luis, 40 años, de Madrid
# == 5. return vs print
#   con return -> 10
# 10
#   con print  -> None
# == 6. Retorno múltiple
#   min=1 max=9
# == 7. *args
#    10
# == 8. **kwargs
#   nombre: Laura
#   ciudad: Tenerife
# == 9. Orden de parámetros
#   a=1 b=2 args=() kwargs={}
#   a=1 b=5 args=(6, 7) kwargs={'x': 8}
# == 10. Ámbito
#   global contador = 2
#   local  contador = 100
#   global sigue    = 2
# == 11-12. Type hints y docstring
#   área: 13.5
#   doc : Calcula el área de un rectángulo.
# == 13. lambda con map / filter / sorted
#   map    : [50, 20, 80, 10]
#   filter : [5, 8]
#   sorted : ['uva', 'kiwi', 'manzana']
#   sorted : [('Luis', 9), ('Ana', 7), ('Eva', 5)]
# == 14. Función como argumento
#    7 16
# == 15. Decorador
#   >>> antes
#   dentro de la función
#   <<< después
# == 16. Recursividad
#   5! = 120
# == 17. Parámetro mutable por defecto
#   mal : [1, 2] [1, 2]
#   bien: [1] [2]
# -----------------------------------------------------------------------------
# RECORDATORIOS RÁPIDOS:
# - Sin return explícito, toda función devuelve None.
# - Pasar una función como dato: SIN paréntesis (sumar). Llamarla: CON (sumar()).
# - lambda solo admite UNA expresión, sin return ni varias líneas.
# - map/filter devuelven objetos perezosos: envuélvelos en list().
# - sorted() devuelve lista NUEVA; lista.sort() ordena la original y devuelve None.
# - En "mal" salen dos [1, 2] porque las dos llamadas devuelven la MISMA lista.
# -----------------------------------------------------------------------------
