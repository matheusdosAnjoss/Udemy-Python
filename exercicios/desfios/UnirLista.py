def zipper(lista1, lista2):
    
    res = list(zip(lista1, lista2))
    return res

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

print(zipper(cidades, estados))


#print(res)
#for v in res:
#    print(v)