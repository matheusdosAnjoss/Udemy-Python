# Definindo a classe que vai criar os nossos carros
class Carro:
    def __init__(self, nome):
        self.nome = nome        # Nome público do carro (ex: "Ferrari")
        self._motor = None      # Atributo "privado" (o _ avisa: não mexa aqui direto!)
        self._fabricante = None # Começa como None porque o carro nasce sem motor/fábrica

    # O "Getter": Permite que a gente veja o motor com 'carro.motor'
    @property
    def motor(self):
        return self._motor
    
    # O "Setter": Permite que a gente instale um motor com 'carro.motor = valor'
    @motor.setter
    def motor(self, valor):
        self._motor = valor 


    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


gol = Carro('gol')
motorGol = Motor('ea111')
volks = Fabricante('volks')
gol.fabricante = volks
gol.motor = motorGol
print(gol.nome, gol.fabricante.nome, gol.motor.nome)

print()

fusca = Carro('fusca')
motor_1_0 = Motor('1.0')
volks = Fabricante('volks')
fusca.motor = motor_1_0
fusca.fabricante = volks
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)