# Registro dos Experimentos e Testes

Este arquivo reúne somente dados realmente observados nos prints e arquivos exportados do projeto.

## 1. Modelo principal

O modelo principal definido para a entrega é o treinado com **160 imagens por classe**:

- Garfo: 160 imagens de treinamento;
- Panela: 160 imagens de treinamento;
- Colher: 160 imagens de treinamento.

O modelo exportado possui entrada de 224 x 224 pixels em RGB e três classes: Garfo, Panela e Colher.

Mapeamento visual confirmado pelos exemplos carregados no projeto:

- Class 1 = Panela;
- Class 2 = Garfo;
- Class 3 = Colher.

## 2. Configurações de treinamento confirmadas

| Experimento | Epochs | Batch Size | Learning Rate | Situação |
|---|---:|---:|---:|---|
| A | 50 | 16 | 0.001 | confirmado por vários prints do modelo de 160 imagens/classe |
| B | 70 | 32 | 0.001 | confirmado por print do modelo de 160 imagens/classe |

Não foram recebidas evidências suficientes para registrar como reais as configurações 100/16/0.001 e 100/32/0.001. Elas não devem ser apresentadas como executadas sem novos prints.

## 3. Testes documentados - modelo de 160 imagens por classe

### Configuração A - 50 epochs, batch 16, learning rate 0.001

| Teste | Conteúdo da imagem | Classe esperada/predominante | Previsão | Confiança | Resultado |
|---|---|---|---|---:|---|
| A1 | Garfo isolado | Garfo | Garfo | 100% | Acerto |
| A2 | Conjunto de panelas | Panela | Panela | 100% | Acerto |
| A3 | Cena com panelas e outros utensílios | Panela (predominante) | Panela | 98% | Acerto aparente |
| A4 | Conjunto de panelas/recipientes | Panela | Panela | 100% | Acerto |
| A5 | Conjunto de panelas de pressão | Panela | Panela | 100% | Acerto |
| A6 | Panelas e frigideiras | Panela | Panela | 100% | Acerto |

### Configuração B - 70 epochs, batch 32, learning rate 0.001

| Teste | Conteúdo da imagem | Classe esperada | Previsão | Confiança | Outras probabilidades visíveis | Resultado |
|---|---|---|---|---:|---|---|
| B1 | Quatro garfos | Garfo | Garfo | 72% | Colher 15%; Panela 14% | Acerto |

## 4. Novo lote de testes finais recebido

Em 15/09/2026 foi recebido um novo lote com 9 imagens testadas no modelo principal de 160 imagens por classe.

**Importante:** estes testes podem ser usados no cálculo oficial somente após a confirmação de que as imagens abaixo não estavam entre as 160 imagens de treinamento de suas respectivas classes.

| Teste | Classe real | Previsão | Confiança principal | Resultado |
|---|---|---|---:|---|
| T1 | Colher | Colher | 100% | Acerto |
| T2 | Colher | Colher | 100% | Acerto |
| T3 | Colher | Colher | 100% | Acerto |
| T4 | Panela | Panela | 53% | Acerto |
| T5 | Panela | Panela | 100% | Acerto |
| T6 | Garfo | Garfo | 91% | Acerto |
| T7 | Garfo | Garfo | 94% | Acerto |
| T8 | Garfo | Garfo | 98% | Acerto |
| T9 | Panela | Panela | 96% | Acerto |

### Resultado deste lote

```text
Total de testes: 9
Acertos: 9
Erros: 0
Acurácia observada no lote: 100%
```

Desempenho por classe neste lote:

| Classe | Testes | Acertos | Erros | Taxa de acerto |
|---|---:|---:|---:|---:|
| Colher | 3 | 3 | 0 | 100% |
| Panela | 3 | 3 | 0 | 100% |
| Garfo | 3 | 3 | 0 | 100% |

Apesar da taxa de acerto de 100% neste lote, a confiança não foi uniforme. O caso mais relevante foi uma Panela reconhecida corretamente com apenas **53%**, enquanto Colher recebeu aproximadamente **47%**. Esse resultado é importante para a análise crítica, pois mostra que uma previsão correta pode ainda apresentar forte incerteza entre classes.

## 5. Observações importantes

- A classe **Panela** apresentou classificações muito seguras em vários exemplos, normalmente entre 96% e 100%, mas houve um teste correto com apenas 53% de confiança.
- Os três novos testes de Colher foram classificados corretamente com 100%.
- Os três novos testes de Garfo foram classificados corretamente com 91%, 94% e 98%.
- O teste de Garfo com a configuração 70/32/0.001 também foi correto, mas com confiança de 72%, mostrando maior incerteza naquele experimento.
- Cenas com vários objetos não constituem um teste ideal de classificação de objeto único. Nelas, o modelo tende a selecionar a classe visualmente dominante.
- Garfo e Colher são visualmente mais semelhantes entre si do que Panela, o que pode elevar a ambiguidade em alguns casos.

## 6. Modelo de 10 imagens por classe - apenas comparação

Também foram documentados testes de um modelo anterior com apenas 10 imagens de treinamento por classe. Esses resultados **não devem ser misturados** com o modelo principal de 160 imagens por classe.

Exemplos observados nesse modelo menor:

| Classe real | Previsão | Confiança | Resultado |
|---|---|---:|---|
| Garfo | Garfo | 99% | Acerto |
| Panela | Panela | 98% | Acerto |
| Colher | Colher | 86% | Acerto |
| Colher | Colher | 93% | Acerto |
| Garfo | Garfo | 100% | Acerto |

Também foi observado anteriormente um caso em que uma imagem majoritariamente de colheres foi classificada como Garfo com 82%, evidenciando a possibilidade de confusão entre as duas classes.

## 7. Acurácia

O novo lote possui distribuição equilibrada, com três testes de cada classe, e apresentou 9 acertos em 9 testes. Entretanto, para apresentar estes números como **acurácia oficial do trabalho**, é necessário confirmar que todas as 9 imagens eram inéditas, isto é, não foram usadas entre as 160 imagens de treinamento.

Se essa condição for confirmada, a acurácia deste lote é:

```text
Acurácia = (9 / 9) x 100 = 100%
```

Para uma avaliação ainda mais robusta, recomenda-se ampliar para 10 imagens inéditas por classe, totalizando 30 testes.

## 8. Evidências recomendadas para o PDF

Usar no relatório:

1. print mostrando as 160 imagens por classe;
2. print da configuração 50 / 16 / 0.001;
3. exemplos novos de Colher com 100%;
4. exemplo de Panela com 53% para discutir incerteza;
5. exemplo de Panela com 100% ou 96%;
6. exemplos de Garfo com 91%, 94% ou 98%;
7. print da configuração 70 / 32 / 0.001 com Garfo em 72%;
8. print do programa Python quando a acurácia final for consolidada.
