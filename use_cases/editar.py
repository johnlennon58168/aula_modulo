from use_cases.buscar_por_codigo import buscarPorCodigo
from use_cases.adicionar import adicionarProduto
from repositorio import banco

def editarProduto(codigo, nome, categoria, preco):
    produto = buscarPorCodigo(codigo)
    if produto:
        produto['nome'] = nome
        produto['categoria'] = categoria
        produto['preco'] = preco

    else:
        print('Profuto não encontrado!')

if __name__ == '__main__':
    adicionarProduto('Mouse', 'Perfericos', 135.00)
    adicionarProduto('Monitor Philco', 'Monitores', 750.00)
    editarProduto(1, 'Mouse logitech', 'perifericos',150)
    print(banco)