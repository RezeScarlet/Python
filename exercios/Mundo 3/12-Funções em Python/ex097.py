def escreva(string):
    print('-' * (len(string)+4))
    print(f'  {string}')
    print('-' * (len(string)+4))


escreva(str(input('Escreva algo: ')))
