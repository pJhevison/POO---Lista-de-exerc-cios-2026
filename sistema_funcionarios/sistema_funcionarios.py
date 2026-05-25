from abc import ABC, abstractmethod


class Funcionario(ABC):
    def __init__(self, nome: str, cpf: str) -> None:
        self.nome = nome
        self.cpf = cpf

    def mostrar_dados(self) -> None:
        print(f"Nome: {self.nome} | CPF: {self.cpf}")

    @abstractmethod
    def calcular_pagamento(self) -> float:
        pass


class FuncionarioAssalariado(Funcionario):
    def __init__(self, nome: str, cpf: str, salario_mensal: float) -> None:
        super().__init__(nome, cpf)
        self.salario_mensal = salario_mensal

    def calcular_pagamento(self) -> float:
        return self.salario_mensal


class FuncionarioHorista(Funcionario):
    def __init__(
        self,
        nome: str,
        cpf: str,
        horas_trabalhadas: float,
        valor_hora: float,
    ) -> None:
        super().__init__(nome, cpf)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcular_pagamento(self) -> float:
        return self.horas_trabalhadas * self.valor_hora


class FuncionarioComissionado(Funcionario):
    def __init__(
        self,
        nome: str,
        cpf: str,
        total_vendas: float,
        percentual_comissao: float,
    ) -> None:
        super().__init__(nome, cpf)
        self.total_vendas = total_vendas
        self.percentual_comissao = percentual_comissao

    def calcular_pagamento(self) -> float:
        return self.total_vendas * (self.percentual_comissao / 100)


class Empresa:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.funcionarios: list[Funcionario] = []

    def adicionar_funcionario(self, funcionario: Funcionario) -> None:
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self) -> None:
        print(f"\nFuncionarios da empresa '{self.nome}':")
        if not self.funcionarios:
            print("Nenhum funcionario cadastrado.")
            return

        for indice, funcionario in enumerate(self.funcionarios, start=1):
            print(f"{indice}.", end=" ")
            funcionario.mostrar_dados()

    def mostrar_folha_pagamento(self) -> None:
        print(f"\nFolha de pagamento - '{self.nome}':")
        if not self.funcionarios:
            print("Nenhum funcionario na folha de pagamento.")
            return

        total = 0.0
        for funcionario in self.funcionarios:
            pagamento = funcionario.calcular_pagamento()
            total += pagamento
            print(f"{funcionario.nome}: R$ {pagamento:.2f}")

        print(f"Total da folha: R$ {total:.2f}")
