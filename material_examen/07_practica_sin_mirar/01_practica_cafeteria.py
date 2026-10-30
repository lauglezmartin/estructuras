"""
PRÁCTICA SIN MIRAR 1 - La cafetería del instituto
==================================================
Tiempo recomendado: 40 minutos. Intenta NO abrir los apuntes; si te atascas
más de 5 minutos en algo, mira solo esa parte y apúntalo.

PARTE A - La clase Producto
  1. Atributo de clase: iva = 0.07 (compartido por todos los productos).
  2. Constructor con atributos públicos: nombre (str) y categoria (str:
     "bebida" o "comida").
     Atributos privados: __precio (float) y __stock (int, por defecto 10).
  3. Getter get_precio() que DEVUELVE el precio sin IVA.
  4. Método precio_con_iva() que DEVUELVE el precio con IVA redondeado
     a 2 decimales.
  5. Método vender(cantidad):
       - Cláusula de guarda: si cantidad <= 0 imprime "Cantidad no válida"
         y sale con return.
       - Si no hay stock suficiente imprime "No hay stock de <nombre>".
       - Si lo hay, resta la cantidad del stock e imprime
         "Vendidos <cantidad> de <nombre>".
  6. __str__ debe devolver exactamente: "Café (bebida) - 1.20 €"
     (precio sin IVA, siempre con 2 decimales).

PARTE B - Funciones (fuera de la clase)
  7. valorar_precio(producto): usa match-case CON GUARDAS sobre el precio
     sin IVA y DEVUELVE (no imprime):
       - "barato"  si precio < 1.5
       - "normal"  si 1.5 <= precio < 3   (usa comparación encadenada)
       - "caro"    en cualquier otro caso (case _)
  8. total_carta(*productos): recibe un número variable de productos y
     DEVUELVE la suma de sus precios con IVA usando un bucle for
     (prohibido usar sum()).

PARTE C - Bloque principal (if __name__ == "__main__":)
  9. Crea una LISTA con estos 5 productos:
       Café (bebida, 1.20), Zumo (bebida, 2.10), Bocadillo (comida, 3.50),
       Donut (comida, 1.40), Batido (bebida, 2.80)
 10. Muéstralos numerados desde 1 con enumerate, junto a su valoración:
       "1. Café (bebida) - 1.20 € -> barato"
 11. Con una COMPRENSIÓN DE LISTAS guarda los nombres de las bebidas
     e imprímela.
 12. Ordena los productos de más caro a más barato con sorted y lambda e
     imprime solo sus nombres.
 13. Crea un DICCIONARIO nombre -> precio con IVA (con comprensión de
     diccionario) y recórrelo con .items() imprimiendo "Café: 1.28 €".
 14. Vende 3 Donuts, luego 20 Donuts y luego -1 Donut.
 15. Imprime el total de la carta llamando a total_carta con los 5
     productos (pista: *lista).

PREGUNTA TEÓRICA (respóndela en un comentario al final):
  ¿Por qué __precio es privado y qué pasaría si escribieras
  print(cafe.__precio) desde el bloque principal?
"""

# Escribe aquí tu solución
