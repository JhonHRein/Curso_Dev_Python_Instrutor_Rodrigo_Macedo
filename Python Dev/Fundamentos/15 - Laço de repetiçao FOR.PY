"""# 10 Percorrer elementos de um dicionário com for.
for chave in filmInception:
    print(chave, filmInception[chave])  # percorre cada chave e mostra o valor

O que é o laço for
- Estrutura de repetição usada para percorrer elementos de uma sequência (listas, strings, dicionários).
- No caso de dicionários, o for percorre as chaves por padrão.
- É possível usar .keys(), .values() ou .items() para controlar o que será percorrido.
Exemplo:
filmInception = {"titulo": "Inception", "ano": 2010, "Director": "Christopher Nolan"}

for chave in filmInception:
    print(chave)  
# saída: titulo, ano, Director

for valor in filmInception.values():
    print(valor)
# saída: Inception, 2010, Christopher Nolan

for chave, valor in filmInception.items():
    print(chave, ":", valor)
# saída: titulo : Inception
#        ano : 2010
#        Director : Christopher Nolan
"""
# LISTA DE FILMES
movieslist = ["Titanic", "The Godfather", "Era do Gelo", "Jurassic Park"]

# 1  Interando Valores de uma lista.
for movie in movieslist:
    print(movie)

print() 
 
 #2  - Quando a condição for atendida o loop sera encerrado- break   
for movie in movieslist:
    if movie == "Era do Gelo":
        break
    print(movie)

print()

# 3 Quando a condição for atendida o loop vai para a proxima iteração.
for movie in movieslist:
    if movie == "Era do Gelo":
        continue
    print(movie)
    
print()

# 4 Avaliação do filme:
movieName = input("Digite o nome do filme: ")
movieRating = int(input("Digite quantas avaliações deseja fazer: "))

total = 0 
for i in range(movieRating):
    note = float(input("Digite a nota para o filme: "))
    total += note

if movieRating > 0:
    avarege = total / movieRating
else:
    avarege = 0 
    
print(f"A média de avaliação do filme {movieName} é : {avarege:.2f}")