# Finalização da Entrega

Este arquivo reúne somente o que ainda precisa ser concluído antes do envio da atividade.

## Estado atual

Já estão concluídos:

- classes `Garfo`, `Panela` e `Colher`;
- modelo principal com 160 imagens por classe (480 imagens de treinamento);
- exportação do modelo;
- código Python modularizado;
- documentação do projeto;
- RMs dos integrantes;
- prints e evidências principais;
- análise crítica preliminar;
- limitações e sugestões de melhoria;
- relatório visual preparado.

## Única intervenção prática realmente necessária

É necessário consolidar os testes finais do modelo principal e gerar a acurácia oficial.

### 1. Usar somente o modelo principal

Modelo oficial:

```text
Garfo: 160 imagens de treinamento
Panela: 160 imagens de treinamento
Colher: 160 imagens de treinamento
```

Não misturar resultados do modelo antigo de 10 imagens por classe.

### 2. Testes finais recomendados

Usar imagens inéditas, que não fizeram parte do treinamento:

```text
10 imagens de Garfo
10 imagens de Panela
10 imagens de Colher
Total: 30 testes
```

Para cada imagem, registrar:

```text
Nome da imagem
Classe real
Classe prevista
Confiança
```

Erros devem ser mantidos.

### 3. Registrar no programa Python

Na raiz do repositório:

```powershell
python codigo\analise_resultados.py
```

Cadastrar todos os testes e depois executar:

- visualizar resultados;
- calcular acurácia;
- desempenho por classe;
- quantidade de testes por classe;
- exportar CSV.

### 4. Evidências finais necessárias

Guardar prints de:

```text
[ ] resultado geral
[ ] desempenho por classe
[ ] quantidade de testes por classe
```

O arquivo `resultados/testes.csv` deve conter somente os testes reais do modelo principal.

## Dados que deverão entrar no relatório final

```text
Total de testes: ______
Acertos: ______
Erros: ______
Acurácia final: ______ %

Garfo: ______ %
Panela: ______ %
Colher: ______ %
```

## Depois desses dados

Com a acurácia final disponível, basta:

1. atualizar `resultados/resumo_final.md`;
2. atualizar `relatorio/relatorio_base.md`;
3. inserir os prints do Python no relatório;
4. revisar o PDF;
5. nomear o arquivo conforme o padrão da faculdade;
6. confirmar os quatro participantes na plataforma;
7. enviar o PDF correto.

## Nome dos integrantes e RMs

| Integrante | RM |
|---|---:|
| Caio Barros Queiroz | RM576443 |
| Paulo Vitor Isidoro Silva | RM575580 |
| Kauê Cavalcanti Araujo | RM576394 |
| Suellen Hellen Pereira Silva | RM574778 |

## Observação metodológica

A acurácia oficial não deve ser inventada nem calculada misturando prints de modelos diferentes. Ela só deve ser declarada usando testes inéditos feitos no mesmo modelo principal.
