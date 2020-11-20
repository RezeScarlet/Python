c = ('\033[m',    # 0 - sem cores
     '\033[41m',  # 1 - vermelho
     '\033[42m')  # 2 - verde


def line(l, cor=0):
    tam = len(l)
    print(c[cor], end='')
    print('-' * tam)
    print(l)
    print('-' * tam)
    print(c[0], end='')


def ajuda(h):
    line(f'Acessando manual do comando {h}', 2)
    help(h)


while True:
    line('Sistema da ajuda PyHELP', 1)
    a = str(input('Função ou Biblioteca > '))
    if a.upper() == 'FIM':
        break
    else:
        ajuda(a)
print('Fim')
