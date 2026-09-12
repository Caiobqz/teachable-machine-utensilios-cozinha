# Importa o módulo csv.
# Ele será usado para criar um arquivo .csv com os resultados dos testes.
import csv


# Cria uma lista vazia.
# Essa lista vai armazenar todos os testes realizados durante a execução.
resultados = []


# Cria uma função responsável por registrar um novo teste.
def registrar_teste():

    # Solicita o nome da imagem usada no teste.
    # O strip() remove espaços extras no início e no fim.
    nome_imagem = input("Nome da imagem: ").strip()

    # Solicita qual é a classe verdadeira da imagem.
    classe_real = input("Classe real: ").strip()

    # Solicita qual foi a classe prevista pelo Teachable Machine.
    classe_prevista = input("Classe prevista pelo modelo: ").strip()

    # Solicita a confiança apresentada pelo modelo.
    # A entrada é recebida primeiro como texto.
    entrada_confianca = input("Confiança do modelo (%): ").strip()

    # Remove o símbolo de porcentagem, caso o usuário digite algo como 98%.
    entrada_confianca = entrada_confianca.replace("%", "")

    # Tenta converter a confiança para número decimal.
    try:
        confianca = float(entrada_confianca)

    # Se o usuário digitar algo que não pode virar número,
    # o programa não será encerrado com erro.
    except ValueError:
        print("Valor de confiança inválido.")
        print("Digite apenas um número entre 0 e 100.")
        return

    # Verifica se o valor informado está dentro do intervalo permitido.
    if confianca < 0 or confianca > 100:
        print("A confiança deve estar entre 0 e 100.")
        return

    # Compara a classe real com a classe prevista.
    #
    # O lower() transforma o texto em letras minúsculas.
    # Dessa forma:
    #
    # Garfo
    # garfo
    # GARFO
    #
    # serão tratados como a mesma classe.
    acertou = classe_real.lower() == classe_prevista.lower()

    # Cria um dicionário para guardar os dados do teste.
    resultado = {
        "imagem": nome_imagem,
        "classe_real": classe_real,
        "classe_prevista": classe_prevista,
        "confianca": confianca,
        "acertou": acertou
    }

    # Adiciona o dicionário criado à lista de resultados.
    resultados.append(resultado)

    # Informa que o teste foi registrado.
    print("Teste registrado com sucesso.")

    # Mostra também se o modelo acertou ou errou.
    if acertou:
        print("Resultado: ACERTO")
    else:
        print("Resultado: ERRO")


# Cria uma função para mostrar todos os testes registrados.
def visualizar_resultados():

    # Verifica se a lista está vazia.
    if len(resultados) == 0:

        # Caso nenhum teste tenha sido registrado,
        # mostra uma mensagem.
        print("Nenhum teste registrado.")

        # Encerra a função.
        return

    # Percorre todos os testes armazenados na lista.
    for resultado in resultados:

        # Mostra os dados do teste atual.
        print("\n--------------------")
        print("Imagem:", resultado["imagem"])
        print("Classe real:", resultado["classe_real"])
        print("Classe prevista:", resultado["classe_prevista"])
        print("Confiança:", resultado["confianca"], "%")

        # Verifica se o teste foi um acerto.
        if resultado["acertou"]:
            print("Resultado: ACERTO")

        # Caso contrário, foi um erro.
        else:
            print("Resultado: ERRO")

    # Linha para organizar visualmente a saída.
    print("--------------------")


# Cria uma função para calcular a acurácia geral do modelo.
def calcular_acuracia():

    # Verifica se existem testes registrados.
    if len(resultados) == 0:

        # Evita divisão por zero.
        print("Nenhum teste disponível.")
        return

    # Variável que começa em zero.
    # Ela será usada para contar os acertos.
    acertos = 0

    # Percorre todos os testes.
    for resultado in resultados:

        # Verifica se o teste atual foi um acerto.
        if resultado["acertou"]:

            # Soma 1 ao contador.
            acertos += 1

    # Calcula a quantidade total de testes.
    total = len(resultados)

    # Calcula quantos testes foram erros.
    erros = total - acertos

    # Calcula a acurácia.
    #
    # Fórmula:
    #
    # acurácia = acertos / total * 100
    acuracia = acertos / total * 100

    # Mostra os resultados.
    print("\n===== RESULTADO GERAL =====")
    print("Total de testes:", total)
    print("Acertos:", acertos)
    print("Erros:", erros)

    # :.2f limita o valor para duas casas decimais.
    print(f"Acurácia: {acuracia:.2f}%")


# Cria uma função para mostrar o desempenho separado por classe.
def desempenho_por_classe():

    # Verifica se existem testes registrados.
    if len(resultados) == 0:
        print("Nenhum teste disponível.")
        return

    # Cria um dicionário vazio.
    #
    # Ele será utilizado para organizar os resultados
    # de cada classe separadamente.
    classes = {}

    # Percorre todos os testes registrados.
    for resultado in resultados:

        # Pega o nome da classe real.
        classe = resultado["classe_real"]

        # Verifica se a classe ainda não existe no dicionário.
        if classe not in classes:

            # Cria os contadores da classe.
            classes[classe] = {
                "total": 0,
                "acertos": 0
            }

        # Soma 1 ao total de testes daquela classe.
        classes[classe]["total"] += 1

        # Se o modelo acertou,
        # soma 1 ao contador de acertos daquela classe.
        if resultado["acertou"]:
            classes[classe]["acertos"] += 1

    # Mostra o título.
    print("\n===== DESEMPENHO POR CLASSE =====")

    # Percorre cada classe registrada.
    for classe, dados in classes.items():

        # Guarda o total de testes da classe.
        total = dados["total"]

        # Guarda a quantidade de acertos.
        acertos = dados["acertos"]

        # Calcula os erros.
        erros = total - acertos

        # Calcula a acurácia da classe.
        acuracia = acertos / total * 100

        # Mostra os dados.
        print("\nClasse:", classe)
        print("Total:", total)
        print("Acertos:", acertos)
        print("Erros:", erros)
        print(f"Acurácia: {acuracia:.2f}%")


# Cria uma função para exportar os resultados para CSV.
def exportar_csv():

    # Verifica se existem testes registrados.
    if len(resultados) == 0:
        print("Nenhum resultado para exportar.")
        return

    # Define o caminho e o nome do arquivo.
    nome_arquivo = "resultados/testes.csv"

    # Tenta criar o arquivo.
    try:

        # Abre o arquivo no modo de escrita.
        #
        # newline="" evita linhas em branco extras.
        #
        # encoding="utf-8" permite trabalhar corretamente
        # com acentos.
        with open(
            nome_arquivo,
            "w",
            newline="",
            encoding="utf-8"
        ) as arquivo:

            # Define as colunas do arquivo CSV.
            campos = [
                "imagem",
                "classe_real",
                "classe_prevista",
                "confianca",
                "acertou"
            ]

            # Cria o objeto responsável pela escrita do CSV.
            escritor = csv.DictWriter(
                arquivo,
                fieldnames=campos
            )

            # Escreve o cabeçalho.
            escritor.writeheader()

            # Escreve todos os resultados armazenados na lista.
            escritor.writerows(resultados)

        # Informa que a exportação funcionou.
        print("Resultados exportados com sucesso.")
        print("Arquivo:", nome_arquivo)

    # Caso a pasta resultados não exista,
    # o programa informa o problema sem encerrar inesperadamente.
    except FileNotFoundError:
        print("A pasta 'resultados' não foi encontrada.")


# Cria a função principal do sistema.
def menu():

    # Mantém o programa funcionando até o usuário escolher sair.
    while True:

        # Exibe o menu.
        print("\n===== ANÁLISE DO MODELO =====")
        print("1 - Registrar teste")
        print("2 - Visualizar resultados")
        print("3 - Calcular acurácia")
        print("4 - Desempenho por classe")
        print("5 - Exportar CSV")
        print("6 - Sair")

        # Recebe a opção digitada pelo usuário.
        opcao = input("Escolha uma opção: ").strip()

        # Caso escolha a opção 1.
        if opcao == "1":
            registrar_teste()

        # Caso escolha a opção 2.
        elif opcao == "2":
            visualizar_resultados()

        # Caso escolha a opção 3.
        elif opcao == "3":
            calcular_acuracia()

        # Caso escolha a opção 4.
        elif opcao == "4":
            desempenho_por_classe()

        # Caso escolha a opção 5.
        elif opcao == "5":
            exportar_csv()

        # Caso escolha a opção 6.
        elif opcao == "6":

            # Informa que o programa será encerrado.
            print("Programa encerrado.")

            # Interrompe o while.
            break

        # Caso seja digitada uma opção inexistente.
        else:
            print("Opção inválida.")


# Verifica se o arquivo está sendo executado diretamente.
#
# Isso impede que o menu seja iniciado automaticamente
# caso este arquivo seja importado por outro programa.
if __name__ == "__main__":

    # Inicia o sistema.
    menu()