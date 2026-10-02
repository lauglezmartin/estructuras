# prueba de impresión
print("Hola, Mundo")
print("¡Bienvenido a Python!")
print("Este es un ejemplo de código en Python.")

# prueba de variables
a =3
print("El valor de a es:", a)
print(type(a))
a ="Pepe"
print("El valor de a ahora es:", a)
print(type(a))

# prueba de listas
lista1 = [1, 2, 3, 4, 5]
lista2 = ["manzana", "banana", "cereza"]
lista3 = [1, "dos", 3.0, True]
lista4 = lista1

# prueba de comparaciones
print(lista1 == lista2) #hace una comparación de valores
print(lista1 == lista4) #hace una comparación de valores

print(lista1 is lista2) #hace una comparación de referencias
print(lista1 is lista4) #hace una comparación de referencias

saludo = "Hola, Mundo!"

print("Hola" in saludo) #hace una comparación de valores
print("Hola" is saludo) #hace una comparación de referencias
print("Hola" == saludo) #hace una comparación de valores
print("Hola" is not saludo) #hace una comparación de referencias
print("Hola" != saludo) #hace una comparación de valores
print("Hola, mundo" is saludo) #hace una comparación de referencias

# Python es un lenguaje sensible a las mayúsculas y minúsculas, 
# por lo que "Hola" y "hola" se consideran diferentes.
# cuando ponemos is, estamos comparando si dos variables apuntan al mismo objeto en memoria,
# mientras que cuando usamos ==, estamos comparando si los valores de las variables son iguales.


#Lectura por teclado

entero = int (input("Ingrese un valor entero: ")) 
#para leer un valor entero desde el teclado tenemos que usar la función int() 
#para convertir la entrada de texto en un número entero ya que la función input() devuelve una cadena de texto (string) por defecto.

print(type(entero))
#esto se utiliza para verificar el tipo de dato de la variable entero, que en este caso será <class 'int'>.



#tengo que hacer un programa que lea por pantalla dos numeros enteros y si los dos numeros son mayores que 0 imprime positivo.
#Lectura por teclado

entero1 = int (input("Introduce un valor entero: "))

#print(type(entero))

entero2 = int (input("Introduce un valor entero: "))

if entero1 > 0 and entero2 >0:
    print("Positivos los dos números:")


#Practicando el if y else if en python que funciona como un switch case en otros lenguajes de programación.
a = 8
if a > 5 and a <= 7:
    print("Mayor que 5 y menos o igual que 7")
elif a > 7:
    print("Mayor que 7")
elif a <= 5:
    print("Menor o igual que 5")


# Un programa que lea una nota por teclado con match si la nota es menor que 5 esta supendido si es entre 5 y 7 aprobado, 
# sin incluir el 7, de 7 a 8,5 notable, sin incluir el 8,5 y de 8,5 a 10 sobresaliente, los dos incluidos, 
# y ademas si la nota es es negativa o nota mayor que 10 es un error dato.

nota = float(input("Introduce una nota: "))
match nota:
    case nota if nota < 0 or nota > 10:
        print("Error: nota fuera de rango")
    case nota if nota < 5:
        print("Suspenso")
    case nota if nota < 7:
        print("Aprobado")
    case nota if nota < 8.5:
        print("Notable")
    case nota if nota <= 10:
        print("Sobresaliente")

        

