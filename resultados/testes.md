# Registro dos Experimentos e Testes

Este arquivo reúne somente dados realmente observados nos prints e arquivos exportados do projeto.

## 1. Modelo principal

O modelo principal definido para a entrega é o treinado com **160 imagens por classe**:

- Garfo: 160 imagens de treinamento;
- Panela: 160 imagens de treinamento;
- Colher: 160 imagens de treinamento.

O modelo exportado possui entrada de 224 x 224 pixels em RGB e três classes: Garfo, Panela e Colher.

## 2. Configuracoes de treinamento confirmadas

| Experimento | Epochs | Batch Size | Learning Rate | Situacao |
|---|---:|---:|---:|---|
| A | 50 | 16 | 0.001 | confirmado por varios prints do modelo de 160 imagens/classe |
| B | 70 | 32 | 0.001 | confirmado por print do modelo de 160 imagens/classe |

Nao foram recebidas evidencias suficientes para registrar como reais as configuracoes 100/16/0.001 e 100/32/0.001. Elas nao devem ser apresentadas como executadas sem novos prints.

## 3. Testes documentados - modelo de 160 imagens por classe

### Configuracao A - 50 epochs, batch 16, learning rate 0.001

| Teste | Conteudo da imagem | Classe esperada/predominante | Previsao | Confianca | Resultado |
|---|---|---|---|---:|---|
| A1 | Garfo isolado | Garfo | Garfo | 100% | Acerto |
| A2 | Conjunto de panelas | Panela | Panela | 100% | Acerto |
| A3 | Cena com panelas e outros utensilios | Panela (predominante) | Panela | 98% | Acerto aparente |
| A4 | Conjunto de panelas/recipientes | Panela | Panela | 100% | Acerto |
| A5 | Conjunto de panelas de pressao | Panela | Panela | 100% | Acerto |
| A6 | Panelas e frigideiras | Panela | Panela | 100% | Acerto |

### Configuracao B - 70 epochs, batch 32, learning rate 0.001

| Teste | Conteudo da imagem | Classe esperada | Previsao | Confianca | Outras probabilidades visiveis | Resultado |
|---|---|---|---|---:|---|---|
| B1 | Quatro garfos | Garfo | Garfo | 72% | Colher 15%; Panela 14% | Acerto |

## 4. Observacoes importantes

- A classe **Panela** apresentou classificacoes muito seguras nos exemplos documentados, normalmente entre 98% e 100%.
- O teste de Garfo com a configuracao 70/32/0.001 foi correto, mas a confianca caiu para 72%, mostrando maior incerteza do modelo.
- Cenas com varios objetos nao constituem um teste ideal de classificacao de objeto unico. Nelas, o modelo tende a selecionar a classe visualmente dominante.
- Garfo e Colher sao visualmente mais semelhantes entre si do que Panela, o que pode elevar a ambiguidade em alguns casos.

## 5. Modelo de 10 imagens por classe - apenas comparacao

Tambem foram documentados testes de um modelo anterior com apenas 10 imagens de treinamento por classe. Esses resultados **nao devem ser misturados** com o modelo principal de 160 imagens por classe.

Exemplos observados nesse modelo menor:

| Classe real | Previsao | Confianca | Resultado |
|---|---|---:|---|
| Garfo | Garfo | 99% | Acerto |
| Panela | Panela | 98% | Acerto |
| Colher | Colher | 86% | Acerto |
| Colher | Colher | 93% | Acerto |
| Garfo | Garfo | 100% | Acerto |

Tambem foi observado anteriormente um caso em que uma imagem majoritariamente de colheres foi classificada como Garfo com 82%, evidenciando a possibilidade de confusao entre as duas classes.

## 6. Acuracia

Os prints recebidos permitem afirmar que os exemplos documentados acima foram classificados conforme indicado, mas **nao formam um conjunto final equilibrado de testes suficiente para calcular uma acuracia oficial geral do projeto**.

Para uma acuracia final academica confiavel, deve-se usar somente testes ineditos do mesmo modelo e registrar o total de acertos dividido pelo total de testes.

Formula:

```text
Acuracia = (acertos / total de testes) x 100
```

## 7. Evidencias recomendadas para o PDF

Usar no relatorio:

1. print mostrando as 160 imagens por classe;
2. print da configuracao 50 / 16 / 0.001;
3. exemplo de Garfo com 100%;
4. exemplos de Panela com 98% e 100%;
5. print da configuracao 70 / 32 / 0.001 com Garfo em 72%;
6. explicacao sobre a queda de confianca e possivel confusao entre Garfo e Colher;
7. print do programa Python quando a acuracia final for calculada.
