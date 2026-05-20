from abc import ABC, abstractmethod
# Importando as ferramentas do Rich
from rich.console import Console
from rich.panel import Panel

# Criamos o console que vai renderizar os painéis bonitões
console = Console()

class Conta(ABC):
    def __init__(self, agencia, numero, saldo=0):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        # Usando Panel com borda verde e título para sucesso
        console.print(Panel(
            f"Depósito de [bold green]R${valor:.2f}[/] realizado com sucesso!\n[bold]Saldo atual:[/] R${self.saldo:.2f}",
            title="[bold green]DEPÓSITO[/]",
            border_style="green",
            expand=False
        ))

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaCorrente(Conta):
    def __init__(self, agencia, numero, saldo=0, limite=500):
        super().__init__(agencia, numero, saldo)
        self.limite = limite

    def sacar(self, valor):
        valor_disponivel = self.saldo + self.limite

        if valor <= valor_disponivel:
            self.saldo -= valor
            console.print(Panel(
                f"Saque de [bold blue]R${valor:.2f}[/] realizado.\n[bold]Saldo atual:[/] R${self.saldo:.2f}",
                title="[bold blue]SAQUE - CONTA CORRENTE[/]",
                border_style="blue",
                expand=False
            ))
            return True
        
        console.print(Panel(
            f"[bold red]Saque de R${valor:.2f} negado![/]\nMotivo: Limite insuficiente.",
            title="[bold red]ERRO DE OPERAÇÃO[/]",
            border_style="red",
            expand=False
        ))
        return False
    

class ContaPoupanca(Conta):  # Corrigido o nome de ContaPopanca para ContaPoupanca
    def __init__(self, agencia, numero, saldo=0):
        super().__init__(agencia, numero, saldo)

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            console.print(Panel(
                f"Saque de [bold blue]R${valor:.2f}[/] realizado.\n[bold]Saldo atual:[/] R${self.saldo:.2f}",
                title="[bold blue]SAQUE - POUPANÇA[/]",
                border_style="blue",
                expand=False
            ))
            return True
        
        console.print(Panel(
            f"[bold red]Saque de R${valor:.2f} negado![/]\nMotivo: Saldo insuficiente.",
            title="[bold red]ERRO DE OPERAÇÃO[/]",
            border_style="red",
            expand=False
        ))
        return False


class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None


class Banco:
    def __init__(self):
        self.agencias = [1111, 2222, 3333]
        self.clientes = []
        self.contas = []

    def inserirClientes(self, cliente):
        self.clientes.append(cliente)

    def inserirConta(self, conta):
        self.contas.append(conta)

    def autenticar(self, cliente, conta):
        if cliente not in self.clientes:
            console.print(Panel(f"Cliente [bold]{cliente.nome}[/] não está cadastrado no Banco.", title="[bold red]ERRO DE AUTENTICAÇÃO[/]", border_style="red", expand=False))
            return False
        if conta not in self.contas:
            console.print(Panel("Conta não cadastrada neste banco.", title="[bold red]ERRO DE AUTENTICAÇÃO[/]", border_style="red", expand=False))
            return False
        if conta.agencia not in self.agencias:
            console.print(Panel(f"Agência [bold]{conta.agencia}[/] inválida ou não cadastrada.", title="[bold red]ERRO DE AUTENTICAÇÃO[/]", border_style="red", expand=False))
            return False
        
        # Painel bonito para quando o login dá certo
        console.print(Panel(
            f"Bem-vindo(a), [bold]{cliente.nome}[/]!\nAgência: {conta.agencia} | Conta: {conta.numero}",
            title="[bold green]ACESSO PERMITIDO[/]",
            border_style="green",
            expand=False
        ))
        return True


# --- Testando o Sistema ---

itau = Banco()

matheus = Cliente('Matheus', 21) # Criamos o avatar do matheus.
minha_conta = ContaCorrente(1111, 54, 300, 500) # Criamos um cartão de Conta Corrente pra ele.
matheus.conta = minha_conta # Entregamos o "cartão" na mão do Matheus.

ana = Cliente('Ana', 30)
itau.inserirClientes(ana)
ana_conta = ContaCorrente(2222, 54, 1000)
itau.inserirConta(ana_conta)
ana.conta = ana_conta

itau.inserirClientes(matheus) # Cadastramos o Matheus no sistema do banco.
itau.inserirConta(minha_conta) # Cadastramos a conta dele no sistema.

# O Thiago vai até o caixa eletrônico:
if itau.autenticar(ana, ana_conta): # O banco checa os documentos.
    ana.conta.depositar(500)
    ana.conta.sacar(200)
    ana.conta.sacar(2000)
else:
    console.print(Panel("Erro crítico de autenticação bancária.", border_style="bold red"))