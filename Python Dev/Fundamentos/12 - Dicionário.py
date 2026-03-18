"""
Dicionário: estrutura de dados em Python,
que armazena pares chave:valor,
sendo representado por chaves {}.

Exemplo:
pessoa = {"nome": "Jhon", "idade": 25}
"""

filmInception = {"tile":"Titanic", 
                  "yearRelease": 2010, 
                  "imdbRating" : 8.8,
                  "genre": ["Romance", "Suspense", "Drama"]
                 }

print(filmInception)
print(len(filmInception))
print(type(filmInception))  

# 1 Recuperar um elemento do dicionário.
print(filmInception["genre"])
print(filmInception.get("imdbRatig")) # acessa valor da chave sem erro se não existir
"""O que é o método .get()
- É um método de dicionários em Python usado para acessar o valor de uma chave.
- Diferença para o acesso direto (dict["chave"]):
- Se a chave não existir, o acesso direto gera erro (KeyError).
- Com .get("chave"), se a chave não existir, o Python retorna None (ou um valor padrão que você pode definir).
"""

# 2 Buscar apenas as chaves do dicionário.
print(filmInception.keys()) 
"""
O que é o método .keys()
- Retorna uma "view" com todas as chaves do dicionário.
- Essa view pode ser convertida em lista se necessário.
Exemplo:
filmInception = {"titulo": "Inception", "ano": 2010}
print(filmInception.keys())  # dict_keys(['titulo', 'ano'])
"""

# 3 Buscar apenas os valores do dicionário.
print(filmInception.values())
"""
O que é o método .values()
- Retorna uma "view" com todos os valores do dicionário.
- Útil para percorrer ou listar apenas os dados armazenados.
Exemplo:
filmInception = {"titulo": "Inception", "ano": 2010}
print(filmInception.values())  # dict_values(['Inception', 2010])
"""
 
# 4 buscar itens do dicionário com chave e valor.
print(filmInception.items())
"""
O que é o método .items()
- Retorna uma "view" com todos os pares chave:valor do dicionário.
- Cada item é representado como uma tupla (chave, valor).
Exemplo:
filmInception = {"titulo": "Inception", "ano": 2010}
print(filmInception.items())  # dict_items([('titulo', 'Inception'), ('ano', 2010)])
"""

# 5 Adicionar items no dicionario.
filmInception["Director"] = "Cristopher Nolan"
"""
Adicionar itens em dicionários
- Para inserir um novo par chave:valor, basta usar a sintaxe dict["chave"] = valor.
- Se a chave já existir, o valor será atualizado.
Exemplo:
filmInception = {"titulo": "Inception", "ano": 2010}
filmInception["Director"] = "Christopher Nolan"
print(filmInception)
# saída: {'titulo': 'Inception', 'ano': 2010, 'Director': 'Christopher Nolan'}
"""

# 6 Remover item do dicionário com del.
del filmInception["genre"]  # remove a chave "genre" e seu valor

"""
Remover itens com del
- O comando del exclui uma chave e o valor associado do dicionário.
- Se a chave não existir, gera erro (KeyError).
Exemplo:
filmInception = {"titulo": "Inception", "ano": 2010, "Director": "Christopher Nolan"}
del filmInception["ano"]
print(filmInception)
# saída: {'titulo': 'Inception', 'Director': 'Christopher Nolan'}
"""

# 7 Atualizar ou adicionar múltiplos itens com .update().
filmInception.update({"yearRelease": 2011, "BoxOffice": "829M"})  # atualiza ou adiciona várias chaves

"""
O que é o método .update()
- Permite adicionar ou atualizar múltiplos pares chave:valor de uma vez.
- Se a chave já existir, o valor é atualizado; se não existir, é criada.
Exemplo:
filmInception = {"titulo": "Inception", "ano": 2010}
filmInception.update({"ano": 2011, "BoxOffice": "829M"})
print(filmInception)
# saída: {'titulo': 'Inception', 'ano': 2011, 'BoxOffice': '829M'}
"""

# 8 Remover item do dicionário com del.
del filmInception["genre"]  # remove a chave "genre" e seu valor

"""
Remover itens com del
- O comando del exclui uma chave e o valor associado do dicionário.
- Se a chave não existir, gera erro (KeyError).
Exemplo:
filmInception = {"titulo": "Inception", "ano": 2010, "Director": "Christopher Nolan"}
del filmInception["ano"]
print(filmInception)
# saída: {'titulo': 'Inception', 'Director': 'Christopher Nolan'}
"""

# 9 Remover item do dicionário com .pop().
filmInception.pop("Director")  # remove a chave "Director" e retorna o valor

"""
Remover itens com .pop()
- O método .pop("chave") remove a chave e retorna o valor associado.
- Se a chave não existir, gera erro (KeyError), mas você pode definir um valor padrão.
Exemplo:
filmInception = {"titulo": "Inception", "ano": 2010, "Director": "Christopher Nolan"}
valor_removido = filmInception.pop("Director")
print(valor_removido)       # saída: Christopher Nolan
print(filmInception)        # saída: {'titulo': 'Inception', 'ano': 2010}
"""
# 10 Remover todos os itens do dicionário com .clear().
filmInception.clear()  # apaga todo o conteúdo do dicionário

"""
Remover todos os itens com .clear()
- O método .clear() remove todos os pares chave:valor do dicionário.
- O dicionário continua existindo, mas fica vazio.
Exemplo:
filmInception = {"titulo": "Inception", "ano": 2010}
filmInception.clear()
print(filmInception)  # saída: {}
"""







