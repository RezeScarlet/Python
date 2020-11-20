maior = soma = 0
lista = [[], [], []]
for c in range(1, 10):
    if c <= 3:
        lista[0].append(int(input(f'Valor para [0, {c - 1}]: ')))
    elif 3 < c <= 6:
        lista[1].append(int(input(f'Valor para [1, {c - 4}]: ')))
        if lista[1][c - 4] > maior:
            maior = lista[1][c - 4]
    elif c > 6:
        lista[2].append(int(input(f'Valor para [2, {c - 7}]: ')))

print('°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸\n')
for c in range(0,3):
    print('+-----+-----+-----+\n'
          f'|{lista[c][0]:^5}|{lista[c][1]:^5}|{lista[c][2]:^5}|\n', end='')
print('+-----+-----+-----+\n'
      '\n°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸\n')

for l in range(0, 3):
    for c in range(0, 3):
        if lista[l][c] % 2 == 0:
            soma += lista[l][c]
print(f'Soma dos valores pares: {soma}')
print(f'A soma dos valores da 3° coluna: {lista[0][2] + lista[1][2] + lista[2][2]}')
print(f'O maior valor da segunda linha: {maior}')
