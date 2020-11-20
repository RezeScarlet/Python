lista = list()
for c in range(0, 5):
    n = int(input(f'Digite o {c+1}° número: '))
    if n not in lista:
        if c == 0:
            lista.append(n)
            print('Adicionado ao final da lista')
        if c == 1:
            if n > lista[0]:
                lista.append(n)
                print('Adicionado ao final da lista')
            else:
                lista.insert(0, n)
                print('Adicionado na posição 0 da lista')
        if c == 2:
            if lista[0] < n < lista[1]:
                lista.insert(1, n)
                print('Adicionado na posição 1 da lista')
            elif n > lista[1]:
                lista.append(n)
                print('Adicionado ao final da lista')
            else:
                lista.insert(0, n)
                print('Adicionado na posição 0 da lista')
        if c == 3 or c == 4:
            if n > lista[-1]:
                lista.append(n)
                print('Adicionado ao final da lista')
            elif n < lista[0]:
                lista.insert(0, n)
                print('Adicionado na posição 0 da lista')
            else:
                for c1, l in enumerate(lista):
                    if n > l:
                        lista.insert(c1-1, n)
                        print(f'Adicionado na posição {c-1} da lista')
                        break
print(*lista, sep=', ')

'''lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                print(f'Adicionamos na posição {pos} da lista...')
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')'''