n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')

nome = 'José'
idade = 33
print(f'O {nome} tem {idade} anos.')
print('O {} tem {} anos.'.format(nome, idade))
