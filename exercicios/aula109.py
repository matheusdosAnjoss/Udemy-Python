def soma(*args):
    total = 0
    for n in args:
        total += n
    return total
        
var_soma = soma(4,6,3)
print(var_soma)


var_soma1 = soma(40,6,30)
print(var_soma1)