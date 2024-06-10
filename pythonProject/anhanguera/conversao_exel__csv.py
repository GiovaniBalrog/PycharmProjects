import pandas as pd

# Lê o arquivo Excel e armazena os dados em um DataFrame
df = pd.read_excel(r"C:\Users\giova\OneDrive\exel basico curso\Test_python.xlsx")

# Salva o DataFrame em um arquivo CSV
caminho_csv = r"C:\Users\giova\OneDrive\exel basico curso\Test_python.csv"
df.to_csv(caminho_csv, index=False)
print(f"Arquivo CSV salvo com sucesso em: {caminho_csv}")

# Especifica as colunas que deseja selecionar
colunas_desejadas = ["VALOR", "DESCRIÇAO", "SUBTOTAL"]  # Substitua com os nomes das colunas que você deseja

# Seleciona apenas as colunas desejadas do DataFrame e cria uma cópia para evitar SettingWithCopyWarning
df_selecionado = df[colunas_desejadas].copy()

# Converte as colunas "VALOR" e "SUBTOTAL" para strings antes de formatá-las
df_selecionado["VALOR"] = df_selecionado["VALOR"].astype(float).apply(lambda x: f"R$ {x:,.2f}")
df_selecionado["SUBTOTAL"] = df_selecionado["SUBTOTAL"].astype(float).apply(lambda x: f"R$ {x:,.2f}")

# Exibe o DataFrame com as colunas selecionadas e formatadas
print(df_selecionado)

# Salva o DataFrame com colunas selecionadas e formatadas em um novo arquivo CSV
caminho_csv_formatado = r"C:\Users\giova\OneDrive\exel basico curso\Test_python_formatado.csv"
df_selecionado.to_csv(caminho_csv_formatado, index=False)
print(f"Arquivo CSV formatado salvo com sucesso em: {caminho_csv_formatado}")

# Lê o arquivo CSV formatado para um DataFrame
df_csv_formatado = pd.read_csv(caminho_csv_formatado)

# Salva o DataFrame lido do CSV em uma planilha Excel
caminho_excel_final = r"C:\Users\giova\OneDrive\exel basico curso\Test_python_final.xlsx"
df_csv_formatado.to_excel(caminho_excel_final, index=False)
print(f"Planilha Excel final salva com sucesso em: {caminho_excel_final}")
