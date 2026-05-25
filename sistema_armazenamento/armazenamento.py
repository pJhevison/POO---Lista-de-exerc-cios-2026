from abc import ABC, abstractmethod
from typing import Protocol


class Armazenador(ABC):
    @abstractmethod
    def salvar(self, dado: str) -> None:
        pass


class ArmazenadorArquivo(Armazenador):
    def salvar(self, dado: str) -> None:
        print(f"[Arquivo] Dado salvo localmente: {dado}")


class ArmazenadorBanco(Armazenador):
    def salvar(self, dado: str) -> None:
        print(f"[Banco] Dado salvo no banco de dados: {dado}")


class Salvavel(Protocol):
    def salvar(self, dado: str) -> None:
        ...


class ArmazenadorNuvem:
    def salvar(self, dado: str) -> None:
        print(f"[Nuvem] Dado salvo na nuvem: {dado}")


def executar_salvamento_formal(armazenador: Armazenador, dado: str) -> None:
    armazenador.salvar(dado)


def executar_salvamento_flexivel(objeto: Salvavel, dado: str) -> None:
    objeto.salvar(dado)
