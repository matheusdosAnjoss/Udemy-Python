def ler_float(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('Por favor digite um número valido!')
            continue
        return n

while True:
    num01 = ler_float('Digite um número: ')
    num02 = ler_float('Digite outro numero: ')
    operador = input('Digite o operador (+-/*): ')

    operadores_permitidos = '+-/*'

    if len(operador) > 1:
        print('Operdor invalido')
        continue
    elif operador not in operadores_permitidos:
        print('ERRO: Digite apenas os operados + - * /')
        continue

    if operador == '+':
        print('='*15)
        soma = num01 + num02
        print(f'{num01} + {num02} = {soma:.2f}')
        print('='*15)
    
    elif operador == '-':
        print('='*15)
        soma = num01 - num02
        print(f'{num01} - {num02} = {soma:.2f}')
        print('='*15)

    elif operador == '*':
        print('='*15)
        soma = num01 * num02
        print(f'{num01} * {num02} = {soma:.2f}')
        print('='*15)

    elif operador == '/':
        print('='*15)
        soma = num01 / num02
        print(f'{num01} / {num02} = {soma:.2f}')
        print('='*15)

    sair = input('Quer Continuar? [S/N] ').lower().startswith('s')
    if sair == False:
        break

print('FIM DO PROGRAMA!')