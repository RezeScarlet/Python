def fatorial(n, show=False):
    """
    -> calculo da fatorial de um número
    param n: número que será calculado
    :param show: se as multiplicações serão mostradas
    :return: O valor do fatorial do n
    """
    f = 1
    for c in range(n, 1, -1):
        f *= c
        if show:
            print(c, end=' x ')
            if c == 2:
                print(f'1 = {f}')
        elif c == 2:
            print(f'{n} = {f}')


fatorial(5, show=True)
