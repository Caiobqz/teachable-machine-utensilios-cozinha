# Resumo Final dos Resultados

Este documento consolida os dados confirmados ate o momento para a entrega do projeto.

## 1. Conjunto principal de treinamento

| Classe | Imagens de treinamento |
|---|---:|
| Garfo | 160 |
| Panela | 160 |
| Colher | 160 |

Total de imagens de treinamento no modelo principal: **480**.

## 2. Informacoes tecnicas do modelo exportado

```text
Classes: Colher, Garfo e Panela
Quantidade de classes: 3
Tamanho de entrada: 224 x 224 pixels
Canais: RGB
Teachable Machine: 2.4.16
Formato exportado: TensorFlow.js
```

## 3. Configuracoes realmente documentadas

| Configuracao | Epochs | Batch Size | Learning Rate | Evidencia |
|---|---:|---:|---:|---|
| A | 50 | 16 | 0.001 | varios prints do modelo de 160 imagens por classe |
| B | 70 | 32 | 0.001 | print do modelo de 160 imagens por classe |

## 4. Resultados observados no modelo principal

Na configuracao A foram documentados:

- Garfo isolado classificado como Garfo com 100%;
- conjunto de panelas classificado como Panela com 100%;
- cena com panelas e outros utensilios classificada como Panela com 98%;
- outros tres exemplos de conjuntos de panelas classificados como Panela com 100%.

Na configuracao B foi documentado:

- imagem com quatro garfos classificada como Garfo com 72%;
- Colher recebeu 15% e Panela 14%, demonstrando maior incerteza da previsao.

## 5. Interpretacao dos resultados

Os exemplos documentados indicam desempenho particularmente forte para a classe Panela, com confiancas entre 98% e 100% nos testes apresentados. Garfo tambem foi reconhecido corretamente, mas a configuracao com 70 epochs e batch size 32 apresentou confianca menor de 72% em um dos testes.

Garfo e Colher possuem maior semelhanca visual entre si do que em relacao a Panela. Isso ajuda a explicar a maior distribuicao de probabilidades entre essas classes em imagens mais dificeis.

Imagens contendo diversos utensilios simultaneamente devem ser interpretadas com cuidado, pois o modelo realiza classificacao de imagem e nao deteccao individual de todos os objetos presentes. Nesses casos, ele tende a escolher a classe visualmente dominante.

## 6. Comparacao com o modelo menor

Tambem foram testados exemplos de um modelo anterior com apenas 10 imagens por classe. Esse modelo apresentou varios acertos isolados, mas tambem houve um caso de confusao relevante no qual uma imagem majoritariamente de colheres foi classificada como Garfo com 82% de confianca.

Essa evidencia reforca a importancia de um conjunto de treinamento maior e mais variado.

## 7. Limitacao para a acuracia final

Os prints recebidos nao constituem um conjunto final equilibrado e completo de testes ineditos das tres classes no mesmo modelo. Por esse motivo, ainda nao e metodologicamente correto declarar uma acuracia geral oficial apenas com esses registros.

A acuracia final deve ser obtida a partir do conjunto completo de testes ineditos, usando:

```text
Acuracia = (acertos / total de testes) x 100
```

## 8. Analise critica

Pontos fortes observados:

- alta confianca na classe Panela;
- capacidade de reconhecer diferentes formatos de panelas;
- classificacao correta de Garfo em exemplos simples;
- conjunto principal de treinamento equilibrado, com 160 imagens por classe.

Pontos de atencao:

- maior semelhanca visual entre Garfo e Colher;
- confianca menor em alguns exemplos de Garfo;
- cenas com varios tipos de utensilios geram ambiguidade;
- classificacao de imagem nao equivale a localizar todos os objetos da cena.

## 9. Melhorias propostas

- aumentar a variedade de Garfos e Colheres;
- incluir fundos e iluminacoes ainda mais diferentes;
- adicionar imagens com objetos parcialmente ocultos;
- evitar excesso de cenas contendo diversas classes simultaneamente nos testes de acuracia;
- repetir experimentos alterando um hiperparametro por vez;
- manter o conjunto de teste separado do treinamento.

## 10. Conclusao preliminar

O modelo demonstrou capacidade de diferenciar Garfo, Panela e Colher, com resultados especialmente consistentes para Panela. Os testes tambem mostraram que a confianca pode variar conforme a configuracao do treinamento e a composicao da imagem. A principal dificuldade observada envolve a semelhanca visual entre Garfo e Colher e cenas com varios utensilios ao mesmo tempo.

A conclusao definitiva do trabalho deve incluir a acuracia calculada a partir do conjunto completo de testes ineditos.
