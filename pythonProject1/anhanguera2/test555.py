import pandas as pd
import matplotlib.pyplot as plt

# Lê o arquivo Excel e armazena os dados em um DataFrame
df = pd.read_excel(r"C:\Users\giova\OneDrive\Documentos\anhanguera\Programação orientada a objetos para dados\Aulas\exercicios_platicos\Test_python.xlsx")

# Limpeza e conversão dos dados
df["VALOR"] = df["VALOR"].apply(lambda x: float(str(x).replace("R$", "").replace(",", "")))
df["SUBTOTAL"] = df["SUBTOTAL"].apply(lambda x: float(str(x).replace("R$", "").replace(",", "")))

# Cria um gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(df["DESCRIÇAO"], df["VALOR"], label='Valor')
plt.bar(df["DESCRIÇAO"], df["SUBTOTAL"], bottom=df["VALOR"], label='Subtotal')

# Adiciona rótulos e título
plt.xlabel('DESCRIÇAO')
plt.ylabel('Valores (R$)')
plt.title('Valores e Subtotais por Descrição')
plt.legend()

# Exibe o gráfico
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
