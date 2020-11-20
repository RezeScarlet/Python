def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Número: '))
if par(num):
    print('É par!')
else:
    print('Não é par')


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
