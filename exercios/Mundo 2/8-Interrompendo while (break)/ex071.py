c50 = c20 = c10 = c1 = 0
v = int(input('Valor a ser sacado: '))
saque = v
while True:
    if v < 50:
        break
    c50 += 1
    print('*======*\n'
          '|  50  |\n'
          '*======*\n')
    v -= 50
while True:
    if v < 20:
        break
    c20 += 1
    print('*======*\n'
          '|  20  |\n'
          '*======*\n')
    v -= 20
while True:
    if v < 10:
        break
    c10 += 1
    print('*======*\n'
          '|  10  |\n'
          '*======*\n')
    v -= 10
while True:
    if v < 1:
        break
    c1 += 1
    print('*=====*\n'
          '|  1  |\n'
          '*=====*\n')
    v -= 1
print(f'  saque de R${saque}\n'
      f'{c50} notas de R$50\n'
      f'{c20} notas de R$20\n'
      f'{c10} notas de R$10\n'
      f'{c1} notas de R$1')
