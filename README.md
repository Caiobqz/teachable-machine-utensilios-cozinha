# Teachable Machine - Utensílios de Cozinha

Projeto acadêmico para criação e avaliação de um modelo de classificação de imagens utilizando o Google Teachable Machine.

## Objetivo

Treinar um modelo capaz de identificar diferentes utensílios de cozinha a partir de fotografias e avaliar seu desempenho com imagens não utilizadas no treinamento.

## Classes sugeridas

- Garfo
- Panela
- Espátula

## Estrutura prevista

```text
imagens/
  treino/
    garfo/
    panela/
    espatula/
  teste/
    garfo/
    panela/
    espatula/
codigo/
  analise_resultados.py
resultados/
  testes.md
  testes.csv
prints/
relatorio/
```

## Etapas

1. Coletar imagens para as três classes.
2. Separar imagens entre treino e teste.
3. Criar o modelo no Teachable Machine.
4. Testar diferentes valores de Epochs, Batch Size e Learning Rate.
5. Registrar previsões, confiança, acertos e erros.
6. Calcular a acurácia.
7. Analisar criticamente os resultados.
8. Elaborar o relatório final em PDF.

## Código-base

O arquivo `codigo/analise_resultados.py` foi deixado propositalmente incompleto em algumas partes marcadas com `TODO`. Essas partes devem ser desenvolvidas durante a atividade para praticar listas, dicionários, funções, estruturas condicionais, repetição e cálculo de acurácia.

## Próxima tarefa

Implemente primeiro apenas a função `registrar_teste()` e teste um caso simples, por exemplo:

```text
Imagem: garfo01.jpg
Classe real: Garfo
Classe prevista: Garfo
Confiança: 95
```
