from sys import path

import aula38_package.modulo
from aula38_package import modulo
from aula38_package.modulo import *

# from aula38_package.modulo import soma_do_modulo

# print(*path, sep='\n')
print(soma_do_modulo(1, 2))
print(aula38_package.modulo.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))
print(variavel)
print(nova_variavel)