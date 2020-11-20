def leiaint(s):
    while True:
        r = input(f'{s}')
        if r.isnumeric():
            break
        else:
            print('Erro! esse valor não é um número inteiro')
    return r


n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')
