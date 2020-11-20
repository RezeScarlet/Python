from math import sqrt, floor

num = int(input('digite um numero: '))
raiz = sqrt(num)
print('a raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))
