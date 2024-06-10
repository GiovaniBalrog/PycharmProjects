# testando dicionario
''' Dicionario são excelentes estruturas de dados principalmente usando em
    '''
dicionario = {'giovani': 28, 'valdir': 12, 'lindines': 28, 'g': ['banana', 'maçã', 'tomate', 'café']}
print(dicionario['g'][2])
""" dicionario anihado um entro do outro
para retornar um elemento  vou precisar usar a anotação completa para retornar um unico elemento
dicionario = {'dic': {'dic2': {'dic3': {'dic4': ['banana', 'maçã', 'tomate', 'café']}}}}
print(dicionario['dic']['dic2']['dic3']['dic4'][3])
print(dicionario['dic']['dic2'])
"""
""" Duas operações em uma primeiro eu faço a subtração e depois
eu atribuo o valor detro de uma variavel dentro do meu proprio dicionario;

dic = {'key': [3, 2, 4, 5] } #  estrair do dicionario um elemento specifico
var = dic['key'][0] - 1  #  e fazer uma operação
print(var)  #  amazerna um resultado na variavel
dic['key'][0] -= 1  # fazeruma operação em um elemento specifico
print(dic)
print(var)
"""
""" fazer operação estraindo elementos especifico da lista
dic = {}
print(dic)
dic['key'] = 2, 4, 6  #  estrair do dicionario um elemento specifico
var = dic['key'][1] - 1  #  e fazer uma operação mathematica com o lelemento
print(var)
"""
""" um dicionario aceita diferentes tipos de dados dentro de sua estrutura,
esse numerico como chave e strings como valores
dic = {}
print(dic)
dic[360] = 'email'  #   numerico como chave e strings como valores
print(dic)
"""
""" para adicionar elementos a meu dicionario 
dic = {}  ::::dicionario vasio
print(dic) ::::: imprimir dicionario vasio
dic["lindy"] = 26  ::::: para adicionar elemento ao dicionario
print(dic) ::::  para imprimir dicionario
"""
"""" função .update() para unir ou atualizar um dicionario ao outro
dic = {'giovani': 28, 'valdir': 12, 'lindines': 28, 'lista': ['banana', 'maçã', 'tomate', 'café']}   #  dicionario 1
dic2 = {'nat': 24, 'mari': 38, 'lind': 28}  # dicionario 2
dic.update(dic2)  # atualizar  dicionario adição do dicionario 2 no dicionario 1
print(dic)
"""
"""   Função .items() usadapara adicionar todos os itens
dic = {'giovani': 28, 'valdir': 12, 'lindines': 28, 'lista': ['banana', 'maçã', 'tomate', 'café']}
print(dic.items())
"""
"""  função .keys() para estrair apenas  as chaves do dicionario
dic = {'giovani': 28, 'valdir': 12, 'lindines': 28, 'lista': ['banana', 'maçã', 'tomate', 'café']}
print(dic.keys())
"""
"""  função .values() usada para estrair apenas os valores
dic = {'giovani': 28, 'valdir': 12, 'lindines': 28, 'lista': ['banana', 'maçã', 'tomate', 'café']}
print(dic.values())
"""
""" esse código retorna um [elemento] detro [da  lista ] , que sem encontra dentro da { chave do dicionario } 
dicionario = {'giovani': 28, 'valdir': 12, 'lindines': 28, 'g': ['banana', 'maçã', 'tomate', 'café']}
print(dicionario['g'][2])
"""
