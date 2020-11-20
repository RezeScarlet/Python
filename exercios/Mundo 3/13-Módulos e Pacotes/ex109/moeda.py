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
