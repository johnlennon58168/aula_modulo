from repositorio import banco
from use_cases.adicionar import adicionarProduto
def buscarPorCodigo(codigo: int) -> dict or None:
    for produto in banco:
        if produto['codigo'] == codigo:
            return True
    return None


if __name__ == '__main__':
  adicionarProduto('Mouse', 'Perfericos', 135.00)
  adicionarProduto('Monitor Philco', 'Monitores', 750.00)
  print(buscarPorCodigo(1))
  print(buscarPorCodigo(99))
