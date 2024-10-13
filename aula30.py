# Introdução às Generator functions em Python
# enerator = (n for n in range(1000000))

def generator(n=0, maximum = 10):

    while True:
        yield n
        n +=1
        if n >= maximum:
            return
        
    # yield 1 #Pausar
    # print('Continuando...')
    # yield 2 #pausa
    # print('Continuando 2...')
    # yield 3 #pausa
    # print('Vou terminar')
    # return "Acabou"

gen = generator(maximum=100000)


# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for n in gen:
    print(n)



