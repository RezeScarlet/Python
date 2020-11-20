lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:4])
print(lanche[1:])
print(sorted(lanche))

# tuplas são imutaveis

print('~~~' * 10)

for comida in lanche:
    print(f'eu comi {comida}')

for cont in range(0, len(lanche)):
    print(f'eu comi {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'eu comi {lanche[cont]} na posição {pos}')

print('~~~' * 10)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.count(5))
print(c.index(5, 1))
