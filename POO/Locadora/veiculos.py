from fucoes import Locadora, Carro, Moto, Cliente

locadora = Locadora()

# Cadastrando a frota
carro1 = Carro('Gol', 'abc-123', 200, 2)
moto1 = Moto('Hornet', 'xyz-999', 150, 600)
locadora.InserirVeiculos(carro1)
locadora.InserirVeiculos(moto1)

# Criando perfis de clientes
ana = Cliente('Ana', 21)
pedro = Cliente('Pedro', 16) # Cliente menor de idade para testar a trava
locadora.InserirClientes(ana)
locadora.InserirClientes(pedro)

# 1. Testando locação bem-sucedida (Ana alugando o Gol por 5 dias)
locadora.processar_locacao(ana, carro1, dias=5)

# 2. Testando locação com erro de idade (Pedro tentando alugar a Hornet)
locadora.processar_locacao(pedro, moto1, dias=3)