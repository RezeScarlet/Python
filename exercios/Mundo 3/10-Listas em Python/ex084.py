lista = []
maior = 0
menor = 9 ** 9
maiorn = list()
menorn = list()

while True:
    pessoa = [str(input('Nome: ')), float(input('Peso: '))]
    lista.append(pessoa[:])
    co = str(input('Continuar?[S/N]: '))
    if co in 'Nn':
        break
for l in lista:
    if l[1] >= maior:
        if l[1] > maior and l != lista[0]:
            maiorn.pop()
        maior = l[1]
        maiorn.append(l[0])
    if l[1] <= menor:
        if l[1] < menor and l != lista[0]:
            menorn.pop()
        menor = l[1]
        menorn.append(l[0])

print(f'Maior peso: {maior}Kg de {maiorn}')
print(f'Menor peso: {menor}Kg de {menorn}')
