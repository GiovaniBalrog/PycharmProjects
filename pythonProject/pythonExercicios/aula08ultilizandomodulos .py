# Aula 8 – Utilizando Módulos
# Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos import e from/import no Python.
# Veja como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas
# utilizando módulos built-in e módulos externos, oferecidos no Pypi.

import math
num = int(input('digite um numero: '))
raiz = math.sqrt(num)
print('a raiz quadrada de: {:.1f} é igual a: {:.2f}'. format(num, raiz))
# math.ceil arredondar para cima
# math.floor arredondar para baixo
