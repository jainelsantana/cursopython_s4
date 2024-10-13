#dir, hasattr e getattr em Python

string = 'Jainel'
metodo = 'lower'

if hasattr(string, metodo):
    print('Existe', metodo)
    print(getattr(string, metodo)())
else:
    print('Não exite o método', metodo)