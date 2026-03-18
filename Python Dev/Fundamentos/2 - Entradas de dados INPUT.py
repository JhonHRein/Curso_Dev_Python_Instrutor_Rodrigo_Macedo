#Utilizano o INPUT
#Comando e entreda INPUT

"""
Input: função em Python que captura dados
digitados pelo usuário no console,
sendo representada por input().
"""


name = input("Digite o nome do filme:\n ")     # o \n é o comando de quebra de linha.
year_Launch = input("Digite o ano de lançamento do filme:\n")
noteMovie = input("Digite a nota do filme:\n")

print(type(name))
print(type(year_Launch))
print(type(noteMovie))

'''Lembrando que o input sozinho transforma todo input em string, mesmo sendo valores numericos
para isso precisamos conveter isso nos tipos utilizados que o type mostra, adicionando seu tipo antes do imput, como parametro'''

name = str((input("Digite o nome do filme:\n "))) # Mesmo sendo string automatico, add STR por boa pratica.      
year_Launch = int(input("Digite o ano de lançamento do filme:\n"))
noteMovie = float(input("Digite a nota do filme:\n"))
