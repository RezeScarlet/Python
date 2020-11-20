from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando...')
    for c in range(0, 5):
        rand = randint(0, 100)
        lista.append(rand)
        print(rand, end=' ')
        sleep(0.4)
    print()


def somapar(lista):
    par = 0
    print(f'Somando os valores pares de {lista}')
    for c in range(0, len(lista)):
        if lista[c] % 2 == 0:
            par += lista[c]
    print(par)


num = []
sorteia(num)
somapar(num)
