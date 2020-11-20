from random import randint as gay
co = 1
user = 11
pc = gay(0, 10)
user = int(input('Acerte o número aleatório de 0 a 10: '))
while user != pc:
    co += 1
    if user > pc:
        user = int(input('Menor...:'))
    elif user < pc:
        user = int(input('Maior...:'))
print('Parabens você ganhou!!!!!!!!!!!\n'
      'Com apenas {} tentativas'.format(co))
