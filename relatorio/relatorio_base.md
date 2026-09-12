# Relatório — Classificação de Utensílios de Cozinha com Teachable Machine

> Preencher os campos marcados como **PREENCHER** somente com dados reais do grupo.

## Capa

**Instituição:** FIAP  
**Disciplina:** PREENCHER  
**Atividade:** Classificação de Utensílios de Cozinha com Inteligência Artificial  
**Fase:** PREENCHER  
**Capítulo:** PREENCHER  
**Integrantes e RMs:** PREENCHER  
**Ano:** 2026

---

## 1. Introdução

A visão computacional permite que sistemas de inteligência artificial identifiquem padrões visuais em imagens. Neste projeto, foi utilizado o Google Teachable Machine para desenvolver um modelo capaz de classificar utensílios de cozinha em três categorias: Garfo, Panela e Colher. O trabalho envolveu coleta e separação de imagens, treinamento do modelo, experimentos com hiperparâmetros, testes com imagens inéditas e análise dos resultados.

## 2. Objetivos

- desenvolver um modelo capaz de classificar utensílios de cozinha a partir de fotografias;
- aplicar conceitos básicos de aprendizado de máquina e visão computacional;
- utilizar o Google Teachable Machine para treinamento e teste;
- comparar diferentes configurações de treinamento;
- avaliar acertos, erros, confiança e acurácia do modelo.

## 3. Metodologia

O projeto foi dividido em coleta de dados, treinamento, experimentação e avaliação. As classes utilizadas foram Garfo, Panela e Colher. As imagens foram divididas em conjuntos independentes de treinamento e teste para evitar que o modelo fosse avaliado com as mesmas imagens utilizadas no aprendizado.

### 3.1 Classes

- Garfo
- Panela
- Colher

### 3.2 Quantidade de imagens

| Classe | Treinamento | Teste | Total |
|---|---:|---:|---:|
| Garfo | PREENCHER | PREENCHER | PREENCHER |
| Panela | PREENCHER | PREENCHER | PREENCHER |
| Colher | PREENCHER | PREENCHER | PREENCHER |

### 3.3 Critérios de seleção

As imagens foram selecionadas buscando boa iluminação, foco adequado e presença clara do utensílio principal. Também foram utilizadas variações de ângulo, distância, posição, fundo e iluminação para reduzir a dependência de padrões específicos do cenário.

**Adicionar aqui um print da organização das imagens.**

## 4. Configuração do modelo

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

**Adicionar print das três classes carregadas no Teachable Machine.**

## 5. Experimentos de treinamento

Foram realizados treinamentos alterando Epochs, Batch Size e Learning Rate.

| Experimento | Epochs | Batch Size | Learning Rate | Resultado observado |
|---|---:|---:|---:|---|
| 1 | 50 | 16 | 0.001 | PREENCHER |
| 2 | 100 | 16 | 0.001 | PREENCHER |
| 3 | 100 | 32 | 0.001 | PREENCHER |

**Adicionar prints das configurações e dos resultados de cada experimento.**

### 5.1 Configuração escolhida

```text
Epochs: PREENCHER
Batch Size: PREENCHER
Learning Rate: PREENCHER
```

**Justificativa:** PREENCHER com base nos resultados reais observados.

## 6. Testes com imagens inéditas

O modelo final foi testado utilizando imagens que não fizeram parte do conjunto de treinamento.

Quantidade total de testes: **PREENCHER**.

**Adicionar prints de pelo menos um teste de Garfo, um de Panela, um de Colher e um erro relevante, caso ocorra.**

## 7. Resultados

### 7.1 Resultado geral

```text
Total de testes: PREENCHER
Acertos: PREENCHER
Erros: PREENCHER
Acurácia: PREENCHER %
```

A acurácia foi calculada pela fórmula:

```text
Acurácia = (acertos / total de testes) × 100
```

### 7.2 Desempenho por classe

| Classe | Testes | Acertos | Erros | Acurácia |
|---|---:|---:|---:|---:|
| Garfo | PREENCHER | PREENCHER | PREENCHER | PREENCHER |
| Panela | PREENCHER | PREENCHER | PREENCHER | PREENCHER |
| Colher | PREENCHER | PREENCHER | PREENCHER | PREENCHER |

**Adicionar print do programa Python mostrando a acurácia e o desempenho por classe.**

## 8. Justificativa técnica dos resultados

PREENCHER após os testes. A análise deve relacionar os resultados com fatores como:

- diversidade das imagens;
- iluminação;
- fundo;
- ângulo;
- semelhança visual entre Garfo e Colher;
- quantidade de exemplos;
- configuração de treinamento.

## 9. Análise dos erros

Registrar os principais erros observados.

Exemplo de estrutura:

```text
Imagem: PREENCHER
Classe real: PREENCHER
Classe prevista: PREENCHER
Confiança: PREENCHER
Possível causa: PREENCHER
```

## 10. Análise crítica

Responder com base nos dados reais:

- qual classe teve melhor desempenho;
- qual teve pior desempenho;
- quais confusões ocorreram;
- se fundo, iluminação ou ângulo influenciaram;
- se houve previsão errada com confiança alta;
- se os dados foram suficientes;
- se o modelo generalizou para imagens novas.

## 11. Sugestões de melhoria

Possíveis melhorias, desde que relacionadas aos resultados observados:

- aumentar o número de imagens;
- variar mais os fundos;
- variar iluminação e distância;
- incluir mais ângulos;
- incluir objetos parcialmente ocultos;
- equilibrar rigorosamente as classes;
- repetir treinamentos com outras configurações;
- incluir novos utensílios em versões futuras.

## 12. Conclusão

PREENCHER somente após os testes finais. A conclusão deve informar se o objetivo foi atingido, a acurácia final, principais pontos fortes, limitações e próximos passos.

---

## Checklist de evidências do PDF

```text
[ ] classes criadas
[ ] imagens carregadas
[ ] separação treino/teste explicada
[ ] configurações avançadas
[ ] experimento 1
[ ] experimento 2
[ ] experimento 3
[ ] configuração final justificada
[ ] testes de Garfo
[ ] testes de Panela
[ ] testes de Colher
[ ] erro do modelo, se houver
[ ] acurácia final
[ ] desempenho por classe
[ ] programa Python
[ ] análise crítica
[ ] conclusão
```
