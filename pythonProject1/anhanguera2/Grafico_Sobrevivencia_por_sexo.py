import matplotlib.pyplot as plt  # Importa a biblioteca matplotlib para plotagem de gráficos
import seaborn as sns  # Importa a biblioteca seaborn para gráficos estatísticos mais elaborados
import pandas as pd  # Importa a biblioteca pandas para manipulação de dados em DataFrame

# Lê o arquivo CSV e armazena os dados em um DataFrame
df = pd.read_csv(r"C:\Users\giova\OneDrive\Documentos\anhanguera\Programação orientada a objetos para dados\Aulas\exercicios_platicos\train.csv")

# Exibe as colunas disponíveis no DataFrame
print("Colunas disponíveis no DataFrame:", df.columns.tolist())

# Agrupa os dados por 'Sex' e calcula a média de sobrevivência
df_plot = df.groupby('Sex', as_index=False)['Survived'].mean()

# Cria uma figura e um eixo para o gráfico de barras, especificando o tamanho da figura
fig, ax = plt.subplots(figsize=(8, 5))

# Cria o gráfico de barras usando seaborn, onde 'x' é o sexo, 'y' é a média de sobrevivência e os dados são do DataFrame 'df_plot'
sns.barplot(x='Sex', y='Survived', data=df_plot)

# Define o título do gráfico
ax.set_title("Taxa de Sobrevivência Por Sexo", fontsize=16)

# Define os rótulos do eixo x como 'male' e 'female' em vez de 0 e 1
ax.set_xticklabels(['male', 'female'])

# Exibe o gráfico
plt.show()



'''
O ax se refere ao objeto do eixo que você está manipulando no gráfico.
ax.set_title("Taxa de Sobrevivência Por Sexo", fontsize=16): Define o título do eixo. Nesse caso, está definindo o título do eixo y (vertical) do gráfico como "Taxa de Sobrevivência Por Sexo", com tamanho da fonte de 16 pontos.

ax.set_xticklabels(['male', 'female']): Define os rótulos dos ticks no eixo x (horizontal) do gráfico. Está substituindo os rótulos padrão dos ticks por 'male' e 'female', que correspondem às categorias de sexo nos seus dados.

Essencialmente, ax.set é uma maneira de personalizar a aparência e o comportamento dos eixos em um gráfico matplotlib.



as_index=False é útil quando você deseja que as colunas de agrupamento não sejam movidas para o índice, facilitando a manipulação e acesso aos dados agrupados.

'''