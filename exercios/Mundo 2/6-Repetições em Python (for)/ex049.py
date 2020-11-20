n1 = int(input('A tabuada de que número?: '))
n2 = int(input('Até qual número ele será multiplicado?: '))
for c in range(0, n2+1):
    print('{} * {} = {}'.format(n1, c, n1*c))
