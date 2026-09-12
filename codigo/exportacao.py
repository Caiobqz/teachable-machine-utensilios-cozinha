import csv
from pathlib import Path


def exportar_csv(resultados):
    """Exporta os resultados registrados para um arquivo CSV."""
    if len(resultados) == 0:
        print("Nenhum resultado para exportar.")
        return

    pasta_resultados = Path(__file__).resolve().parent.parent / "resultados"
    pasta_resultados.mkdir(exist_ok=True)

    nome_arquivo = pasta_resultados / "testes.csv"

    campos = [
        "imagem",
        "classe_real",
        "classe_prevista",
        "confianca",
        "acertou",
    ]

    with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(resultados)

    print("Resultados exportados com sucesso.")
    print("Arquivo:", nome_arquivo)
