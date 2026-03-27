def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

def criarFuncao(funcao, *args):
    return lambda *novos_args: funcao(*args, *novos_args)

# criarFuncao = fábrica de funções
# *args = argumentos fixos (iniciais)
# *novos_args = argumentos passados depois
# lambda = função criada dinamicamente
# closure = a função lembra dos valores antigos

somaComCinco = criarFuncao(soma, 5)
print(somaComCinco(10))

multiplicaPorDez = criarFuncao(multiplica, 10)
print(multiplicaPorDez(10))