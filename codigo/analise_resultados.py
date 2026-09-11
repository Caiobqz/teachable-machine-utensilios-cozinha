# Importa o módulo csv, usado para criar o arquivo com os resultados.
import csv


# Lista que armazenará os resultados dos testes realizados.
resultados = []


# Cria uma função responsável por registrar um teste do modelo.
def registrar_teste():

    # Solicita ao usuário o nome da imagem utilizada no teste.
    nome_imagem = input("Nome da imagem: ")

    # Solicita qual é a classe correta da imagem.
    classe_real = input("Classe real: ")

    # Solicita qual classe o modelo do Teachable Machine previu.
    classe_prevista = input("Classe prevista pelo modelo: ")

    # Solicita a porcentagem de confiança apresentada pelo modelo.
    confianca = float(input("Confiança do modelo (%): "))

    # TODO:
    # Compare classe_real com classe_prevista.
    # Você precisa descobrir se o modelo acertou ou errou.
    #
    # Dica:
    # acertou = classe_real == classe_prevista


    # TODO:
    # Crie um dicionário contendo:
    #
    # nome da imagem
    # classe real
    # classe prevista
    # confiança
    # se acertou ou não
    #
    # Depois adicione esse dicionário na lista "resultados".


# Cria uma função para mostrar todos os testes cadastrados.
def visualizar_resultados():

    # Verifica se a lista está vazia.
    if len(resultados) == 0:

        # Informa que ainda não existem testes.
        print("Nenhum teste registrado.")

        # Encerra a função.
        return

    # Percorre todos os resultados armazenados.
    for resultado in resultados:

        # TODO:
        # Exiba as informações de cada resultado.
        #
        # Exemplo:
        #
        # Imagem: garfo01.jpg
        # Classe real: Garfo
        # Previsão: Garfo
        # Confiança: 96%
        # Resultado: Acerto
        pass


# Cria uma função responsável pelo cálculo da acurácia.
def calcular_acuracia():

    # Verifica se existem testes cadastrados.
    if len(resultados) == 0:

        # Evita divisão por zero.
        print("Nenhum teste disponível.")

        # Encerra a função.
        return

    # Cria uma variável para contar os acertos.
    acertos = 0

    # Percorre todos os testes registrados.
    for resultado in resultados:

        # TODO:
        # Verifique se resultado["acertou"] é verdadeiro.
        #
        # Se for verdadeiro:
        # aumente a variável "acertos" em 1.
        pass

    # Guarda a quantidade total de testes.
    total = len(resultados)

    # TODO:
    # Calcule a acurácia.
    #
    # Fórmula:
    # acuracia = acertos / total * 100


    # TODO:
    # Mostre:
    #
    # total de testes
    # quantidade de acertos
    # quantidade de erros
    # porcentagem de acurácia


# Cria uma função responsável por salvar os resultados em CSV.
def exportar_csv():

    # Define o nome do arquivo que será criado.
    nome_arquivo = "resultados/testes.csv"

    # Abre o arquivo para escrita.
    with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo:

        # Define os nomes das colunas.
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

        # Escreve o cabeçalho do arquivo.
        escritor.writeheader()

        # TODO:
        # Escreva todos os resultados da lista no CSV.
        #
        # Pesquise:
        # escritor.writerows()

    # Mostra uma mensagem após finalizar.
    print("Resultados exportados.")


# Cria a função principal do programa.
def menu():

    # Mantém o programa funcionando até o usuário escolher sair.
    while True:

        # Exibe as opções disponíveis.
        print("\n===== ANÁLISE DO MODELO =====")
        print("1 - Registrar teste")
        print("2 - Visualizar resultados")
        print("3 - Calcular acurácia")
        print("4 - Exportar CSV")
        print("5 - Sair")

        # Recebe a opção escolhida.
        opcao = input("Escolha uma opção: ")

        # Verifica se o usuário escolheu registrar um teste.
        if opcao == "1":

            # Chama a função correspondente.
            registrar_teste()

        # Verifica se o usuário escolheu visualizar os resultados.
        elif opcao == "2":

            # Chama a função correspondente.
            visualizar_resultados()

        # Verifica se o usuário escolheu calcular a acurácia.
        elif opcao == "3":

            # Chama a função correspondente.
            calcular_acuracia()

        # Verifica se o usuário escolheu exportar o CSV.
        elif opcao == "4":

            # Chama a função correspondente.
            exportar_csv()

        # Verifica se o usuário escolheu sair.
        elif opcao == "5":

            # Mostra mensagem de encerramento.
            print("Programa encerrado.")

            # Interrompe o while.
            break

        # É executado caso seja informada uma opção inexistente.
        else:

            # Informa o erro ao usuário.
            print("Opção inválida.")


# Verifica se este arquivo está sendo executado diretamente.
if __name__ == "__main__":

    # Inicia o programa.
    menu()
