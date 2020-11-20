from math import factorial as fatorial
n = int(input('Qual fatorial você deseja saber?: '))
fat = fatorial(n)
co = 0
print('{}! = {} x '.format(n, n), end='')
while co != n-1:
    co += 1
    mult = n - co
    print(mult, end='')
    if mult != 1:
        print(' x ', end='')
print(' = {}'.format(fat))
