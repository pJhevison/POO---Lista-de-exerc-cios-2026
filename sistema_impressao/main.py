from impressao import Boleto, Etiqueta, RelatorioSimples, processar_impressao


def main() -> None:
    boleto = Boleto("34191.79001 01043.510047 91020.150008 8 97170000015000", 150.00)
    etiqueta = Etiqueta("Pedro Silva", "Rua das Flores, 123 - Manaus")
    relatorio = RelatorioSimples("Resumo de Vendas do Dia")

    processar_impressao(boleto)
    processar_impressao(etiqueta)
    processar_impressao(relatorio)


if __name__ == "__main__":
    main()
