"""
TEMA 6 (integrador) - Variante 05: "PyBank: cuentas y movimientos"
==================================================================
ENUNCIADO (redactado al estilo del profesor, modelo Teletubbies):

    Objetivo: Implementar una cuenta bancaria con encapsulamiento estricto
    del saldo, historial de movimientos (lista de diccionarios) y
    validaciones, más funciones de análisis con lambda y comprensiones.

    Requisitos de la clase CuentaBancaria:
    1. Atributos de clase: banco = "PyBank", comision_retirada = 1.5,
       limite_operacion = 3000 y un contador num_cuentas.
    2. Atributos públicos: titular, iban. Privados: __saldo (float, por
       defecto 0) y __movimientos (lista de diccionarios
       {"tipo": ..., "importe": ..., "saldo": ...}).
       El saldo inicial, si es mayor que 0, se registra como "ingreso".
    3. Método privado __registrar(tipo, importe): añade un diccionario
       al historial.
    4. ingresar(importe): válido solo si 0 < importe <= limite_operacion
       (COMPARACIÓN ENCADENADA). Devuelve un string (return temprano si error).
    5. ingresar_varios(*importes): *args; devuelve la lista de mensajes.
    6. retirar(importe): valida el rango igual que ingresar, y que haya
       saldo para importe + comisión. Devuelve un string.
    7. transferir(destino, importe, **opciones): **kwargs con opciones
       como concepto="..." o urgente=True (urgente cobra 2 € extra).
       Devuelve un string.
    8. consultar_saldo(): GETTER que DEVUELVE un string "Saldo de X: 123.45 €".
       get_saldo(): getter que devuelve el número.
    9. get_movimientos(): devuelve una COPIA de la lista.
    10. nivel_cliente(): MATCH-CASE con GUARDAS sobre el saldo:
        < 0 imposible (no debe pasar), 0 "Sin fondos", < 1000 "Básico",
        1000 a 9999.99 "Plus", resto "Premium".
    11. __str__ y __repr__.

    Funciones de análisis:
    12. resumen_por_tipo(cuenta) -> dict: {tipo: total} recorriendo los
        movimientos; después se recorre con .items().
    13. ingresos_grandes(cuenta, minimo): FILTER + LAMBDA.
    14. importes(cuenta): MAP + LAMBDA (lista solo de importes).
    15. cuenta_mas_rica(cuentas): MAX con key=lambda.
    16. anios_para_objetivo(saldo, interes, objetivo): WHILE que calcula
        cuántos años de interés compuesto hacen falta.

    Bloque principal: 3 cuentas, todas las operaciones (correctas y
    erróneas), historial con enumerate(start=1), análisis y ranking.
    El menú interactivo (while + input) va en una función aparte.

    Cuestión teórica: ¿Por qué __saldo es privado y no hay set_saldo()?

FORMA QUE EXIGE EL PROFESOR:
    - Atributos de clase (incluido contador), privados con __, método
      privado __registrar.
    - Getter que devuelve string (consultar_saldo).
    - *args (ingresar_varios) y **kwargs (transferir).
    - Comparación encadenada, match-case con guardas, return temprano.
    - Lista de diccionarios, .items(), filter/map/max con lambda,
      comprensión, while, enumerate(start=1).

CONCEPTOS QUE PRACTICA:
    - Encapsulamiento real: el saldo solo cambia por métodos que validan
    - Dos objetos que interactúan (transferencia)

CÓMO EJECUTARLO:  python 05_cuenta_bancaria.py   (en Linux: python3 ...)
"""


# ---------------------------------------------------------------
# PASO 1: Clase CuentaBancaria.
# ---------------------------------------------------------------
class CuentaBancaria:
    """Cuenta bancaria con historial de movimientos."""

    banco = "PyBank"
    comision_retirada = 1.5
    limite_operacion = 3000
    num_cuentas = 0

    def __init__(self, titular, iban, saldo=0.0):
        """Crea la cuenta. Si hay saldo inicial se apunta como ingreso."""
        self.titular = titular
        self.iban = iban
        self.__saldo = 0.0
        self.__movimientos = []      # lista de diccionarios
        CuentaBancaria.num_cuentas += 1
        if saldo > 0:
            self.__saldo = float(saldo)
            self.__registrar("ingreso", saldo)

    def __registrar(self, tipo, importe):
        """Método PRIVADO: solo se usa dentro de la clase."""
        self.__movimientos.append({
            "tipo": tipo,
            "importe": float(importe),   # float para que todos se vean igual
            "saldo": round(self.__saldo, 2),
        })

    def ingresar(self, importe):
        """Ingresa dinero si el importe es válido."""
        if not (0 < importe <= CuentaBancaria.limite_operacion):
            return f"Error: ingreso de {importe} € no permitido."
        self.__saldo += importe
        self.__registrar("ingreso", importe)
        return f"Ingreso de {importe:.2f} € en la cuenta de {self.titular}."

    def ingresar_varios(self, *importes):
        """*args: recibe varios importes sueltos y los ingresa uno a uno."""
        # Comprensión que llama a un método: devuelve la lista de mensajes.
        return [self.ingresar(importe) for importe in importes]

    def retirar(self, importe):
        """Retira dinero cobrando comisión. Cláusulas de guarda."""
        if not (0 < importe <= CuentaBancaria.limite_operacion):
            return f"Error: retirada de {importe} € no permitida."
        total = importe + CuentaBancaria.comision_retirada
        if total > self.__saldo:
            return f"Error: saldo insuficiente para retirar {importe} € (+comisión)."
        # Restamos y registramos por separado para que el historial
        # muestre el saldo después de cada paso.
        self.__saldo -= importe
        self.__registrar("retirada", importe)
        self.__saldo -= CuentaBancaria.comision_retirada
        self.__registrar("comision", CuentaBancaria.comision_retirada)
        return f"Retirada de {importe:.2f} € (+{CuentaBancaria.comision_retirada} € de comisión)."

    def transferir(self, destino, importe, **opciones):
        """Transfiere a otra cuenta. **opciones: concepto, urgente..."""
        # opciones es un diccionario; .get(clave, valor_por_defecto)
        concepto = opciones.get("concepto", "Sin concepto")
        extra = 2 if opciones.get("urgente", False) else 0
        if not (0 < importe <= CuentaBancaria.limite_operacion):
            return f"Error: transferencia de {importe} € no permitida."
        if importe + extra > self.__saldo:
            return f"Error: {self.titular} no tiene saldo para transferir {importe} €."
        self.__saldo -= importe
        self.__registrar("transferencia_enviada", importe)
        if extra:                     # 0 cuenta como False, 2 como True
            self.__saldo -= extra
            self.__registrar("comision", extra)
        # Accedemos al otro objeto SOLO a través de sus métodos públicos:
        # destino.__saldo += importe aquí sí funcionaría (estamos dentro de
        # la misma clase), pero no quedaría registrado en SU historial;
        # recibir_transferencia() suma y registra, que es lo correcto.
        destino.recibir_transferencia(importe)
        return f"Transferencia de {importe:.2f} € a {destino.titular} ('{concepto}')."

    def recibir_transferencia(self, importe):
        """Suma una transferencia recibida y la registra."""
        self.__saldo += importe
        self.__registrar("transferencia_recibida", importe)

    def consultar_saldo(self):
        """GETTER que devuelve un string."""
        return f"Saldo de {self.titular}: {self.__saldo:.2f} €"

    def get_saldo(self):
        """Getter numérico (para ordenar, comparar...)."""
        return round(self.__saldo, 2)

    def get_movimientos(self):
        """Devuelve una copia de la lista para proteger el historial."""
        return self.__movimientos.copy()

    def nivel_cliente(self):
        """Nivel según el saldo: match-case con guardas y comparación encadenada."""
        match self.__saldo:
            case s if s < 0:
                return "ERROR: saldo negativo"
            case 0 | 0.0:                    # el | significa "o" en un patrón
                # (case 0 solo ya valdría también para 0.0, porque 0 == 0.0;
                # aquí se pone | para que veas la sintaxis)
                return "Sin fondos"
            case s if s < 1000:
                return "Básico"
            case s if 1000 <= s < 10000:     # comparación encadenada
                return "Plus"
            case _:
                return "Premium"

    def __str__(self):
        """Texto amigable para el usuario (lo usa print)."""
        return (f"[{CuentaBancaria.banco}] {self.titular} ({self.iban}) - "
                f"{self.__saldo:.2f} € - {self.nivel_cliente()}")

    def __repr__(self):
        """Texto técnico: cómo se crearía este objeto."""
        return f"CuentaBancaria('{self.titular}', '{self.iban}', {self.get_saldo()})"


# ---------------------------------------------------------------
# PASO 2: Funciones de análisis.
# ---------------------------------------------------------------
def resumen_por_tipo(cuenta):
    """Diccionario {tipo: total de importes de ese tipo}."""
    resumen = {}
    for mov in cuenta.get_movimientos():   # cada mov es un diccionario
        tipo = mov["tipo"]
        resumen[tipo] = round(resumen.get(tipo, 0) + mov["importe"], 2)
    return resumen


def ingresos_grandes(cuenta, minimo):
    """filter + lambda: ingresos con importe >= minimo."""
    return list(filter(lambda m: m["tipo"] == "ingreso" and m["importe"] >= minimo,
                       cuenta.get_movimientos()))


def importes(cuenta):
    """map + lambda: solo los importes del historial."""
    return list(map(lambda m: m["importe"], cuenta.get_movimientos()))


def cuenta_mas_rica(cuentas):
    """max con key=lambda: devuelve el OBJETO con más saldo."""
    return max(cuentas, key=lambda c: c.get_saldo())


def anios_para_objetivo(saldo, interes, objetivo):
    """while: años de interés compuesto hasta llegar al objetivo.
    interes en tanto por uno (0.05 = 5 %)."""
    if saldo <= 0 or interes <= 0:
        return -1     # nunca llegaría: evitamos el bucle infinito
    anios = 0
    while saldo < objetivo:
        saldo *= 1 + interes
        anios += 1
    return anios


# ---------------------------------------------------------------
# PASO 3 (opcional): cajero interactivo con while + input.
# Descomenta la llamada al final del main para probarlo.
# ---------------------------------------------------------------
def cajero_interactivo(cuenta):
    """Menú repetitivo con while True y break."""
    while True:
        print(f"\n{cuenta.consultar_saldo()}")
        print("1) Ingresar  2) Retirar  3) Movimientos  0) Salir")
        opcion = input("Opción: ")
        match opcion:
            case "1":
                print(cuenta.ingresar(float(input("Importe: "))))
            case "2":
                print(cuenta.retirar(float(input("Importe: "))))
            case "3":
                for n, mov in enumerate(cuenta.get_movimientos(), start=1):
                    print(n, mov)
            case "0":
                print("Gracias por usar PyBank.")
                break                 # sale del while True
            case _:
                print("Opción incorrecta.")


# ---------------------------------------------------------------
# PASO 4: Bloque principal.
# ---------------------------------------------------------------
if __name__ == "__main__":
    ana = CuentaBancaria("Ana", "ES01", 500)
    luis = CuentaBancaria("Luis", "ES02")
    marta = CuentaBancaria("Marta", "ES03", 12000)
    cuentas = [ana, luis, marta]

    print("--- Cuentas abiertas ---")
    for num, cuenta in enumerate(cuentas, start=1):
        print(f"{num}. {cuenta}")

    print("\n--- Operaciones ---")
    for mensaje in ana.ingresar_varios(200, 1500, -50, 5000):
        print(mensaje)
    print(ana.retirar(100))
    print(luis.retirar(10))                    # saldo 0 -> error
    print(ana.transferir(luis, 300, concepto="Cena", urgente=True))
    print(luis.transferir(marta, 1000))       # sin saldo suficiente
    print(marta.transferir(luis, 2500, concepto="Préstamo"))

    print("\n--- Saldos (getter que devuelve string) ---")
    for cuenta in cuentas:
        print(cuenta.consultar_saldo(), "|", cuenta.nivel_cliente())

    print("\n--- Historial de Ana ---")
    for num, mov in enumerate(ana.get_movimientos(), start=1):
        print(f"{num}. {mov['tipo']:<22} {mov['importe']:>8.2f} € -> saldo {mov['saldo']:.2f}")

    print("\n--- Resumen por tipo (Ana) ---")
    for tipo, total in resumen_por_tipo(ana).items():
        print(f"{tipo}: {total}")

    print("\nIngresos >= 500 de Ana:", ingresos_grandes(ana, 500))
    print("Importes de Luis:", importes(luis))
    print("Total movido por Ana (comprensión):",
          sum([m["importe"] for m in ana.get_movimientos()]))

    print("\nCuenta más rica:", cuenta_mas_rica(cuentas))
    ranking = sorted(cuentas, key=lambda c: c.get_saldo(), reverse=True)
    print("Ranking:", ranking)
    print("Años para que Luis llegue a 4000 € al 5 %:",
          anios_para_objetivo(luis.get_saldo(), 0.05, 4000))
    print(f"Cuentas creadas en {CuentaBancaria.banco}: {CuentaBancaria.num_cuentas}")

    # cajero_interactivo(ana)   # <- descomenta para probar el menú con input()

# ---------------------------------------------------------------
# SALIDA ESPERADA (copiada de la ejecución real):
# --- Cuentas abiertas ---
# 1. [PyBank] Ana (ES01) - 500.00 € - Básico
# 2. [PyBank] Luis (ES02) - 0.00 € - Sin fondos
# 3. [PyBank] Marta (ES03) - 12000.00 € - Premium
#
# --- Operaciones ---
# Ingreso de 200.00 € en la cuenta de Ana.
# Ingreso de 1500.00 € en la cuenta de Ana.
# Error: ingreso de -50 € no permitido.
# Error: ingreso de 5000 € no permitido.
# Retirada de 100.00 € (+1.5 € de comisión).
# Error: saldo insuficiente para retirar 10 € (+comisión).
# Transferencia de 300.00 € a Luis ('Cena').
# Error: Luis no tiene saldo para transferir 1000 €.
# Transferencia de 2500.00 € a Luis ('Préstamo').
#
# --- Saldos (getter que devuelve string) ---
# Saldo de Ana: 1796.50 € | Plus
# Saldo de Luis: 2800.00 € | Plus
# Saldo de Marta: 9500.00 € | Plus
#
# --- Historial de Ana ---
# 1. ingreso                  500.00 € -> saldo 500.00
# 2. ingreso                  200.00 € -> saldo 700.00
# 3. ingreso                 1500.00 € -> saldo 2200.00
# 4. retirada                 100.00 € -> saldo 2100.00
# 5. comision                   1.50 € -> saldo 2098.50
# 6. transferencia_enviada    300.00 € -> saldo 1798.50
# 7. comision                   2.00 € -> saldo 1796.50
#
# --- Resumen por tipo (Ana) ---
# ingreso: 2200.0
# retirada: 100.0
# comision: 3.5
# transferencia_enviada: 300.0
#
# Ingresos >= 500 de Ana: [{'tipo': 'ingreso', 'importe': 500.0, 'saldo': 500.0}, {'tipo': 'ingreso', 'importe': 1500.0, 'saldo': 2200.0}]
# Importes de Luis: [300.0, 2500.0]
# Total movido por Ana (comprensión): 2603.5
#
# Cuenta más rica: [PyBank] Marta (ES03) - 9500.00 € - Plus
# Ranking: [CuentaBancaria('Marta', 'ES03', 9500.0), CuentaBancaria('Luis', 'ES02', 2800.0), CuentaBancaria('Ana', 'ES01', 1796.5)]
# Años para que Luis llegue a 4000 € al 5 %: 8
# Cuentas creadas en PyBank: 3
# ---------------------------------------------------------------
# RESPUESTA A LA CUESTIÓN TEÓRICA:
# - Si el saldo fuera público, cualquiera podría hacer ana.saldo = 1000000
#   sin dejar movimiento ni pasar validaciones. Con __saldo, el ÚNICO modo
#   de cambiarlo es ingresar/retirar/transferir, que validan y registran.
# - No hay set_saldo() a propósito: un banco no "pone" un saldo, lo
#   calcula a partir de los movimientos.
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Dentro de la clase se escribe self.__saldo; fuera da AttributeError.
# - max(cuentas) sin key da TypeError (no sabe comparar objetos).
# - opciones.get("urgente", False): si no se pasa urgente=..., vale False.
#   opciones["urgente"] daría KeyError si no se pasa.
# - Un while sin condición de salida alcanzable = bucle infinito
#   (por eso anios_para_objetivo comprueba antes saldo > 0 e interes > 0).
# EN JAVA SERÍA... private double saldo; y sin setter, solo métodos.
# ALTERNATIVA (funciona, pero NO es lo que pide el enunciado):
#   if importe > 0 and importe <= 3000      -> pide comparación encadenada.
#   transferir(destino, importe, concepto="", urgente=False) con parámetros
#   fijos -> funciona, pero el enunciado pide **kwargs.
# ---------------------------------------------------------------
