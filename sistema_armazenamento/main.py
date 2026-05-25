from armazenamento import (
    ArmazenadorArquivo,
    ArmazenadorBanco,
    ArmazenadorNuvem,
    executar_salvamento_flexivel,
    executar_salvamento_formal,
)


def main() -> None:
    dado_teste = "Usuario: Pedro | Curso: POO"

    armazenador_arquivo = ArmazenadorArquivo()
    armazenador_banco = ArmazenadorBanco()
    armazenador_nuvem = ArmazenadorNuvem()

    print("=== Salvamento formal (ABC) ===")
    executar_salvamento_formal(armazenador_arquivo, dado_teste)
    executar_salvamento_formal(armazenador_banco, dado_teste)

    print("\n=== Salvamento flexivel (Protocol) ===")
    executar_salvamento_flexivel(armazenador_arquivo, dado_teste)
    executar_salvamento_flexivel(armazenador_banco, dado_teste)
    executar_salvamento_flexivel(armazenador_nuvem, dado_teste)


if __name__ == "__main__":
    main()
