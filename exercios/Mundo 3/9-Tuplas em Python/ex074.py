from random import randint
lista = (randint(0, 1000), randint(0, 1000), randint(0, 1000), randint(0, 1000), randint(0, 1000))
print(f'Números sorteados: {lista}')
print(f'Menor número     : {sorted(lista)[0]}\n'
      f'Maior número     : {sorted(lista)[-1]}')
# da para usar max(lista) e min(lista) nessa situação no lugar do sorted