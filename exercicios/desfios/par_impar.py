def ParImpar():
    while True:
        try:
            n = int(input('Digite um numero: '))
            if n % 2 == 0:
                return 'Par'
            else:
                return 'Impar'
            
        except TypeError, ValueError:
            print('Digite apenas numeros inteiros')
            continue
        
            
    

print(ParImpar())

