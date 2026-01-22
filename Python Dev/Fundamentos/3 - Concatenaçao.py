#concatenação de  valores
"""
CONCATENAÇÃO COM F-STRINGS (Python 3.6+)

O que é: A forma mais moderna, rápida e legível de unir textos e variáveis.
Sintaxe: Prefixo 'f' antes das aspas e variáveis entre chaves {}.

Vantagens:
1. Legibilidade: O código reflete o resultado final da frase.
2. Expressividade: Permite cálculos e chamadas de métodos dentro das chaves.
3. Performance: É processada em tempo de execução de forma otimizada.

Exemplo rápido:
nome = "Mundo"
print(f"Olá, {nome}!") # Resultado: Olá, Mundo!
"""

name = input("Digite o nome do filme:\n ")     
year_Launch = input("Digite o ano de lançamento do filme:\n")
noteMovie = input("Digite a nota do filme:\n")


print("Dados do Filme")
print("=-="*10)
#Alternativa número 1
print(f"Nome do Filme:", {name})
print(f"Ano de lançamento:", {year_Launch})
print(f"Nota do Filme", {noteMovie})


#Alternativa numero 2
print("Nome do filme:", name, "\nAno de lançamento:", year_Launch, "\nNota do filme:", noteMovie)