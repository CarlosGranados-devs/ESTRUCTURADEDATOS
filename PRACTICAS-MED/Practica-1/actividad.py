import re

# 1. TIPO DE DATO: Email
class Email:
    def __init__(self, direccion: str):
        # EVITA: Cadenas arbitrarias o sin formato estándar que impidan el envío de notificaciones o contacto con el usuario.
        if not isinstance(direccion, str) or "@" not in direccion or "." not in direccion.split("@")[-1]:
            raise ValueError(f"'{direccion}' no es una dirección de correo electrónico válida.")
        self.direccion = direccion

    def __repr__(self):
        return f"Email('{self.direccion}')"

# 2. TIPO DE DATO: Edad
class Edad:
    def __init__(self, valor: int):
        # EVITA: Registros con edades negativas, tipos de datos no enteros o valores biológicamente imposibles (e.g., mayor a 120).
        if not isinstance(valor, int) or valor < 0 or valor > 120:
            raise ValueError(f"'{valor}' no es una edad válida. Debe ser un entero entre 0 y 120.")
        self.valor = valor

    def __repr__(self):
        return f"Edad({self.valor})"

# 3. TIPO DE DATO: Precio
class Precio:
    def __init__(self, monto: float):
        # EVITA: Precios negativos o tipos no numéricos que alteren el cálculo de facturas, transacciones o inventario.
        if not isinstance(monto, (int, float)) or monto < 0:
            raise ValueError(f"'{monto}' no es un precio válido. Debe ser un número mayor o igual a 0.")
        self.monto = float(monto)

    def __repr__(self):
        return f"Precio(${self.monto:.2f})"


# 4. TIPO DE DATO: Porcentaje
class Porcentaje:
    def __init__(self, valor: float):
        # EVITA: Asignar valores fuera del intervalo [0, 100] que distorsionen cálculos de descuentos, tasas o estadísticas.
        if not isinstance(valor, (int, float)) or not (0 <= valor <= 100):
            raise ValueError(f"'{valor}' no es un porcentaje válido. Debe estar entre 0 y 100.")
        self.valor = float(valor)

    def __repr__(self):
        return f"Porcentaje({self.valor}%)"


# 5. TIPO DE DATO: CodigoProducto
class CodigoProducto:
    def __init__(self, codigo: str):
        # EVITA: Códigos de producto con formatos incoherentes que fallen en consultas a la base de datos o en el sistema de inventarios.
        if not isinstance(codigo, str) or not re.match(r"^PROD-\d{4}$", codigo):
            raise ValueError(f"'{codigo}' no es un código válido. Debe seguir el patrón 'PROD-XXXX' (donde X son 4 dígitos).")
        self.codigo = codigo

    def __repr__(self):
        return f"CodigoProducto('{self.codigo}')"

# CASOS DE USO (VÁLIDOS E INVÁLIDOS)
if __name__ == "__main__":
    
    # 1. Caso de uso: Email
    print("--- 1. Email ---")
    valido_email = Email("estudiante@universidad.edu")  # Válido
    print("Válido:", valido_email)
    try:
        invalido_email = Email("correo_sin_dominio@")     # Inválido
    except ValueError as e:
        print("Rechazado:", e)

    # 2. Caso de uso: Edad
    print("\n--- 2. Edad ---")
    valida_edad = Edad(22)                              # Válido
    print("Válido:", valida_edad)
    try:
        invalida_edad = Edad(-5)                         # Inválido
    except ValueError as e:
        print("Rechazado:", e)

    # 3. Caso de uso: Precio
    print("\n--- 3. Precio ---")
    valido_precio = Precio(29.99)                       # Válido
    print("Válido:", valido_precio)
    try:
        invalido_precio = Precio(-15.00)                # Inválido
    except ValueError as e:
        print("Rechazado:", e)

    # 4. Caso de uso: Porcentaje
    print("\n--- 4. Porcentaje ---")
    valido_porcentaje = Porcentaje(15.5)               # Válido
    print("Válido:", valido_porcentaje)
    try:
        invalido_porcentaje = Porcentaje(120.0)         # Inválido
    except ValueError as e:
        print("Rechazado:", e)

    # 5. Caso de uso: CodigoProducto
    print("\n--- 5. CodigoProducto ---")
    valido_codigo = CodigoProducto("PROD-8492")         # Válido
    print("Válido:", valido_codigo)
    try:
        invalido_codigo = CodigoProducto("PRODUCTO-12") # Inválido
    except ValueError as e:
        print("Rechazado:", e)