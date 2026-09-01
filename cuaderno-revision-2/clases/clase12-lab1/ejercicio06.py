#lista con 5 materias sugeridas
materias = ["Programación", "Estructura de Datos", "Base de Datos", "Ingeniería de Software", "Redes"]

#Mostrar la lista completa
print(f"Lista completa: {materias}")

#Agregar 2 materias más
materias.append("Servidores Web")
materias.append("POE")
print(f"Lista tras agregar 2 materias: {materias}")

#Insertar una materia en la posición 2 
materias.insert(1, "Ciberseguridad")
print(f"Lista tras insertar en la posición 2: {materias}")

# Eliminar la última materia agregada (POE)
materias.remove("POE")
print(f"Lista tras eliminar la última materia: {materias}")

# e) Mostrar el número total de materias con len()
print(f"Total de materias actuales: {len(materias)}")