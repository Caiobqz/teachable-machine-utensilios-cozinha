# Relatório — Classificação de Utensílios de Cozinha com Teachable Machine

> Este arquivo reúne a estrutura do relatório final. Os campos marcados como **PREENCHER** ainda dependem dos dados acadêmicos finais ou da consolidação completa dos testes.

## Capa

**Instituição:** FIAP  
**Disciplina:** PREENCHER  
**Atividade:** Classificação de Utensílios de Cozinha com Inteligência Artificial  
**Fase:** PREENCHER  
**Capítulo:** PREENCHER  
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

As imagens utilizadas para avaliação devem permanecer separadas das imagens de treinamento.

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

## 5. Experimentos de treinamento

As seguintes configurações foram confirmadas por prints do modelo principal:

| Configuração | Epochs | Batch Size | Learning Rate | Situação |
|---|---:|---:|---:|---|
| A | 50 | 16 | 0.001 | Confirmada por múltiplos testes |
| B | 70 | 32 | 0.001 | Confirmada por teste |

A comparação deve considerar não apenas se a classificação foi correta, mas também a confiança apresentada pelo modelo e a estabilidade diante de imagens diferentes.

## 6. Testes documentados

Entre as evidências registradas no modelo principal, foram observados:

| Situação | Classe esperada | Previsão | Confiança | Resultado |
|---|---|---|---:|---|
| Garfo isolado | Garfo | Garfo | 100% | Acerto |
| Conjunto de panelas | Panela | Panela | 100% | Acerto |
| Cena com panelas visualmente dominantes | Panela | Panela | 98% | Acerto aparente |
| Garfos na Configuração B | Garfo | Garfo | 72% | Acerto |

Os prints correspondentes devem ser inseridos no PDF final como evidência do comportamento do modelo.

## 7. Resultados finais

### 7.1 Resultado geral

```text
Total de testes: PREENCHER
Acertos: PREENCHER
Erros: PREENCHER
Acurácia: PREENCHER %
```

A acurácia será calculada pela fórmula:

```text
Acurácia = (acertos / total de testes) × 100
```

### 7.2 Desempenho por classe

| Classe | Testes | Acertos | Erros | Acurácia |
|---|---:|---:|---:|---:|
| Garfo | PREENCHER | PREENCHER | PREENCHER | PREENCHER |
| Panela | PREENCHER | PREENCHER | PREENCHER | PREENCHER |
| Colher | PREENCHER | PREENCHER | PREENCHER | PREENCHER |

## 8. Justificativa técnica

Os testes já documentados indicam que a classe Panela apresentou comportamento consistente e previsões com confiança elevada. Garfo e Colher possuem maior semelhança visual, pois são objetos alongados e podem aparecer em posições e fundos semelhantes, o que pode reduzir a confiança do modelo.

Também foi observado que cenas com vários utensílios podem fazer o classificador priorizar a classe visualmente dominante, já que o modelo realiza classificação da imagem inteira e não detecção individual de cada objeto presente.

## 9. Análise crítica

A análise final deve considerar:

- qual classe apresentou maior estabilidade;
- quais classes apresentaram maior semelhança visual;
- influência de fundo, iluminação, distância e ângulo;
- diferenças de confiança entre as configurações testadas;
- desempenho em imagens inéditas;
- limitações do conjunto de dados.

## 10. Sugestões de melhoria

- ampliar o conjunto de imagens de teste;
- aumentar a diversidade de Garfo e Colher;
- incluir diferentes condições de iluminação;
- variar ainda mais fundo, distância e ângulo;
- testar objetos parcialmente ocultos;
- evitar cenas com várias classes no cálculo da acurácia de objeto único;
- registrar todos os testes no CSV para tornar a avaliação reproduzível.

## 11. Conclusão

O projeto demonstrou que o Google Teachable Machine pode ser utilizado para construir um classificador de imagens de maneira acessível. O modelo principal foi treinado de forma balanceada com 160 imagens por classe e apresentou resultados especialmente consistentes para Panela. Os testes também mostraram que a confiança pode variar conforme a semelhança visual entre as classes e a configuração de treinamento.

A conclusão final deverá ser complementada com a acurácia consolidada calculada a partir do conjunto completo de testes inéditos.

---

## Checklist antes da entrega

```text
[x] classes Garfo, Panela e Colher definidas
[x] modelo principal com 160 imagens por classe
[x] modelo exportado
[x] código Python modularizado
[x] RMs dos integrantes registrados
[x] evidências e prints organizados
[ ] fase, capítulo e disciplina preenchidos
[ ] acurácia final consolidada
[ ] print final do programa Python
[ ] PDF final revisado
[ ] nome do arquivo conforme padrão da faculdade
```
