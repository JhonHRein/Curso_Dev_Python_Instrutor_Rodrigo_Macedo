"""
Tupla: estrutura de dados imutável em Python,
que armazena múltiplos valores em ordem fixa,
sendo representada por parênteses ().
"""

filmsTuple = ("Titanic", "Era do Gelo", "Vingadores", "Pulp Fiction", "Samurai X") #tuplas são imutáveis.

print(type(filmsTuple))

# 1 Buscar os dois primeiros itens da tupla.
print(filmsTuple[:2])

# 2 Buscar o ultimo item da tupla.
print(filmsTuple[-1]) #Negativo, um retorno da lista: filme 1,  -1 volta negativa, imprime o ultimo filme igual um loop.

# 3 Filmes até uma determinada posição.
print(filmsTuple[:3]) #Começa em zero, filme 1, filme 2 e filme 3.

# 4 Buscar filmes de uma posição em diante.
print(filmsTuple[2:]) #Pula os dois primeiros filmes.

# 5 Recuperar um item da Tupla pelo nome, objetivo trazer o indice de um determinado filme.
print(filmsTuple.index("Pulp Fiction")) # Indice do filme 3.