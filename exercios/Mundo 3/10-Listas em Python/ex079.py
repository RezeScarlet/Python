lista = []
c = 0
while True:
    c += 1
    n = int(input(f'Digite o {c}° número: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Valor duplicado!(ignorado)')
    p = str(input('Continuar?[S/N]: '))
    if p == 'Nn':
        break
lista.sort()
print('=-'*20)
print(f'Você digitou: {lista}')
