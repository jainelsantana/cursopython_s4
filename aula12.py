#Manipulando chaves e valores em dicionários

pessoa = {}

chave = 'nome'
pessoa[chave] = 'Jainel Santana'
pessoa['sobrenome'] = 'Teste'


print(pessoa)

del pessoa['sobrenome']
print(pessoa)

pessoa[chave] = 'Maria'
print(pessoa[chave])

if pessoa.get('sobrenome') is None:
    print('Sem Sobrenome')
else:
    print(pessoa['sobrenome'])

