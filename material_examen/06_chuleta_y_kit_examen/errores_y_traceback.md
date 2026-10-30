# Errores y traceback: qué hacer cuando Python se queja

## 1. Cómo leer un traceback paso a paso

Ejemplo real:

```text
Traceback (most recent call last):
  File "C:\examen\tienda.py", line 42, in <module>
    total = calcular_total(precios)
  File "C:\examen\tienda.py", line 15, in calcular_total
    suma = suma + precio
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

1. **Lee primero la ÚLTIMA línea.** Te da el tipo de error (`TypeError`) y el motivo (`+` entre `int` y `str`).
2. **Sube a la línea de encima.** Esa es la instrucción exacta que falló (`suma = suma + precio`) y el archivo, la línea (`line 15`) y la función (`calcular_total`) donde está.
3. **Sigue subiendo si hace falta.** Cada bloque `File ... line ...` es una llamada anterior. El de más arriba es el punto de partida (`<module>` = tu código principal). Así ves el camino: la línea 42 llamó a `calcular_total`, y dentro falló la línea 15.
4. **Ve a esa línea en VS Code**: `Ctrl+G` y escribe el número. También puedes hacer `Ctrl+clic` sobre la ruta en la terminal.
5. **Pregúntate qué valor tenía cada variable.** Si no lo sabes, pon un `print(f"{precio=} {type(precio)=}")` justo antes de la línea que falla y vuelve a ejecutar.
6. **Arregla, guarda (`Ctrl+S`) y vuelve a ejecutar.** Arregla un error cada vez: muchas veces el segundo desaparece al arreglar el primero.

> **Ojo:** en `SyntaxError` e `IndentationError` el programa **no llega a ejecutarse**. La línea señalada a veces es la **siguiente** a la que tiene el fallo (p. ej. si falta un `:` o un paréntesis de cierre, mira también la línea anterior). El `^` marca dónde se dio cuenta Python.

## 2. Tabla de errores típicos en el examen

| Error que ves | Causa más probable | Ejemplo que falla | Solución |
|---|---|---|---|
| `IndentationError: expected an indented block` | Falta sangría tras `if`/`for`/`def`… | `if x > 0:`<br>`print(x)` | Sangra 4 espacios el cuerpo |
| `IndentationError: unexpected indent` / `unindent does not match` | Sangría de más, o mezcla de tabuladores y espacios | `    x = 1` suelto | Alinea con el bloque; en VS Code: "Convert Indentation to Spaces" |
| `SyntaxError: expected ':'` | Olvidaste los dos puntos | `for i in range(5)` | `for i in range(5):` (también `if`, `elif`, `else`, `while`, `def`, `class`, `case`, `try`, `except`) |
| `SyntaxError: invalid syntax` (con `=`) | `=` en vez de `==` en una condición | `if x = 5:` | `if x == 5:` |
| `SyntaxError: '(' was never closed` | Paréntesis/comillas sin cerrar | `print("hola"` | Cierra el paréntesis (mira la línea anterior a la señalada) |
| `NameError: name 'x' is not defined` | Variable/función mal escrita, sin crear todavía, o local de otra función | `print(totla)` | Revisa mayúsculas y nombre; define antes de usar; usa `return` para sacar valores de funciones |
| `NameError: name 'true' is not defined` | Costumbre de Java | `activo = true` | `True`, `False`, `None` con mayúscula |
| `TypeError: can only concatenate str (not "int") to str` | Sumar texto y número | `"Edad: " + 20` | `f"Edad: {20}"` o `"Edad: " + str(20)` |
| `TypeError: '>=' not supported between instances of 'str' and 'int'` | `input()` sin convertir | `edad = input()`<br>`if edad >= 18:` | `edad = int(input())` |
| `TypeError: jugar() takes 0 positional arguments but 1 was given` | Olvidaste `self` en un método | `def jugar():` dentro de la clase | `def jugar(self):` |
| `TypeError: f() missing 1 required positional argument` | Faltan argumentos al llamar | `multiplicar(3)` | Pasa todos o pon valor por defecto |
| `TypeError: __str__ returned non-string (type NoneType)` | `__str__` hace `print` en lugar de `return` | `print(f"...")` dentro de `__str__` | `return f"..."` |
| `TypeError: 'NoneType' object is not ...` | Usas el resultado de una función sin `return` (o de `sort()`) | `lista = lista.sort()` | Añade `return`; usa `sorted(lista)` o `lista.sort()` sin asignar |
| `ValueError: invalid literal for int() with base 10: 'hola'` | `int()` de algo que no es entero (`"hola"`, `"3.5"`, `""`) | `int(input())` y escriben `abc` | Valida con `isdigit()` o `try/except ValueError`; para decimales `float()` |
| `ValueError: list.remove(x): x not in list` | Borrar algo que no está | `lista.remove(99)` | Comprueba antes: `if 99 in lista:` |
| `IndexError: list index out of range` | Índice ≥ `len(lista)` o lista vacía | `range(len(l) + 1)`, `while i <= len(l)` | `range(len(l))`, `i < len(l)`, o mejor `for x in lista:` |
| `KeyError: 'edad'` | Clave que no existe en el diccionario | `persona["edad"]` | `persona.get("edad", valor_por_defecto)` o `if "edad" in persona:` |
| `AttributeError: 'Producto' object has no attribute '__precio'` | Acceder a un privado desde fuera de la clase | `p.__precio` | Usa el getter `p.get_precio()` |
| `AttributeError: ... has no attribute 'nombre'` | En `__init__` pusiste `nombre = nombre` sin `self.` (o lo escribiste distinto) | `nombre = nombre` | `self.nombre = nombre` |
| `AttributeError: 'list' object has no attribute 'add'` | Método de Java | `lista.add(3)` | `lista.append(3)` |
| `RecursionError: maximum recursion depth exceeded` | Recursividad sin caso base | `return n * f(n - 1)` sin `if` | `if n <= 1: return 1` |
| `ZeroDivisionError: division by zero` | Dividir entre 0 (p. ej. media de lista vacía) | `sum(l) / len(l)` con `l = []` | Guarda: `if not l: return 0` |

## 3. Errores que NO dan mensaje (los más traicioneros)

| Síntoma | Causa | Solución |
|---|---|---|
| Sale `<function saludar at 0x...>` o `<bound method ...>` | Olvidaste los paréntesis al llamar | `saludar()`, `obj.metodo()` |
| Sale `None` donde esperabas un valor | La función no tiene `return` (o hace `print` en vez de `return`) | Añade `return resultado` |
| La función solo mira el primer elemento | `return` **dentro** del bucle (o un `else: return None` dentro del `for`) | Saca el `return` fuera del bucle (menos sangría) |
| El programa se queda colgado | `while` infinito: la variable de la condición nunca cambia | Actualiza la variable dentro del bucle o usa `break`. Para pararlo: `Ctrl+C` en la terminal |
| El total sale mal o 0 | Acumulador inicializado **dentro** del bucle | `total = 0` antes del `for` |
| Sale `<map object at ...>` | Falta `list()` | `list(map(...))` |
| `range(1, 10)` no imprime el 10 | El final de `range` no se incluye | `range(1, 11)` |
| `7 / 2` da `3.5` | `/` siempre da float | `//` para división entera |
| Todos los objetos comparten la misma lista | Lista como atributo de clase o `def f(l=[])` | Créala en `__init__` / usa `None` por defecto |
| `p.__precio = 0` "funciona" pero el precio no cambia | Creaste un atributo nuevo; el privado real es `_Producto__precio` | Usa el setter |

## 4. Rutina rápida cuando algo falla

1. Última línea del traceback → tipo de error.
2. Línea señalada → `Ctrl+G` y número.
3. Busca el error en la tabla de arriba (`Ctrl+F` con el nombre, p. ej. `KeyError`).
4. Si sigue sin verse, `print(f"{variable=}")` antes de la línea.
5. Arregla, guarda, ejecuta. Un error cada vez.
