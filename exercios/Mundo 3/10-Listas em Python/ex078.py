maior = 0
menor = 9**9
v = []
for c in range(0, 5):
    v.append(int(input(f'Digite o {c+1}° número: ')))
    if v[c] > maior:
        maior = v[c]
    if v[c] < menor:
        menor = v[c]
print(f'Lista: {v}\n'
      f'Maior: {maior} |posição: ', end='')
for c, b in enumerate(v):
    if b == maior:
        print(f'{c}...', end='')
print(f'\nMenor: {menor} |posição: ', end='')
for c, b in enumerate(v):
    if b == menor:
        print(f'{c}...', end='')
