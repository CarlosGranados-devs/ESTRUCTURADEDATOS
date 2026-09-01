# Definir tuplas
puntos = [(3, 4), (1, 1), (5, 12), (-2, 2), (0, 3)]

# Lista
distancias = []

# Calcular la raíz cuadrada usando la potencia ** 0.5 sin importar nada
for p in puntos:
    dist = (p[0]**2 + p[1]**2) ** 0.5
    distancias.append(dist)
    print(f"Punto {p} -> Distancia al origen: {dist:.2f}")

# Encontrar el menor valor de distancia
menor_distancia = min(distancias)
indice = distancias.index(menor_distancia)
punto_cercano = puntos[indice]

print(f"\nEl punto más cercano al origen es {punto_cercano} con una distancia de {menor_distancia:.2f}")