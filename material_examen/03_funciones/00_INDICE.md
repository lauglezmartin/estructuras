# Tema 5 - Funciones (15 Ejercicios Funciones Python)

| Archivo | Qué pide | Forma exigida | Conceptos clave |
|---|---|---|---|
| 01_primera_funcion.py | `saludar_mundo()` imprime "¡Hola, mundo de las funciones!" | Sin parámetros; imprime dentro | def, llamada con () |
| 02_parametros_simples.py | `saludo_personalizado(nombre)` imprime saludo | Un parámetro `nombre` | parámetro vs argumento, f-string |
| 03_retornar_valor.py | `multiplicar(a, b)` | **return obligatorio, NADA de print dentro** | return vs print, None |
| 04_mayor_de_edad.py | `es_mayor_de_edad(edad)` -> True/False | **`return edad >= 18`** (if/else = menos bueno) | booleanos, función predicado |
| 05_contar_vocales.py | `contar_vocales(texto)` (may. y min.) | Devolver con return | for sobre str, `in`, contador |
| 06_parametros_por_defecto.py | `presentar_usuario(nombre, rol)` | **`rol="Estudiante"`**, formato `Usuario: x \| Rol: y`, 2 llamadas | valores por defecto al final |
| 07_retornar_multiples_valores.py | `obtener_extremos(lista)` | **`return min(l), max(l)`** + desempaquetar en 2 variables | tuplas, desempaquetado |
| 08_filtrar_pares.py | `filtrar_pares(lista)` | Iterar con for y retornar lista NUEVA | append, `%` |
| 09_promedio_args.py | `calcular_promedio(*args)` | **`*args` obligatorio**; controla 0 argumentos | args = tupla, sum/len |
| 10a_kwargs_perfil_diccionario.py | Variante A: `crear_perfil_usuario(nombre, apellido, **kwargs)` | **`**kwargs`**, RETORNA diccionario | kwargs = dict, update |
| 10b_kwargs_perfil_imprimir.py | Variante B: `crear_perfil_usuario(**kwargs)` | **`**kwargs`**, IMPRIME `Clave: valor` con capitalize | `.items()`, capitalize |
| 11_type_hints_celsius.py | `celsius_a_fahrenheit` | **`(celsius: float) -> float`** + docstring triple comilla | type hints, docstring |
| 12_decorador.py | decorador `anunciar_ejecucion` + `tarea_importante` | **Aplicar con `@anunciar_ejecucion`** | función que envuelve a otra |
| 13_map_lambda.py | Cuadrados de una lista | **`list(map(lambda x: x**2, numeros))`** | lambda, map, list() |
| 14_orden_superior.py | `aplicar_operacion(a, b, funcion)` + sumar/restar | Función como 3er parámetro, `return funcion(a, b)` | funciones como valores |
| 15_recursividad_factorial.py | `calcular_factorial(n)` recursiva | **Recursiva + caso base 0 y 1**; traza de factorial(4) | caso base, caso recursivo |
| 16_resumen_funciones.py | Chuleta ejecutable de todo el tema | - | def, parámetros, return/None, *args, **kwargs, orden, global, hints, docstring, lambda+map/filter/sorted, orden superior, decorador, recursividad, mutable por defecto |
