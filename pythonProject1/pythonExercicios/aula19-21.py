'''
Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre Interactive Help em Python,
o uso de docstrings para documentar nossas funções,
argumentos opcionais para dar mais dinamismo em funções Python, escopo de variáveis e retorno de resultados.
'''

def soma(* valores):
    """
    é so abrir aspas duplas  tres vezes logo la linha de baixo do comandon def
    # docstrings ==> é uma string de documentação, é um manual que pode ser exibido durante a ajuda interativa
     para qualquer programador que importa minha função
    #  docstrings elas começaos logo depois do comando def
    # para acessar é só usar o comando help(soma)
    """
    s = 0   # soma recebe 0
    for num in valores: # para cada numeros em valores
        s += num    # soma mais = num
    print(f'Somando Os Valore {valores} temos {s}')


soma(1 ,3)

help(soma)

