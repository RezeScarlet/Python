while True:
    print('-='*10)
    n = int(input('Qual tabuada?: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n * c}')
