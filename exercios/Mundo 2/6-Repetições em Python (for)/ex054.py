from datetime import date
n = int(input('Quantas pessoas você deseja saber se possuem maioridade?: '))
atual = date.today().year
maior= 0
menor= 0
for c in range(1, n+1):
    ano = int(input('Em que ano a {}° pessoa nasceu: '.format(c)))
    if atual-ano >= 21:
        maior += 1
    else:
        menor += 1
if maior == 1:
    print('1 dessas pessoas é maiores de idade')
elif maior == 0:
    print('Nenhuma dessas pessoas é maior de idade')
elif maior == n:
    print('Todas essas pessoas são maiores de idade')
else:
    print('{} das dessas pessoas são maiores de idade'.format(maior))
if menor == 1:
    print('1 dessas pessoas é menor de idade')
elif menor == 0:
    print('Nenhuma dessas pessoas é menor de idade')
elif menor == n:
    print('Todas essas pessoas são menores de idade')
else:
    print('{} das dessas pessoas são manores de idade'.format(menor))
