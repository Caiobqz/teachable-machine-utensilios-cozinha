# Importa o módulo csv para gerar a planilha com os resultados.
import csv

# Importa Path para trabalhar com caminhos de arquivos de forma segura.
from pathlib import Path


# Define a pasta principal do projeto.
PASTA_PROJETO = Path(__file__).resolve().parent.parent

# Define a pasta onde os resultados serão salvos.
PASTA_RESULTADOS = PASTA_PROJETO / "resultados"

# Define o arquivo CSV final.
ARQUIVO_CSV = PASTA_RESULTADOS / "testes.csv"

# Garante que a pasta resultados exista.
PASTA_RESULTADOS.mkdir(parents=True, exist_ok=True)


# Classes utilizadas no projeto.
# O valor em minúsculo facilita a comparação das entradas digitadas.
CLASSES_VALIDAS = {
    "garfo": "Garfo",
    "panela": "Panela",
    "espatula": "Espátula",
    "espátula": "Espátula"
}


# Lista que armazenará os testes realizados durante a execução do programa.
resultados = []


# Padroniza o nome de uma classe.
# Exemplo: "GARFO", "garfo" e "Garfo" passam a ser "Garfo".
def normalizar_classe(classe):
    classe_normalizada = classe.strip().lower()
    return CLASSES_VALIDAS.get(classe_normalizada)


# Solicita uma classe e só aceita as três classes usadas no projeto.
def ler_classe(mensagem):
    while True:
        classe_digitada = input(mensagem).strip()
        classe = normalizar_classe(classe_digitada)

        if classe is not None:
            return classe

        print("Classe inválida.")
        print("Digite apenas: Garfo, Panela ou Espátula.")


# Solicita a confiança do modelo.
# Aceita valores como 98 ou 98%.
def ler_confianca():
    while True:
        entrada = input("Confiança do modelo (%): ").strip()

        # Remove o símbolo de porcentagem caso ele seja digitado.
        entrada = entrada.replace("%", "").replace(",", ".")

        try:
            confianca = float(entrada)
        except ValueError:
            print("Valor inválido. Digite um número entre 0 e 100.")
            continue

        if 0 <= confianca <= 100:
            return confianca

        print("A confiança deve estar entre 0 e 100.")


# Registra um novo teste feito no Teachable Machine.
def registrar_teste():
    print("\n===== REGISTRAR TESTE =====")

    # Nome da imagem usada no teste.
    nome_imagem = input("Nome da imagem: ").strip()

    # Evita registrar uma imagem sem nome.
    if not nome_imagem:
        print("O nome da imagem não pode ficar vazio.")
        return

    # Classe verdadeira da imagem.
    classe_real = ler_classe("Classe real: ")

    # Classe prevista pelo Teachable Machine.
    classe_prevista = ler_classe("Classe prevista pelo modelo: ")

    # Confiança mostrada pelo Teachable Machine.
    confianca = ler_confianca()

    # Verifica se a previsão corresponde à classe real.
    acertou = classe_real == classe_prevista

    # Organiza os dados do teste em um dicionário.
    resultado = {
        "imagem": nome_imagem,
        "classe_real": classe_real,
        "classe_prevista": classe_prevista,
        "confianca": confianca,
        "acertou": acertou
    }

    # Adiciona o teste à lista.
    resultados.append(resultado)

    print("Teste registrado com sucesso.")

    if acertou:
        print("Resultado: ACERTO")
    else:
        print("Resultado: ERRO")


# Mostra todos os testes registrados na sessão atual.
def visualizar_resultados():
    if len(resultados) == 0:
        print("Nenhum teste registrado.")
        return

    print("\n===== TESTES REGISTRADOS =====")

    for numero, resultado in enumerate(resultados, start=1):
        print(f"\nTeste {numero}")
        print("Imagem:", resultado["imagem"])
        print("Classe real:", resultado["classe_real"])
        print("Classe prevista:", resultado["classe_prevista"])
        print(f"Confiança: {resultado['confianca']:.2f}%")
        print("Resultado:", "ACERTO" if resultado["acertou"] else "ERRO")

    print("\n--------------------")


# Calcula a acurácia geral do modelo usando os testes registrados.
def calcular_acuracia():
    if len(resultados) == 0:
        print("Nenhum teste disponível.")
        return

    # Conta quantos testes foram classificados corretamente.
    acertos = sum(1 for resultado in resultados if resultado["acertou"])

    # Total de testes realizados.
    total = len(resultados)

    # Quantidade de erros.
    erros = total - acertos

    # Acurácia geral em porcentagem.
    acuracia = acertos / total * 100

    print("\n===== RESULTADO GERAL =====")
    print("Total de testes:", total)
    print("Acertos:", acertos)
    print("Erros:", erros)
    print(f"Acurácia: {acuracia:.2f}%")


# Calcula o desempenho individual de cada classe.
def desempenho_por_classe():
    if len(resultados) == 0:
        print("Nenhum teste disponível.")
        return

    # Cria a estrutura inicial para as três classes.
    classes = {
        "Garfo": {"total": 0, "acertos": 0},
        "Panela": {"total": 0, "acertos": 0},
        "Espátula": {"total": 0, "acertos": 0}
    }

    # Soma os testes e acertos de cada classe.
    for resultado in resultados:
        classe = resultado["classe_real"]
        classes[classe]["total"] += 1

        if resultado["acertou"]:
            classes[classe]["acertos"] += 1

    print("\n===== DESEMPENHO POR CLASSE =====")

    for classe, dados in classes.items():
        total = dados["total"]
        acertos = dados["acertos"]
        erros = total - acertos

        print(f"\nClasse: {classe}")
        print("Total:", total)
        print("Acertos:", acertos)
        print("Erros:", erros)

        # Evita divisão por zero caso uma classe ainda não tenha sido testada.
        if total == 0:
            print("Acurácia: sem testes registrados")
        else:
            acuracia = acertos / total * 100
            print(f"Acurácia: {acuracia:.2f}%")


# Exporta todos os testes registrados para um arquivo CSV.
def exportar_csv():
    if len(resultados) == 0:
        print("Nenhum resultado para exportar.")
        return

    # Colunas que serão gravadas no arquivo.
    campos = [
        "imagem",
        "classe_real",
        "classe_prevista",
        "confianca",
        "acertou"
    ]

    # Cria ou substitui o arquivo de resultados.
    with open(ARQUIVO_CSV, "w", newline="", encoding="utf-8-sig") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(resultados)

    print("Resultados exportados com sucesso.")
    print("Arquivo:", ARQUIVO_CSV)


# Mostra um resumo rápido para conferir se o conjunto de testes está equilibrado.
def resumo_testes():
    if len(resultados) == 0:
        print("Nenhum teste registrado.")
        return

    quantidades = {
        "Garfo": 0,
        "Panela": 0,
        "Espátula": 0
    }

    for resultado in resultados:
        quantidades[resultado["classe_real"]] += 1

    print("\n===== RESUMO DOS TESTES =====")
    print("Garfo:", quantidades["Garfo"])
    print("Panela:", quantidades["Panela"])
    print("Espátula:", quantidades["Espátula"])
    print("Total:", len(resultados))

    if len(set(quantidades.values())) == 1:
        print("Conjunto de testes equilibrado entre as classes.")
    else:
        print("Atenção: as classes possuem quantidades diferentes de testes.")


# Menu principal do programa.
def menu():
    while True:
        print("\n===== ANÁLISE DO MODELO =====")
        print("1 - Registrar teste")
        print("2 - Visualizar resultados")
        print("3 - Calcular acurácia")
        print("4 - Desempenho por classe")
        print("5 - Resumo dos testes")
        print("6 - Exportar CSV")
        print("7 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            registrar_teste()
        elif opcao == "2":
            visualizar_resultados()
        elif opcao == "3":
            calcular_acuracia()
        elif opcao == "4":
            desempenho_por_classe()
        elif opcao == "5":
            resumo_testes()
        elif opcao == "6":
            exportar_csv()
        elif opcao == "7":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida.")


# Inicia o programa quando este arquivo for executado diretamente.
if __name__ == "__main__":
    menu()
