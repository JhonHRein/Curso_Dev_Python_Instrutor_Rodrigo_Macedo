# Python é Case sensitive:  dois valores iguais, porem um com letras maiúscula e outra minúscula existe diferença.

"""
String: sequência de caracteres em Python,
utilizada para representar texto,
sendo delimitada por aspas '' ou "".
"""

movieName = "Top Gun Maverick"
movieName2 = "top gun"
print(movieName == movieName2)  # resposta FALSE, CASE SENSITIVE 


# A utilização de """ """, abre um DocString, uma forma de texto, para uma descrição dentro de uma variavel.
# strings multilinhas.
movieDescription = """Top Gun Maverick é um filme de aviação e aventura\nmuito consagrado na indústria do cinemoa mundial""" 

print(f"Nome do filme: {movieName}")
 #Multiplicação de strings
print("=-="*18) 
print(f"Descrição:\n{movieDescription}")
print("=-="*18)

#Procurar uma palavra dentro de um texto utilizando (in).
print("top" in movieName)
print("ação" in movieName)  