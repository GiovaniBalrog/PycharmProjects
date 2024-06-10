#Exercício 11 – Pintando Parede
larg = float(input('largura da parede: '))
alt = float(input('autura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de: {}x{}\n e sua área é de: {}m²'.format(larg, alt, area))
tinta = area / 2
print('para pintar essa parede de você precisara de:\n {}l de tinta'.format(tinta))
