#Try, except, else e finally
# a = 18

# b = 0 
# c= a/b
# b = 0   
# print(b[0])

try:
    a = 18
    b = 0   
    #print(b[0])
    #print('Linha 1'[10000])
    c= a/b
    print('Linha 2')


except ZeroDivisionError as e:
    print(e)
    print()
    print(e.__class__.__name__)
except NameError:
    print('b não está definido')
except (TypeError, IndexError) as error:
    print('TypeError, IndexError')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)


except Exception:
    print('Erro desconhecido')


print('Continuar')