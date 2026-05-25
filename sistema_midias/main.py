from sistema_midias import Plataforma, Podcast, TextoNarrado, Video


def main() -> None:
    plataforma = Plataforma("EducaPlay")

    video = Video("Introducao ao Polimorfismo", 18, "1080p")
    podcast = Podcast("POO em Debate", 35, "Ana Martins")
    texto_narrado = TextoNarrado("Guia de Classes Abstratas", 12, "Portugues")

    plataforma.adicionar_midia(video)
    plataforma.adicionar_midia(podcast)
    plataforma.adicionar_midia(texto_narrado)

    plataforma.listar_midias()
    plataforma.reproduzir_todas()


if __name__ == "__main__":
    main()
