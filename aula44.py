# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açúcar sintático)

def criar_funcao(func):
    def interna(*args,**kwargs):
        print("Vou te decorar")
        for arg in args:
            is_string(arg)
        resultado = func(*args,**kwargs)
        print(f'O resultado foi {resultado}')
        print ("OK, agora você foi decorado")
        return resultado
    return interna

@criar_funcao
def inverte_string(string):
       return string[::-1]


def is_string(param):
    if not isinstance(param, str):
          raise TypeError ("param deve ser uma string")
    ...

#inverte_string_checando_paramentro = criar_funcao(inverte_string)
invertida = inverte_string("123")
print(invertida)