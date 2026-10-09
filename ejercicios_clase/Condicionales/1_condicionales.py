# Ejercicio 1: Verificador de Rangos y Estilo de Comparación
# En Java, para comprobar si una temperatura T está en un rango seguro entre 18C y 27C,
# escribirías if (temp >= 18 && temp <= 27). Escribe un programa en Python que pida al usuario 
# una temperatura flotante e indique si la temperatura está en estado ÓPTIMO (18T27), ALERTA FRÍO (T<18) o ALERTA CALOR (T>27).
# Requisito: Debes utilizar la sintaxis de comparaciones encadenadas directa 
# de Python en lugar del operador and tradicional para la evaluación del rango óptimo.

temp = float(input("Introduce una temperatura en grados Celsius: ")) 
#Float sirve para poder introducir decimales, ya que la temperatura puede no ser un número entero.
# Input sirve para obtener la entrada del usuario y devuelve un string, por lo que es necesario convertirlo a float para poder hacer comparaciones numéricas 
if temp < 18:
    print("ESTADO: HACE FRÍO")
elif 18 <= temp <= 27: 
    print("ESTADO: ÓPTIMO")
else:
    print("ESTADO: HACE CALOR")
