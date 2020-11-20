num = int(input('Digite um número inteiro: '))
if num % 2 == 1:
    print('O número {}{}{} é ímpar'.format('\033[1;36m', num, '\033[m'))
else:
    print('O número {}{}{} é par'.format('\033[1;36m', num, '\033[m'))
