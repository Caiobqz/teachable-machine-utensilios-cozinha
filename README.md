# Teachable Machine - Utensílios de Cozinha

Projeto acadêmico para criação e avaliação de um modelo de classificação de imagens utilizando o Google Teachable Machine.

## Integrantes

- Caio Barros Queiroz
- Suellen Hellen Pereira Silva
- Paulo Vitor Isidoro Silva
- Kauê Cavalcanti Araujo

## Objetivo

Treinar um modelo capaz de identificar diferentes utensílios de cozinha a partir de fotografias e avaliar seu desempenho com imagens não utilizadas no treinamento.

## Classes sugeridas

- Garfo
- Panela
- Espátula

## Estrutura prevista

```text
imagens/
  treino/
    garfo/
    panela/
    espatula/
  teste/
    garfo/
    panela/
    espatula/
codigo/
  analise_resultados.py
resultados/
  testes.md
  testes.csv
prints/
relatorio/
```

# Etapas detalhadas do projeto

## Etapa 1 — Coleta e organização das imagens

Objetivo: montar o conjunto de dados que será usado no treinamento e nos testes.

Tarefas:

1. Separar imagens de Garfo, Panela e Espátula.
2. Buscar boa iluminação, foco e enquadramento.
3. Evitar imagens com muitos objetos extras.
4. Variar ângulo, distância, posição, fundo e iluminação.
5. Tentar obter aproximadamente 40 imagens por classe.
6. Separar aproximadamente 30 imagens por classe para treinamento e 10 para teste.
7. Garantir que nenhuma imagem de teste seja usada também no treinamento.
8. Organizar as imagens nas pastas do projeto.

Resultado esperado:

- Conjunto de treinamento organizado.
- Conjunto de teste separado.
- Registro de quantas imagens foram utilizadas por classe.

Responsável sugerido: **Suellen Hellen Pereira Silva**.

---

## Etapa 2 — Criação e treinamento no Teachable Machine

Objetivo: criar o modelo de classificação de imagens.

Tarefas:

1. Acessar o Google Teachable Machine.
2. Criar um projeto do tipo `Image Project`.
3. Selecionar `Standard Image Model`.
4. Criar as classes Garfo, Panela e Espátula.
5. Carregar apenas as imagens de treinamento.
6. Conferir se as imagens foram adicionadas às classes corretas.
7. Fazer um treinamento inicial.
8. Tirar prints das classes, imagens e tela de treinamento.

Resultado esperado:

- Modelo treinado pela primeira vez.
- Prints documentando o processo.

Responsável sugerido: **Paulo Vitor Isidoro Silva**.

---

## Etapa 3 — Experimentos com os parâmetros do modelo

Objetivo: comparar diferentes configurações e verificar como elas afetam o resultado.

Realizar pelo menos três experimentos.

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

Tarefas:

1. Alterar os parâmetros avançados.
2. Treinar o modelo em cada configuração.
3. Registrar a configuração utilizada.
4. Registrar os resultados observados.
5. Tirar prints das configurações e resultados.
6. Comparar qual configuração apresentou melhor comportamento.
7. Não inventar resultados; todos devem vir dos testes reais.

Os resultados devem ser registrados em `resultados/testes.md`.

Resultado esperado:

- Três treinamentos documentados.
- Comparação entre configurações.
- Evidências em prints.

Responsável sugerido: **Kauê Cavalcanti Araujo**.

---

## Etapa 4 — Teste do modelo e análise em Python

Objetivo: testar o modelo com imagens que ele nunca utilizou no treinamento e organizar os resultados.

Tarefas:

1. Usar as imagens separadas para teste.
2. Testar imagens de todas as classes.
3. Registrar:
   - nome da imagem;
   - classe correta;
   - classe prevista pelo modelo;
   - porcentagem de confiança;
   - se houve acerto ou erro.
4. Registrar também os erros do modelo.
5. Desenvolver as partes marcadas com `TODO` em `codigo/analise_resultados.py`.
6. Implementar primeiro `registrar_teste()`.
7. Depois implementar `visualizar_resultados()`.
8. Implementar `calcular_acuracia()`.
9. Por último, implementar `exportar_csv()`.
10. Calcular a acurácia final dos testes.
11. Gerar `resultados/testes.csv`.
12. Tirar print do programa funcionando.

Fórmula utilizada:

```text
Acurácia = (quantidade de acertos / quantidade total de testes) × 100
```

Resultado esperado:

- Resultados de teste registrados.
- Acurácia calculada.
- CSV gerado.
- Código Python funcional.

Responsável sugerido: **Caio Barros Queiroz**.

---

## Etapa 5 — Análise crítica dos resultados

Objetivo: explicar tecnicamente o comportamento do modelo.

Esta etapa deve ser feita em conjunto pelo grupo.

Responder perguntas como:

1. Qual configuração teve melhor desempenho?
2. Qual classe foi mais fácil de identificar?
3. Qual classe gerou mais erros?
4. O modelo confundiu algum utensílio com outro?
5. A iluminação interferiu nos resultados?
6. O fundo das imagens influenciou?
7. O ângulo do objeto interferiu na classificação?
8. O conjunto de treinamento tinha imagens suficientemente variadas?
9. Mais imagens poderiam melhorar o desempenho?
10. Como o modelo poderia ser melhorado em uma próxima versão?

Possíveis melhorias:

- aumentar a quantidade de imagens;
- variar mais os fundos;
- variar iluminação;
- variar ângulos;
- equilibrar a quantidade de imagens entre as classes;
- remover imagens ruins ou repetitivas;
- adicionar novas classes futuramente.

Resultado esperado:

- Texto de análise crítica baseado nos resultados reais.
- Sugestões de melhoria justificadas.

Responsáveis: **todos os integrantes**.

---

## Etapa 6 — Relatório final em PDF

Objetivo: reunir todas as evidências e explicar o desenvolvimento completo do projeto.

Estrutura sugerida:

1. Capa
2. Integrantes
3. Introdução
4. Objetivos
5. Metodologia
6. Coleta e preparação das imagens
7. Criação das classes
8. Treinamento do modelo
9. Experimentos com Epochs, Batch Size e Learning Rate
10. Testes com imagens inéditas
11. Resultados e acurácia
12. Análise crítica
13. Sugestões de melhoria
14. Conclusão

O relatório deve conter prints das principais etapas, incluindo:

- classes criadas;
- imagens carregadas;
- parâmetros avançados;
- treinamento;
- resultados;
- testes corretos;
- pelo menos um erro interessante, se houver;
- acurácia final;
- programa Python funcionando.

Antes da entrega, todos devem revisar o PDF.

Responsáveis sugeridos:

- **Suellen:** seção de coleta e preparação das imagens.
- **Paulo:** seção de criação e treinamento do modelo.
- **Kauê:** seção de experimentos e comparação de parâmetros.
- **Caio:** resultados, código Python, acurácia e integração final do documento.
- **Todos:** análise crítica, conclusão e revisão final.

---

# Divisão resumida

| Integrante | Responsabilidade principal |
|---|---|
| Caio Barros Queiroz | Código Python, testes, cálculo de acurácia, organização final e integração do relatório |
| Suellen Hellen Pereira Silva | Coleta, seleção, separação e organização das imagens |
| Paulo Vitor Isidoro Silva | Criação das classes e treinamento inicial no Teachable Machine |
| Kauê Cavalcanti Araujo | Experimentos com Epochs, Batch Size e Learning Rate e comparação dos resultados |
| Todos | Análise crítica, revisão do relatório e conferência da entrega |

> A divisão acima é uma sugestão de organização. Todos os integrantes devem conhecer o processo completo, porque as etapas dependem umas das outras.

# Fluxo do trabalho

```text
Coleta das imagens
        ↓
Separação treino/teste
        ↓
Criação das classes
        ↓
Treinamento inicial
        ↓
Experimentos com parâmetros
        ↓
Teste com imagens inéditas
        ↓
Registro dos resultados
        ↓
Cálculo de acurácia
        ↓
Análise crítica
        ↓
Relatório PDF
        ↓
Revisão final e entrega
```

## Código-base

O arquivo `codigo/analise_resultados.py` foi deixado propositalmente incompleto em algumas partes marcadas com `TODO`. Essas partes devem ser desenvolvidas durante a atividade para praticar listas, dicionários, funções, estruturas condicionais, repetição e cálculo de acurácia.

## Próxima tarefa

Antes de avançar para o treinamento, o grupo deve concluir a **Etapa 1 — Coleta e organização das imagens** e confirmar quantas imagens de Garfo, Panela e Espátula serão utilizadas em treino e teste.
