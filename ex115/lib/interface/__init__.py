def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print('\033[33m', txt.center(42), '\033[m')
    print(linha())


def menu(lista):
    cabeçalho('Menu principal')
    c = 0
    for item in lista:
        c += 1
        print(f'\033[35m{c}\033[m - \033[32m{item}\033[m')
    print(linha())
    opc = leiaint('\033[33mSua Opção: \033[m')
    return opc


def leiaint(s):
    while True:
        try:
            r = int(input(f'{s}'))
        except (ValueError, TypeError):
            print(f'\033[1;32mErro! digite um número inteiro valido\033[m')
        except KeyboardInterrupt:
            print(f'\033[1;32mEntrada de dados interrompida\033[m')
            return 0
        else:
            return r