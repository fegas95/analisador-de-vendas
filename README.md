# 📊 Analisador de Dados de Vendas

Script Python que lê dados de vendas em CSV, calcula métricas e gera um relatório formatado automaticamente.

## 🚀 Funcionalidades

- Leitura e validação de arquivos CSV
- Cálculo de receita total, por produto e por categoria
- Identificação do produto mais vendido
- Geração de relatório `.txt` formatado com percentuais

## 🛠️ Tecnologias

- Python 3.10+
- Módulos nativos: `csv`, `os`, `datetime`, `collections`

> Sem dependências externas — roda direto com Python puro!

## ▶️ Como executar

```bash
# Clone o repositório
git clone https://github.com/fegas95/analisador-de-vendas.git
cd data-report

# Execute o script
python analyzer.py
```

O programa pedirá o caminho do CSV. Pressione Enter para usar o arquivo de exemplo `sample_data.csv`.

## 📸 Exemplo de saída

```
=======================================================
          RELATÓRIO DE VENDAS
          Gerado em: 01/06/2024 14:30
=======================================================

  Total de registros analisados : 15
  Receita total                 : R$ 45.894,50
  Produto mais vendido          : Mouse Logitech (35 unidades)

-------------------------------------------------------
  RECEITA POR PRODUTO
-------------------------------------------------------
  Notebook Dell             R$  17.999,40  (39.2%)
  Monitor LG 24"            R$   8.799,20  (19.2%)
  SSD 512GB                 R$   7.998,00  (17.4%)
  ...
```

## 📁 Estrutura do projeto

```
data-report/
├── analyzer.py       # Script principal de análise
├── sample_data.csv   # Dados de exemplo para teste
└── README.md
```
