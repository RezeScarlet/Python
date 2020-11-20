from random import randint as rand
from time import sleep
lista = []
print('______________ FURTO ______________')
jo = int(input('Quantos Jogos?: '))
for c in range(0, jo):
    jogo = []
    while True:
        n = rand(0, 60)
        if n not in jogo and len(jogo) != 6:
            jogo.append(n)
        if len(jogo) == 6:
            lista.append(jogo)
            break
    print(f'Jogo {c+1}: ', end='')
    print(sorted(lista[c]), sep='')
    sleep(1)
print('Tenha um bom prejuizo!')
