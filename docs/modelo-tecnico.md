# Ficha Técnica do Modelo

Este documento registra apenas informações confirmadas no arquivo exportado pelo Google Teachable Machine.

## Modelo analisado

Arquivo exportado: `tm-my-image-model.zip`

Conteúdo do pacote:

```text
metadata.json
model.json
weights.bin
```

## Informações confirmadas

| Item | Valor |
|---|---|
| Nome do modelo | tm-my-image-model |
| Quantidade de classes | 3 |
| Classes | Colher, Garfo, Panela |
| Tamanho da imagem | 224 × 224 pixels |
| Canais de entrada | 3 (RGB) |
| Formato exportado | TensorFlow.js |
| Teachable Machine | 2.4.16 |
| TensorFlow.js | 1.7.4 |
| Pacote | @teachablemachine/image 0.8.4-alpha2 |

## Estrutura da entrada

O `model.json` confirma a entrada no formato:

```text
[altura, largura, canais] = [224, 224, 3]
```

Ou seja, cada imagem é processada em 224 × 224 pixels utilizando os canais RGB.

## Uso no relatório

Esses dados podem ser utilizados na seção de metodologia e na justificativa técnica do projeto.

Não constam no ZIP exportado:

- acurácia final dos testes;
- precisão por classe;
- Epochs utilizados;
- Batch Size utilizado;
- Learning Rate utilizado;
- quantidade de imagens de treino e teste;
- resultados individuais das imagens de teste.

Esses dados precisam ser registrados durante os experimentos no Teachable Machine e nos testes finais.
