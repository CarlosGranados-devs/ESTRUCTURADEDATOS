estudiante = {
    "nombre": "Ana",
    "edad": 21,
    "cursos": ["python", "estructura de datos"]

}

# print(estudiante["nombre"])
# print(estudiante["edad"])
# print(estudiante["cursos"])

estudiante["edad"] = 22
print(estudiante)

estudiante["carrera"] = "ing. software"
print(estudiante)
del estudiante["edad"]
print(estudiante)

#persona.pop("cursos") (borra la clave o le ultimo dato)