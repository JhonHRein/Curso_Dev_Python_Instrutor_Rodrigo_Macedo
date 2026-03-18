"""
Set: coleção não ordenada em Python,
que armazena elementos únicos (sem repetição),
sendo representada por chaves {}.
"""
filmsSet = {"Titanic", "Era do Gelo", "Vingadores", "Pulp Fiction", "Samurai X"}
print(type(filmsSet)) 

# 1 Buscando o tamanho do Set, usando o Len().
print(len(filmsSet))

# 2 True e valor: 1, são considerados o mesmo valor, podendo o 1 ser ignorado.
exempleSet = {"Era do Gelo", True, 1, 8.7} 
print(exempleSet)
# Saída: {'Era do Gelo', True, 8.7} #Numero 1 ignorado ambos tem o mesmo valor.

# 3 Adicionar um item de outro Set.
filmsSet.update(exempleSet)
print(filmsSet) #Junta as duas variaveis utiliando o Update(), removendo itens duplicados.

# 4 Remover um item do Set.
filmsSet.remove(True)
filmsSet.remove(8.7)
print(filmsSet)