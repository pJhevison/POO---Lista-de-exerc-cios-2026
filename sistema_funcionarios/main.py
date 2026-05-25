from sistema_funcionarios import (
    Empresa,
    FuncionarioAssalariado,
    FuncionarioComissionado,
    FuncionarioHorista,
)


def main() -> None:
    empresa = Empresa("Tech Solucoes")

    assalariado = FuncionarioAssalariado("Carla Souza", "111.111.111-11", 4500.00)
    horista = FuncionarioHorista("Joao Lima", "222.222.222-22", 160, 28.50)
    comissionado = FuncionarioComissionado(
        "Marina Alves",
        "333.333.333-33",
        52000.00,
        4.0,
    )

    empresa.adicionar_funcionario(assalariado)
    empresa.adicionar_funcionario(horista)
    empresa.adicionar_funcionario(comissionado)

    empresa.listar_funcionarios()
    empresa.mostrar_folha_pagamento()


if __name__ == "__main__":
    main()
