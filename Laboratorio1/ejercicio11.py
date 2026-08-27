#lista de módulos del sistema
modulos = ["Autenticación", "Usuarios", "Productos", "Reportes", "Notificaciones"]

#Mostrar la lista completa de módulos
print(f"a) Lista inicial de módulos: {modulos}")

#Agregar el módulo Pagos
modulos.append("Pagos")
print(f"b) Tras agregar 'Pagos': {modulos}")

#Insertar Dashboard
modulos.insert(1, "Dashboard")
print(f"c) Tras insertar 'Dashboard' en la posición 2: {modulos}")

#Modificar Productos por Inventario mediante el acceso por índice
indice_productos = modulos.index("Productos")
modulos[indice_productos] = "Inventario"
print(f"d) Tras modificar 'Productos' por 'Inventario': {modulos}")

#Eliminar 'Notificaciones' usando remove()
modulos.remove("Notificaciones")
print(f"e) Tras eliminar 'Notificaciones': {modulos}")

#Mostrar la cantidad actual de módulos usando len()
print(f"f) Cantidad de módulos actuales: {len(modulos)}")

#Mostrar la lista final de módulos
print(f"g) Lista final de módulos: {modulos}")