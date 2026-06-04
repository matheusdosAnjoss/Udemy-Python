from pathlib import Path
import csv

CAMINHO_CSV = Path(__file__).parent / 'aula296.csv'

with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)
    #next(leitor)

    for linha in leitor:
        print(linha)