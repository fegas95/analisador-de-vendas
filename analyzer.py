import csv
import os
from datetime import datetime
from collections import defaultdict


def load_data(filepath: str) -> list[dict]:
    """Carrega os dados do arquivo CSV."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Arquivo '{filepath}' não encontrado.")

    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = []
        for row in reader:
            row["quantidade"] = int(row["quantidade"])
            row["preco_unitario"] = float(row["preco_unitario"])
            row["total"] = row["quantidade"] * row["preco_unitario"]
            data.append(row)
    return data


def total_por_produto(data: list[dict]) -> dict:
    """Calcula o total vendido por produto."""
    totais = defaultdict(float)
    for row in data:
        totais[row["produto"]] += row["total"]
    return dict(sorted(totais.items(), key=lambda x: x[1], reverse=True))


def total_por_categoria(data: list[dict]) -> dict:
    """Calcula o total vendido por categoria."""
    totais = defaultdict(float)
    for row in data:
        totais[row["categoria"]] += row["total"]
    return dict(sorted(totais.items(), key=lambda x: x[1], reverse=True))


def produto_mais_vendido(data: list[dict]) -> tuple:
    """Retorna o produto com maior quantidade vendida."""
    quantidades = defaultdict(int)
    for row in data:
        quantidades[row["produto"]] += row["quantidade"]
    top = max(quantidades.items(), key=lambda x: x[1])
    return top


def receita_total(data: list[dict]) -> float:
    """Soma toda a receita."""
    return sum(row["total"] for row in data)


def gerar_relatorio(data: list[dict], output_path: str = "relatorio.txt"):
    """Gera um relatório formatado em arquivo .txt."""
    now = datetime.now().strftime("%d/%m/%Y %H:%M")
    receita = receita_total(data)
    por_produto = total_por_produto(data)
    por_categoria = total_por_categoria(data)
    mais_vendido, qtd_mais_vendido = produto_mais_vendido(data)

    linhas = [
        "=" * 55,
        "          RELATÓRIO DE VENDAS",
        f"          Gerado em: {now}",
        "=" * 55,
        "",
        f"  Total de registros analisados : {len(data)}",
        f"  Receita total                 : R$ {receita:,.2f}",
        f"  Produto mais vendido          : {mais_vendido} ({qtd_mais_vendido} unidades)",
        "",
        "-" * 55,
        "  RECEITA POR PRODUTO",
        "-" * 55,
    ]

    for produto, total in por_produto.items():
        pct = (total / receita) * 100
        linhas.append(f"  {produto:<25} R$ {total:>10,.2f}  ({pct:.1f}%)")

    linhas += [
        "",
        "-" * 55,
        "  RECEITA POR CATEGORIA",
        "-" * 55,
    ]

    for categoria, total in por_categoria.items():
        pct = (total / receita) * 100
        linhas.append(f"  {categoria:<25} R$ {total:>10,.2f}  ({pct:.1f}%)")

    linhas += ["", "=" * 55]

    relatorio = "\n".join(linhas)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(relatorio)

    print(relatorio)
    print(f"\n  ✅ Relatório salvo em: {output_path}")


def main():
    print("\nAnalisador de Dados de Vendas")
    print("─" * 35)

    filepath = input("Caminho do arquivo CSV [Enter para usar sample_data.csv]: ").strip()
    if not filepath:
        filepath = "sample_data.csv"

    try:
        data = load_data(filepath)
        print(f"\n  {len(data)} registros carregados com sucesso.\n")
        gerar_relatorio(data)
    except FileNotFoundError as e:
        print(f"\n  ❌ Erro: {e}")
    except Exception as e:
        print(f"\n  ❌ Erro inesperado: {e}")


if __name__ == "__main__":
    main()
