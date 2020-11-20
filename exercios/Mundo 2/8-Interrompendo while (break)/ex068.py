from time import sleep
from random import randint
co = 0
pi = 'ana'
nome = str(input('Nome: '))
while True:
    pc = randint(0, 10)
    pi = str(input('+-+- Par ou Ímpar? -+-+\n')).lower().strip()
    if pi == 'par':
        pipc = 'ímpar'
    else:
        pipc = 'par'
    user = int(input('número: '))
    r = (user + pc) % 2
    print(f'{nome} ({pi}): {user}')
    sleep(1)
    print(f'PC ({pipc}): {pc}')
    if pi == 'par' and r == 0 or pi == 'impar' and r != 0:
        print('VITORIAAA!')
        co += 1
    else:
        break
print(f'DERROTA após {co} vitorias')
