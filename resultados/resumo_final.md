# Resumo Final dos Resultados

Este documento consolida os dados confirmados até o momento para a entrega do projeto.

## 1. Conjunto principal de treinamento

| Classe | Imagens de treinamento |
|---|---:|
| Garfo | 160 |
| Panela | 160 |
| Colher | 160 |

Total de imagens de treinamento no modelo principal: **480**.

## 2. Informações técnicas do modelo exportado

```text
Classes: Colher, Garfo e Panela
Quantidade de classes: 3
Tamanho de entrada: 224 x 224 pixels
Canais: RGB
Teachable Machine: 2.4.16
Formato exportado: TensorFlow.js
```

Mapeamento observado na interface:

```text
Class 1 = Panela
Class 2 = Garfo
Class 3 = Colher
```

## 3. Configurações realmente documentadas

| Configuração | Epochs | Batch Size | Learning Rate | Evidência |
|---|---:|---:|---:|---|
| A | 50 | 16 | 0.001 | vários prints do modelo de 160 imagens por classe |
| B | 70 | 32 | 0.001 | print do modelo de 160 imagens por classe |

## 4. Resultado dos testes recentes

Foi identificado um print repetido de Garfo com 91% de confiança. Para evitar duplicidade, ele foi contabilizado apenas uma vez.

Considerando apenas os **14 testes únicos** visíveis nos prints recentes:

```text
Total de testes únicos: 14
Acertos: 13
Erros: 1
Acurácia observada: 92,86%
```

Desempenho por classe:

| Classe | Testes | Acertos | Erros | Taxa de acerto |
|---|---:|---:|---:|---:|
| Garfo | 4 | 3 | 1 | 75% |
| Panela | 5 | 5 | 0 | 100% |
| Colher | 5 | 5 | 0 | 100% |
| **Total** | **14** | **13** | **1** | **92,86%** |

**Observação metodológica:** esses resultados devem ser considerados finais apenas se o grupo confirmar que as imagens usadas nesses testes não estavam entre as 160 imagens de treinamento de cada classe.

## 5. Principais resultados observados

- Colher foi corretamente classificada em todos os cinco testes únicos recentes, sempre com 100% de confiança.
- Panela foi corretamente classificada nos cinco testes recentes, com confianças de 53%, 71%, 96% e 100% nos exemplos documentados.
- Garfo apresentou três acertos com 91%, 94% e 98% de confiança.
- Em um teste, um Garfo foi classificado incorretamente como Colher com 54%, enquanto Garfo recebeu 46%.

## 6. Interpretação dos resultados

O modelo apresentou desempenho muito consistente para Panela e Colher. Apesar disso, alguns acertos de Panela ocorreram com confiança moderada, como 53% e 71%, o que mostra que uma classificação correta não significa necessariamente alta certeza do modelo.

A maior dificuldade observada ocorreu entre Garfo e Colher. No único erro do conjunto recente, um Garfo foi classificado como Colher por uma diferença pequena de probabilidade (54% contra 46%). Esse comportamento é coerente com a semelhança visual entre essas classes, que compartilham formato alongado, material semelhante e proporções próximas em certas imagens.

Fundos, iluminação, orientação e enquadramento também podem ter contribuído para as diferenças de confiança. Por isso, o desempenho deve ser interpretado em conjunto com as características das imagens de teste.

## 7. Comparação com o modelo menor

Também foram testados exemplos de um modelo anterior com apenas 10 imagens por classe. Esse modelo apresentou vários acertos isolados, mas também houve um caso de confusão relevante no qual uma imagem majoritariamente de colheres foi classificada como Garfo com 82% de confiança.

Essa evidência reforça a importância de um conjunto de treinamento maior e mais variado.

## 8. Análise crítica

Pontos fortes observados:

- treinamento equilibrado com 160 imagens por classe;
- 100% de acerto nos testes recentes de Panela e Colher;
- boa capacidade de generalização nos exemplos recentes;
- identificação correta mesmo quando a confiança não foi máxima.

Pontos de atenção:

- confusão entre Garfo e Colher em uma imagem;
- confiança baixa ou moderada em alguns testes de Panela;
- influência possível de fundo, iluminação e orientação;
- número de testes ainda relativamente pequeno, devendo a acurácia ser interpretada como desempenho no conjunto avaliado.

## 9. Melhorias propostas

- aumentar a quantidade e diversidade de imagens de Garfo;
- incluir mais exemplos de Garfo e Colher em fundos e ângulos semelhantes;
- variar iluminação e distância;
- adicionar objetos parcialmente ocultos;
- ampliar o conjunto de testes futuros;
- alterar um hiperparâmetro por vez em experimentos futuros;
- manter rigorosamente separados os conjuntos de treinamento e teste.

## 10. Conclusão

O modelo demonstrou capacidade satisfatória de classificar Garfo, Panela e Colher. No conjunto recente de 14 testes únicos, foram registrados 13 acertos e 1 erro, correspondendo a uma acurácia observada de **92,86%**. Panela e Colher apresentaram 100% de acerto nesse conjunto, enquanto Garfo apresentou maior dificuldade, com um erro de classificação para Colher.

Os resultados mostram que o Teachable Machine foi capaz de construir um classificador funcional com o conjunto preparado pelo grupo. Ao mesmo tempo, a ocorrência de um erro entre Garfo e Colher e as variações de confiança mostram a importância de utilizar imagens variadas e de avaliar o modelo com exemplos que não participaram do treinamento.

A acurácia de 92,86% deve ser apresentada como resultado do conjunto testado, e não como garantia de desempenho em qualquer imagem futura.
