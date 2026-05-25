from abc import ABC, abstractmethod


class Midia(ABC):
    def __init__(self, titulo: str, duracao: int) -> None:
        self.titulo = titulo
        self.duracao = duracao

    def mostrar_info(self) -> None:
        print(f"Titulo: {self.titulo} | Duracao: {self.duracao} min")

    @abstractmethod
    def reproduzir(self) -> None:
        pass


class Video(Midia):
    def __init__(self, titulo: str, duracao: int, resolucao: str) -> None:
        super().__init__(titulo, duracao)
        self.resolucao = resolucao

    def reproduzir(self) -> None:
        print(
            f"Reproduzindo video '{self.titulo}' em {self.resolucao} "
            f"({self.duracao} min)."
        )


class Podcast(Midia):
    def __init__(self, titulo: str, duracao: int, apresentador: str) -> None:
        super().__init__(titulo, duracao)
        self.apresentador = apresentador

    def reproduzir(self) -> None:
        print(
            f"Reproduzindo podcast '{self.titulo}' apresentado por "
            f"{self.apresentador} ({self.duracao} min)."
        )


class TextoNarrado(Midia):
    def __init__(self, titulo: str, duracao: int, idioma: str) -> None:
        super().__init__(titulo, duracao)
        self.idioma = idioma

    def reproduzir(self) -> None:
        print(
            f"Reproduzindo texto narrado '{self.titulo}' no idioma "
            f"{self.idioma} ({self.duracao} min)."
        )


class Plataforma:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.midias: list[Midia] = []

    def adicionar_midia(self, midia: Midia) -> None:
        self.midias.append(midia)

    def listar_midias(self) -> None:
        print(f"\nMidias na plataforma '{self.nome}':")
        if not self.midias:
            print("Nenhuma midia cadastrada.")
            return

        for indice, midia in enumerate(self.midias, start=1):
            print(f"{indice}.", end=" ")
            midia.mostrar_info()

    def reproduzir_todas(self) -> None:
        print(f"\nReproducao de todas as midias em '{self.nome}':")
        if not self.midias:
            print("Nenhuma midia para reproduzir.")
            return

        for midia in self.midias:
            midia.reproduzir()
