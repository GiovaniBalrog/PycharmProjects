import pandas as pd

# Criando um objeto pd.Series com um valor único e imprimindo
serie_numero = pd.Series(data=5)
print(serie_numero)

# Criando um objeto pd.Series com uma lista e imprimindo
lista_nomes = "giovani valdir lindines".split()
serie_nomes = pd.Series(lista_nomes)
print(serie_nomes)

# Criando um objeto pd.Series com um dicionário e imprimindo
dados = {
    "nome1": "giovani",
    "nome2": "lindines",
    "nome3": "valdir"
}
serie_dados = pd.Series(dados)
print(serie_dados)
