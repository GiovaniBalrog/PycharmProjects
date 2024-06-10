import pandas as pd

# Criando uma série com um único valor
pd.Series(data=4)


# Corrigindo a criação da lista de nomes
lista_nome = "gloria miguel rafael maria".split()

# Criando uma série a partir da lista de nomes
pd.Series(lista_nome)
print(lista_nome)

# Corrigindo a criação do dicionário
dados = {
    "nome1": "gloria",
    "nome2": "miguel",
    "nome3": "rafael",
    "nome4": "maria"
}


