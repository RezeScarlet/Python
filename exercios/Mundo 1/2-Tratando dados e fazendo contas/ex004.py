v = input('Digite algo: ')

cor = {'l': '\033[m',
       'c': '\033[1;32m'}
print('O tipo primitivo do valor é\033[1;32m', type(v))
print('{}É um número?       {}'.format(cor['l'], cor['c']), v.isnumeric())
print('{}É alfabético?      {}'.format(cor['l'], cor['c']), v.isalpha())
print('{}Só tem espaço?     {}'.format(cor['l'], cor['c']), v.isspace())
print('{}É alfanumérico?    {}'.format(cor['l'], cor['c']), v.isalnum())
print('{}Está capitalizado? {}'.format(cor['l'], cor['c']), v.istitle())
print('{}Esta em maiúsculas?{}'.format(cor['l'], cor['c']), v.isupper())
print('{}Esta em minúsculas?{}'.format(cor['l'], cor['c']), v.islower())

