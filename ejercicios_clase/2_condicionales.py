#Ejercicio 2: Saneamiento de Entrada y Validación de Datos de Usuario
#Conceptos aplicados: Métodos de cadenas (.strip(), .lower(), .isdigit()), veracidad implícita (falsy values como ""), if-elif-else.
#Enunciado:
#Crea un script para validar el formulario de registro de un usuario en un sistema web. El programa solicitará el nombre de usuario y el código postal (CP).
#Requisitos:
#Aplica .strip() a ambas entradas para eliminar espacios accidentales al inicio y final.
#Verifica si el nombre está vacío aprovechando la evaluación de falsedad de cadenas vacías (if not nombre_limpio:).
#Comprueba con .isdigit() si el código postal contiene únicamente dígitos.
#Si todo es correcto, muestra "Registro válido". Si no, muestra el mensaje de error específico correspondiente (campo vacío o CP no numérico).

# LECTURA DE DATOS: Solicitar datos al usuario
# SANEAMIENTO VALORES VACÍOS: Aplicar .strip() para limpiar al principio y al final y .lower() para normalizar el nombre
# Aqui lo hago directamnete la lectura de datos, ya que no es necesario almacenar el valor original sin limpiar, y no se requiere mantener mayúsculas en el nombre de usuario.
nombre = input("Introduce el nombre el usuario: ").strip().lower()
cp = input("Introduce el código postal (CP): ").strip()

# 2 y 4. Validación del nombre de usuario aprovechando la falsedad de cadenas vacías
if not nombre:
    print("Error: El campo de nombre de usuario no puede estar vacío.")

# 3 y 4. Validación del código postal comprobando si contiene únicamente dígitos
elif not cp.isdigit():
    print("Error: El código postal debe contener únicamente dígitos.")

# Si ambas validaciones son correctas
# Imprimimos los datos ya limpios utilizando un f-string (f"...") 
# para comprobar visualmente que las variables almacenan la información correcta.
else:
    print("¡Registro válido!")
    print(f"Usuario guardado: '{nombre}' | Código postal guardado: '{cp}'" )

