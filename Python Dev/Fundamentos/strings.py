#Python é Case sensitive
movie_name = "Top Gun"
movie_name2 = "top gun"
print(movie_name == movie_name2) # Resultado é False.

movie_Description = """
Top Gun Maverick é um filme de aviação e aventura muito consagrado na industria de filmes.
"""    #Doc string ou string multilinhas, usada para explicar o codigo ou um indice do contexto. 

print(movie_name)

#Multiplicação de strings
line = "=-="
print(line*20)
print(movie_Description)

#Procurar uma palavra dentro de um texto

print("Top" in movie_name)
print("ação" in movie_name)
