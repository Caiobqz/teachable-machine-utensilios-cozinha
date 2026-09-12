# Registro dos Experimentos e Testes

Preencher apenas com dados reais observados no Teachable Machine.

## 1. Treinamentos

| Experimento | Epochs | Batch Size | Learning Rate | Resultado observado | Observações |
|---|---:|---:|---:|---|---|
| 1 | 50 | 16 | 0.001 | Configuração confirmada por print | Há evidências com 160 imagens por classe e também prints de outro estado com 10 imagens por classe; não misturar os resultados |
| 2 | 100 | 16 | 0.001 | PREENCHER | PREENCHER |
| 3 | 100 | 32 | 0.001 | PREENCHER | PREENCHER |

## 2. Configuração escolhida

```text
Experimento escolhido: PREENCHER
Epochs: PREENCHER
Batch Size: PREENCHER
Learning Rate: PREENCHER
```

Justificativa: **PREENCHER com base nos resultados reais.**

## 3. Testes com imagens inéditas

### Garfo

| Imagem | Classe real | Previsão | Confiança | Acertou? |
|---|---|---|---:|---|
| garfo_01 | Garfo | | | |
| garfo_02 | Garfo | | | |
| garfo_03 | Garfo | | | |
| garfo_04 | Garfo | | | |
| garfo_05 | Garfo | | | |
| garfo_06 | Garfo | | | |
| garfo_07 | Garfo | | | |
| garfo_08 | Garfo | | | |
| garfo_09 | Garfo | | | |
| garfo_10 | Garfo | | | |

### Panela

| Imagem | Classe real | Previsão | Confiança | Acertou? |
|---|---|---|---:|---|
| panela_01 | Panela | | | |
| panela_02 | Panela | | | |
| panela_03 | Panela | | | |
| panela_04 | Panela | | | |
| panela_05 | Panela | | | |
| panela_06 | Panela | | | |
| panela_07 | Panela | | | |
| panela_08 | Panela | | | |
| panela_09 | Panela | | | |
| panela_10 | Panela | | | |

### Colher

| Imagem | Classe real | Previsão | Confiança | Acertou? |
|---|---|---|---:|---|
| colher_01 | Colher | | | |
| colher_02 | Colher | | | |
| colher_03 | Colher | | | |
| colher_04 | Colher | | | |
| colher_05 | Colher | | | |
| colher_06 | Colher | | | |
| colher_07 | Colher | | | |
| colher_08 | Colher | | | |
| colher_09 | Colher | | | |
| colher_10 | Colher | | | |

## 4. Evidências recebidas até agora

### Modelo com 160 imagens por classe

Configuração confirmada:

```text
Colher: 160 imagens de treinamento
Garfo: 160 imagens de treinamento
Panela: 160 imagens de treinamento
Epochs: 50
Batch Size: 16
Learning Rate: 0.001
```

Resultados visíveis nos prints recebidos:

| Imagem observada | Previsão | Confiança visível | Observação |
|---|---|---:|---|
| Garfo isolado | Garfo | 100% | classificação correta aparente |
| Conjunto de panelas | Panela | 100% | classificação correta aparente |

### Outro estado do projeto com 10 imagens por classe

Também foram recebidos prints mostrando:

```text
Colher: 10 imagens
Garfo: 10 imagens
Panela: 10 imagens
Epochs: 50
Batch Size: 16
Learning Rate: 0.001
```

Resultados visíveis:

| Imagem observada | Previsão principal | Confiança principal | Outras probabilidades visíveis |
|---|---|---:|---|
| Quatro garfos | Garfo | 71% | Colher 22%; Panela ~6% |
| Conjunto de panelas | Panela | 100% | demais classes próximas de 0% |
| Conjunto misto com panelas/talheres | Panela | 100% | demais classes próximas de 0% |
| Cena de mesa com vários utensílios | Panela | 86% | Colher 13%; Garfo ~1% |
| Conjunto majoritariamente de colheres | Garfo | 82% | Panela 13%; Colher ~6% |

**Importante:** os prints de 10 imagens por classe não devem ser misturados com os resultados do modelo de 160 imagens por classe. Antes de calcular a acurácia final, o grupo deve definir qual conjunto/modelo será o oficial e realizar todos os testes finais nele.

## 5. Resultado geral

```text
Total de testes: PREENCHER
Acertos: PREENCHER
Erros: PREENCHER
Acurácia: PREENCHER %
```

## 6. Desempenho por classe

| Classe | Total | Acertos | Erros | Acurácia |
|---|---:|---:|---:|---:|
| Garfo | PREENCHER | PREENCHER | PREENCHER | PREENCHER |
| Panela | PREENCHER | PREENCHER | PREENCHER | PREENCHER |
| Colher | PREENCHER | PREENCHER | PREENCHER | PREENCHER |

## 7. Análise preliminar

Os prints já indicam que imagens simples e centradas podem ser classificadas com confiança muito alta. Ao mesmo tempo, imagens com vários utensílios ou classes visualmente semelhantes podem reduzir a confiança ou gerar confusões, especialmente entre Garfo e Colher.

Essa observação é preliminar. A análise final deve ser feita somente após os 30 testes oficiais usando o mesmo modelo.
