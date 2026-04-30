# Método de classe usado como "construtor alternativo"
# Recebe a classe (cls) em vez da instância (self)
# Permite criar um objeto Pessoa com um nome padrão ("Anonima")
# Exemplo de uso: Pessoa.criaSemNome(20) → Pessoa('Anonima', 20)

class Pessoa:
    ano = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodoClasse(cls):
        print('Olá')

    @classmethod
    def criaSemNome(cls, idade):
        return cls('Anonima', idade)


p1 = Pessoa('Ana', 30)
p2 = Pessoa.criaSemNome(19)

print(Pessoa.ano)
Pessoa.metodoClasse()
print(p2.nome, p2.idade)