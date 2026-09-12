# Classes utilizadas no projeto.
CLASSES_VALIDAS = ["Garfo", "Panela", "Colher"]


def normalizar_classe(texto):
    """Padroniza o nome da classe digitada pelo usuário."""
    texto = texto.strip().lower()

    if texto == "garfo":
        return "Garfo"
    if texto == "panela":
        return "Panela"
    if texto == "colher":
        return "Colher"

    return None


def registrar_teste(resultados):
    """Registra um resultado obtido no Teachable Machine."""
    nome_imagem = input("Nome da imagem: ").strip()

    classe_real = normalizar_classe(input("Classe real: "))
    if classe_real is None:
        print("Classe inválida. Use Garfo, Panela ou Colher.")
        return

    classe_prevista = normalizar_classe(
        input("Classe prevista pelo modelo: ")
    )
    if classe_prevista is None:
        print("Classe inválida. Use Garfo, Panela ou Colher.")
        return

    entrada_confianca = input("Confiança do modelo (%): ").strip()
    entrada_confianca = entrada_confianca.replace("%", "").replace(",", ".")

    try:
        confianca = float(entrada_confianca)
    except ValueError:
        print("Confiança inválida. Digite um número entre 0 e 100.")
        return

    if confianca < 0 or confianca > 100:
        print("A confiança deve estar entre 0 e 100.")
        return

    acertou = classe_real == classe_prevista

    resultado = {
        "imagem": nome_imagem,
        "classe_real": classe_real,
        "classe_prevista": classe_prevista,
        "confianca": confianca,
        "acertou": acertou,
    }

    resultados.append(resultado)

    print("Teste registrado com sucesso.")
    print("Resultado:", "ACERTO" if acertou else "ERRO")


def visualizar_resultados(resultados):
    """Mostra todos os testes cadastrados."""
    if len(resultados) == 0:
        print("Nenhum teste registrado.")
        return

    for resultado in resultados:
        print("\n--------------------")
        print("Imagem:", resultado["imagem"])
        print("Classe real:", resultado["classe_real"])
        print("Classe prevista:", resultado["classe_prevista"])
        print(f"Confiança: {resultado['confianca']:.2f}%")
        print("Resultado:", "ACERTO" if resultado["acertou"] else "ERRO")

    print("--------------------")
