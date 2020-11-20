maior = media = co = 0
n = 1
menor = 9**9
print('Digite vários números (0 para parar): ')
while n != 0:
    n = int(input(''))
    co += 1
    media += n
    if n < menor and n != 0:
        menor = n
    if n > maior:
        maior = n
print('A média entre esses números foi: {}\n'
      'O maior número digitado foi {} e o menor foi {}'.format(media / (co - 1), maior, menor))
