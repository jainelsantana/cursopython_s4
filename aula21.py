def executa(funcao, *args):
    return funcao(*args)

def soma(x,y):
    return x+y

print('def executa soma', executa(soma, 1,2))
print('soma', soma(1,2))
print( 'lamnda', executa(lambda x, y: x + y, 1, 2))



def cria_multiplicador (multiplicador):
    def multiplica (numero):
        return numero * multiplicador
    return multiplica

# duplica = cria_multiplicador(2)

duplica = executa(lambda m: lambda n: n*m, 2)

print(duplica(9))

print( executa( lambda *args: sum(args), 1,2,3,4,5,6,7,8,9,10))