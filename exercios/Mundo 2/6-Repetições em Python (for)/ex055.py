n = int(input('Quantas pessoas serão analisadas?: '))
menor = 1000
maior = 0
for c in range(1, n + 1):
    p = float(input('Digite o {}° peso: '.format(c)))
    if p > maior:
        maior = p
    if p < menor:
        menor = p
print('O maior peso é de {}Kg'.format(maior))
print('O menor peso é de {}Kg'.format(menor))
