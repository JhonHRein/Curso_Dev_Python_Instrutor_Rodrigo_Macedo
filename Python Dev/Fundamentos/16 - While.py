"""
O que é o laço while
- Estrutura de repetição que executa um bloco de código ENQUANTO uma condição for verdadeira.
- Diferente do for, que percorre uma sequência definida, o while depende de uma condição lógica.
- É importante garantir que a condição se torne falsa em algum momento, para evitar loops infinitos.
Exemplo:
contador = 0
while contador < 3:
    print("Loop número:", contador)
    contador += 1
# saída:
# Loop número: 0
# Loop número: 1
# Loop número: 2
"""
#Lista de filmes
movieslist = ["Titanic", "The Godfather", "Era do Gelo", "Jurassic Park"]

#1 Iterando valores deuma lista de filmes usando while.
index = 0
while index < len(movieslist):
    print(movieslist[index])
    index += 1 
    
# 2 Quando a condição for atendida, o loop sera encerrado. 
"""# 12 Interromper um loop com break.
for numero in range(5):
    if numero == 3:
        break
    print(numero)

Comando break
- Interrompe imediatamente a execução de um loop (for ou while).
- Útil para parar quando uma condição é atingida.
Exemplo:
for n in range(5):
    if n == 3:
        break
    print(n)
# saída: 0, 1, 2
"""

index = 0
while index < len(movieslist):
    if movieslist[index] == "The Godfather":
        break
    print(movieslist[index])
    index += 1 
    
# 3 Quando a condição for atendida, o loop vai para a proxima iteração;
"""
Comando continue
- Faz o loop pular a iteração atual e seguir para a próxima.
- Diferente do break, não encerra o loop, apenas ignora aquele passo.
Exemplo:
for n in range(5):
    if n == 3:
        continue
    print(n)
# saída: 0, 1, 2, 4
"""

while index < len(movieslist):
    if movieslist[index] == "The Godfather":
        index += 1
        continue
    print(movieslist[index])
    index += 1 

# 4 Avaliação com while.
movieName = input("Digite o nome do filme: ")
movieRating = int(input("Digite quantas avaliações deseja fazer: "))
total = 0 
count = 0

while count < movieRating:
    note = float(input("Digite a nota para o filme: "))
    total += note
    count += 1

if movieRating > 0:
    average = total / movieRating
else:
    average = 0
    
print(f"A média de avaliação do filme {movieName} é : {average:.2f}")