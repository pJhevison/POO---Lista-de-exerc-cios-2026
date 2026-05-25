from notificacoes import (
    CentralNotificacoes,
    NotificadorApp,
    NotificadorEmail,
    NotificadorSMS,
)


def main() -> None:
    central = CentralNotificacoes()

    notificador_email = NotificadorEmail()
    notificador_sms = NotificadorSMS()
    notificador_app = NotificadorApp()

    central.adicionar_notificador(notificador_email)
    central.adicionar_notificador(notificador_sms)
    central.adicionar_notificador(notificador_app)

    central.enviar_para_todos("Aula nova liberada na plataforma.")


if __name__ == "__main__":
    main()
