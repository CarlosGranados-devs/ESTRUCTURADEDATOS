#Definición de cadena
frase = "Universidad de Oriente - El Salvador"

#Extraer Universidad
universidad = frase[:11]
print(f"Extraer 'Universidad': {universidad}")

#Extraer El Salvador
el_salvador = frase[-11:]
print(f"Extraer 'El Salvador': {el_salvador}")

#Frase al revés -1
frase_invertida = frase[::-1]
print(f"Frase al revés: {frase_invertida}")

# Mostrar cada tercera letra
cada_tercera = frase[::3]
print(f"Cada tercera letra: {cada_tercera}")