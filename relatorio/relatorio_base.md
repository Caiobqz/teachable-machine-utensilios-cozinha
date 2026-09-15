# Relatório — Classificação de Utensílios de Cozinha com Teachable Machine

## Capa

**Instituição:** FIAP  
**Fase:** 1 — Raízes da Inteligência: preparando o terreno  
**Capítulo:** 2 — IA e seu mundo de possibilidades  
**Atividade:** Classificação de Utensílios de Cozinha com Inteligência Artificial  
**Ano:** 2026

### Integrantes

| Integrante | RM |
|---|---:|
| Caio Barros Queiroz | RM576443 |
| Paulo Vitor Isidoro Silva | RM575580 |
| Kauê Cavalcanti Araujo | RM576394 |
| Suellen Hellen Pereira Silva | RM574778 |

---

## 1. Introdução

A visão computacional permite que sistemas de inteligência artificial identifiquem padrões visuais em imagens. Neste projeto, foi utilizado o Google Teachable Machine para desenvolver um modelo capaz de classificar utensílios de cozinha em três categorias: Garfo, Panela e Colher. O trabalho envolveu coleta e organização das imagens, treinamento do modelo, experimentação com diferentes configurações, testes com imagens novas e análise crítica dos resultados.

## 2. Objetivos

- desenvolver um modelo capaz de classificar utensílios de cozinha a partir de fotografias;
- aplicar conceitos básicos de aprendizado de máquina e visão computacional;
- utilizar o Google Teachable Machine para treinamento e teste;
- observar o impacto das configurações de treinamento;
- avaliar acertos, erros, confiança, precisão e acurácia do modelo;
- identificar limitações e possibilidades de melhoria.

## 3. Metodologia

O projeto foi dividido em coleta de dados, treinamento, experimentação e avaliação. As classes utilizadas foram Garfo, Panela e Colher. O modelo principal foi construído com um conjunto equilibrado de **160 imagens de treinamento por classe**, totalizando **480 amostras**.

### 3.1 Classes e quantidade de treinamento

| Classe | Treinamento |
|---|---:|
| Garfo | 160 |
| Panela | 160 |
| Colher | 160 |
| **Total** | **480** |

### 3.2 Critérios de seleção das imagens

As imagens foram selecionadas buscando boa iluminação, foco adequado e presença clara do utensílio principal. Também foram consideradas variações de ângulo, distância, posição, fundo e aparência dos objetos para reduzir a dependência de padrões específicos do cenário.

Para garantir uma avaliação válida, as imagens utilizadas nos testes finais foram inéditas, ou seja, não faziam parte do conjunto de treinamento.

## 4. Configuração técnica do modelo

Foi utilizado o Google Teachable Machine na modalidade `Image Project` com `Standard Image Model`.

O modelo exportado confirmou:

| Característica | Valor |
|---|---|
| Classes | Colher, Garfo e Panela |
| Quantidade de classes | 3 |
| Tamanho de entrada | 224 × 224 pixels |
| Canais | RGB |
| Formato exportado | TensorFlow.js |
| Teachable Machine | 2.4.16 |

Na interface usada nos testes, o mapeamento observado foi:

```text
Class 1 = Panela
Class 2 = Garfo
Class 3 = Colher
```

## 5. Experimentos de treinamento

As seguintes configurações foram confirmadas por prints do modelo principal:

| Configuração | Epochs | Batch Size | Learning Rate | Situação |
|---|---:|---:|---:|---|
| A | 50 | 16 | 0.001 | Confirmada por múltiplos testes |
| B | 70 | 32 | 0.001 | Confirmada por teste |

A comparação considera não apenas se a classificação foi correta, mas também a confiança apresentada e a estabilidade do modelo diante de imagens diferentes.

## 6. Testes com imagens inéditas

Nos envios finais foram recebidos 15 prints. Um deles, referente a um Garfo classificado com 91%, era repetido. Para preservar a validade da avaliação, ele foi contabilizado apenas uma vez.

Assim, foram considerados **14 testes únicos e inéditos**:

| Classe | Testes únicos | Acertos | Erros | Taxa de acerto |
|---|---:|---:|---:|---:|
| Garfo | 4 | 3 | 1 | 75% |
| Panela | 5 | 5 | 0 | 100% |
| Colher | 5 | 5 | 0 | 100% |
| **Total** | **14** | **13** | **1** | **92,86%** |

Principais exemplos registrados:

- Colher classificada corretamente com 100% de confiança em cinco testes únicos;
- Panela classificada corretamente com confianças de 53%, 71%, 96% e 100% nos exemplos documentados;
- Garfo classificado corretamente com 91%, 94% e 98%;
- um Garfo classificado incorretamente como Colher com 54%, enquanto Garfo recebeu 46%.

## 7. Resultados finais

### 7.1 Acurácia geral

```text
Total de testes únicos: 14
Acertos: 13
Erros: 1
Acurácia final: 92,86%
```

A acurácia foi calculada pela fórmula:

```text
Acurácia = (acertos / total de testes) × 100
Acurácia = (13 / 14) × 100
Acurácia = 92,86%
```

### 7.2 Desempenho por classe

| Classe | Testes | Acertos | Erros | Acurácia |
|---|---:|---:|---:|---:|
| Garfo | 4 | 3 | 1 | 75% |
| Panela | 5 | 5 | 0 | 100% |
| Colher | 5 | 5 | 0 | 100% |

### 7.3 Precisão formal por classe

A precisão foi calculada como `TP / (TP + FP)`, considerando as previsões feitas para cada classe.

| Classe prevista | Verdadeiros positivos | Falsos positivos | Precisão |
|---|---:|---:|---:|
| Garfo | 3 | 0 | 100% |
| Panela | 5 | 0 | 100% |
| Colher | 5 | 1 | 83,33% |
| **Média macro** | — | — | **94,44%** |

A classe Colher apresentou precisão menor porque recebeu uma previsão incorreta proveniente de uma imagem de Garfo.

## 8. Justificativa técnica dos resultados

O modelo apresentou comportamento consistente para Panela e Colher, com 100% de acerto nos testes únicos registrados dessas duas classes. Entretanto, a confiança das previsões variou. Uma Panela foi classificada corretamente com apenas 53%, enquanto a classe Colher recebeu 47%. Em outro teste de Panela, a confiança foi de 71% contra 29% para Colher. Isso demonstra que uma classificação correta não significa necessariamente alta certeza.

A maior dificuldade observada envolveu Garfo e Colher. Ambas as classes possuem formato alongado, material semelhante e podem ocupar regiões parecidas da imagem. No único erro do lote final, um Garfo foi classificado como Colher com 54%, enquanto Garfo ficou com 46%. A proximidade entre as probabilidades indica uma decisão incerta do modelo.

Fundos, iluminação, posição e orientação dos utensílios também podem modificar os padrões visuais percebidos pelo classificador. Dessa forma, a diversidade das imagens é um fator importante tanto no treinamento quanto na avaliação.

## 9. Análise do erro principal

```text
Classe real: Garfo
Classe prevista: Colher
Confiança da previsão: 54%
Probabilidade de Garfo: 46%
Resultado: Erro
```

Esse teste evidencia uma limitação real do modelo. A diferença de apenas 8 pontos percentuais entre Colher e Garfo indica que o classificador encontrou características compatíveis com ambas as classes.

## 10. Análise crítica

Os resultados mostram que o modelo conseguiu classificar corretamente a maior parte das imagens testadas, alcançando 92,86% de acurácia no conjunto de 14 testes únicos e inéditos. Panela e Colher tiveram os melhores resultados em taxa de acerto, sem erros no lote analisado.

Garfo apresentou maior dificuldade. Embora três imagens tenham sido corretamente reconhecidas com confiança alta, uma imagem foi confundida com Colher. Esse resultado é coerente com a proximidade visual entre essas duas categorias e mostra que o modelo ainda pode ser melhorado com mais exemplos variados.

Outro ponto relevante é a variação de confiança. Alguns exemplos foram classificados com 100%, enquanto outros acertos ocorreram com 53% ou 71%. Portanto, além da taxa de acerto, a distribuição das probabilidades também foi considerada na interpretação do desempenho.

A precisão formal também reforça a análise: Garfo e Panela apresentaram 100% de precisão no conjunto avaliado, enquanto Colher apresentou 83,33% devido ao falso positivo originado pela imagem de Garfo classificada incorretamente.

Como o conjunto de teste ainda é relativamente pequeno, a acurácia deve ser entendida como o desempenho observado nas imagens avaliadas, e não como garantia de que o modelo manterá o mesmo resultado em qualquer cenário.

## 11. Sugestões de melhoria

- aumentar a quantidade e diversidade de imagens de Garfo;
- incluir mais imagens de Garfo e Colher em condições visuais semelhantes;
- variar iluminação, fundo, distância e orientação;
- incluir objetos parcialmente ocultos;
- ampliar o conjunto de testes em uma versão futura;
- alterar um hiperparâmetro por vez durante novos experimentos;
- em futuros treinamentos, variar também o learning rate para ampliar a comparação entre configurações;
- manter rigorosamente separados os conjuntos de treinamento e avaliação.

## 12. Conclusão

O projeto atingiu o objetivo de desenvolver um modelo de classificação de utensílios de cozinha utilizando o Google Teachable Machine. O modelo principal foi treinado de maneira equilibrada, com 160 imagens por classe, totalizando 480 amostras de treinamento.

Na avaliação final com 14 imagens inéditas e únicas, o modelo obteve 13 acertos e 1 erro, resultando em uma acurácia de **92,86%**. Panela e Colher alcançaram 100% de acerto nas imagens avaliadas, enquanto Garfo apresentou um caso de confusão com Colher.

Na métrica de precisão formal, Garfo e Panela atingiram 100% e Colher atingiu 83,33%, com média macro de 94,44%. Esses resultados mostram que o modelo é funcional, mas também revelam limitações importantes, especialmente na separação visual entre Garfo e Colher.

A atividade permitiu observar na prática como qualidade dos dados, variedade visual, configuração de treinamento e escolha das imagens de teste influenciam o desempenho de um sistema de visão computacional.

---

## Checklist antes da entrega

```text
[x] classes Garfo, Panela e Colher definidas
[x] modelo principal com 160 imagens por classe
[x] modelo exportado
[x] código Python modularizado
[x] RMs dos integrantes registrados
[x] Fase 1 confirmada
[x] Capítulo 2 confirmado
[x] imagens finais confirmadas como inéditas
[x] resultados únicos consolidados
[x] acurácia final de 92,86%
[x] precisão formal calculada
[x] análise crítica atualizada
[x] conclusão atualizada
[x] nome final do PDF definido: Grupo_Cap2_IA_Fase1.pdf
```
