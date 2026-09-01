producto = {
    "codigo": "P001",
    "nombre": "Teclado Mecanico",
    "precio": 45.99,
    "stock": 20,
    "disponible": True
}
print(producto["nombre"])
producto["stock"] = 0
producto["disponible"] = None
print (producto)