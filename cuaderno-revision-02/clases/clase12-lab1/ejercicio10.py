#3conjuntos con 6 materias
ing_software = {"Programación", "Estructura de Datos", "Base de Datos", "Ingeniería de Software", "Redes", "Ciberseguridad"}
ing_sistemas = {"Programación", "Estructura de Datos", "Base de Datos", "Redes", "Sistemas Operativos", "Arquitectura de Computadoras"}
ing_datos = {"Programación", "Estructura de Datos", "Base de Datos", "Estadística", "Machine Learning", "Minería de Datos"}

# Materias comunes
comunes = ing_software & ing_sistemas & ing_datos
print(f"Materias comunes en todas las carreras: {comunes}")

# Materias exclusivas de cada carrera
exclusivas_sw = ing_software - ing_sistemas - ing_datos
exclusivas_sis = ing_sistemas - ing_software - ing_datos
exclusivas_datos = ing_datos - ing_software - ing_sistemas

print(f"Exclusivas de Software: {exclusivas_sw}")
print(f"Exclusivas de Sistemas: {exclusivas_sis}")
print(f"Exclusivas de Ciencia de Datos: {exclusivas_datos}")

#todas las materias de las tres carreras
todas_las_materias = ing_software | ing_sistemas | ing_datos
print(f"Unión de todas las materias: {todas_las_materias}")

# Cantidad total de materias únicas
print(f"Total de materias únicas: {len(todas_las_materias)}")