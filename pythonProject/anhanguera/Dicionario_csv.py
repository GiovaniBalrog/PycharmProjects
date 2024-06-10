# Importa a biblioteca pandas para manipulação de dados
import pandas as pd

# Definindo o dicionário com os dados do cliente
# Cada chave do dicionário representa uma coluna e cada valor é uma lista com os dados dessa coluna
Cadastro_Cliente = {
    "Nome": ["Giovani", "Lindines", "Valdir"],  # Lista com os nomes dos clientes
    "Idade": [30, 29, 6],  # Lista com as idades dos clientes
    "Peso": [80, 70, 25]  # Lista com os pesos dos clientes
}

# Criando o DataFrame a partir do dicionário
# O DataFrame é uma estrutura de dados bidimensional que pode ser vista como uma tabela
data = pd.DataFrame(Cadastro_Cliente)

# Exibe o DataFrame no console
# Esta linha imprime o DataFrame para verificar os dados
print(data)

# Definindo o caminho onde o arquivo CSV será salvo
# O 'r' antes da string indica uma string bruta, que trata barras invertidas corretamente no Windows
caminho_csv = r"C:\Users\giova\OneDrive\Documentos\anhanguera\Programação orientada a objetos para dados\Aulas\exercicios_platicos\Cadastro_Cliente.csv"

# Salvando o DataFrame em um arquivo CSV
# O parâmetro 'index=False' evita que o índice do DataFrame seja salvo como uma coluna no arquivo CSV
data.to_csv(caminho_csv, index=False)

# Mensagem de confirmação indicando que o arquivo CSV foi salvo com sucesso
print(f"Arquivo CSV salvo com sucesso em: {caminho_csv}")
