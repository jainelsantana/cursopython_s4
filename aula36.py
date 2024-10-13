# Entendento os seus prórios módulos Python 
# O Primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O Python conhece a pasta onde__main__ está e as pastas abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por padrão
# O Python conhece todos os módulos e pacotes presentes nos caminhos sys.path
# try:
#     import sys
#    # sys.path.append('/home/jainel/Desktop')
# except ModuleNotFoundError:
#     ...
import aula36_m
from aula36_m import variavel_modulo, soma
# #import modulo_py
# print ('Esté módulo se chama', __name__)

# print(*sys.path, sep='\n')
print('Este módulo se chama',__name__)
print(aula36_m.variavel_modulo)
print(variavel_modulo)
print(soma(2, 3))
print(aula36_m.soma(5, 3))

