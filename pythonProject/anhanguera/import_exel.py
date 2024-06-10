# Importa a biblioteca pandas para manipulação de dados
import pandas as pd

# Tenta ler o arquivo Excel
try:
    print("Tentando ler o arquivo Excel...")
    # Lê o arquivo Excel e armazenar os dados em um DataFrame chamado df.
    df = pd.read_excel(r"C:\Users\giova\OneDrive\exel basico curso\Test_python.xlsx")
    print("Arquivo lido com sucesso!")
except Exception as e:
    # Captura e imprime qualquer erro que ocorrer ao tentar ler o arquivo
    print(f"Ocorreu um erro: {e}")

# Especifica as colunas que deseja selecionar
colunas_desejadas = ["VALOR", "DESCRIÇAO", "SUBTOTAL"]  # Substitua com os nomes das colunas que você deseja

# Seleciona apenas as colunas desejadas do DataFrame e cria uma cópia para evitar SettingWithCopyWarning
df_selecionado = df[colunas_desejadas].copy()

# Converte as colunas "VALOR" e "SUBTOTAL" para strings antes de formatá-las
df_selecionado["VALOR"] = df_selecionado["VALOR"].astype(float).apply(lambda x: f"R$ {x:,.2f}")
df_selecionado["SUBTOTAL"] = df_selecionado["SUBTOTAL"].astype(float).apply(lambda x: f"R$ {x:,.2f}")

# Exibe o DataFrame com as colunas selecionadas e formatadas
print(df_selecionado)



# Exibe todas as colunas do DataFrame original para referência
print("\n Colunas Disponiveis Para Seleção \n  ", df.columns)



''''

try. Exception é uma classe base para todas as exceções em Python,
então isso captura qualquer erro que aconteça. A variável e armazena a instância da exceção capturada.  

Exemplos de Erros que Podem Ocorrer
FileNotFoundError: Se o arquivo no caminho especificado não existir.
PermissionError: Se você não tiver permissão para ler o arquivo.
IOError: Se houver algum problema de entrada/saída ao acessar o arquivo.
ValueError: Se o arquivo não for um arquivo Excel válido

'''


