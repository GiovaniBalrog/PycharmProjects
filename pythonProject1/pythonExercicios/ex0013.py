#Exercício 13 – Reajuste Salarial
fun = float(input('qual o salario de um funcionario:'))
am = fun + (fun * 15 / 100)
print('um funcionario que ganhava: ${:.2f}, com 15% de aumento passa a receber: ${:.2f}  '.format(fun, am))
