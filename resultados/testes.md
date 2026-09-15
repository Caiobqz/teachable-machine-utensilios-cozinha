# Registro dos Experimentos e Testes

Este arquivo reúne somente dados realmente observados nos prints e arquivos exportados do projeto.

## 1. Modelo principal

O modelo principal definido para a entrega é o treinado com **160 imagens por classe**:

- Garfo: 160 imagens de treinamento;
- Panela: 160 imagens de treinamento;
- Colher: 160 imagens de treinamento.

O modelo exportado possui entrada de 224 x 224 pixels em RGB e três classes: Garfo, Panela e Colher.

Mapeamento observado na interface do Teachable Machine:

- Class 1 = Panela
- Class 2 = Garfo
- Class 3 = Colher

## 2. Configurações de treinamento confirmadas

| Experimento | Epochs | Batch Size | Learning Rate | Situação |
|---|---:|---:|---:|---|
| A | 50 | 16 | 0.001 | confirmado por vários prints do modelo de 160 imagens/classe |
| B | 70 | 32 | 0.001 | confirmado por print do modelo de 160 imagens/classe |

Não foram recebidas evidências suficientes para registrar como reais as configurações 100/16/0.001 e 100/32/0.001. Elas não devem ser apresentadas como executadas sem novos prints.

## 3. Testes documentados - modelo de 160 imagens por classe

### 3.1 Evidências anteriores

| Teste | Conteúdo da imagem | Classe esperada/predominante | Previsão | Confiança | Resultado |
|---|---|---|---|---:|---|
| A1 | Garfo isolado | Garfo | Garfo | 100% | Acerto |
| A2 | Conjunto de panelas | Panela | Panela | 100% | Acerto |
| A3 | Cena com panelas e outros utensílios | Panela (predominante) | Panela | 98% | Acerto aparente |
| A4 | Conjunto de panelas/recipientes | Panela | Panela | 100% | Acerto |
| A5 | Conjunto de panelas de pressão | Panela | Panela | 100% | Acerto |
| A6 | Panelas e frigideiras | Panela | Panela | 100% | Acerto |

### 3.2 Configuração B - 70 epochs, batch 32, learning rate 0.001

| Teste | Conteúdo da imagem | Classe esperada | Previsão | Confiança | Outras probabilidades visíveis | Resultado |
|---|---|---|---|---:|---|---|
| B1 | Quatro garfos | Garfo | Garfo | 72% | Colher 15%; Panela 14% | Acerto |

## 4. Lote recente de testes com imagens novas

Os prints mais recentes foram organizados abaixo. Um print de Garfo com **91%** apareceu repetido em dois envios; ele foi contado apenas uma vez para não inflar artificialmente a amostra.

### Colher

| Teste | Classe real | Previsão | Confiança | Resultado |
|---|---|---|---:|---|
| C1 | Colher | Colher | 100% | Acerto |
| C2 | Colher | Colher | 100% | Acerto |
| C3 | Colher | Colher | 100% | Acerto |
| C4 | Colher | Colher | 100% | Acerto |
| C5 | Colher | Colher | 100% | Acerto |

### Panela

| Teste | Classe real | Previsão | Confiança | Observação | Resultado |
|---|---|---|---:|---|---|
| P1 | Panela | Panela | 53% | Colher recebeu 47% | Acerto |
| P2 | Panela | Panela | 100% | - | Acerto |
| P3 | Panela | Panela | 96% | - | Acerto |
| P4 | Panela | Panela | 71% | Colher recebeu 29% | Acerto |
| P5 | Panela | Panela | 100% | - | Acerto |

### Garfo

| Teste | Classe real | Previsão | Confiança | Observação | Resultado |
|---|---|---|---:|---|---|
| G1 | Garfo | Garfo | 91% | print repetido em envio posterior; contado uma vez | Acerto |
| G2 | Garfo | Garfo | 94% | - | Acerto |
| G3 | Garfo | Garfo | 98% | - | Acerto |
| G4 | Garfo | Colher | 54% | Garfo recebeu 46% | **Erro** |

## 5. Resultado do lote recente

Considerando apenas os **14 testes únicos** visíveis nos prints recentes:

```text
Total de testes únicos: 14
Acertos: 13
Erros: 1
Acurácia observada: 92,86%
```

Desempenho por classe:

| Classe | Testes únicos | Acertos | Erros | Taxa de acerto |
|---|---:|---:|---:|---:|
| Colher | 5 | 5 | 0 | 100% |
| Panela | 5 | 5 | 0 | 100% |
| Garfo | 4 | 3 | 1 | 75% |
| **Total** | **14** | **13** | **1** | **92,86%** |

**Importante:** esses números só devem ser apresentados como avaliação final oficial se o grupo confirmar que todas essas imagens eram inéditas, isto é, não estavam entre as 160 imagens usadas no treinamento.

## 6. Análise dos resultados

O lote recente mostrou desempenho muito forte para Colher e Panela, ambas com 100% de acerto nas imagens testadas. Ainda assim, a confiança não foi sempre alta: duas imagens de Panela foram corretamente classificadas com apenas 53% e 71%, indicando que o modelo apresentou dúvida relevante em relação à classe Colher.

A principal dificuldade apareceu em Garfo. Em um dos testes, um garfo foi classificado como Colher com 54% de confiança, enquanto Garfo recebeu 46%. Esse erro é particularmente útil para a análise crítica porque confirma que Garfo e Colher são as classes visualmente mais próximas e que pequenas diferenças de fundo, ângulo, enquadramento ou iluminação podem alterar a decisão do modelo.

O resultado de 92,86% no conjunto de 14 testes únicos é bom para um modelo simples de classificação treinado no Teachable Machine, mas deve ser interpretado como resultado do conjunto testado e não como uma medida universal do desempenho do modelo.

## 7. Observações importantes

- A classe **Panela** apresentou classificações corretas em todas as imagens recentes, embora com níveis de confiança bastante diferentes.
- A classe **Colher** apresentou 100% de acerto nos cinco testes únicos recentes.
- O único erro do lote recente ocorreu entre **Garfo e Colher**, reforçando a maior semelhança visual entre essas classes.
- Prints repetidos não devem ser contados como testes diferentes.
- Cenas com vários objetos não constituem um teste ideal de classificação de objeto único.

## 8. Modelo de 10 imagens por classe - apenas comparação

Também foram documentados testes de um modelo anterior com apenas 10 imagens de treinamento por classe. Esses resultados **não devem ser misturados** com o modelo principal de 160 imagens por classe.

Exemplos observados nesse modelo menor:

| Classe real | Previsão | Confiança | Resultado |
|---|---|---:|---|
| Garfo | Garfo | 99% | Acerto |
| Panela | Panela | 98% | Acerto |
| Colher | Colher | 86% | Acerto |
| Colher | Colher | 93% | Acerto |
| Garfo | Garfo | 100% | Acerto |

Também foi observado anteriormente um caso em que uma imagem majoritariamente de colheres foi classificada como Garfo com 82% de confiança, evidenciando a possibilidade de confusão entre as duas classes.

## 9. Evidências recomendadas para o PDF

Usar no relatório:

1. print mostrando as 160 imagens por classe;
2. print da configuração 50 / 16 / 0.001;
3. pelo menos um teste correto de Colher;
4. uma Panela classificada corretamente com confiança baixa (53% ou 71%);
5. uma Panela classificada com 100%;
6. um Garfo corretamente classificado com confiança alta;
7. o Garfo classificado incorretamente como Colher com 54%, por ser o melhor exemplo para a análise crítica;
8. print do programa Python quando os resultados finais forem registrados.
