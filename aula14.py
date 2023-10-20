# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
#import copy
import copy

d1 = {
    'c1':1,
    'c2':2,
    'l1':[0,2,3],
}

#d2=d1.copy()

d2=copy.deepcopy(d1)


d2['c1']=1000
d2['l1'][1] =99999
print(d1)
print(d2)