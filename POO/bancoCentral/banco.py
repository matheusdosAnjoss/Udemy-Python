from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, numero, saldo=0):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f'Deposito de R${valor:.2f}. Realizado com sucesso! Saldo atual: R${self.saldo:.2f}')

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaCorrente(Conta):
    def __init__(self, agencia, numero, saldo=0, limite= 500):
        super().__init__(agencia, numero, saldo)
        self.limite = limite

    def sacar(self, valor):
        valor_disponivel = self.saldo + self.limite

        if valor <= valor_disponivel:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} realizado. Saldo: R${self.saldo:.2f}')
            return True
        print('Saque negado! limite insuficiente.')
        return False
    

class ContaPopanca(Conta):
    def __init__(self, agencia, numero, saldo=0):
        super().__init__(agencia, numero, saldo)

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} realizado. Saldo: R${self.saldo:.2f}')
            return True
        print('Saque negado! limite insuficiente.')
        return False


class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None # Será associada depois


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
            return False
        if conta not in self.contas:
            return False
        if conta.agencia not in self.agencias:
            return False
        
        return True


itau = Banco()

matheus = Cliente('Matheus', 21) # Criamos o avatar do matheus.
minha_conta = ContaCorrente(1111, 54, 300, 500) # Criamos um cartão de Conta Corrente pra ele.
matheus.conta = minha_conta # Entregamos o "cartão" na mão do Matheus.

itau.inserirClientes(matheus) # Cadastramos o Matheus no sistema do banco.
itau.inserirConta(minha_conta) # Cadastramos a conta dele no sistema.

# O Thiago vai até o caixa eletrônico:
if itau.autenticar(matheus, minha_conta): # O banco checa os documentos.
    matheus.conta.depositar(100)
    matheus.conta.sacar(200)
    matheus.conta.sacar(100)
else:
    print("Erro de autenticação bancária.")