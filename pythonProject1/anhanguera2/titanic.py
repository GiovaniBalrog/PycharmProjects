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

# Calcula a proporção de valores nulos em cada coluna
proporcao_nulos = df.isna().sum() / df.shape[0]

# Exibe a proporção de valores nulos
print("Proporção de valores nulos por coluna:")
print(proporcao_nulos)

# Exibe o DataFrame com as colunas selecionadas
print("DataFrame selecionado:")
print(df_selecionado)

# Convertendo os dados do DataFrame para uma planilha Excel
df_selecionado.to_excel(r"C:\Users\giova\OneDrive\Documentos\anhanguera\Programação orientada a objetos para dados\Aulas\exercicios_platicos\train_selecionado.xlsx", index=False)

# Agrupa os dados por 'Pclass' e 'Sex' e calcula a mediana da idade
df_idade = df.groupby(['Pclass', 'Sex'], as_index=False)['Age'].median()

# Exibe o DataFrame resultante com as medianas das idades
print("Mediana das idades por classe e sexo:")
print(df_idade)

# Agrupamento por sexo e cálculo da média da idade:

df_idade_media = df.groupby(['Sex'], as_index=False)['Age'].mean()

# Exibição do DataFrame resultante com a média das idades:
print("Média das idades por sexo:")
print(df_idade_media)
