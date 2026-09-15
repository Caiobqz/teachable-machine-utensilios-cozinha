# Resumo Final dos Resultados

Este documento consolida os dados confirmados para a entrega final do projeto da **Fase 1 — Capítulo 2: IA e seu mundo de possibilidades**.

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

## 3. Configurações documentadas

| Configuração | Epochs | Batch Size | Learning Rate |
|---|---:|---:|---:|
| A | 50 | 16 | 0.001 |
| B | 70 | 32 | 0.001 |

## 4. Avaliação final com imagens inéditas

O grupo confirmou que as imagens utilizadas na avaliação final **não estavam entre as imagens de treinamento**.

Um print repetido de Garfo com 91% foi identificado e contabilizado apenas uma vez. Assim, o conjunto final possui **14 testes únicos e inéditos**.

```text
Total de testes únicos: 14
Acertos: 13
Erros: 1
Acurácia final: 92,86%
```

Desempenho por classe:

| Classe | Testes | Acertos | Erros | Acurácia |
|---|---:|---:|---:|---:|
| Garfo | 4 | 3 | 1 | 75% |
| Panela | 5 | 5 | 0 | 100% |
| Colher | 5 | 5 | 0 | 100% |
| **Total** | **14** | **13** | **1** | **92,86%** |

## 5. Precisão formal

Precisão calculada como `TP / (TP + FP)`:

| Classe prevista | TP | FP | Precisão |
|---|---:|---:|---:|
| Garfo | 3 | 0 | 100% |
| Panela | 5 | 0 | 100% |
| Colher | 5 | 1 | 83,33% |
| **Média macro** | — | — | **94,44%** |

## 6. Principais resultados observados

- Colher foi classificada corretamente nos cinco testes inéditos, todos com 100% de confiança.
- Panela foi corretamente classificada nos cinco testes, incluindo exemplos com confiança de 53%, 71%, 96% e 100%.
- Garfo apresentou três acertos com 91%, 94% e 98%.
- O único erro ocorreu quando um Garfo foi classificado como Colher com 54%, enquanto Garfo recebeu 46%.

## 7. Interpretação dos resultados

O modelo apresentou desempenho consistente para Panela e Colher, mas a confiança variou em alguns acertos. Isso mostra que uma previsão correta não implica necessariamente alta certeza.

A maior dificuldade ocorreu entre Garfo e Colher, duas classes visualmente semelhantes em material, formato alongado e proporção. O único erro final ocorreu justamente entre essas classes.

Fundos, iluminação, orientação e enquadramento também podem influenciar as probabilidades produzidas pelo modelo.

## 8. Análise crítica

Pontos fortes:

- conjunto de treinamento equilibrado com 160 imagens por classe;
- uso de imagens inéditas na avaliação final;
- 92,86% de acurácia no conjunto testado;
- 100% de acerto para Panela e Colher;
- registro do erro em vez de removê-lo da análise.

Pontos de atenção:

- confusão entre Garfo e Colher;
- confiança moderada em alguns acertos de Panela;
- conjunto de teste relativamente pequeno;
- learning rate permaneceu em 0.001 nas configurações documentadas.

## 9. Melhorias propostas

- ampliar e diversificar imagens de Garfo e Colher;
- aumentar o conjunto de testes futuros;
- variar fundos, iluminação, distância e ângulo;
- incluir objetos parcialmente ocultos;
- testar alterações no learning rate em experimentos futuros;
- modificar um hiperparâmetro por vez para facilitar comparações;
- manter treinamento e teste rigorosamente separados.

## 10. Conclusão

O modelo desenvolvido no Google Teachable Machine atingiu o objetivo de classificar Garfo, Panela e Colher. Com 480 imagens de treinamento e 14 imagens inéditas de avaliação, foram obtidos 13 acertos e 1 erro, resultando em **92,86% de acurácia final**.

A precisão formal foi de 100% para Garfo, 100% para Panela e 83,33% para Colher, com média macro de 94,44%. O único erro ocorreu entre Garfo e Colher, reforçando a necessidade de maior diversidade visual para separar melhor classes semelhantes.

O desempenho apresentado deve ser interpretado como o resultado do conjunto efetivamente testado, não como garantia de desempenho universal.

## 11. Identificação acadêmica

```text
Fase: 1
Capítulo: 2 - IA e seu mundo de possibilidades
Arquivo final: Grupo_Cap2_IA_Fase1.pdf
```
