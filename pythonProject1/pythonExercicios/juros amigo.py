#juros ao mes
fun = float(input('valor da divida: $  '))
am = fun + (fun * 15 / 100)

print('o valor da sua divida é de: ${:.2f}, \ncom a taxa de juros de 15% ao mês \nhoje sua divida fica exatamente: ${:.2f}'. format(fun, am))
