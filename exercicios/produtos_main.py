import copy
from dados import produtos

def mostra(lista, titulo):
    print(titulo)
    for p in lista:
        print(p)
    print()

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
] 

produtosOrdenados = sorted(
    copy.deepcopy(produtos),
    key=lambda x: x['nome'], reverse=True
)

produtosOrdenadosPreco = sorted(
    copy.deepcopy(produtos),
    key=lambda x: x['preco'], reverse=False
)

mostra(produtos, 'Produtos Originais')
mostra(novos_produtos, 'COM AUMENTO')
mostra(produtosOrdenados, 'ORDENADOS POR NOME')
mostra(produtosOrdenadosPreco, 'ORDENADOS POR PREÇO')


#produtos.sort(key=lambda x: x['nome'], reverse=True)
#produtos.sort(key=lambda n: n['preco'], reverse=True)

#produtos.linha()
#for item in produtos:
#    aumentarPreco = (item['preco'] * 10 ) / 100
#    item['preco'] += aumentarPreco
#    print(f'{item['nome']}: {item['preco']:.2f}')
#produtos.linha()