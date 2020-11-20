lista = [[], []]
for c in range(0, 7):
    n = int(input(f'{c + 1}° Número: '))
    if n % 2 == 0:
        lista[1].append(n)
    else:
        lista[0].append(n)
print(f'Pares  : {sorted(lista[1])}\n'
      f'ímpares: {sorted(lista[0])}')
