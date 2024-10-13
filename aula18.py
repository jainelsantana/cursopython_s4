# Exemplo de uso de sets

letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra)

    if 'l' in letra:
        print('Parabéns')
        break

    print(letras,type(letras))