class PersonajeTeletubby:
    
    # Esto lo comparten todos por igual
    saludo_oficial = "¡Tubby abrazo!"

    # El constructor: se ejecuta cada vez que creo un nuevo personaje
    def __init__(self, nombre, color, antena, objeto_favorito):
        # Atributos normales (se pueden ver y cambiar desde fuera)
        self.nombre = nombre
        self.color = color
        self.antena = antena
        self.objeto_favorito = objeto_favorito

        # Atributos privados: pongo dos guiones bajos para que nadie los pueda cambiar por fuera por error
        self.__nivel_hambre = 50      # Empieza en 50
        self.__nivel_felicidad = 100  # Empieza en 100

    # Método para que se presenten
    def saludar(self):
        print(f"¡Hola! Soy {self.nombre}, soy de color {self.color} y mi antena es de {self.antena}.")

    # Cuando juegan, gastan energía (sube el hambre) y se ponen contentos (sube la felicidad)
    def jugar(self):
        print(f"{self.nombre} está jugando con su {self.objeto_favorito}.")
        self.__nivel_hambre += 20
        self.__nivel_felicidad += 10

    # Método para comer y recuperarse
    def comer_tubby_papilla(self):
        print(f"{self.nombre} se está comiendo su tubby-papilla.")
        # Bajo el hambre (uso max para que nunca baje de 0) y subo la felicidad
        self.__nivel_hambre = max(0, self.__nivel_hambre - 30)
        self.__nivel_felicidad += 20

    # Como los atributos de antes son privados, uso esto para poder verlos en pantalla
    def ver_estado(self):
        return f"-> {self.nombre} | Hambre: {self.__nivel_hambre} | Felicidad: {self.__nivel_felicidad}"


# Aquí empieza el programa principal para hacer las pruebas
if __name__ == "__main__":
    
    # 1. Creo dos teletubbies diferentes
    tb1 = PersonajeTeletubby("Tinky Winky", "morado", "triángulo", "bolso rojo")
    tb2 = PersonajeTeletubby("Po", "rojo", "círculo", "patinete")

    # 2. Muestro el saludo oficial y hago que saluden
    print("Saludo oficial:", PersonajeTeletubby.saludo_oficial)
    tb1.saludar()
    tb2.saludar()
    print("-" * 30)

    # 3. Pongo a los dos a jugar
    tb1.jugar()
    tb2.jugar()
    print("-" * 30)

    # 4. Compruebo cómo han quedado
    print(tb1.ver_estado())
    print(tb2.ver_estado())
    print("-" * 30)

    # 5. Hago que solo coma Po
    tb2.comer_tubby_papilla()
    print("-" * 30)

    # 6. Miro el estado final (aquí se ve que al único que le bajó el hambre es a Po)
    print("Estado final:")
    print(tb1.ver_estado())
    print(tb2.ver_estado())