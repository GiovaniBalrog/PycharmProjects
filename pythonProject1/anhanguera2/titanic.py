import pandas as pd

# Lê o arquivo CSV e armazena os dados em um DataFrame
df = pd.read_csv(r"C:\Users\giova\OneDrive\Documentos\anhanguera\Programação orientada a objetos para dados\Aulas\exercicios_platicos\train.csv")

# Exibe as colunas disponíveis no DataFrame
print("Colunas disponíveis no DataFrame:", df.columns.tolist())

# Colunas que estão presentes no arquivo CSV
colunas_desejadas = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex']

# Verifica se as colunas desejadas estão presentes no DataFrame
colunas_existentes = [coluna for coluna in colunas_desejadas if coluna in df.columns]

# Seleciona apenas as colunas desejadas do DataFrame usando .loc
df_selecionado = df.loc[:, colunas_existentes]

# Exibe o DataFrame com as colunas selecionadas
print(df_selecionado)

# ////// df.isna().sum() / df.shape[0] //////////////////////

# Convertendo os dados do DataFrame para uma planilha Excel
df_selecionado.to_excel(r"C:\Users\giova\OneDrive\Documentos\anhanguera\Programação orientada a objetos para dados\Aulas\exercicios_platicos\train_selecionado.xlsx", index=False)

