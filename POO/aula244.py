from contextlib import contextmanager

@contextmanager
def myOpen(caminhoArquivo, modo):
    try:
        print('ABRINDO ARQUIVO')
        arquivo = open(caminhoArquivo, modo, encoding='utf8')
        yield arquivo
    except Exception as e:
        print(f'Ocorreu erro {e}')
    finally:
        print('fechando arquivo')
        arquivo.close()


with myOpen('aula244.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n', 1234)
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)