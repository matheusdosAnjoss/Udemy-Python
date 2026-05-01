class CarrinhoCompras:
    def __init__(self):
        self._produtos = []

    
    def total(self):
        return sum([p.preco for p in self._produtos])
    
    def inserirProdutos(self, *produtos):
        for p in produtos:
            self._produtos.append(p)
    
    def lista_produtos(self):
        print()
        for p in self._produtos:
            print(p.nome, p.preco)


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        

carrinho = CarrinhoCompras()

p1, p2 = Produto('arroz', 10), Produto('Camiseta', 29.20)
carrinho.inserirProdutos(p1, p2)
carrinho.lista_produtos()
print(carrinho.total())

