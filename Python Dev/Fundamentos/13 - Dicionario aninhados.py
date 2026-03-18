import pprint

filmsDict = {
    "Titanic" : {
        "yearRelease": 1998, 
        "imdbRating" : 8.8,
        "genre": ["Romance", "Suspense", "Drama"]
    },
    "Era do Gelo":{
        "yearRelease": 2005, 
        "imdbRating" : 6.0,
        "genre": ["Comédia", "Infantil"]
    }, 
    "Vingadores":{
        "yearRelease": 2012, 
        "imdbRating" : 9.0,
        "genre": ["Comédia", "Infantil", "Ação", "Heroi"]
    }
} 
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmsDict)

# 1 - Buscar uma informaçao dentro de um dicionario aninhado.
print(filmsDict["Titanic"]["genre"])  

# 2 - Adicionar um novo item.
filmsDict["Vingadores"]["Director"] = "Cristopher Nolan"
print(filmsDict["Vingadores"])  

# 3 Excluir um dicionario.

del filmsDict["Era do Gelo"]
pp.pprint(filmsDict)