def moeda(p):
    return f'R${p:.2f}'


def metade(p, m=False):
    if m:
        return moeda(p / 2)
    else:
        return p / 2


def dobro(p, m=False):
    if m:
        return moeda(p * 2)
    else:
        return p * 2


def aumentar(p, n=0, m=False):
    if m:
        return moeda(((p / 100) * n) + p)
    else:
        return ((p / 100) * n) + p


def diminuir(p, n=0, m=False):
    if m:
        return moeda(p-((p/100)*n))
    else:
        return p - ((p / 100) * n)


def resumo(p, n1, n2):
    print('-' * 29)
    print('       RESUMO DO valor')
    print('-' * 29)
    print(f'Preço analisado:   {moeda(p)}')
    print(f'Dobro do preço :   {dobro(p, True)}')
    print(f'Metade do preço:   {metade(p, True)}')
    print(f'{n1} de aumento  :   {aumentar(p, n1, True)}')
    print(f'{n2} de redução  :   {diminuir(p, n2,True)}')
    print('-' * 29)
