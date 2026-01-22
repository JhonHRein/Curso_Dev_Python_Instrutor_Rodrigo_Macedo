num1 = int(input("Digite o primeiro numero:\n"))
num2 = int(input("Digite o segundo numero:\n"))

#Aritiméticos 
sum = num1 + num2
sub =  num1 - num2
div =  num1 / num2
mult = num1 * num2
mod = num1 % num2  #resto da divisao
exp = num1 ** num2  #potenciação

print(f"- A soma do {num1} e {num2} é: {sum}\n- A subtração é: {sub}\n- A divisão é: {div:.2f}\n- A multiplicação é: {mult} ")  

#Comparação
bigger = num1 > num2
smaller = num1 < num2 
equal = num1 == num2
different = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2 

print(f"Os numeros {num1} e {num2} são iguais? {equal}")
print(f"O numero {num1} é maior ou iugal a {num2}? {bigger_equal}")

#Atribuição

num1 += 1 #num1 = num1 + 1
num1 +- 1 #num1 = num1 - 1
num1 *= 1 #num1 = num1 * 1
num1 /= 1 #num1 = num1 / 1