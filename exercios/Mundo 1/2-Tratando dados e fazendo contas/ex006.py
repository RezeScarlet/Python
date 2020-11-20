n = int(input('digite um número: '))
r1 = n * 2
r2 = n * 3
r3 = n ** (1 / 2)
cor = {'l': '\033[m',
       'c': '\033[1;36m'}
print('O dobro de {}{}{} é {}{}{}'.format(cor['c'], n, cor['l'], cor['c'], r1, cor['l']))
print('O triplo de {}{}{} é {}{}{}'.format(cor['c'], n, cor['l'], cor['c'], r2, cor['l']))
print('A raiz quadrada de {}{}{} é {}{:.2f}'.format(cor['c'], n, cor['l'], cor['c'], r3))
