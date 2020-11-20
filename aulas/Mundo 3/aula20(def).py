def soma(a, b):
    s = a+b
    print(f'A soma de {a} + {b} = {s}')


soma(4, 5)
soma(b=8, a=9)
############################################


def contador(*num):
    tam = len(num)
    print(f'{tam} valores: {num}')


contador(2, 1, 7)
contador(4, 4, 7, 6, 2)
############################################


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
print(dobra(valores))
