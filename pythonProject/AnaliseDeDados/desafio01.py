import pandas as pd

# Carregar os dados das tabelas
tabela1 = pd.read_csv(r"C:\Users\giova\Aula-PowerBIDSA\Desafio-JOWW\olist_customers_dataset.csv")
tabela2 = pd.read_csv(r"C:\Users\giova\Aula-PowerBIDSA\Desafio-JOWW\olist_geolocation_dataset.csv")
tabela3 = pd.read_csv(r"C:\Users\giova\Aula-PowerBIDSA\Desafio-JOWW\olist_order_items_dataset.csv")
tabela4 = pd.read_csv(r"C:\Users\giova\Aula-PowerBIDSA\Desafio-JOWW\olist_order_payments_dataset.csv")
tabela5 = pd.read_csv(r"C:\Users\giova\Aula-PowerBIDSA\Desafio-JOWW\olist_order_reviews_dataset.csv")
tabela6 = pd.read_csv(r"C:\Users\giova\Aula-PowerBIDSA\Desafio-JOWW\olist_orders_dataset.csv")
tabela7 = pd.read_csv(r"C:\Users\giova\Aula-PowerBIDSA\Desafio-JOWW\olist_products_dataset.csv")
tabela8 = pd.read_csv(r"C:\Users\giova\Aula-PowerBIDSA\Desafio-JOWW\olist_sellers_dataset.csv")
tabela9 = pd.read_csv(r"C:\Users\giova\Aula-PowerBIDSA\Desafio-JOWW\product_category_name_translation.csv")

# Exibir os nomes das colunas das tabelas
print(tabela1.columns)


# Lista com os caminhos dos arquivos das tabelas
caminhos_tabelas = [
    r"C:\Users\giova\Aula-PowerBIDSA\Desafio-JOWW\olist_customers_dataset.csv",
    r"C:\Users\giova\Aula-PowerBIDSA\Desafio-JOWW\olist_geolocation_dataset.csv",
    r"C:\Users\giova\Aula-PowerBIDSA\Desafio-JOWW\olist_order_items_dataset.csv",
    r"C:\Users\giova\Aula-PowerBIDSA\Desafio-JOWW\olist_order_payments_dataset.csv",
    r"C:\Users\giova\Aula-PowerBIDSA\Desafio-JOWW\olist_order_reviews_dataset.csv",
    r"C:\Users\giova\Aula-PowerBIDSA\Desafio-JOWW\olist_orders_dataset.csv",
    r"C:\Users\giova\Aula-PowerBIDSA\Desafio-JOWW\olist_products_dataset.csv",
    r"C:\Users\giova\Aula-PowerBIDSA\Desafio-JOWW\olist_sellers_dataset.csv",
    r"C:\Users\giova\Aula-PowerBIDSA\Desafio-JOWW\product_category_name_translation.csv"
]
# Carregar as tabelas e exibir os nomes das colunas
for caminho in caminhos_tabelas:
    tabela = pd.read_csv(caminho)
    print(f"Colunas da tabela {caminhos_tabelas.index(caminho) + 1}:")
    print(tabela.columns)
    print("\n")

    # Lista de tabelas
    tabelas = [tabela1, tabela2, tabela3, tabela4, tabela5, tabela6, tabela7, tabela8, tabela9]

    # Nomes das tabelas
    nomes_tabelas = [
        'tabela1', 'tabela2', 'tabela3',
        'tabela4', 'tabela5', 'tabela6',
        'tabela7', 'tabela8', 'tabela9'
    ]

    # Verificação da cardinalidade para cada coluna chave em cada tabela
    for tabela, nome in zip(tabelas, nomes_tabelas):
        print(f"Colunas da {nome}:")
        for coluna in tabela.columns:
            contagem_valores_unicos = tabela[coluna].nunique()
            print(f"O número de valores únicos na coluna {coluna} é: {contagem_valores_unicos}")
        print("\n")



