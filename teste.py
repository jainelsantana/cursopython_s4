import copy

# Lista de produtos original
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Aumentar os preços dos produtos em 10%
for produto in produtos:
    produto['preco'] *= 1.1

# Exibir os produtos com os preços atualizados
print("Produtos com preços atualizados:")
for produto in produtos:
    print(produto)

# Lista para armazenar novos produtos
novos_produtos = []

# Adicionar novos produtos
while True:
    novo_item = input('Digite o nome do novo produto ou "stop" para terminar de adicionar: ')

    if novo_item.lower() == 'stop':
        break

    preco_novo = float(input("Digite o preço do novo produto: "))
    novo_produto = {'nome': novo_item, 'preco': preco_novo}
    novos_produtos.append(novo_produto)

    # Gerar novos produtos por cópia profundabb
    produtos_copia = copy.deepcopy(produtos)

    # Adicionar novo produto à cópia profunda
    produtos_copia.extend(novos_produtos)

    # Ordenar a lista de produtos baseada nos preços, do maior para o menor
    produtos_copia_ordenados = sorted(produtos_copia, key=lambda x: x['preco'], reverse=True)

    # Exibir a lista de produtos atualizada
    print('Lista de produtos atualizada:')
    for idx, produto in enumerate(produtos_copia_ordenados, start=1):
        print(f"{idx}. Nome: {produto['nome']}, Preço: {produto['preco']:.2f}")

#validvsdcsdfyjgl 