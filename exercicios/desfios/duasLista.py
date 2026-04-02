lista1 = [10, 20, 30]
lista2 = [5, 5, 5, 50, 100]

list_soma = [x + y for x, y in zip(lista1, lista2)]

print(list_soma)