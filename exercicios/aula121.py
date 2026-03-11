pessoas = dict()

pessoas['nome'] = 'Matheus'
pessoas['sobrenome'] = 'Oliveira'

if pessoas.get("nome") is None:
    print('Não existe')
else:
    print(pessoas['nome'])


for n in pessoas.values():
    print(f'{n}')

print('=='*10)
for chave, valor in  pessoas.items():
    print(f'{chave} - {valor}')