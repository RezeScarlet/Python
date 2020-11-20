from random import randint
from operator import itemgetter
from time import sleep
j = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6),
     'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
rank = []
c = 0
for k in j:
    c += 1
    print(f'jogador {c} = {j[k]}')
    sleep(1)
rank = sorted(j.items(), key=itemgetter(1), reverse=True)
for k, l in enumerate(rank):
    print(f'{k+1}°-> {l[0]}: {l[1]}')