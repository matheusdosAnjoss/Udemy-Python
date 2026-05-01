

# class Foo:
#     def __init__(self):
#         self.public = 'isso e publico'
#         self._protected = 'isso é protegido'

#     def metodoPublico(self):
#         self._medoto_protegido()
#         return 'metodo publico'
    
#     def _medoto_protegido(self):
#         print('_medoto protegido')
#         return '_medoto_protegido'
    

# f = Foo()

# #print(f._protected)
# print(f.metodoPublico())

class Robo:
    def __init__(self):
        self._pilha = 0  # Começa sem pilha

    # O OLHINHO (Property) - para ler o valor
    @property
    def pilha(self):
        print("Robô: Estou verificando quanta energia eu tenho...")
        return f"{self._pilha}%"

    # O SEGURANÇA (Setter) - para mudar o valor com cuidado
    @pilha.setter
    def pilha(self, valor):
        if valor < 0:
            print("Segurança: Ei! Você não pode tirar energia que não existe!")
        elif valor > 100:
            print("Segurança: Cuidado! Muita pilha vai me explodir!")
        else:
            print(f"Segurança: {valor}% de pilha? OK, pode colocar!")
            self._pilha = valor

# --- Brincando com o Robô ---

meu_robo = Robo()

# Usando o SETTER para colocar 50% de pilha
meu_robo.pilha = 50 

# Usando a PROPERTY para ver quanta pilha tem
print(meu_robo.pilha) 

# Tentando fazer algo errado (o segurança vai barrar!)
meu_robo.pilha = 999 
