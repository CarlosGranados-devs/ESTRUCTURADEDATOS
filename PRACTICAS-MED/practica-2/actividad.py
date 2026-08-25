
#lista
catalogo_nintendo = []

#set
consolas_unicas = set()

#Datos del primer juego
titulo1 = "Kirby Battle Royale"
consola1 = "Nintendo 3DS"
año1 = 2017

#tupla con los datos
juego1 = (titulo1, consola1, año1)

#Guardar la tupla en la lista y la consola en el set
catalogo_nintendo.append(juego1)
consolas_unicas.add(consola1)

#segundo juego
titulo2 = "Shovel Knight"
consola2 = "Nintendo 3DS"
año2 = 2014

#guardar los datos del segundo juego
juego2 = (titulo2, consola2, año2)
catalogo_nintendo.append(juego2)
consolas_unicas.add(consola2)

#Datos del tercer juego
titulo3 = "The Legend of Zelda: Breath of the Wild"
consola3 = "Nintendo Switch"
año3 = 2017

#guardar los datos del tercer juego
juego3 = (titulo3, consola3, año3)
catalogo_nintendo.append(juego3)
consolas_unicas.add(consola3)

#Mostrar la lista completa de juegos
print("=== CATÁLOGO COMPLETO DE NINTENDO (LISTA + TUPLAS) ===")
for juego in catalogo_nintendo:
    print(f"Juego: {juego[0]} | Consola: {juego[1]} | Año: {juego[2]}")

#Mostrar las cnsolas registradas
print("\n=== CONSOLAS EN TU COLECCIÓN (SET) ===")
for consola in consolas_unicas:
    print(f"- {consola}")