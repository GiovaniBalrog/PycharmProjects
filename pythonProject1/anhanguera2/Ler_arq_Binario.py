import pandas as pd  # Importa a biblioteca pandas, usada para manipulação e análise de dados

# Caminho para o arquivo pickle que você criou
caminho_pickle = r"C:\Users\giova\OneDrive\Documentos\anhanguera\Programação orientada a objetos para dados\Aulas\exercicios_platicos\CrinadoArqBinario.pkl"

# Carrega os dados do arquivo pickle em um DataFrame
dados_pickle = pd.read_pickle(caminho_pickle)

# Exibe os dados carregados do arquivo pickle
print(dados_pickle)
