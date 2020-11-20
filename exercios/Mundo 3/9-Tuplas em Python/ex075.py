n = 11
lista = (int(input('Digite um numeros de 0 a 10: ')), int(input('Digite um numeros de 0 a 10: ')),
         int(input('Digite um numeros de 0 a 10: ')), int(input('Digite um numeros de 0 a 10: ')))
'''for c in range(1, 5):
    while 0 > n or n > 10:
        n = int(input('Número de 0 a 10: '))
    if c == 1:
        c1 = n
    elif c == 2:
        c2 = n
    elif c == 3:
        c3 = n
    elif c == 4:
        c4 = n
    n = 11
lista = (c1, c2, c3, c4)'''
if 9 in lista:
    print(f'{lista.count(9)} Número(s) 9')
else:
    print('Nenhum número foi 9')
if 3 in lista:
    print(f'o 1° 3 esta na posição {lista.index(3) + 1}')
else:
    print('Não há nenhum 3 entre estes números')
co = 0
for c in range(0, 4):
    if lista[c] % 2 == 0:
        print(f'{lista[c]}, ', end='')
        co += 1
if co != 0:
    print('São números pares')
else:
    print('Não há número pares')