from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool:
        pass


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print(f'Email: enviando - {self.mensagem}')
        return True


class NotificacaoSms(Notificacao):
    def enviar(self) -> bool:
        print(f'SMS: enviando - {self.mensagem}')
        return False


def notificar(notificacao: Notificacao):
    notificacaoEnviada = notificacao.enviar()

    if notificacaoEnviada:
        print('Notificação envida')
    else:
        print('Notificação NÂO enviada')


n1 = NotificacaoEmail('Mensagem enviada')
n2 = NotificacaoSms('Testando notificacao')

# n1.enviar()
# n2.enviar()
notificar(NotificacaoEmail('testando email'))