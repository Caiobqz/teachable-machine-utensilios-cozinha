# 🍴 Teachable Machine — Utensílios de Cozinha

Projeto acadêmico de **Inteligência Artificial e Visão Computacional** desenvolvido com o Google Teachable Machine para classificar imagens de utensílios de cozinha.

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

---

## ⚙️ Configurações documentadas

Foram registradas configurações diferentes durante os testes do modelo principal.

| Configuração | Epochs | Batch Size | Learning Rate |
|---|---:|---:|---:|
| A | 50 | 16 | 0.001 |
| B | 70 | 32 | 0.001 |

Os resultados e observações estão organizados em `resultados/testes.md` e `resultados/resumo_final.md`.

---

## 🗂️ Estrutura do projeto

```text
teachable-machine-utensilios-cozinha/
│
├── codigo/
│   ├── analise_resultados.py   # ponto de entrada
│   ├── sistema.py              # menu principal
│   ├── cadastro.py             # registro dos testes
│   ├── analise.py              # acurácia e desempenho por classe
│   └── exportacao.py           # geração do CSV
│
├── docs/
│   ├── como-comecar.md
│   ├── metodologia.md
│   └── modelo-tecnico.md
│
├── resultados/
│   ├── testes.md
│   ├── testes.csv
│   └── resumo_final.md
│
├── relatorio/
│   └── relatorio_base.md
│
├── imagens/
│   ├── treino/
│   │   ├── garfo/
│   │   ├── panela/
│   │   └── colher/
│   └── teste/
│       ├── garfo/
│       ├── panela/
│       └── colher/
│
└── README.md
```

---

## 💻 Código de análise

A parte em Python foi separada em módulos para deixar o projeto mais legível e facilitar alterações pontuais.

| Arquivo | Função |
|---|---|
| `analise_resultados.py` | inicia o programa |
| `sistema.py` | controla o menu |
| `cadastro.py` | registra e exibe os testes |
| `analise.py` | calcula acurácia e desempenho por classe |
| `exportacao.py` | exporta os resultados para CSV |

Para executar, na raiz do projeto:

```powershell
python codigo\analise_resultados.py
```

O programa permite registrar:

```text
Nome da imagem
Classe real
Classe prevista
Confiança do modelo
Acerto ou erro
```

Depois calcula:

```text
Acurácia = (acertos / total de testes) x 100
```

---

## 🔬 Metodologia

O fluxo adotado no projeto foi:

```text
Coleta e organização das imagens
            ↓
Separação entre treino e teste
            ↓
Criação das classes no Teachable Machine
            ↓
Treinamento do modelo
            ↓
Testes com diferentes hiperparâmetros
            ↓
Avaliação com imagens inéditas
            ↓
Registro dos resultados em Python
            ↓
Análise crítica e relatório final
```

Durante a coleta, foram priorizadas imagens com:

- boa iluminação;
- foco adequado;
- diferentes fundos;
- diferentes ângulos;
- diferentes posições e distâncias;
- poucos elementos extras quando possível.

---

## 📈 Evidências observadas

Os testes documentados mostram comportamento consistente para a classe **Panela**, com exemplos classificados entre **98% e 100% de confiança**.

Também foram observadas situações em que **Garfo** e **Colher** apresentaram maior proximidade visual, reduzindo a confiança da previsão. Em uma das configurações, uma imagem de garfos foi corretamente classificada como Garfo com **72% de confiança**, enquanto outras classes receberam probabilidades menores.

Esses resultados são importantes para a análise crítica porque mostram que confiança alta em exemplos simples não elimina dificuldades em imagens mais ambíguas.

---

## 📝 Relatório

O relatório final deve incluir:

- introdução e objetivos;
- metodologia;
- quantidade e organização das imagens;
- características técnicas do modelo;
- configurações de treinamento;
- prints das principais etapas;
- testes com imagens novas;
- cálculo de acurácia;
- desempenho por classe;
- análise de erros;
- análise crítica;
- sugestões de melhoria;
- conclusão.

A base do relatório está disponível em:

```text
relatorio/relatorio_base.md
```

---

## ✅ Checklist final

- [x] Classes definidas: Garfo, Panela e Colher
- [x] Modelo principal treinado com 160 imagens por classe
- [x] Modelo exportado
- [x] Código Python modularizado
- [x] Testes e evidências organizados
- [x] Documentação técnica criada
- [ ] Inserir acurácia final consolidada no relatório
- [ ] Inserir dados acadêmicos finais de fase/capítulo/disciplina
- [ ] Revisar o PDF antes do envio na plataforma

---

## 📌 Observação acadêmica

Os resultados apresentados no relatório devem corresponder aos testes realmente realizados. Erros de classificação também fazem parte da avaliação do modelo e são utilizados na análise crítica, sem alteração manual para melhorar artificialmente o desempenho.
