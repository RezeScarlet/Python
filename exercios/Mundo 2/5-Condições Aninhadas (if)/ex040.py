n1 = float(input('Digite sua 1° nota: '))
n2 = float(input('Digite sua 2° nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('Sua média é {:.1f} portando esta reprovado.'.format(media))
elif 5.0 < media <= 6.9:
    print('Sua média é {:.1f} portanto esta de recuperação.'.format(media))
elif media > 7.0:
    print('sua média é {:.1f} portanto você esta aprovado.'.format(media))
