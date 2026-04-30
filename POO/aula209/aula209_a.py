import json

CAMINHO_ARQUIVO = 'aula209.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade



p1 = Pessoa('João', 20)
p2 = Pessoa('Ana', 18)
p3 = Pessoa('Maria', 30)

li = [vars(p1), vars(p2), vars(p3)]

with open(CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(li, arquivo, ensure_ascii=False, indent=2)