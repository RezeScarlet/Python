lista = []
c = 0
while True:
    c += 1
    lista.append(int(input(f'{c + 1}° número: ')))
    p = str(input('Continuar?[S/N]: '))
    if p in 'Nn': break
print(f'Tamanho: {len(lista)}')
lista.sort(reverse=True)
print(*lista, sep=' -> ')
if 5 in lista:
    print('O número 5 está presente na lista')
else:
    print('O número 5 não esta presente na lista')
