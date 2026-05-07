from log import LogPrintMixin, LogFileMixin

class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True

    def desligar(self):
        if self._ligado:
            self._ligado = False


class Smartphone(Eletronico, LogFileMixin):
    def ligar(self):
        super().ligar()

        if self._ligado:
            msg = f'{self,self._nome} esta ligado'
            self.log_success(msg)

    def desligar(self):
        super().desligar()

        if not self._ligado:
            msg = f'{self,self._nome} esta desligado'
            self.log_success(msg)



galaxyS = Smartphone('galaxy s')
iphone = Smartphone('iphone')
iphone.ligar()
iphone.desligar()