from typing import Protocol


class Imprimivel(Protocol):
    def imprimir(self) -> None:
        ...


class Boleto:
    def __init__(self, codigo: str, valor: float) -> None:
        self.codigo = codigo
        self.valor = valor

    def imprimir(self) -> None:
        print(f"Boleto | Codigo: {self.codigo} | Valor: R$ {self.valor:.2f}")


class Etiqueta:
    def __init__(self, destinatario: str, endereco: str) -> None:
        self.destinatario = destinatario
        self.endereco = endereco

    def imprimir(self) -> None:
        print(
            f"Etiqueta | Destinatario: {self.destinatario} | "
            f"Endereco: {self.endereco}"
        )


class RelatorioSimples:
    def __init__(self, titulo: str) -> None:
        self.titulo = titulo

    def imprimir(self) -> None:
        print(f"Relatorio Simples | Titulo: {self.titulo}")


def processar_impressao(item: Imprimivel) -> None:
    item.imprimir()
