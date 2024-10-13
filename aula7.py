# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.
def multiplicador(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

print(f'total teste {1*2*3*4*5*6}')

multip= multiplicador(1,2,3,4,5,6)
print(multip)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def impar(numero):
    multiplo_dois = numero % 2 == 0

    if multiplo_dois:
        return f'{numero} par'
    return f'{numero} impar'
        
resultado = impar(2)
print(resultado)
        

    