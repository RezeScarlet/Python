from random import choice

print('\033[1;35mVamos jogar Jokenpô!!\033[m')
a = int(input('[1] PEDRA\n[2] PAPEL\n[3] TESOURA\nEscolha: '))
c = ['PEDRA', 'PAPEL', 'TESOURA']
b = choice(c)

if a == 1:
    a = 'PEDRA'
elif a == 2:
    a = 'PAPEL'
else:
    a = 'TESOURA'

c1 = '\033[34m'
c2 = '\033[31m'
c0 = '\033[m'

if a == b:
    print('{}{}|EMP{}ATE|{}'.format(c1, a, c2, b))
else:
    if a == 'PEDRA':
        if b == 'TESOURA':
            re = 1
        else:
            re = 2
    elif a == 'PAPEL':
        if b == 'PEDRA':
            re = 1
        else:
            re = 2
    else:
        if b == 'PAPEL':
            re = 1
        else:
            re = 2
    if re == 1:
        print('{}{}|VITÓRIA|{}{}'.format(c1, a, c2, b))
    else:
        print('{}{}{}|VITÓRIA|{}'.format(c1, a, c2, b))
