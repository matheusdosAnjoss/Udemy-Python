def mult(*args):
    tot = 1
    for n in args: 
        tot *= n
    return tot

var_soma = mult(1,2,3,4,5)
print(var_soma)
