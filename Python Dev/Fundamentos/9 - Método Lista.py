filmsList = ["Titanic", "Era do Gelo", "Vingadores", "Pulp Fiction", "Samurai X"] 

#1 -  Tamanho da lista
print(len(filmsList))

#2 - Recuperar um item da lista pelo nome.
    #Lembrando que contagem de numero começa com zero (0,1,2,3,4)
print(filmsList.index("Samurai X")) 


#3 - Adiconar um item no final da lista metodo (.append)
filmsList.append("Senhor dos Aneis")
print(filmsList)

#4 - Ordenação da lista - metodo (.sort())
filmsList.sort()
print(filmsList)

#5 - Copiar itens de uma lista para outra - metodo (.copy())
    #Acrescenta um variavel nova, (filmeCopy) onde vai receber a copia da lista/variavel desejada.
filmsCopy = filmsList.copy()
print(filmsCopy)

#6 - Metodo de remover item da lista usando o (.remove())
filmsCopy.remove("Pulp Fiction")
print(filmsCopy)

#7 - Remove todos os itens da lista (.clear())
filmsList.clear()
print(filmsList)