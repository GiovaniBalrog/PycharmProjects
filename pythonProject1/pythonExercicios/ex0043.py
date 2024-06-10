#  Exercício 43 – Índice de Massa Corporal
peso = float(input('Qual é seu peso?: (Kg)'))
altura = float(input('Qual é sua altura? (m)'))
imc = peso / (altura ** 2)
print('o imc dessa pesoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif 185.5 <= imc < 25:
    print('peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade Morbida')



'''
Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida
'''