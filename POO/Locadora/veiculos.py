from fucoes import Carro, Cliente, Locadora

locadora = Locadora()

carro1 = Carro('gol', 'abc-123', 200, 2)
locadora.InserirVeiculos(carro1)

cliente1 = Cliente('Ana', 21)
locadora.InserirClientes(cliente1)

if locadora.autenticar_locacao(cliente1, carro1):
    cliente1.veiculo_alugado = carro1
    print(f'Locação autorizada para {cliente1.nome}!')
else:
    print('Locação negada!')