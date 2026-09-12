# Metodologia do Projeto

Este documento registra como o grupo deve conduzir o experimento de classificação de utensílios de cozinha com o Google Teachable Machine.

## 1. Objetivo experimental

Criar um modelo capaz de classificar imagens de utensílios de cozinha e avaliar seu desempenho com imagens que não foram utilizadas no treinamento.

## 2. Classes utilizadas

As classes definidas pelo grupo são:

- Garfo
- Panela
- Colher

### Justificativa das classes

As três classes foram escolhidas por apresentarem características visuais diferentes e por serem utensílios comuns de cozinha. Garfo e Colher permitem avaliar a distinção entre talheres visualmente semelhantes, enquanto Panela possui formato mais distinto.

## 3. Coleta de dados

Para cada classe, recomenda-se utilizar aproximadamente:

- 30 imagens para treinamento;
- 10 imagens para teste.

Total sugerido:

- 90 imagens para treinamento;
- 30 imagens para teste.

### Critérios de qualidade

As imagens devem:

- ter foco razoável;
- ter boa iluminação;
- mostrar claramente o objeto principal;
- evitar excesso de objetos extras;
- variar ângulo, posição, distância, fundo e iluminação;
- evitar duplicatas ou imagens quase idênticas.

## 4. Separação treino e teste

As imagens de teste não podem ser as mesmas utilizadas no treinamento. O conjunto de treinamento serve para o modelo aprender, enquanto o conjunto de teste verifica se o modelo consegue generalizar para imagens novas.

## 5. Estrutura sugerida

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
```

## 6. Treinamento no Teachable Machine

Criar um projeto do tipo `Image Project` e selecionar `Standard Image Model`.

Criar as três classes e carregar apenas as imagens de treinamento.

O modelo exportado pelo grupo confirma:

- 3 classes: Colher, Garfo e Panela;
- tamanho de entrada: 224 × 224 pixels;
- 3 canais de cor (RGB);
- formato de exportação TensorFlow.js;
- Teachable Machine 2.4.16.

O grupo deve registrar evidências das etapas principais por meio de prints.

## 7. Experimentos com hiperparâmetros

Devem ser feitos pelo menos três treinamentos com configurações diferentes.

| Experimento | Epochs | Batch Size | Learning Rate |
|---|---:|---:|---:|
| 1 | 50 | 16 | 0.001 |
| 2 | 100 | 16 | 0.001 |
| 3 | 100 | 32 | 0.001 |

Os valores acima são pontos de partida. O grupo deve registrar os resultados reais obtidos em cada treinamento e justificar qual configuração foi escolhida.

## 8. Avaliação

Cada imagem de teste deve registrar:

- nome da imagem;
- classe real;
- classe prevista;
- porcentagem de confiança;
- acerto ou erro.

## 9. Cálculo de acurácia

```text
Acurácia = (quantidade de acertos / quantidade total de testes) × 100
```

## 10. Avaliação por classe

Além da acurácia geral, registrar quantos acertos e erros ocorreram em cada classe.

| Classe | Total testado | Acertos | Erros |
|---|---:|---:|---:|
| Garfo | 10 | preencher | preencher |
| Panela | 10 | preencher | preencher |
| Colher | 10 | preencher | preencher |

## 11. Análise crítica

A análise deve responder, com base nos dados reais:

- qual classe teve melhor desempenho;
- qual classe teve mais erros;
- se Garfo e Colher foram confundidos;
- quais tipos de imagem geraram dúvida;
- se iluminação, fundo ou ângulo influenciaram;
- se o modelo demonstrou confiança alta em algum erro;
- se mais imagens poderiam melhorar o modelo;
- quais limitações existiram no experimento.

## 12. Possíveis limitações

- quantidade pequena de imagens;
- apenas três classes;
- pouca variedade de ambientes;
- objetos muito centralizados;
- imagens coletadas em condições parecidas;
- desequilíbrio entre classes;
- ausência de objetos parcialmente ocultos.

## 13. Possíveis melhorias futuras

- aumentar o conjunto de dados;
- adicionar mais utensílios;
- usar fundos mais variados;
- testar objetos parcialmente ocultos;
- testar diferentes distâncias e iluminações;
- equilibrar rigorosamente as classes;
- remover imagens duplicadas;
- repetir o treinamento com novas configurações.

## 14. Evidências que devem ser preservadas

Guardar prints de:

1. classes criadas;
2. imagens carregadas;
3. configurações avançadas;
4. cada treinamento relevante;
5. resultado final;
6. exemplos de classificações corretas;
7. exemplos de erro, se houver;
8. código Python funcionando;
9. acurácia calculada.

Este documento deve ser atualizado conforme os resultados reais do grupo forem obtidos.
