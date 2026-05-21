from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


p1 = Pessoa('Matheus', 'Oliveira')

print(p1.nome_completo())