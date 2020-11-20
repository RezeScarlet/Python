n = int(input('Primeiro termo da progressão aritmetica: '))
r = int(input('Razão: '))
co = 0
mais = 9**9
print('{} -> '.format(n), end='')
while mais != 0:
    co += 1
    n += r
    print('{} -> '.format(n), end='')
    if co == 9 or co == mais:
        co = 0
        mais = int(input('\nQuantos termos você ainda quer ver?(0 para parar): '))
print('Fim')
