import pandas as pd

# Lê o arquivo Excel e armazena os dados em um DataFrame
df = pd.read_csv(r"C:\Users\giova\OneDrive\Documentos\anhanguera\Programação orientada a objetos para dados\Aulas\exercicios_platicos\train.csv")

'''

colunas_desejadas = ["VALOR", "DESCRIÇAO", "SUBTOTAL"]  # Substitua com os nomes das colunas que você deseja



# Seleciona apenas as colunas desejadas do DataFrame e cria uma cópia para evitar SettingWithCopyWarning
df_selecionado = df[colunas_desejadas].copy()

# Converte as colunas "VALOR" e "SUBTOTAL" para strings antes de formatá-las
df_selecionado["VALOR"] = df_selecionado["VALOR"].astype(float).apply(lambda x: f"R$ {x:,.2f}")
df_selecionado["SUBTOTAL"] = df_selecionado["SUBTOTAL"].astype(float).apply(lambda x: f"R$ {x:,.2f}")
'''

# Exibe o DataFrame com as colunas selecionadas e formatadas
print(df)

# convertendo os dados do arquivo csv para uma planilha

