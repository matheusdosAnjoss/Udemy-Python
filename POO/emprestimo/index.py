from datetime import datetime
from dateutil.relativedelta import relativedelta


valorTotal = 1000000
dataEmprestimo = datetime(2020, 12, 20)
deltaAnos = relativedelta(years=5)
dataFinal = dataEmprestimo + deltaAnos

dataParcelas = []
dataParcela = dataEmprestimo

while dataParcela < dataFinal:
    dataParcelas.append(dataParcela)
    dataParcela += relativedelta(months=+1)

numParcelas = len(dataParcelas)
valorParcela = valorTotal / numParcelas

for data in dataParcelas:
    print(data.strftime('%d/%m/%Y'), f'R${valorParcela:.2f}')

print()
print(
    f'Voce pegou R${valorTotal:.2f} para pagar'
    f'em {deltaAnos.years} anos'
    f'({numParcelas} meses) em parcelas de R${valorParcela:.2f}'
)



