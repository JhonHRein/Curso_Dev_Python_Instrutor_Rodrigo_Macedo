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

bigger = num1 > num2
smaller = num1 < num2 
equal = num1 == num2
different = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2 

print(bigger)
print(smaller)
