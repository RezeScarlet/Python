'''lista, par, impar = list(), list(), list()
c = 0
while True:
    c += 1
    n = (int(input(f'{c}° número: ')))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    p = str(input('Continuar?[S/N]: ')).upper().strip()
    if p == 'N':
        break
print('Números', *lista, sep='->')
print('Pares', *par, sep='->')
print('Ímpares', *impar, sep='->')
'''
lista, par, impar = list(), list(), list()
c = 0
while True:
    c += 1
    lista.append(int(input(f'{c}° número: ')))
    p = str(input('Continuar?[S/N]: '))
    if p in 'Nn':
        break
for co, l in enumerate(lista):
    if l % 2 == 0:
        par.append(l)
    else:
        impar.append(l)
print('Números', *lista, sep='->')
print('Pares  ', *par, sep='->')
print('Ímpares', *impar, sep='->')
