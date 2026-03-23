def generator(n=0):
    yield 1  #pausar
    print('Continuando...')
    yield 2 # Pausar
    print('Mais uma...')
    yield 3 # Pausar


gen = generator(n=0)

for n in gen:
    print(n)