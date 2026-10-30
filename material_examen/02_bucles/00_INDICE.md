# Tema 4 - Bucles (Ejercicios Bucles python.pdf)

| Archivo | Qué pide | Forma exigida | Conceptos clave |
|---|---|---|---|
| `01_total_carrito_sin_sum.py` | Total de la lista de precios | for sobre lista, **sin sum()** | acumulador `total += precio` |
| `02_contar_vocales.py` | Contar vocales de una palabra (input) | for letra a letra | `for letra in palabra`, `in`, contador |
| `03_tabla_del_8_range.py` | Tabla del 8 del 1 al 10 | `range()` | `range(1, 11)`, el fin se excluye |
| `04_cuenta_atras_pares.py` | Pares del 20 al 0 | `range` con **paso** | `range(20, -1, -2)` |
| `05_tareas_enumerate.py` | Tareas numeradas desde 1 | `enumerate(tareas, start=1)` | desempaquetado `for n, t in ...` |
| `06_combinaciones_anidados.py` | Tallas x colores | for **anidados** | 2 x 3 = 6 combinaciones |
| `07_cubos_comprension.py` | Cubos de una lista | comprensión en **una línea** | `[n ** 3 for n in numeros]` |
| `08_filtrar_palabras_comprension.py` | Palabras de más de 3 letras | comprensión con **if** | `[p for p in palabras if len(p) > 3]` |
| `09_contrasena_while.py` | Pedir contraseña hasta 'python123' (input) | **while** | condición `!=`, input dentro del bucle |
| `10_contador_acumulador_while.py` | Sumar hasta superar 50 y contar (input) | **while** | contador vs acumulador, `suma <= 50` |
| `11_login_cajero_while.py` | PIN '1234', máx. 3 intentos (input) | **while** con condición compuesta | `and`, De Morgan, por qué salió |
| `12_calculadora_while_true_break.py` | Sumas hasta 'salir' (input) | **while True + break** | comprobar 'salir' antes de convertir; isdigit / try-except (comentado) |
| `13_saltar_multiplos_continue.py` | 1-10 sin múltiplos de 3 | **continue** | `% 3 == 0` |
| `14_buscar_99_for_else.py` | Buscar 99 en una lista | **else del bucle** + break | el else solo si NO hubo break |
| `15_inventario_dict_items.py` | Imprimir clave y valor del inventario | **.items()** | `for fruta, cantidad in d.items()` |
| `16_resumen_bucles.py` | Chuleta ejecutable | — | for/range/enumerate/zip/dict, while, break, continue, else, anidados, comprensiones, tabla "si me piden X → uso Y" |

Notas: en los ejercicios 7 y 14 la lista del enunciado salió cortada; se usan `[1, 2, 3, 4, 5]` y `[12, 45, 99, 7, 30]` (más una lista sin el 99 para ver el `else`).
