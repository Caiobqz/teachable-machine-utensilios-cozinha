from cadastro import registrar_teste, visualizar_resultados
from analise import (
    calcular_acuracia,
    desempenho_por_classe,
    resumo_quantidade_por_classe,
)
from exportacao import exportar_csv


def menu():
    """Controla o menu principal do programa."""
    resultados = []

    while True:
        print("\n===== ANÁLISE DO MODELO =====")
        print("1 - Registrar teste")
        print("2 - Visualizar resultados")
        print("3 - Calcular acurácia")
        print("4 - Desempenho por classe")
        print("5 - Quantidade de testes por classe")
        print("6 - Exportar CSV")
        print("7 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            registrar_teste(resultados)

        elif opcao == "2":
            visualizar_resultados(resultados)

        elif opcao == "3":
            calcular_acuracia(resultados)

        elif opcao == "4":
            desempenho_por_classe(resultados)

        elif opcao == "5":
            resumo_quantidade_por_classe(resultados)

        elif opcao == "6":
            exportar_csv(resultados)

        elif opcao == "7":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")
