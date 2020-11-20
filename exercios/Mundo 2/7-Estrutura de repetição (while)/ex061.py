n = int(input('Primeiro termo da progressão aritmetica: '))
r = int(input('Razão: '))
co = 0
print('{} -> '.format(n), end='')
while True:
    co += 1
    n += r
    print('{} -> '.format(n), end='')
    if co == 9:
        break
print('Fim')
