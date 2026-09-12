# Como começar a trabalhar no projeto

Este guia organiza o trabalho do grupo para o projeto de classificação de utensílios com Google Teachable Machine.

## Objetivo

Criar, testar e avaliar um modelo capaz de classificar três utensílios:

- Garfo
- Panela
- Colher

Depois, registrar os resultados, calcular a acurácia e documentar tudo em um relatório PDF.

---

# 1. Suellen Hellen Pereira Silva — imagens

## Responsabilidade

Preparar as imagens de treinamento e teste.

## Como fazer

1. Separar imagens de Garfo, Panela e Colher.
2. Tentar usar aproximadamente 30 imagens de treino e 10 de teste por classe.
3. Variar ângulo, posição, distância, fundo e iluminação.
4. Evitar imagens borradas, muito escuras, repetidas ou com muitos objetos extras.
5. Não usar a mesma imagem em treino e teste.
6. Organizar assim:

```text
imagens/treino/garfo/
imagens/treino/panela/
imagens/treino/colher/

imagens/teste/garfo/
imagens/teste/panela/
imagens/teste/colher/
```

## Entrega

- quantidade real de imagens por classe;
- confirmação de separação treino/teste;
- prints da organização;
- observações sobre qualidade das imagens.

---

# 2. Paulo Vitor Isidoro Silva — modelo inicial

## Responsabilidade

Criar o projeto no Teachable Machine e realizar o treinamento inicial.

## Como fazer

1. Acessar o Google Teachable Machine.
2. Escolher `Image Project`.
3. Escolher `Standard Image Model`.
4. Criar as classes Garfo, Panela e Colher.
5. Carregar somente imagens de treinamento.
6. Conferir se cada imagem está na classe correta.
7. Fazer o treinamento inicial.
8. Testar rapidamente as três classes.

## Prints necessários

- classes criadas;
- imagens carregadas;
- tela de treinamento;
- treinamento concluído;
- exemplo de previsão.

## Entrega

- modelo criado;
- quantidade de imagens por classe;
- prints;
- observações do primeiro treinamento.

---

# 3. Kauê Cavalcanti Araujo — experimentos

## Responsabilidade

Testar configurações avançadas e comparar resultados.

## Experimentos sugeridos

| Experimento | Epochs | Batch Size | Learning Rate |
|---|---:|---:|---:|
| 1 | 50 | 16 | 0.001 |
| 2 | 100 | 16 | 0.001 |
| 3 | 100 | 32 | 0.001 |

## Como fazer

Para cada experimento:

1. configurar os parâmetros;
2. tirar print da configuração;
3. treinar o modelo;
4. registrar o resultado observado;
5. tirar print do resultado;
6. anotar diferenças entre os treinamentos.

No final, indicar qual configuração pareceu melhor e justificar com os resultados reais.

## Entrega

- tabela dos três experimentos;
- prints das configurações;
- resultados observados;
- indicação da configuração final.

---

# 4. Caio Barros Queiroz — análise em Python e integração

## Responsabilidade

Registrar os testes reais do modelo, calcular acurácia, exportar os resultados e integrar o material final.

O código já está organizado em módulos:

```text
codigo/
  analise_resultados.py
  sistema.py
  cadastro.py
  analise.py
  exportacao.py
```

Para executar:

```powershell
python codigo\analise_resultados.py
```

## Dados que devem ser registrados

Para cada imagem de teste:

- nome da imagem;
- classe real;
- classe prevista;
- confiança;
- acerto ou erro.

Depois usar o programa para:

- visualizar resultados;
- calcular acurácia geral;
- calcular desempenho por classe;
- verificar quantidade de testes por classe;
- exportar `resultados/testes.csv`.

## Entrega

- CSV final;
- acurácia geral;
- desempenho por classe;
- total de acertos e erros;
- prints do programa;
- resumo dos erros relevantes.

---

# 5. Testes finais — grupo

Depois de escolher o melhor treinamento, testar apenas imagens que não foram usadas no treino.

Sugestão:

```text
Garfo: 10 testes
Panela: 10 testes
Colher: 10 testes
Total: 30 testes
```

Para cada teste registrar previsão e confiança. Guardar também erros do modelo, pois eles serão usados na análise crítica.

---

# 6. Informações técnicas já confirmadas no modelo exportado

O arquivo exportado pelo Teachable Machine confirmou:

```text
Classes: Colher, Garfo e Panela
Quantidade de classes: 3
Entrada: 224 × 224 pixels
Canais: RGB (3 canais)
Teachable Machine: 2.4.16
Formato exportado: TensorFlow.js
```

Essas informações podem ser usadas na metodologia do relatório.

---

# 7. Relatório final

O PDF deve incluir:

1. Capa
2. Integrantes
3. Introdução
4. Objetivos
5. Metodologia
6. Coleta de dados
7. Separação treino/teste
8. Classes utilizadas
9. Treinamento
10. Experimentos com Epochs, Batch Size e Learning Rate
11. Testes com imagens inéditas
12. Resultados
13. Acurácia geral e por classe
14. Análise dos erros
15. Justificativa técnica
16. Análise crítica
17. Sugestões de melhoria
18. Conclusão

---

# 8. Git

Antes de trabalhar:

```powershell
git pull origin main
```

Para enviar alterações:

```powershell
git status
git add .
git commit -m "Descrição do que foi feito"
git push origin main
```

---

# 9. Regra de passagem entre integrantes

Antes de considerar uma etapa concluída:

```text
[ ] tarefa concluída
[ ] arquivos organizados
[ ] resultados registrados
[ ] prints salvos
[ ] nenhum dado inventado
[ ] próxima pessoa recebeu o necessário
```
