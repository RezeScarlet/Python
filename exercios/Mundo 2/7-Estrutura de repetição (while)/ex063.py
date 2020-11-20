n = int(input('Quantos elementos da fibonacci você deseja ver?: '))
fib3 = 1
fib2 = 1
fib = 2
co = 0
print('0 - 1 - 1 - 2 - ', end='')
while co != n-4:
    co += 1
    fib3 = fib2
    fib2 = fib
    fib = fib2 + fib3
    print('{} - '.format(fib), end='')
print('Fim')
