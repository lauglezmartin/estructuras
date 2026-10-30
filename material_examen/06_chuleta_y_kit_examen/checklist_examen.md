# Checklist del examen de Python (2h45: 14:30 a 17:15)

## 1. Plan de tiempo

| Hora | Minutos | Qué hago |
|---|---|---|
| 14:30-14:45 | 15 | **Leer TODO el examen** antes de escribir nada. Subrayar en cada enunciado la **forma exigida** (palabras como "usando", "sin usar", "con match", "en una línea", "retorna", "*args", "else del bucle", "privado", "decorador @"). Apuntar los puntos de cada ejercicio. |
| 14:45-15:00 | 15 | Crear la carpeta y los archivos (`ejercicio1.py`, …) con el esqueleto: docstring, funciones vacías e `if __name__ == "__main__":`. |
| 15:00-16:30 | 90 | **Resolver empezando por lo seguro** (lo que sé hacer seguro y lo que más puntúa). Probar **cada parte al terminarla**. Si me atasco más de 10 minutos, paso al siguiente y vuelvo luego. |
| 16:30-16:55 | 25 | Volver a lo que dejé a medias. Algo que funcione a medias puntúa más que nada. |
| 16:55-17:10 | 15 | **Checklist de entrega** (abajo) archivo por archivo. |
| 17:10-17:15 | 5 | Guardar todo, ejecutar una última vez cada archivo y entregar. |

### Reglas de oro
- **Guardar a menudo**: `Ctrl+S` después de cada cambio (o activa *File > Auto Save* en VS Code al empezar).
- **Ejecutar a menudo**: no escribas 50 líneas sin probar. Escribe una función, pruébala, sigue.
- **La forma pedida manda**: el profe solo da el máximo si se resuelve como pide. Si dice `match`, no vale `if/elif`; si dice "sin `sum()`", nada de `sum()`; si dice "comprensión en una línea", nada de `for` + `append`.
- **Si no sé hacerlo de la forma pedida**: lo hago de otra forma que funcione (algo puntúa) y dejo un comentario `# TODO: el enunciado pide X`. Si sobra tiempo, vuelvo.
- **No borres código que funciona** para probar otra cosa: comenta con `Ctrl+K Ctrl+C` (descomentar: `Ctrl+K Ctrl+U`) o copia el archivo.

## 2. Al empezar cada ejercicio

- [ ] Copio el enunciado como docstring al principio del archivo (así no lo pierdo de vista).
- [ ] Marco la **forma exigida** en un comentario: `# FORMA EXIGIDA: match-case con case _`.
- [ ] ¿Pide **imprimir** (`print`) o **devolver** (`return`)? Lo apunto.
- [ ] ¿Pide pedir datos al usuario (`input`)? Entonces hay que **convertir** (`int()`, `float()`) y, si da tiempo, **validar**.
- [ ] Busco en mi material una plantilla parecida (ver apartado 4) y la adapto.

## 3. Checklist antes de entregar (por cada archivo)

**Funciona**
- [ ] Se ejecuta sin errores: `python archivo.py` (Linux: `python3 archivo.py`).
- [ ] Probado con un caso normal **y con casos límite**: lista vacía, 0, número negativo, texto en vez de número, opción de menú no válida, elemento que no existe al buscar o borrar, mayúsculas/minúsculas.
- [ ] La salida coincide con lo que pide el enunciado (textos y formato, p. ej. `:.2f`).

**Forma exigida**
- [ ] He usado exactamente la estructura que pide cada apartado (repasa lo que subrayaste).
- [ ] Nada prohibido: `sum()` donde dice "sin sum", `and` en rangos (`a <= x <= b`), `print` dentro de funciones que "retornan", `lista=[]` como parámetro por defecto.

**PEP 8 y estilo**
- [ ] Sangría de 4 espacios, sin tabuladores mezclados.
- [ ] Variables y funciones en `snake_case`; clases en `PascalCase`; constantes en `MAYUSCULAS`.
- [ ] Nombres que se entienden (`precio_total`, no `pt` ni `x2`).
- [ ] Espacios alrededor de `=`, `+`, `==` y después de las comas.
- [ ] 2 líneas en blanco entre funciones y clases; 1 entre métodos.
- [ ] Líneas no excesivamente largas (≈ 79 caracteres).

**Documentación**
- [ ] Docstring `"""..."""` al inicio del archivo, en cada función, en cada clase y en cada método.
- [ ] Comentarios `#` en las partes que no son obvias (el porqué, no lo evidente).
- [ ] Respuestas a preguntas teóricas, si las hay, como comentario o docstring en el archivo.

**Estructura**
- [ ] Pruebas dentro de `if __name__ == "__main__":` (nada de código suelto al final).
- [ ] Clases: `__init__` con `self`, privados con `__`, getters/setters con `return`, `__str__` devuelve str.
- [ ] Nombre del archivo correcto, sin tildes ni espacios, extensión `.py`.
- [ ] **Guardado** (en VS Code la pestaña no tiene el punto blanco de "sin guardar").

## 4. Cómo buscar rápido en tu material

| Quiero… | Atajo / dónde |
|---|---|
| Buscar una palabra en **todos** los archivos de la carpeta | `Ctrl+Shift+F` en VS Code (p. ej. `enumerate`, `match`, `**kwargs`, `__repr__`, `lambda`) |
| Buscar dentro del archivo abierto | `Ctrl+F` |
| Abrir un archivo por su nombre | `Ctrl+P` y escribe parte del nombre |
| Ir a una línea (la del traceback) | `Ctrl+G` |
| Ir a una función del archivo | `Ctrl+Shift+O` |
| Buscar en la chuleta HTML/PDF | Ábrela en el navegador y `Ctrl+F`; usa el **índice** con enlaces |
| Plantillas listas | `plantillas_examen.py`: busca `[P1]` … `[P8]` |
| Un error que no entiendo | `errores_y_traceback.md`: `Ctrl+F` con el nombre del error (`KeyError`, `TypeError`…) |

**Palabras clave útiles para buscar** (en los `00_INDICE.md` de cada carpeta y con `Ctrl+Shift+F`):
`FORMA QUE EXIGE`, `match`, `case _`, `guarda`, `enumerate`, `range(`, `while True`, `break`, `continue`, `else:` (bucle), `comprensión`, `lambda`, `map(`, `sorted(`, `*args`, `**kwargs`, `@`, `__init__`, `__str__`, `__repr__`, `get_`, `set_`, `.items()`, `.get(`, `isdigit`, `try`.

## 5. Antes de salir de casa / al sentarte
- [ ] Llevar la carpeta `ejercicios/` completa (con `.py` y PDF) en el pendrive o donde se pueda.
- [ ] Comprobar en el ordenador del examen: `python --version` (o `python3 --version`) y que VS Code abre la terminal con `Ctrl+ñ`.
- [ ] Abrir la chuleta en el navegador desde el principio.
- [ ] Respirar: lee, marca la forma, empieza por lo seguro, prueba, guarda.
