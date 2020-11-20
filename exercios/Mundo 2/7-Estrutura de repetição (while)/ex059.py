lu = 0
while lu != 5:
    n1 = int(input('1° valor: '))
    n2 = int(input('2° valor: '))
    lu = 0
    while lu != 5 and lu != 4:
        lu = int(input('[1]Somar\n'
                       '[2]Multiplicar\n'
                       '[3]Maior\n'
                       '[4]Novos números\n'
                       '[5]Sair do Programa\n'))

        r = 0
        if 5 < lu or lu < 1:
            print('Número invalido')
            input('=-'*10)
        elif lu == 1:
            r = n1 + n2
            print('{} + {} = {}'.format(n1, n2, r))
            input('=-'*10)
        elif lu == 2:
            r = n1 * n2
            print('{} * {} = {}'.format(n1, n2, r))
            input('=-'*10)
        elif lu == 3:
            if n1 > n2:
                print('{} > {}'.format(n1, n2))
                input('=-'*10)
            else:
                print('{} > {}'.format(n2, n1))
                input('=-'*10)
