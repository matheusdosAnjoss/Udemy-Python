#METODOS DE INSTANCIAS DE CLASSES PYTHON
class Carro:
    def __init__(self, nome=""):
        self.nome = nome

    def acelerar(self):  #INSTANCIA
        print(f'{self.nome} esta acelerando!')


c1 = Carro('Fusca')
c1.acelerar()

c2 = Carro('Gol')
c2.acelerar()