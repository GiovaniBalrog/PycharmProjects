#
m1 = float(input('Primeira nota do aluno '))
m2 = float(input('segunda nota do aluno '))
media = (m1 + m2) / 2
if media >= 7:
    print('somando {:.1f} e {:.1f}, a media de : {:.1f} aluno  foi aprovado'.format(media, m1, m2))
elif 7 > media >= 5:
    print('somando {:.1f} e {:.1f}, a media de : {:.1f} aluno esta de recuperação '.format(media, m1, m2))
elif media < 5:
    print('somando {:.1f} e {:.1f}, a media de : {:.1f} aluno reprovado '.format(media, m1, m2))


'''

'''
