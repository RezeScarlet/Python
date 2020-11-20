n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite 0 3° numero: '))
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print("\033[35m{}\033[m é o maior dos números:\033[35m{}, {}, {}".format(maior, n1, n2, n3))
print("\033[35m{}\033[m é o menor dos números:\033[35m{}, {}, {}".format(menor, n1, n2, n3))
