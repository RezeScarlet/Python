from time import sleep


def contador(i, f, p):
    print(f'Contagem de {i} até {f} pulando {p}')
    co = i
    sleep(2)
    if p < 0:
        p *= -1
    elif p == 0:
        p = 1
    if i < f:
        while co <= f:
            print(f'{co}', end=' ')
            sleep(0.5)
            co += p
    elif i > f:
        while co >= f:
            print(f'{co}', end=' ')
            sleep(0.5)
            co -= p
    print('Fim')
    print('<>'*20)


contador(1, 10, 1)
contador(10, 0, 2)
contador(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passo: ')))
