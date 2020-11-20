n = int(input('digite um número:'))
cor = {'l': '\033[m',
       'c': '\033[1;30m'}
print('o sucessor de {}{}{} é {}{}{} e o seu antecessor é {}{}'.format('\033[1;30m', n, '\033[m', '\033[1;30m',
                                                                       n+1, '\033[m', '\033[1;30m', n-1))
