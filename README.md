# Teachable Machine - Utensílios de Cozinha

Projeto acadêmico para criação e avaliação de um modelo de classificação de imagens utilizando o Google Teachable Machine.

## Integrantes

- Caio Barros Queiroz
- Suellen Hellen Pereira Silva
- Paulo Vitor Isidoro Silva
- Kauê Cavalcanti Araujo

## Objetivo

Treinar um modelo capaz de identificar diferentes utensílios de cozinha a partir de fotografias e avaliar seu desempenho com imagens não utilizadas no treinamento.

## Classes utilizadas

- Garfo
- Panela
- Colher

## Estrutura prevista

```text
imagens/
  treino/
    garfo/
    panela/
    colher/
  teste/
    garfo/
    panela/
    colher/
codigo/
  analise_resultados.py
  sistema.py
  cadastro.py
  analise.py
  exportacao.py
resultados/
  testes.md
  testes.csv
  resumo_final.md
prints/
relatorio/
docs/
```

# Divisão detalhada do trabalho

A divisão abaixo busca evitar que duas pessoas façam a mesma coisa, deixar claro o que cada integrante deve entregar e facilitar a montagem do relatório final. Mesmo com tarefas principais separadas, todos devem entender o fluxo completo do projeto.

## Caio Barros Queiroz — Código, testes, acurácia e integração final

### Responsabilidade principal

Transformar os resultados obtidos no Teachable Machine em dados organizados, verificáveis e fáceis de usar no relatório final.

### O que deve fazer

1. Manter e testar os arquivos da pasta `codigo/`.
2. Receber os resultados reais dos testes realizados no Teachable Machine.
3. Registrar no programa:
   - nome da imagem testada;
   - classe correta;
   - classe prevista pelo modelo;
   - confiança em porcentagem.
4. Visualizar os resultados registrados.
5. Calcular a acurácia geral usando:

```text
Acurácia = (acertos / total de testes) × 100
```

6. Calcular o desempenho separado por Garfo, Panela e Colher.
7. Conferir se a quantidade de testes está equilibrada entre as classes.
8. Exportar os resultados para `resultados/testes.csv`.
9. Registrar também os erros do modelo, sem excluir resultados ruins.
10. Executar o código e tirar prints do programa funcionando.
11. Juntar os materiais enviados pelos outros integrantes na versão final do projeto.
12. Ajudar na montagem da seção de resultados do relatório.
13. Conferir se a acurácia apresentada no relatório corresponde aos testes registrados.
14. Fazer uma revisão técnica final antes da entrega.

### Estrutura do código

O código foi dividido em módulos para facilitar a leitura e permitir alterações mínimas:

- `codigo/analise_resultados.py`: ponto de entrada do programa;
- `codigo/sistema.py`: menu principal;
- `codigo/cadastro.py`: cadastro e visualização dos testes;
- `codigo/analise.py`: acurácia, desempenho por classe e contagem dos testes;
- `codigo/exportacao.py`: exportação do CSV.

### O que deve entregar ao grupo

- código Python funcional;
- `resultados/testes.csv` com os resultados reais;
- resultado da acurácia final;
- desempenho por classe;
- prints do programa em execução;
- texto curto explicando como o cálculo da acurácia foi realizado;
- confirmação de que os dados do relatório batem com os testes reais.

### Cuidados

- Não inventar resultados.
- Não modificar manualmente a acurácia para parecer melhor.
- Usar sempre as classes `Garfo`, `Panela` e `Colher`.
- Guardar os resultados antes de montar o relatório final.

---

## Suellen Hellen Pereira Silva — Coleta, qualidade e organização das imagens

### Responsabilidade principal

Montar um conjunto de imagens com qualidade suficiente para que o modelo consiga aprender a diferença entre as classes.

### O que deve fazer

1. Organizar imagens de:
   - Garfo;
   - Panela;
   - Colher.
2. Tentar obter aproximadamente 40 imagens de cada classe.
3. Separar aproximadamente:
   - 30 imagens por classe para treinamento;
   - 10 imagens por classe para teste.
4. Garantir que as imagens usadas no teste não apareçam também no treinamento.
5. Conferir a qualidade das imagens:
   - boa iluminação;
   - objeto visível;
   - foco adequado;
   - enquadramento claro.
6. Evitar fotos com muitos objetos extras que possam confundir o modelo.
7. Variar:
   - ângulo;
   - distância;
   - posição;
   - fundo;
   - iluminação;
   - orientação do utensílio.
8. Remover imagens repetidas ou quase idênticas.
9. Organizar corretamente as pastas de treino e teste.
10. Contar quantas imagens existem em cada classe.
11. Registrar essa quantidade para ser usada na metodologia do relatório.
12. Tirar pelo menos um print mostrando como as imagens foram organizadas.

### O que deve entregar ao grupo

- conjunto de imagens de treinamento;
- conjunto separado de imagens de teste;
- quantidade exata de imagens por classe;
- confirmação de que não existem imagens duplicadas entre treino e teste;
- prints da organização do conjunto de dados;
- pequeno texto explicando os critérios usados para escolher as imagens.

### Cuidados

- Não usar a mesma foto em treino e teste.
- Não deixar uma classe com muito mais imagens que as outras.
- Não escolher apenas imagens com o mesmo fundo.
- Não usar fotos ruins apenas para aumentar a quantidade.

---

## Paulo Vitor Isidoro Silva — Criação e treinamento do modelo

### Responsabilidade principal

Configurar corretamente o projeto no Teachable Machine e realizar o treinamento inicial usando o conjunto preparado pelo grupo.

### O que deve fazer

1. Acessar o Google Teachable Machine.
2. Criar um projeto de `Image Project`.
3. Selecionar `Standard Image Model`.
4. Criar exatamente três classes:
   - Garfo;
   - Panela;
   - Colher.
5. Receber de Suellen somente as imagens destinadas ao treinamento.
6. Carregar cada imagem na classe correta.
7. Conferir se nenhuma imagem foi adicionada na classe errada.
8. Verificar se a quantidade de exemplos está relativamente equilibrada.
9. Fazer um primeiro treinamento do modelo.
10. Testar rapidamente o modelo para verificar se ele está funcionando.
11. Tirar prints das etapas principais:
    - classes criadas;
    - imagens carregadas;
    - tela antes do treinamento;
    - treinamento concluído;
    - previsão de uma imagem de exemplo.
12. Registrar qualquer problema encontrado, como classe com desempenho pior ou confusão frequente entre objetos.
13. Passar o projeto treinado e os resultados iniciais para Kauê continuar os experimentos.
14. Escrever um pequeno resumo explicando como o modelo foi criado.

### O que deve entregar ao grupo

- modelo criado no Teachable Machine;
- confirmação das três classes utilizadas;
- primeiro treinamento concluído;
- prints do processo;
- texto curto explicando a criação e o treinamento inicial;
- observações sobre dificuldades ou comportamentos estranhos do modelo.

### Cuidados

- Não colocar imagens de teste dentro do treinamento.
- Conferir o nome das classes antes de treinar.
- Não apagar prints das primeiras versões do treinamento.
- Não considerar uma previsão isolada como prova de que o modelo está bom.

---

## Kauê Cavalcanti Araujo — Experimentos, parâmetros e comparação dos resultados

### Responsabilidade principal

Testar diferentes configurações do modelo e observar como os parâmetros influenciam a classificação.

### O que deve fazer

1. Utilizar o projeto já configurado por Paulo.
2. Abrir as configurações avançadas de treinamento.
3. Realizar pelo menos três experimentos diferentes.
4. Usar inicialmente as seguintes configurações como referência:

### Experimento 1

```text
Epochs: 50
Batch Size: 16
Learning Rate: 0.001
```

### Experimento 2

```text
Epochs: 100
Batch Size: 16
Learning Rate: 0.001
```

### Experimento 3

```text
Epochs: 100
Batch Size: 32
Learning Rate: 0.001
```

5. Treinar o modelo separadamente em cada configuração.
6. Registrar cada experimento em `resultados/testes.md`.
7. Anotar:
   - Epochs;
   - Batch Size;
   - Learning Rate;
   - resultado observado;
   - possíveis diferenças percebidas.
8. Tirar print das configurações antes de cada treinamento.
9. Tirar print dos resultados obtidos.
10. Comparar os experimentos e identificar qual configuração pareceu mais consistente.
11. Não escolher automaticamente o treinamento com mais épocas como o melhor.
12. Explicar por que uma configuração foi considerada melhor ou pior.
13. Passar para Caio os resultados da configuração escolhida para os testes finais.
14. Escrever um resumo comparativo dos três experimentos.

### O que deve entregar ao grupo

- três experimentos documentados;
- tabela com parâmetros utilizados;
- prints de cada configuração;
- comparação dos resultados;
- indicação da configuração escolhida para os testes finais;
- texto explicando as diferenças observadas.

---

# Testes finais do modelo

Depois dos experimentos, o grupo deve testar o modelo escolhido com imagens que não fizeram parte do treinamento.

Sugestão de quantidade:

```text
Garfo: 10 imagens
Panela: 10 imagens
Colher: 10 imagens
Total: 30 testes
```

Para cada imagem, registrar:

- nome da imagem;
- classe correta;
- previsão do modelo;
- confiança;
- acerto ou erro.

É importante testar as três classes e guardar também exemplos de erros.

# Análise crítica

Todos devem ajudar a responder:

1. Qual classe teve melhor desempenho?
2. Qual classe teve mais erros?
3. Quais utensílios foram confundidos?
4. O fundo das imagens influenciou?
5. A iluminação influenciou?
6. O ângulo alterou a classificação?
7. O modelo teve baixa confiança em alguma situação?
8. Mais imagens poderiam melhorar o desempenho?
9. As classes estavam equilibradas?
10. Qual seria a principal melhoria para uma próxima versão?

# Relatório final

Cada integrante deve escrever ou revisar a parte relacionada à própria tarefa:

- **Suellen:** coleta, qualidade e separação das imagens.
- **Paulo:** criação das classes e treinamento inicial.
- **Kauê:** experimentos, parâmetros e comparação.
- **Caio:** testes, código Python, acurácia, resultados e integração do relatório.
- **Todos:** análise crítica, conclusão e revisão final.

## Estrutura recomendada do PDF

1. Capa
2. Integrantes
3. Introdução
4. Objetivos
5. Metodologia
6. Coleta e preparação das imagens
7. Separação entre treino e teste
8. Criação das classes
9. Treinamento do modelo
10. Experimentos com Epochs, Batch Size e Learning Rate
11. Testes com imagens inéditas
12. Resultados
13. Acurácia geral
14. Desempenho por classe
15. Análise dos erros
16. Análise crítica
17. Sugestões de melhoria
18. Conclusão

# Ordem recomendada de execução

```text
1. Suellen prepara o conjunto de imagens
              ↓
2. Paulo cria e treina o modelo inicial
              ↓
3. Kauê realiza os experimentos com parâmetros
              ↓
4. Grupo escolhe a configuração final
              ↓
5. Grupo realiza os testes com imagens inéditas
              ↓
6. Caio registra os resultados no Python e calcula a acurácia
              ↓
7. Todos participam da análise crítica
              ↓
8. Cada integrante escreve sua seção do relatório
              ↓
9. Caio integra o documento final
              ↓
10. Todos revisam antes da entrega
```

# Checklist individual

| Integrante | Entrega mínima |
|---|---|
| Caio | Código Python funcional, CSV, acurácia, prints e integração final |
| Suellen | Imagens de treino/teste organizadas, contagem e critérios de seleção |
| Paulo | Projeto no Teachable Machine, primeiro treinamento, prints e explicação |
| Kauê | Três experimentos, tabela de parâmetros, prints e comparação |
| Todos | Testes finais, análise crítica, conclusão e revisão do PDF |

# Regra de trabalho do grupo

Nenhuma etapa deve ser considerada concluída apenas porque funcionou. O responsável deve deixar uma evidência que o próximo integrante consiga usar: arquivo, print, tabela, resultado ou explicação curta. Isso evita retrabalho e facilita a montagem do relatório final.

## Como executar o código

Na raiz do repositório:

```powershell
python codigo\analise_resultados.py
```

O programa trabalha com as classes `Garfo`, `Panela` e `Colher` e permite registrar os resultados obtidos no Teachable Machine, calcular a acurácia e exportar o CSV.

## Próxima tarefa

A primeira dependência prática do projeto é preparar e separar corretamente as imagens de Garfo, Panela e Colher entre os conjuntos de treinamento e teste.