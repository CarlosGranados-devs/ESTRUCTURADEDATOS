# Datos de registro
nombre_estudiante = "Carlos Granados"
edad_estudiante = 19
promedio_acumulado = 9.2
es_becado = False

# Presentación organizada de la información
print("=== REGISTRO DEL ESTUDIANTE ===")
print(f"Nombre: {nombre_estudiante}")
print(f"Edad: {edad_estudiante} años")
print(f"Promedio: {promedio_acumulado}")
print(f"Estado de beca: {es_becado}")

# Cálculos con las variables
anos_para_graduacion = 25 - edad_estudiante
proyeccion_promedio = promedio_acumulado * 1.05

# Mostrar resultados de los cálculos
print("\n=== CÁLCULOS Y PROYECCIONES ===")
print(f"Años estimados para maestría (a los 25): {anos_para_graduacion} años")
print(f"Proyección de rendimiento (+5%): {proyeccion_promedio:.2f}")