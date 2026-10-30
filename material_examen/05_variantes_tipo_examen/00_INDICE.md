# 05 - Variantes tipo examen (modelo "La Galaxia de los Teletubbies")

Seis ejercicios integradores ORIGINALES, de dificultad igual o mayor que la práctica de los Teletubbies.
Cada archivo trae el enunciado con requisitos numerados, la solución comentada, la **SALIDA ESPERADA** real,
la respuesta a la cuestión teórica, errores típicos y la alternativa que "funciona pero no es lo que pide".

Todos se ejecutan sin pedir datos: `python 0N_nombre.py` (en Linux: `python3`).
Los menús con `while` + `input()` (variantes 01 y 05) están en una función aparte; para probarlos,
descomenta la última línea del bloque `if __name__ == "__main__":`.

## Ejercicios

| Archivo | Qué pide | Forma exigida | Conceptos clave |
|---|---|---|---|
| `01_tamagotchi_mascotas.py` | Clase `MascotaVirtual` con niveles privados y un refugio (lista) | `*args` en `alimentar`, `1 <= minutos <= 60`, match-case con guardas, getter que devuelve string | Contador de clase, método privado `__limitar`, menú `while` |
| `02_biblioteca_prestamos.py` | Clases `Libro`, `Socio` y `Biblioteca` con préstamos | `**kwargs` en `alta_libro`, `for ... else`, cláusulas de guarda, `filter`/`sorted` + lambda | Dict de objetos, composición de clases, `dict.get` |
| `03_tienda_carrito.py` | Inventario `Producto` y `Carrito` con ticket, IVA y cupones | Atributo de clase `IVA`, match-case con guarda sobre texto (`"VIP" if total >= 100`), `*args`, `map`/`filter`/`sorted` | Dict con valor `[objeto, cantidad]`, tuplas de retorno, formato `:.2f` |
| `04_gestor_alumnos_notas.py` | Alumnos con notas en un dict privado, medias y calificaciones | match-case con guardas para la calificación, `**kwargs` en `crear_alumno`, type hints, comprensiones | Comprensión de diccionario, copia de dict, `while` con límite |
| `05_cuenta_bancaria.py` | Cuenta con saldo privado, historial y transferencias | Atributos de clase, método privado `__registrar`, `*args` y `**kwargs`, `0 < importe <= limite` | Lista de diccionarios, `max(key=lambda)`, interés compuesto con `while`, cajero `while True` + `break` |
| `06_videojuego_herencia.py` | Clase base `Personaje` y dos hijas, `Guerrero` y `Mago`, con combate por turnos | `class Hija(Padre)`, `super().__init__`, sobrescritura con `super().metodo()`, match-case sobre texto en la fábrica, `if/elif` + `isinstance()` en `describir` | Polimorfismo, name mangling en herencia, `isinstance`, `type(obj).__name__` |

## Qué concepto aparece en qué variante (para buscar rápido un ejemplo)

Busca el nombre de la función o método (Ctrl+F) dentro del archivo.

| Concepto | 01 Tamagotchi | 02 Biblioteca | 03 Tienda | 04 Notas | 05 Banco | 06 Videojuego |
|---|---|---|---|---|---|---|
| Atributo de clase | `nombre_app` | `max_prestamos` | `IVA` | `nota_aprobado` | `comision_retirada` | `mundo` |
| Contador de clase (`Clase.x += 1`) | `total_mascotas` | `total_libros` | - | - | `num_cuentas` | `total_personajes` |
| Atributos privados `__` | `__hambre`... | `__disponible`, `__catalogo` | `__stock`, `__lineas` | `__notas` (dict) | `__saldo`, `__movimientos` | `__vida`, `__mana` |
| Método privado `__metodo` | `__limitar` | - | - | - | `__registrar` | - |
| Getter que devuelve string | `ver_estado` | `ver_prestamos` | `ver_stock` | `ver_boletin` | `consultar_saldo` | `ver_estado` |
| Getter que devuelve una copia | - | - | - | `get_notas` | `get_movimientos` | - |
| `__str__` y `__repr__` | sí | sí (2 clases) | sí | sí | sí | sí (con `super().__str__()`) |
| match-case con guardas | `estado_animo` | `epoca` | `ver_stock`, `descuento` | `calificacion` | `nivel_cliente` | (comentada en `describir`) |
| match-case con texto / menú | `menu_interactivo` | - | `descuento` | - | `cajero_interactivo` | `crear_personaje` |
| match-case con `\|` (o) | - | - | - | - | `nivel_cliente` | - |
| `isinstance()` para saber la clase | - | - | - | - | - | `describir`, main |
| Comparación encadenada | `jugar` | `epoca` | `ver_stock`, `agregar` | `poner_nota` | `ingresar`, `nivel_cliente` | - |
| Cláusulas de guarda (return temprano) | `alimentar`, `jugar` | `prestar` | `agregar` | `poner_nota`, `media` | `retirar`, `transferir` | `curar` |
| Ternario `x if c else y` | - | `__str__` de Libro | - | `ver_boletin` | `transferir` | `combate` |
| `while` | `menu_interactivo` | - | - | `dieces_necesarios` | `anios_para_objetivo`, `cajero_interactivo` | `combate` |
| `for ... else` | - | `buscar_libro` | - | - | - | - |
| `enumerate(start=1)` | main | main | `ticket`, main | main | main | main |
| Recorrer dict con `.items()` | main | main | `ticket`, main | `suspensas`, `crear_alumno` | main | main |
| Contar con `dict.get(k, 0) + 1` | - | `libros_por_epoca` | - | - | `resumen_por_tipo` | `contar_por_clase` |
| `setdefault(k, []).append(...)` | - | - | `inventario_por_categoria` | `medias_por_asignatura` | - | - |
| Comprensión de listas | `mascotas_que_necesitan_cuidado` | `disponibles` | `subtotal` | `suspensas`, `aprobados` | `ingresar_varios` | `vivos` |
| Comprensión de diccionario | (comentada en `resumen_refugio`) | - | - | `medias_por_asignatura` | - | - |
| `sorted` + lambda | ranking en main | `ordenados_por_anio` | `mas_caros` | `ranking` | ranking en main | `clasificacion` |
| `filter` + lambda | - | `libros_de` | `bajo_stock` | - | `ingresos_grandes` | - |
| `map` + lambda | - | - | `precios_con_iva` | `nombres_en_mayusculas` | `importes` | - |
| `max(key=lambda)` | - | - | - | - | `cuenta_mas_rica` | - |
| `*args` | `alimentar` | - | `agregar_varios` | - | `ingresar_varios` | - |
| `**kwargs` | - | `alta_libro` (`Libro(**datos)`) | - | `crear_alumno` | `transferir` | `crear_personaje` |
| Type hints | - | - | - | todas las funciones | - | - |
| Lista de objetos | `refugio` | `__catalogo` | `inventario` | `grupo` | `cuentas` | `personajes` |
| Lista de diccionarios | - | - | - | - | `__movimientos` | - |
| Herencia + `super()` | - | - | - | - | - | `Guerrero`, `Mago` |
| Polimorfismo | - | - | - | - | - | `atacar` |
| Varias clases que colaboran | - | `Biblioteca`/`Socio`/`Libro` | `Carrito`/`Producto` | - | `transferir` entre cuentas | `atacar` entre personajes |
| Demostrar `AttributeError` con privado | final del main | - | - | - | - | (explicado en la cuestión teórica) |
| Menú `while` + `input` (opcional) | `menu_interactivo` | - | - | - | `cajero_interactivo` | - |

## Cuestiones teóricas resueltas (al final de cada archivo)

- **01**: para qué sirve `*args` y por qué un getter hace `return` y no `print`.
- **02**: diferencia entre `for-else` y un `else` dentro del `for`; por qué el catálogo es privado.
- **03**: atributo de clase frente a atributo de instancia (qué pasa si cambia el IVA).
- **04**: por qué devolver una copia del diccionario privado.
- **05**: por qué `__saldo` es privado y no tiene `set_saldo()`.
- **06**: name mangling en herencia (la hija no ve `self.__vida`) y qué hace `super()`.
