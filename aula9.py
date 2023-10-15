"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


fala_bomdia = criar_saudacao('Bom dia')
falar_boanoite = criar_saudacao('Boa noite')

for nome in ['Maria Jose', 'Jainel', 'Miguel', 'Jadson']:
    print(fala_bomdia(nome))
    print(falar_boanoite(nome))