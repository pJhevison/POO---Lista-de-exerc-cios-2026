from abc import ABC, abstractmethod


class Notificador(ABC):
    @abstractmethod
    def notificar(self, mensagem: str) -> None:
        pass


class NotificadorEmail(Notificador):
    def notificar(self, mensagem: str) -> None:
        print(f"[E-mail] Mensagem enviada: {mensagem}")


class NotificadorSMS(Notificador):
    def notificar(self, mensagem: str) -> None:
        print(f"[SMS] Mensagem enviada: {mensagem}")


class NotificadorApp(Notificador):
    def notificar(self, mensagem: str) -> None:
        print(f"[App] Notificacao enviada: {mensagem}")


class CentralNotificacoes:
    def __init__(self) -> None:
        self.notificadores: list[Notificador] = []

    def adicionar_notificador(self, notificador: Notificador) -> None:
        self.notificadores.append(notificador)

    def enviar_para_todos(self, mensagem: str) -> None:
        if not self.notificadores:
            print("Nenhum notificador cadastrado.")
            return

        for notificador in self.notificadores:
            notificador.notificar(mensagem)
