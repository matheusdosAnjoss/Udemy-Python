import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula297.csv'

lista_clientes = [
    { 'Matheus','Rua joao de barro'},
    { 'Ana','AV. 1'},
    { 'Carlos','R.jose'}
]

with open(CAMINHO_CSV, 'w') as arquivo:
    #colunas = lista_clientes[0].keys()
    colunas = ['Nome', 'Endereco']
    escritor = csv.writer(arquivo)

    escritor.writerow(colunas)

    for cliente in lista_clientes:
        escritor.writerow(cliente)