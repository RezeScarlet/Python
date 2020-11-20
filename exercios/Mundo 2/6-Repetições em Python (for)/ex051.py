n1 = int(input('Primeiro termo da progressão aritmetica: '))
r = int(input('Razão: '))
n10 = n1 + (10 - 1) * r
for c in range(n1, n10 + 1, r):
    print(c, end=' -> ')
print('Fim')
