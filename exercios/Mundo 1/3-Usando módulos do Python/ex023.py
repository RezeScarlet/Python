num = int((input('digite um número: ')))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
cor = {'r': '\033[1;35m', 'a': '\033[1;33m', 'l': '\033[m'}
print('Analisando o numero {}{}{}, temos a:'.format(cor['r'], num, cor['l']))
print('Unidade: {}{}{}'.format(cor['a'], u, cor['l']))
print('Dezena:  {}{}{}'.format(cor['a'], d, cor['l']))
print('Centena: {}{}{}'.format(cor['a'], c, cor['l']))
print('Milhar:  {}{}'.format(cor['a'], m))
# o // é divisão inteira e % é o resto da divisão
