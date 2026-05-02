class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.endereco = []


    def inserirEndereco(self, rua, num):
        self.endereco.append(Endereco(rua, num))

    def listaEndereco(self):
        for e in self.endereco:
            print(e.rua, e.num)


class Endereco:
    def __init__(self, rua, num):
        self.rua = rua
        self.num = num
        

cliente1 = Cliente("Ana")
cliente1.inserirEndereco('av. brasil', 54)


cliente2 = Cliente("João")
cliente2.inserirEndereco('R.tucano', 129)

cliente1.listaEndereco()
cliente2.listaEndereco()
