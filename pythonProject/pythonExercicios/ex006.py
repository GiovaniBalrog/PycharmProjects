#Exercício 6 – Dobro, Triplo, Raiz Quadrada
n = int(input('Diga um numero: '))
#b = (n*2)
#c = (n*3)
#d = n** (1/2)
print('seu numero é {} \n {} o dobro \n {} o tripo \n {:.2f} É a raiz quadrada'. format(n, (n*2), (n*3), pow(n, (1/2))))
# a raiz quadrada pode ser representada atravez de uma esponenciaçao **potencia** (1/2) elevado ao meio dessa forma==> (n**(1/2) ==> ou dessa pow(n, (1/2))))