"""
Dicionarios: chave e valor - chaves
"""

empty_dict = {}
grades = { "Nome 1" : 80, "Nome 2" : 95 }

#pesquisar elemento na lista pela chave
print "valor Nome 1: " + str(grades["Nome 1"])

#erro ao perguntar por um valor inxistente
try:
    print "valor Nome 3: " + str(grades["Nome 3"])
except KeyError:
    print "erro ao pesquisar por Nome 3"

#verificar se exite na lista
print "Verificar Nome 1: " + str("Nome 1" in grades)
print "Verificar Nome 3: " + str("Nome 3" in grades)

#retornar valor sem exception get
print "Recuperar Nome 1: " + str(grades.get("Nome 1",0))
print "Recuperar Nome 3: " + str(grades.get("Nome 3",0))
print "Recuperar Nome 4: " + str(grades.get("Nome 4"))

#alterando a lista
grades["Nome 1"] = 83
grades["Nome 3"] = 84

print "Alterado Nome 1: " + str(grades.get("Nome 1",0))
print "Alterado Nome 3: " + str(grades.get("Nome 3",0))

#dicionario como dados estruturado, como um json
tweet = {
    "user" : "nome",
    "text" : "informacao",
    "retweet_count" : 100,
    "hashtags" : ["#t1","#t2","#t3","#t4"]
}

print "keys: " + str(tweet.keys())
print "values: " + str(tweet.values())
print "items: " + str(tweet.items())

#verificando exixstencia na lista

print "verifica uma chave na lista: " + str("user" in tweet)
print "verifica um nome na lista: " + str("nome" in tweet)
print "verifica um nome nos valores: " + str("nome" in tweet.values())

#criando dicionarios de contagem

document = "contar as palavras existentes em um texto"

#contar verificando 
words_count = {}
for word in document:
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1

print "verificando: " + str(words_count)

#contar inicializando 
words_count = {}
for word in document:
    p_count = words_count.get(word,0)
    words_count[word] = p_count + 1

print "inicializando: " + str(words_count)

#defaultdict, incializa automanticamente com o valor inicial do tipo
from _collections import defaultdict

words_count = defaultdict(int)
for word in document:
    words_count[word] += 1

print "defaultdict - int: " + str(words_count)

#utilizando defaultdict para dicts
dd_dict = defaultdict(dict)
dd_dict["Pessoa"]["Cidade"] = "Nome"

print "defaultdict - dict: " + str(dd_dict)

#contador
# from _collections import Counter

# words_count = Counter(document)
# print "counter: " + str(words_count)

# words_count.most_common(10)