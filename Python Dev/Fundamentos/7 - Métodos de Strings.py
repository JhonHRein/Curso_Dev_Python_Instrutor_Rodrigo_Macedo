movieName = "Top Gun"
movieDescription = """Top Gun Maverick é um filme de aviação e aventura\nmuito consagrado na indústria do cinemoa mundial""" 

print(movieName.upper)   #.upper para deixar 1 letra Maiúscula
print(movieName.lower)   #.lower para deixar as letras minúsculas
print(movieName.capitalize) #.capitalize deixa a primeira letra em maiúsculo
print(movieName.title) #.title deixa as duas primeiras letras da strings em maiúsculo.
print(movieName.center(10, "-")) #.center Retorna a string centralizada com caractere de preenchimento.
print(movieName.find("u")) #.find Retorna a posição de um determinado caractere.
print(movieName.replace("Top", "Matrix")) #.replace altera um elemento por outro.
print(movieName.strip(','))  #.strip Remove todos os espaços no começo e no fim da string.
print(movieDescription.split(',')) #.split Divide a string em pequenos grupos de cadeia e novos indices para a cadeia.