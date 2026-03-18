movieName = "Top Gun"

"""
Slice/Fatiamento: técnica em Python para acessar
partes de uma sequência (string, lista, tupla),
utilizando colchetes [] com índices e intervalos.
"""


# string[valor de inicio:valor de fim] - indice começa na posição 0 / indice final  -1. 
# Obs: No python os espaços vazios dentro de uma string, também conta como indice.
# O espaço entre a palavra "top e o gun" também soma indice.

#1 - Buscar toda stringa a partir da 1 posição.
print(movieName[0:])    # com o indice inicial com zero, ele percorre a string inteira.

#2 - Buscar toda a string até a ultima posição.
print(movieName[:6])   #Com o indicce final, apos os : ele percorre a string e discarta o ultimo indice. 

#3 - Buscar toda string  da terceira até a ultima posição.
print(movieName[2:]) 

"""# string[valor de inicio:valor de fim] - indice começa na posição 0 / indice final  -1. 
passo -  determina o incremento. Por padrão esse numero é o 1.
"""

#4 - Buscar toda a string de 2 em 2 caracteres.
print(movieName[::2]) # Quero pegar toda a string, e quero que percorra de 2 em 2 caractere. 

#5 - Buscar toda a string nos indices ímpares.
print(movieName[1::2]) # Começa percorrer a string apos o indice zero.

#6 - Inverter uma string de trás pra frente.
print(movieName[::-1]) #retorna a string invertido.

