# Como começar a trabalhar no projeto

Este guia foi feito para quem está começando agora e ainda não tem experiência com GitHub, Teachable Machine ou organização de um projeto em grupo.

A regra mais importante é: **cada pessoa deve começar apenas pela sua etapa e entregar evidências claras para a próxima pessoa continuar**.

---

## Antes de qualquer coisa — todos devem fazer isso

### 1. Ler o README

Abra o `README.md` do repositório e leia a parte de etapas do projeto.

O objetivo é entender o fluxo completo antes de mexer em qualquer coisa.

### 2. Entender o objetivo do trabalho

O grupo precisa criar um modelo no Google Teachable Machine capaz de classificar utensílios de cozinha em três classes:

- Garfo
- Panela
- Espátula

Depois, o grupo deve testar o modelo, analisar seus erros, calcular a acurácia e documentar tudo em PDF.

### 3. Não trabalhar com arquivos aleatórios

Cada integrante deve salvar seus arquivos dentro da estrutura do projeto.

Exemplo:

```text
imagens/
resultados/
prints/
docs/
codigo/
relatorio/
```

### 4. Sempre registrar o que foi feito

Ao terminar uma etapa, a pessoa deve deixar claro:

- o que fez;
- quais arquivos criou ou alterou;
- quais resultados obteve;
- quais prints tirou;
- o que a próxima pessoa precisa fazer.

---

# Suellen Hellen Pereira Silva — como começar

## Sua responsabilidade

Preparar as imagens que serão usadas para treinamento e teste do modelo.

Essa etapa é essencial porque um modelo ruim geralmente começa com dados ruins.

## O que fazer primeiro

1. Separe três grupos de objetos:
   - garfos;
   - panelas;
   - espátulas.
2. Tire ou separe várias imagens de cada tipo.
3. Evite usar imagens muito parecidas entre si.
4. Varie:
   - posição do objeto;
   - distância;
   - iluminação;
   - fundo;
   - ângulo;
   - orientação.
5. Evite imagens:
   - borradas;
   - muito escuras;
   - com vários objetos juntos;
   - em que o utensílio quase não aparece.

## Quantidade sugerida

Tente montar aproximadamente:

```text
Garfo: 30 treino + 10 teste
Panela: 30 treino + 10 teste
Espátula: 30 treino + 10 teste
```

Total aproximado:

```text
90 imagens de treinamento
30 imagens de teste
```

## Cuidado mais importante

Uma imagem usada no treinamento **não pode ser usada novamente no teste**.

O teste deve mostrar se o modelo consegue reconhecer imagens novas.

## Onde organizar

```text
imagens/treino/garfo/
imagens/treino/panela/
imagens/treino/espatula/

imagens/teste/garfo/
imagens/teste/panela/
imagens/teste/espatula/
```

## O que você deve entregar ao grupo

Ao terminar, informe:

- quantas imagens de treino existem em cada classe;
- quantas imagens de teste existem em cada classe;
- se todas foram revisadas;
- se treino e teste estão separados corretamente.

Também guarde pelo menos um print mostrando a organização das imagens.

---

# Paulo Vitor Isidoro Silva — como começar

## Sua responsabilidade

Criar o projeto no Google Teachable Machine e fazer o primeiro treinamento.

## O que você precisa receber antes

Não comece antes de Suellen concluir a organização das imagens de treinamento.

## Passo a passo

1. Acesse o Google Teachable Machine.
2. Clique em `Get Started`.
3. Escolha `Image Project`.
4. Escolha `Standard Image Model`.
5. Crie três classes:
   - Garfo;
   - Panela;
   - Espátula.
6. Carregue apenas as imagens da pasta de treino.
7. Confira se cada imagem foi colocada na classe correta.
8. Faça o primeiro treinamento.
9. Observe se o modelo consegue diferenciar as classes.

## O que registrar

Tire prints de:

- classes criadas;
- imagens carregadas;
- tela antes do treinamento;
- treinamento concluído;
- primeira prévia de classificação.

## O que não fazer

- Não misturar imagens de teste com treinamento.
- Não apagar prints depois.
- Não alterar muitas configurações avançadas ainda; isso será trabalhado na etapa do Kauê.

## O que você deve entregar ao grupo

Ao terminar, informe:

- que o modelo foi criado;
- quais classes foram usadas;
- quantidade de imagens por classe;
- se o treinamento terminou corretamente;
- onde estão os prints.

---

# Kauê Cavalcanti Araujo — como começar

## Sua responsabilidade

Testar diferentes configurações do modelo e comparar os resultados.

## O que você precisa receber antes

Paulo deve ter criado o projeto no Teachable Machine e confirmado que o treinamento básico funciona.

## Conceitos que você precisa entender

### Epochs

Indica quantas vezes o modelo passa pelos dados de treinamento.

Mais épocas podem melhorar o aprendizado, mas também podem fazer o modelo memorizar demais os dados.

### Batch Size

Indica quantas imagens são processadas por vez durante o treinamento.

### Learning Rate

Controla o tamanho dos ajustes feitos pelo modelo durante o aprendizado.

## Experimentos sugeridos

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

## O que fazer em cada experimento

1. Alterar os parâmetros.
2. Treinar o modelo.
3. Anotar a configuração usada.
4. Observar o comportamento do modelo.
5. Registrar o resultado em `resultados/testes.md`.
6. Tirar print das configurações.
7. Tirar print do resultado.

## O que comparar

Tente responder:

- Qual configuração pareceu mais estável?
- Alguma configuração piorou o desempenho?
- Houve diferença de confiança entre os testes?
- Alguma classe continuou sendo confundida?

## O que você deve entregar ao grupo

Uma tabela com:

- configuração de cada experimento;
- resultado observado;
- qual configuração pareceu melhor;
- prints de cada treinamento.

Não invente valores. Use apenas resultados observados de verdade.

---

# Caio Barros Queiroz — como começar

## Sua responsabilidade

Desenvolver a parte em Python, organizar os resultados, calcular a acurácia e integrar as entregas do grupo.

## O que você precisa receber antes

Você depende dos resultados dos testes do modelo.

Não faz sentido calcular acurácia sem testes reais.

## Primeiro arquivo a abrir

```text
codigo/analise_resultados.py
```

O arquivo possui partes marcadas com `TODO`.

Essas partes devem ser implementadas aos poucos.

## Ordem recomendada

### 1. Implementar `registrar_teste()`

O programa deve receber:

- nome da imagem;
- classe real;
- classe prevista;
- confiança;
- se houve acerto ou erro.

Primeiro teste manual sugerido:

```text
Imagem: garfo01.jpg
Classe real: Garfo
Classe prevista: Garfo
Confiança: 95
```

### 2. Implementar `visualizar_resultados()`

Depois de cadastrar testes, o programa deve mostrar todos os registros.

### 3. Implementar `calcular_acuracia()`

Fórmula:

```text
Acurácia = (acertos / total de testes) × 100
```

### 4. Implementar `exportar_csv()`

O resultado final deve ser salvo em:

```text
resultados/testes.csv
```

## O que você deve conferir

- nenhum resultado foi inventado;
- os testes registrados correspondem aos testes reais do Teachable Machine;
- acertos e erros estão corretos;
- a acurácia foi calculada corretamente;
- o CSV foi gerado;
- os prints foram organizados.

## O que você deve entregar ao grupo

- programa funcionando;
- acurácia final;
- total de testes;
- total de acertos;
- total de erros;
- CSV final;
- resumo dos principais erros do modelo.

---

# Como todos devem trabalhar juntos no final

Depois que as quatro responsabilidades principais forem concluídas, o grupo deve fazer uma revisão conjunta.

Todos devem conseguir responder:

1. O que foi treinado?
2. Quantas imagens foram usadas?
3. Como treino e teste foram separados?
4. Quais parâmetros foram testados?
5. Qual configuração foi escolhida?
6. Quantos testes foram feitos?
7. Qual foi a acurácia?
8. Em quais situações o modelo errou?
9. Por que esses erros podem ter acontecido?
10. Como o modelo poderia ser melhorado?

---

# Para quem nunca usou Git

Antes de começar a trabalhar localmente:

```powershell
git clone https://github.com/Caiobqz/teachable-machine-utensilios-cozinha.git
cd teachable-machine-utensilios-cozinha
```

Se o projeto já estiver na máquina:

```powershell
git pull origin main
```

Antes de enviar alterações:

```powershell
git status
```

Depois:

```powershell
git add .
git commit -m "Descrição do que foi feito"
git push origin main
```

Exemplos de commits melhores:

```text
Organiza imagens de treino e teste
Adiciona prints do treinamento inicial
Registra experimentos de hiperparâmetros
Implementa cálculo de acurácia
```

Evite commits vagos como:

```text
update
coisa nova
mudança
```

---

# Regra de passagem entre integrantes

Antes de dizer que sua etapa terminou, confirme:

```text
[ ] Minha tarefa foi concluída
[ ] Os arquivos estão organizados
[ ] Os resultados estão registrados
[ ] Os prints necessários foram salvos
[ ] Não inventei nenhum dado
[ ] A próxima pessoa sabe o que precisa receber
[ ] Expliquei ao grupo o que fiz
```

Se uma dessas respostas for "não", a etapa ainda não está realmente pronta para ser passada adiante.
