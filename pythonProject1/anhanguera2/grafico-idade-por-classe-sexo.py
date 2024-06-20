import matplotlib.pyplot as plt
import seaborn as sns
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

# Plotagem do gráfico de barras
plt.figure(figsize=(8, 5))
sns.barplot(x='Pclass', y='Age', hue='Sex', data=df_idade)
plt.title("Idade por Classe e Sexo", fontsize=16)
plt.show()

'''
plt.figure(figsize=(8, 5)): Esta linha cria uma nova figura para o gráfico, especificando o tamanho da figura com figsize=(8, 5). Isso define a largura como 8 unidades e a altura como 5 unidades. A figura é onde o gráfico será desenhado.

sns.barplot(x='Pclass', y='Age', hue='Sex', data=df_idade): Esta linha cria o gráfico de barras usando a biblioteca Seaborn (sns). Aqui estão os parâmetros:

x='Pclass': Indica que os valores ao longo do eixo x serão os valores da coluna 'Pclass' do DataFrame df_idade.
y='Age': Indica que os valores ao longo do eixo y serão os valores da coluna 'Age' do DataFrame df_idade.
hue='Sex': Indica que as barras serão coloridas de acordo com os valores da coluna 'Sex' do DataFrame df_idade.
data=df_idade: Indica que os dados utilizados para plotagem são provenientes do DataFrame df_idade.
plt.title("Idade por Classe e Sexo", fontsize=16): Esta linha adiciona um título ao gráfico, com o texto "Idade por Classe e Sexo", e especifica o tamanho da fonte (fontsize=16).

plt.show(): Esta linha exibe o gráfico na figura criada anteriormente. É importante incluir esta linha para que o gráfico seja mostrado na saída do código.

Essas linhas juntas criam e exibem um gráfico de barras utilizando a biblioteca Seaborn, mostrando a relação entre a idade, a classe e o sexo dos dados contidos no DataFrame df_idade.

'''