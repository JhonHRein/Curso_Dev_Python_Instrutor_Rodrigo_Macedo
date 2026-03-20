# List Comprehension. 
"""
List Comprehension
- Forma curta e legível de criar listas em Python.
- Substitui loops for simples dentro da lista.
Exemplo:
quadrados = [x**2 for x in range(5)]
print(quadrados)  # saída: [0, 1, 4, 9, 16]
"""

# 1 listar valores de 0 a 10 que sejam menores que 4.
listNunbers = [i for i in range(10) if i < 4]
print(listNunbers)

# LISTA DE FILMES:
movieslist = ["Titanic", "The Godfather", "Era do Gelo", "Jurassic Park"]

# 2 Filmes que possuem a letra 'e' no titulo.
movieWithe = [movie for movie in movieslist if "e" in movie.lower()]
print(movieWithe)

# 3 Filmes assistidos.
movieWatched = [movie for movie in movieslist if movie != "Jurassic Park"]
print(movieWatched)

# 4 Encontrando um filme pelo nome.
while True:
    searchName = input("Digite o nome do filme para buscar na lista (ou sair para encerrar): ")
    if searchName == "sair":
        print("Programa encerrado!")
        break
    
    foundMovie = [movie for movie in movieslist if searchName.lower() in movie.lower()]
    if foundMovie:
        print(f"Filme(s) encontrad(s) com o nome: {searchName}")
        for foundMovie in foundMovie:
            print(f"Filme encontrado: {foundMovie}")
    else:
        print(f" Nenhum fimlme foi encontrado com o nome  {searchName}, tente novamente!.")