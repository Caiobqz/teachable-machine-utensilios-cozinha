def calcular_acuracia(resultados):
    """Calcula e exibe a acurácia geral dos testes."""
    if len(resultados) == 0:
        print("Nenhum teste disponível.")
        return

    acertos = 0

    for resultado in resultados:
        if resultado["acertou"]:
            acertos += 1

    total = len(resultados)
    erros = total - acertos
    acuracia = acertos / total * 100

    print("\n===== RESULTADO GERAL =====")
    print("Total de testes:", total)
    print("Acertos:", acertos)
    print("Erros:", erros)
    print(f"Acurácia: {acuracia:.2f}%")


def desempenho_por_classe(resultados):
    """Calcula e exibe o desempenho separado por classe."""
    if len(resultados) == 0:
        print("Nenhum teste disponível.")
        return

    classes = {}

    for resultado in resultados:
        classe = resultado["classe_real"]

        if classe not in classes:
            classes[classe] = {
                "total": 0,
                "acertos": 0,
            }

        classes[classe]["total"] += 1

        if resultado["acertou"]:
            classes[classe]["acertos"] += 1

    print("\n===== DESEMPENHO POR CLASSE =====")

    for classe, dados in classes.items():
        total = dados["total"]
        acertos = dados["acertos"]
        erros = total - acertos
        acuracia = acertos / total * 100

        print("\nClasse:", classe)
        print("Total:", total)
        print("Acertos:", acertos)
        print("Erros:", erros)
        print(f"Acurácia: {acuracia:.2f}%")


def resumo_quantidade_por_classe(resultados):
    """Mostra quantos testes foram feitos em cada classe."""
    if len(resultados) == 0:
        print("Nenhum teste disponível.")
        return

    contagem = {
        "Garfo": 0,
        "Panela": 0,
        "Colher": 0,
    }

    for resultado in resultados:
        contagem[resultado["classe_real"]] += 1

    print("\n===== QUANTIDADE DE TESTES POR CLASSE =====")

    for classe, quantidade in contagem.items():
        print(f"{classe}: {quantidade}")

    valores = list(contagem.values())

    if max(valores) != min(valores):
        print("Aviso: o conjunto de testes está desequilibrado entre as classes.")
