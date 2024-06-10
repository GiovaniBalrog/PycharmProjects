""""disciplina = "python"
curso = "ads"



def imprimir_mensagem():
    print(f"Minha primeira função em python desenvolvida na diciplina: {disciplina}, do curso: {curso}")

imprimir_mensagem()"""

'''

def somar (a,b):
    return a + b
r = somar(2,3)
print(r)

'''
'''
def saudacao(nome, saudacao_padrao="Olá"):
    print(f"{saudacao_padrao}, {nome}!")

# Exemplo de uso da função:
saudacao("Maria")  # Output: Olá, Maria!
saudacao("João", "Oi")  # Output: Oi, João!
saudacao("valdir", "deboa")
'''
'''
def info_pessoa(nome, idade, cidade):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Cidade: {cidade}")

# Exemplo de chamada da função usando parâmetros nomeados
info_pessoa(idade=30, nome="Ana", cidade="São Paulo")
'''
'''
def info_pessoa(nome, idade=25, cidade="Desconhecida"):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Cidade: {cidade}")

# Exemplo de chamada da função com parâmetros nomeados
info_pessoa(nome="roberta", idade=35)

'''
'''
def soma_numeros(*args):
    total = 0
    for numero in args:
        total += numero
    return total

# Exemplo de chamada da função com diferentes números de argumentos
resultado1 = soma_numeros(5,7)
resultado2 = soma_numeros(10, 20, 30, 40, 50)

print(resultado1)  # Output: 10
print(resultado2)  # Output: 150
'''


#2 aula

'''

# Definindo uma lista de exemplo
vogais = ['a', 'e', 'i', 'o', 'u']

# Usando um loop for para percorrer a lista e imprimir cada elemento com seu índice e valor
for vogal in vogais:
    print(f"Posição = {vogais.index(vogal)}, Valor = {vogal}")
'''

'''
'''
# Exemplo de uso da função split() sem parâmetros
texto = "Olá, mundo! Estamos aprendendo Python."
lista_palavras = texto.split()

print("Lista de palavras após o split:")
print(lista_palavras)

# Exemplo de uso da função split() com parâmetro ","
texto_com_virgulas = "Maçã, Banana, Pêra, Uva"
lista_frutas = texto_com_virgulas.split(",")

print("\nLista de frutas após o split com vírgulas:")
print(lista_frutas)

''''''

