# Relatório — Classificação de Utensílios de Cozinha com Teachable Machine

## Capa

**Instituição:** FIAP  
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
- avaliar acertos, erros, confiança e acurácia do modelo;
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

Para que a avaliação represente a capacidade de generalização do modelo, as imagens de teste devem ser diferentes das imagens utilizadas durante o treinamento.

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

## 6. Testes com imagens novas

Nos envios mais recentes foram recebidos 15 prints. Um deles, referente a um Garfo classificado com 91%, era repetido. Para preservar a validade da avaliação, ele foi contabilizado apenas uma vez.

Assim, foram considerados **14 testes únicos**:

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

### 7.1 Resultado geral

```text
Total de testes únicos: 14
Acertos: 13
Erros: 1
Acurácia observada: 92,86%
```

A acurácia foi calculada pela fórmula:

```text
Acurácia = (acertos / total de testes) × 100
Acurácia = (13 / 14) × 100
Acurácia = 92,86%
```

**Observação:** este resultado deve ser apresentado como acurácia final do experimento apenas se o grupo confirmar que essas imagens não faziam parte das 160 imagens utilizadas no treinamento de cada classe.

### 7.2 Desempenho por classe

| Classe | Testes | Acertos | Erros | Acurácia |
|---|---:|---:|---:|---:|
| Garfo | 4 | 3 | 1 | 75% |
| Panela | 5 | 5 | 0 | 100% |
| Colher | 5 | 5 | 0 | 100% |

## 8. Justificativa técnica dos resultados

O modelo apresentou comportamento consistente para Panela e Colher, com 100% de acerto nos testes únicos registrados dessas duas classes. Entretanto, a confiança das previsões variou. Uma Panela foi classificada corretamente com apenas 53%, enquanto a classe Colher recebeu 47%. Em outro teste de Panela, a confiança foi de 71% contra 29% para Colher. Isso demonstra que uma classificação correta não significa necessariamente alta certeza.

A maior dificuldade observada envolveu Garfo e Colher. Ambas as classes possuem formato alongado, material semelhante e podem ocupar regiões parecidas da imagem. No único erro do lote recente, um Garfo foi classificado como Colher com 54%, enquanto Garfo ficou com 46%. A proximidade entre as probabilidades indica uma decisão incerta do modelo.

Fundos, iluminação, posição e orientação dos utensílios também podem modificar os padrões visuais percebidos pelo classificador. Dessa forma, a diversidade das imagens é um fator importante tanto no treinamento quanto na avaliação.

## 9. Análise do erro principal

```text
Classe real: Garfo
Classe prevista: Colher
Confiança da previsão: 54%
Probabilidade de Garfo: 46%
Resultado: Erro
```

Esse teste é importante porque evidencia uma limitação real do modelo. A diferença de apenas 8 pontos percentuais entre Colher e Garfo indica que o classificador encontrou características compatíveis com ambas as classes. A semelhança visual entre os utensílios e as condições da imagem podem ter contribuído para o resultado.

## 10. Análise crítica

Os resultados mostram que o modelo conseguiu classificar corretamente a maior parte das imagens testadas, alcançando 92,86% de acurácia no conjunto de 14 testes únicos. Panela e Colher tiveram os melhores resultados, sem erros no lote analisado.

Garfo apresentou maior dificuldade. Embora três imagens tenham sido corretamente reconhecidas com confiança alta, uma imagem foi confundida com Colher. Esse resultado é coerente com a proximidade visual entre essas duas categorias e mostra que o modelo ainda pode ser melhorado com mais exemplos variados.

Outro ponto relevante é a variação de confiança. Alguns exemplos foram classificados com 100%, enquanto outros acertos ocorreram com 53% ou 71%. Portanto, além da taxa de acerto, a distribuição das probabilidades também foi considerada na interpretação do desempenho.

Como o conjunto de teste ainda é relativamente pequeno, a acurácia deve ser entendida como o desempenho observado nas imagens avaliadas, e não como garantia de que o modelo manterá o mesmo resultado em qualquer cenário.

## 11. Sugestões de melhoria

- aumentar a quantidade e diversidade de imagens de Garfo;
- incluir mais imagens de Garfo e Colher em condições visuais semelhantes;
- variar iluminação, fundo, distância e orientação;
- incluir objetos parcialmente ocultos;
- ampliar o conjunto de testes em uma versão futura;
- alterar um hiperparâmetro por vez durante novos experimentos;
- manter rigorosamente separados os conjuntos de treinamento e avaliação.

## 12. Conclusão

O projeto atingiu o objetivo de desenvolver um modelo de classificação de utensílios de cozinha utilizando o Google Teachable Machine. O modelo principal foi treinado de maneira equilibrada, com 160 imagens por classe, totalizando 480 amostras de treinamento.

No conjunto recente de 14 testes únicos, o modelo obteve 13 acertos e 1 erro, resultando em uma acurácia observada de **92,86%**. Panela e Colher alcançaram 100% de acerto nas imagens avaliadas, enquanto Garfo apresentou um caso de confusão com Colher.

A análise mostrou que o modelo é funcional, mas também revelou limitações importantes. A semelhança entre Garfo e Colher e a variação de confiança em algumas imagens indicam que mais diversidade de dados poderia aumentar a robustez do classificador. Dessa forma, além de demonstrar o funcionamento da ferramenta, o projeto permitiu observar na prática como qualidade dos dados, variedade visual e configuração de treinamento influenciam o desempenho de um sistema de visão computacional.

---

## Checklist antes da entrega

```text
[x] classes Garfo, Panela e Colher definidas
[x] modelo principal com 160 imagens por classe
[x] modelo exportado
[x] código Python modularizado
[x] RMs dos integrantes registrados
[x] evidências e prints organizados
[x] acurácia observada calculada com os testes únicos
[x] análise crítica atualizada
[x] conclusão atualizada
[ ] confirmar que as imagens dos testes recentes eram inéditas
[ ] gerar print final do programa Python com os mesmos dados
[ ] revisar e gerar o PDF definitivo
[ ] nomear o arquivo conforme o padrão da faculdade
```
