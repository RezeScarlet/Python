from time import sleep


def maior(* num):
    tam = len(num)
    print('-<>-' * 10)
    ma = 0
    print('Analisando valor(s)...')
    for c in range(0, tam):
        print(f'{num[c]}', end=' ')
        if num[c] > ma:
            ma = num[c]
        sleep(0.4)
    print(f'Foram informado(s) {tam} valor(s).\n'
          f'Sendo o maior valor {ma}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
