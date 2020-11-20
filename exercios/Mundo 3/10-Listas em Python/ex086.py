lista = [[], [], []]
for c in range(1, 10):
    if c <= 3:
        lista[0].append(int(input(f'Valor para [0, {c - 1}]: ')))
    elif 3 < c <= 6:
        lista[1].append(int(input(f'Valor para [1, {c - 4}]: ')))
    elif c > 6:
        lista[2].append(int(input(f'Valor para [2, {c - 7}]: ')))

print('\n°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸\n'
      '\n+-----+-----+-----+\n'
      f'|{lista[0][0]:^5}|{lista[0][1]:^5}|{lista[0][2]:^5}|\n'
      '+-----+-----+-----+\n'
      f'|{lista[1][0]:^5}|{lista[1][1]:^5}|{lista[1][2]:^5}|\n'
      '+-----+-----+-----+\n'
      f'|{lista[2][0]:^5}|{lista[2][1]:^5}|{lista[2][2]:^5}|\n'
      '+-----+-----+-----+\n')
