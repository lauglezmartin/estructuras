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
