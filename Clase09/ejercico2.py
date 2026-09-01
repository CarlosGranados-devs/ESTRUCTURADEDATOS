# Creación de las tres tuplas individuales
dispositivo1 = ("PC001", "Servidor principal", (150, 300), "Activo")
dispositivo2 = ("SW002", "Switch de distribución", (220, 450), "Activo")
dispositivo3 = ("RT003", "Router Border", (80, 120), "Mantenimiento")

# Mostrar datos del primer dispositivo accediendo a sus posiciones
print("===== DATOS DEL DISPOSITIVO 1 =====")
print(f"Código: {dispositivo1[0]}")
print(f"Nombre: {dispositivo1[1]}")
print(f"Coordenada X: {dispositivo1[2][0]}")
print(f"Coordenada Y: {dispositivo1[2][1]}")
print(f"Estado: {dispositivo1[3]}\n")

# Tupla anidada con los tres dispositivos
dispositivos = (dispositivo1, dispositivo2, dispositivo3)

# Acceso a la coordenada Y del segundo dispositivo
# dispositivos[1] -> obtiene dispositivo2
# dispositivos[1][2] -> obtiene la tupla de coordenadas (220, 450)
# dispositivos[1][2][1] -> obtiene el valor de Y (450)
coordenada_y_disp2 = dispositivos[1][2][1]

print("===== ACCESO A TUPLA ANIDADA =====")
print(f"Coordenada Y del segundo dispositivo: {coordenada_y_disp2}")