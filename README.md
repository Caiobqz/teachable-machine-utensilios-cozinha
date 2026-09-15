# 🍴 Teachable Machine — Utensílios de Cozinha

Projeto acadêmico de **Inteligência Artificial e Visão Computacional** desenvolvido com o Google Teachable Machine para classificar imagens de utensílios de cozinha.

> **Fase 1 — Raízes da Inteligência: preparando o terreno**  
> **Capítulo 2 — IA e seu mundo de possibilidades**

> O modelo trabalha com três classes: **Garfo**, **Panela** e **Colher**.

---

## 👥 Equipe

| Integrante | RM | Responsabilidade principal |
|---|---:|---|
| **Caio Barros Queiroz** | RM576443 | Código Python, análise dos resultados, acurácia e integração final |
| **Paulo Vitor Isidoro Silva** | RM575580 | Criação e treinamento inicial do modelo |
| **Kauê Cavalcanti Araujo** | RM576394 | Experimentos com hiperparâmetros e comparação |
| **Suellen Hellen Pereira Silva** | RM574778 | Coleta, seleção e organização das imagens |

---

## 🎯 Objetivo

Desenvolver e avaliar um modelo de classificação de imagens capaz de reconhecer diferentes utensílios de cozinha a partir de fotografias, aplicando conceitos introdutórios de aprendizado de máquina e visão computacional.

O projeto também busca analisar:

- comportamento do modelo em imagens inéditas;
- nível de confiança das previsões;
- diferenças de desempenho entre as classes;
- impacto de parâmetros de treinamento;
- limitações e possibilidades de melhoria.

---

## 🧠 Classes utilizadas

| Classe | Descrição |
|---|---|
| 🍴 **Garfo** | Utensílio com dentes utilizado para servir e consumir alimentos |
| 🍲 **Panela** | Recipiente utilizado para preparo e cozimento de alimentos |
| 🥄 **Colher** | Utensílio com cavidade utilizado para servir e consumir alimentos |

---

## 📊 Modelo principal

O modelo principal foi treinado com um conjunto equilibrado de imagens:

| Classe | Amostras de treinamento |
|---|---:|
| Garfo | 160 |
| Panela | 160 |
| Colher | 160 |
| **Total** | **480** |

Informações técnicas confirmadas no modelo exportado:

```text
Classes: Colher, Garfo e Panela
Entrada: 224 x 224 pixels
Canais: RGB
Formato exportado: TensorFlow.js
Teachable Machine: 2.4.16
```

Mapeamento observado na interface do Teachable Machine:

```text
Class 1 = Panela
Class 2 = Garfo
Class 3 = Colher
```

---

## ⚙️ Configurações documentadas

| Configuração | Epochs | Batch Size | Learning Rate |
|---|---:|---:|---:|
| A | 50 | 16 | 0.001 |
| B | 70 | 32 | 0.001 |

Os resultados e observações estão organizados em `resultados/testes.md` e `resultados/resumo_final.md`.

---

## ✅ Resultado final da avaliação

O grupo confirmou que as imagens utilizadas na avaliação final eram **inéditas**, ou seja, não faziam parte das 160 imagens de treinamento de cada classe.

Foram considerados **14 testes únicos**. Um print repetido foi removido da contagem para evitar duplicidade.

| Classe | Testes | Acertos | Erros | Acurácia |
|---|---:|---:|---:|---:|
| Garfo | 4 | 3 | 1 | 75% |
| Panela | 5 | 5 | 0 | 100% |
| Colher | 5 | 5 | 0 | 100% |
| **Total** | **14** | **13** | **1** | **92,86%** |

### Precisão por classe

Considerando a precisão formal `TP / (TP + FP)` no conjunto testado:

| Classe prevista | Precisão |
|---|---:|
| Garfo | 100% |
| Panela | 100% |
| Colher | 83,33% |
| **Média macro** | **94,44%** |

O único erro final ocorreu em uma imagem de **Garfo**, classificada como **Colher** com 54% de confiança, enquanto Garfo recebeu 46%.

---

## 🗂️ Estrutura do projeto

```text
teachable-machine-utensilios-cozinha/
│
├── codigo/
│   ├── analise_resultados.py
│   ├── sistema.py
│   ├── cadastro.py
│   ├── analise.py
│   └── exportacao.py
│
├── docs/
│   ├── como-comecar.md
│   ├── metodologia.md
│   ├── modelo-tecnico.md
│   └── finalizacao-entrega.md
│
├── resultados/
│   ├── testes.md
│   ├── testes.csv
│   └── resumo_final.md
│
├── relatorio/
│   └── relatorio_base.md
│
└── README.md
```

---

## 💻 Código de análise

Para executar, na raiz do projeto:

```powershell
python codigo\analise_resultados.py
```

O programa permite registrar os testes, visualizar os resultados, calcular acurácia, analisar o desempenho por classe e exportar os dados para CSV.

---

## 🔬 Metodologia

```text
Coleta e organização das imagens
            ↓
Separação entre treino e teste
            ↓
Criação das classes no Teachable Machine
            ↓
Treinamento do modelo
            ↓
Testes com diferentes configurações
            ↓
Avaliação com imagens inéditas
            ↓
Registro dos resultados
            ↓
Análise crítica e relatório final
```

As imagens foram selecionadas buscando boa iluminação, foco adequado e diversidade de fundo, posição, ângulo e distância.

---

## 📈 Principais observações

- Panela e Colher obtiveram 100% de acerto no conjunto final avaliado.
- Garfo apresentou maior dificuldade, com um erro de classificação para Colher.
- Uma Panela foi classificada corretamente com apenas 53% de confiança, mostrando que acerto não significa necessariamente alta certeza.
- A diferença de 54% para Colher e 46% para Garfo no único erro evidencia a proximidade visual entre essas duas classes.
- A acurácia final de **92,86%** representa o desempenho nas 14 imagens inéditas testadas.

---

## 📝 Relatório final

A base atualizada do relatório está disponível em:

```text
relatorio/relatorio_base.md
```

Nome escolhido para o PDF entregue pelo grupo:

```text
Grupo_Cap2_IA_Fase1.pdf
```

---

## ✅ Checklist final

- [x] Classes definidas: Garfo, Panela e Colher
- [x] Modelo principal treinado com 160 imagens por classe
- [x] Modelo exportado
- [x] Código Python modularizado
- [x] Testes inéditos confirmados
- [x] CSV final atualizado
- [x] Acurácia final: 92,86%
- [x] Precisão formal calculada
- [x] Fase 1 e Capítulo 2 confirmados
- [x] Análise crítica atualizada
- [x] Conclusão atualizada
- [x] Nome do PDF final definido

---

## 📌 Observação acadêmica

Os resultados apresentados correspondem aos testes realmente realizados. O print duplicado não foi contado duas vezes, e o único erro foi mantido na avaliação e utilizado na análise crítica.
