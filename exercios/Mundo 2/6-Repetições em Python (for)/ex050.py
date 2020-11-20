n2 = 0
for c in range(1, 7):
    n1 = float(input('Digite o {}° número: '.format(c)))
    if n1 % 2 == 0:
        n2 = n2 + n1
print('A soma dos números PARES escritos é: {:.1f}'.format(n2))
