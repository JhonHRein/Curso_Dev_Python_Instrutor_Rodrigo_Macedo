#Todas as listas abre e fecha colchetes
#Os valores são passados como itens dentro da lista, nada mais que mapear os itens das variaveis.

filmMatrix = ["Matrix", 1999, 8.7, True]
print(type(filmMatrix))

filmList = ["Titanic", "Era do Gelo", "Vingadores", "Pulp Fiction", "Samurai X"] # Listas recebem valores heterogêneo, itens desiguais str, float...

##Fezendo o fatiamento de lista.

#1 - Buscar os dois primeiros itens da lista
print(filmList[:2]) 

#2 - Buscara o ultimo item da lista
print(filmList[-1])

#3 - Buscar filmes ate uma determinada posiçao
print(filmList[:3])

#4 - Buscar filmes de uma posição em diantes.
print(filmList[1:4])