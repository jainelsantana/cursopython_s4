#Try, except, else e finally

try:
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError:
    print('dividiu por zero')

else:
    print('Não deu erro')

finally:
    print('Fecha arquivo')
 