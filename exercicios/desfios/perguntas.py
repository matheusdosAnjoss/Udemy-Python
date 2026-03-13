from rich import print
pergurtas = [
    {
        'pergunta': 'Quantos é 2+2? ',
        'opcoes': ['1','3','4','5'],
        'resposta': 4,
    },

    {
        'pergunta': 'Quantos é 5*5? ',
        'opcoes': ['25','30','40','50'],
        'resposta': 25,
    },

    {
        'pergunta': 'Quantos é 10/2? ',
        'opcoes': ['4','5','2','1'],
        'resposta': 5,
    }
]

acertou = 0
errou = 0

for p in pergurtas:
    print(p['pergunta'])

    print('Opções:')
    for chave, valor in enumerate(p['opcoes']):
        print(f'{chave}) {valor}')
    
    while True:
        try:
            resposta = int(input('Escolha uma opção: '))

            if resposta == p['resposta']:
                acertou += 1
                print('=='*10)
                print("[green]Você acertou 👏👍")
                print('=='*10)
                break
            else:
                errou += 1
                print('=='*10)
                print('[red]ERROU!')
                print('=='*10)
                break
        except ValueError:
            print('Digite apenas o numero da opcao')

if acertou >= 1:
    print(f'Parabens você acertou {acertou} perguntas! 🥳')
else:
    print('[red]Você Errou todas as perguntas tente novamente!')