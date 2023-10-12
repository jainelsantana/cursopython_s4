"""
args -  Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento

# x, y, *resto = 1,2,3,4

# print(x, y, resto)


# def soma(x, y):
#     return x + y

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

soma_1_2_3 = soma(1,2,3)
#print(soma_1_2_3)
soma_4_5_6 = soma(4,5,6)
#print(soma_4_5_6)
soma_7_8_9 = soma(7,8,9)
#print(soma_7_8_9)

numeros=1,2,3,4,5,6,7,8,9,10,55,66,99,66
soma_=soma(*numeros)
soma_2 = sum(numeros)
print(soma_)
print(soma_2)
print(*numeros)


