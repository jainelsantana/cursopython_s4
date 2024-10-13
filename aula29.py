#Generator expression, Iterables e Iterators em Python

import sys

interable = ['Eu','Tenho', '__iter__']
iterator = iter(interable) #tem __inter__ e __next__
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

lista = [n for n in range(100000000)]
generator = (n for n in range(100000000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))


for n in generator:
    print (n)