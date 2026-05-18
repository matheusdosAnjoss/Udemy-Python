from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, modelo, placa, valor_diaria):
        self.modelo = modelo
        self.placa = placa
        self.valor_diaria = valor_diaria


    @abstractmethod
    def calcular_aluguel(dias):
        pass


class Carro(Veiculo):
    def __init__(self, modelo, placa, valor_diaria, capacidade_malas):
        super().__init__(modelo, placa, valor_diaria)
        self.capacidade_malas = capacidade_malas

    def calcular_aluguel(self, dias):
        calculo = dias * self.valor_diaria
        return calculo


class Moto(Veiculo):
    def __init__(self, modelo, placa, valor_diaria, cilindrada):
        super().__init__(modelo, placa, valor_diaria)
        self.cilindrada = cilindrada
        self.taxa = 50

    def calcular_aluguel(self, dias):
        valor_total = dias * self.valor_diaria
        if self.cilindrada > 250:
            valor_total += self.taxa
            return valor_total
    


class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Cliente(Pessoa):
    def __init__(self, nome, idade, ):
        super().__init__(nome, idade)
        self.veiculo_alugado = None


class Locadora():
    def __init__(self):
        self.veiculos_disponivel = []
        self.cliente_cadastrado = []

    def InserirVeiculos(self, veiculos):
        self.veiculos_disponivel.append(veiculos)

    def InserirClientes(self, clientes):
        self.cliente_cadastrado.append(clientes)

    def autenticar_locacao(self, cliente, veiculo):
        if cliente not in self.cliente_cadastrado:
            print(f'ERRO: Cliente {cliente.nome} não está cadastrado na locadora.')
            return False
        if veiculo not in self.veiculos_disponivel:
            print(f'ERRO: Veiculo {veiculo.modelo} não está cadastrado na locadora.')
            return False
        if cliente.idade < 18:
            print(f'ERRO: Cliente {cliente.nome} tem {cliente.idade} anos não tem permisão para dirigir.')
            return False
        
        return True