# Tema 6: Clases, listas de objetos, diccionarios, comprensiones y lambda

Es el tema que más pesa en el examen. Si vas con prisa, empieza por `01` (la práctica evaluada) y `09` (la chuleta).

| Archivo | Qué pide | Forma exigida | Conceptos clave |
|---|---|---|---|
| `01_teletubbies.py` | Práctica evaluada "La Galaxia de los Teletubbies": clase `PersonajeTeletubby`, pruebas en el main y cuestión teórica | Atributo de clase `saludo_oficial`; privados `__nivel_hambre=50` y `__nivel_felicidad=100`; `ver_estado()` hace **return** de un str; `__str__`/`__repr__` como en el ejemplo; pruebas en `if __name__ == "__main__":` en el orden pedido | `self`, `__init__`, clase vs instancia, name mangling, getter, `__str__`/`__repr__`. Al final, la respuesta teórica lista para copiar |
| `02_teletubbies_ampliado.py` | La misma clase con getters y setter con validación, más una lista de Teletubbies | Filtrar con comprensión de listas; ordenar con `sorted(key=lambda t: ...)`; recorrer diccionarios con `.items()` | Lista de objetos, buscar, filtrar, ordenar, `max` con key, diccionario nombre -> objeto, comprensión de diccionario |
| `03_clases_basico.py` | Teoría: la clase mínima | PascalCase, docstrings, pruebas en el main | Constructor, atributos de clase/instancia, métodos, `__str__`/`__repr__`, error de la lista como atributo de clase (Dog) |
| `04_encapsulamiento_getters_setters.py` | Teoría: público, `_protegido`, `__privado` | Getters y setters como **métodos** `get_`/`set_` (la forma de los apuntes); `@property` solo si lo piden | Name mangling, validación en el setter, `@property` como alternativa |
| `05_herencia_super.py` | Teoría: herencia y `Cyborg(Humano, Robot)` | `class Hija(Padre):`, `super().__init__(...)`, `**kwargs` y `Cyborg.mro()` | Override, ampliar con `super()`, polimorfismo, `isinstance`, MRO |
| `06_listas_de_objetos.py` | Teoría: CRUD sobre una lista de `Producto` | for / `enumerate(start=1)`, comprensión para filtrar, `key=lambda` | Añadir, listar, buscar, modificar, eliminar, contar, sumar, `max`/`min` con key, borrar sin romper el for |
| `07_diccionarios.py` | Teoría: diccionarios | `.items()` / `.values()` para recorrer; `.get()` para acceder sin riesgo | `[]` vs `get`, `del`/`pop`, `in`, diccionario de listas, lista de diccionarios, contar apariciones |
| `08_comprensiones_y_lambda.py` | Teoría: comprensiones y lambda | Comprensión para filtrar/transformar; `list(map(lambda x: x**2, numeros))` | Comprensiones con if / if-else / de diccionario; `map`, `filter`, `sorted`, `max`/`min` con key; siempre al lado del for equivalente |
| `09_resumen_poo.py` | Chuleta mínima de todo lo anterior | (Resumen) | Para copiar y adaptar rápido |

Ejecutar: `python NN_nombre.py` (en Linux/Docker: `python3 NN_nombre.py`). Ninguno usa `input()`.
