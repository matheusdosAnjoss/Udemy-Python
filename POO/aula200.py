class Pessoa:
    def __init__(self, nome="", idade= 0):
        self.nome = nome
        self.idade = idade

    def FazerAniversario(self):
        self.idade += 1
        print(f'A {self.nome} tinha {self.idade-1} e agora tem {self.idade} anos!')



p1 = Pessoa(nome='Ana', idade=21)
p1.FazerAniversario()
print()
p2 = Pessoa('Matheus', 28)
p2.FazerAniversario()