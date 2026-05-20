# from abc import ABC, abstractmethod

# class Veiculo(ABC):
#     def __init__(self, modelo, placa, valor_diaria):
#         self.modelo = modelo
#         self.placa = placa
#         self.valor_diaria = valor_diaria


#     @abstractmethod
#     def calcular_aluguel(dias):
#         pass


# class Carro(Veiculo):
#     def __init__(self, modelo, placa, valor_diaria, capacidade_malas):
#         super().__init__(modelo, placa, valor_diaria)
#         self.capacidade_malas = capacidade_malas

#     def calcular_aluguel(self, dias):
#         calculo = dias * self.valor_diaria
#         return calculo


# class Moto(Veiculo):
#     def __init__(self, modelo, placa, valor_diaria, cilindrada):
#         super().__init__(modelo, placa, valor_diaria)
#         self.cilindrada = cilindrada
#         self.taxa = 50

#     def calcular_aluguel(self, dias):
#         valor_total = dias * self.valor_diaria
#         if self.cilindrada > 250:
#             valor_total += self.taxa
#             return valor_total
    


# class Pessoa(ABC):
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

# class Cliente(Pessoa):
#     def __init__(self, nome, idade, ):
#         super().__init__(nome, idade)
#         self.veiculo_alugado = None


# class Locadora():
#     def __init__(self):
#         self.veiculos_disponivel = []
#         self.cliente_cadastrado = []

#     def InserirVeiculos(self, veiculos):
#         self.veiculos_disponivel.append(veiculos)

#     def InserirClientes(self, clientes):
#         self.cliente_cadastrado.append(clientes)

#     def autenticar_locacao(self, cliente, veiculo):
#         if cliente not in self.cliente_cadastrado:
#             print(f'ERRO: Cliente {cliente.nome} não está cadastrado na locadora.')
#             return False
#         if veiculo not in self.veiculos_disponivel:
#             print(f'ERRO: Veiculo {veiculo.modelo} não está cadastrado na locadora.')
#             return False
#         if cliente.idade < 18:
#             print(f'ERRO: Cliente {cliente.nome} tem {cliente.idade} anos não tem permisão para dirigir.')
#             return False
        
#         return True
from abc import ABC, abstractmethod
# Importando os componentes do Rich
from rich.console import Console
from rich.panel import Panel

# Inicializando o console global para renderizar as saídas estilizadas
console = Console()

class Veiculo(ABC):
    def __init__(self, modelo, placa, valor_diaria):
        self.modelo = modelo.upper()
        self.placa = placa.upper()
        self.valor_diaria = valor_diaria

    @abstractmethod
    def calcular_aluguel(self, dias):  # Adicionado 'self' que faltava aqui
        pass


class Carro(Veiculo):
    def __init__(self, modelo, placa, valor_diaria, capacidade_malas):
        super().__init__(modelo, placa, valor_diaria)
        self.capacidade_malas = capacidade_malas

    def calcular_aluguel(self, dias):
        return dias * self.valor_diaria


class Moto(Veiculo):
    def __init__(self, modelo, placa, valor_diaria, cilindrada):
        super().__init__(modelo, placa, valor_diaria)
        self.cilindrada = cilindrada
        self.taxa = 50

    def calcular_aluguel(self, dias):
        valor_total = dias * self.valor_diaria
        if self.cilindrada > 250:
            valor_total += self.taxa
        return valor_total  # Ajustado para retornar o valor mesmo se for <= 250cc


class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.veiculo_alugado = None


class Locadora:
    def __init__(self):
        self.veiculos_disponiveis = []  # Corrigido o plural de 'veiculos_disponivel'
        self.clientes_cadastrados = []  # Corrigido o plural de 'cliente_cadastrado'

    def InserirVeiculos(self, veiculo):
        self.veiculos_disponiveis.append(veiculo)

    def InserirClientes(self, cliente):
        self.clientes_cadastrados.append(cliente)

    def autenticar_locacao(self, cliente, veiculo):
        if cliente not in self.clientes_cadastrados:
            console.print(Panel(
                f"O cliente [bold]{cliente.nome}[/] não foi encontrado no sistema.",
                title="[bold red]ERRO: CLIENTE NÃO CADASTRADO[/]",
                border_style="red",
                expand=False
            ))
            return False
            
        if veiculo not in self.veiculos_disponiveis:
            console.print(Panel(
                f"O veículo [bold]{veiculo.modelo}[/] ({veiculo.placa}) não pertence à nossa frota.",
                title="[bold red]ERRO: VEÍCULO NÃO ENCONTRADO[/]",
                border_style="red",
                expand=False
            ))
            return False
            
        if cliente.idade < 18:
            console.print(Panel(
                f"Cliente [bold]{cliente.nome}[/] tem apenas [yellow]{cliente.idade} anos[/].\nLocação permitida apenas para maiores de 18 anos.",
                title="[bold red]ERRO: IDADE INSUFICIENTE[/]",
                border_style="red",
                expand=False
            ))
            return False
        
        # Se passar por todas as validações, exibe o painel de sucesso de autenticação
        console.print(Panel(
            f"Verificação de perfil concluída com sucesso para [bold green]{cliente.nome}[/].",
            title="[bold green]AUTENTICAÇÃO APROVADA[/]",
            border_style="green",
            expand=False
        ))
        return True

    def processar_locacao(self, cliente, veiculo, dias):
        """Método auxiliar para encapsular a regra de negócio do aluguel de forma elegante."""
        if self.autenticar_locacao(cliente, veiculo):
            cliente.veiculo_alugado = veiculo
            custo_total = veiculo.calcular_aluguel(dias)
            
            console.print(Panel(
                f"Veículo: [bold blue]{veiculo.modelo}[/]\n"
                f"Placa: [bold]{veiculo.placa}[/]\n"
                f"Período: [bold]{dias} dias[/]\n"
                f"Total a pagar: [bold green]R${custo_total:.2f}[/]",
                title=f"[bold green]CONTRATO DE LOCAÇÃO - {cliente.nome.upper()}[/]",
                border_style="green",
                expand=False
            ))
        else:
            console.print(Panel(
                f"Não foi possível emitir o contrato de locação para [bold]{cliente.nome}[/].",
                title="[bold red]LOCAÇÃO NEGADA[/]",
                border_style="bold red",
                expand=False
            ))
