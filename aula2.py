"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z):
    #definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z =', x + y + z)


#não nomeado
soma(1,2,3)

#argumentos nomeadas
soma(x=1, y=2, z=5)




