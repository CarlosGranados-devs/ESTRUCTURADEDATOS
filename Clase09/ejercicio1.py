# Definición de la tupla de configuración
configuracion = (
    "Sistema Académico",  # Índice 0: Nombre de la aplicación
    "1.0.0",              # Índice 1: Versión
    "localhost",          # Índice 2: Servidor
    8080,                 # Índice 3: Puerto
    "producción"          # Índice 4: Modo de ejecución
)

print("===== CONFIGURACIÓN DEL SISTEMA =====")
print(f"Aplicación: {configuracion[0]}")
print(f"Versión: {configuracion[1]}")
print(f"Servidor: {configuracion[2]}")
print(f"Puerto: {configuracion[3]}")
print(f"Modo: {configuracion[4]}")

# A. Acceso a elementos específicos
print("--- A. Acceso a datos requeridos ---")
print(f"Versión: {configuracion[1]}")
print(f"Servidor: {configuracion[2]}")
print(f"Puerto: {configuracion[3]}\n")

# B. Longitud de la tupla
print("--- B. Longitud ---")
longitud = len(configuracion)
print(f"La tupla contiene {longitud} elementos.")