print('Digite os números que deseja adicionar(999 para parar): ')
soma = co = n = 0
while True:
    n = int(input('->'))
    if n == 999:
        break
    soma += n
    co += 1
print(f'A soma dos {co} números digitados é {soma}')
