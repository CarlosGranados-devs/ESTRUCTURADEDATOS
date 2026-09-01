edad = 19
promedio = 8.5
nombre = "Carlos"
activo = True

print(f"Variable: edad = {edad}, Tipo: {type(edad)}")
print(f"Variable: promedio = {promedio}, Tipo: {type(promedio)}")
print(f"Variable: nombre = \"{nombre}\", Tipo: {type(nombre)}")
print(f"Variable: activo = {activo}, Tipo: {type(activo)}")

saludo = "Estudiante: " + nombre
puntos_extra = edad + promedio

print(f"Operación concatenación: {saludo}")
print(f"Operación matemática (edad + promedio): {puntos_extra}")