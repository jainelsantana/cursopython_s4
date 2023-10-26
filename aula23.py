# List comprehension em Python
# Lista comprehensio [e uma forma rápida para criar listas
# a partir de interáveis
# print (list(range(10)))
import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


lista = []

# for numero in range(10):
# #     lista.append(numero)
# # #print(lista)

lista = [
    numero * 2
    for numero in range(10)
] #list comprehension

# print (list(range(10)))
# print(lista)

# Mapeamento de dados em list comprehension

produtos =[
    {'nome':'p1', 'preco': 20,},
    {'nome':'p2', 'preco': 10,},
    {'nome':'p3', 'preco': 30,},

]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} #mapeamento
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco']>= 20 and produto['preco'] * 1.05 > 20) #filtro
]
p (novos_produtos)


#p(novos_produtos)
#print(*novos_produtos, sep='\n')

#lista = [n for n in range(10) if n < 5]
# print(lista)