#informaçoes sobre o filme
name = input("Digite o nome do filme:\n")
yearRealease = int(input("Digite o ano de lançamento:\n"))
rating = float(input("Digite a nota de avaliação do filme:\n"))

#Verificação se o filme é recomendado.
"""
if: Estrutura condicional usada para executar um bloco de código
quando uma expressão booleana é avaliada como verdadeira.
"""
"""
elif: Complemento do if que permite testar múltiplas condições
em sequência, executando o bloco associado à primeira condição verdadeira.
"""
"""
else: Parte final da estrutura condicional que define o bloco
a ser executado quando nenhuma das condições anteriores é satisfeita.
"""

if rating > 8.0 and yearRealease > 2015: 
    print(f"O filme {name} é execelnte, recomendado.")
else:
    print(f"O filme {name} ainda não atingiu uma boa nota")  


# Segundo Exemplo de condição ELIF.

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
operation = input("Digite a operação a ser realizada (+ - * /): " )
            
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Erro de divisão por zero")
        result = 0
else:
    print("Erro! Operação inválida")
    result = 0

print(f"Resultado da operação é: {result:.2f}")