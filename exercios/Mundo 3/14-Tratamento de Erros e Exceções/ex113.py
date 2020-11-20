def leiaint(s):
    while True:
        try:
            r = int(input(f'{s}'))
        except (ValueError, TypeError):
            print(f'Erro! digite um número inteiro valido')
        except KeyboardInterrupt:
            print(f'Entrada de dados interrompida')
            return 0
        else:
            return r



def leiafloat(s):
    while True:

        try:
            r = float(input(f'{s}'))
        except (ValueError, TypeError):
            print(f'Erro! Digite um número real valido')
        except KeyboardInterrupt:
            print(f'Entrada de dados interrompida')
            return 0
        else:
            return r


r = leiaint('Digite um número inteiro: ')
s = leiafloat('Digite um número real: ')
print(r, s)
