f = str(input('Digite um frase: ')).replace(' ', '').upper()
n = len(f)
r = 0
if n % 2 == 0:
    for c in range(1, n//2+1):
        if f[c-1] == f[-c]:
            r = r + 1
    if r == n//2:
        print('Esta frase é um palíndromo')
    elif r != n//2:
        print('Esta frase não é um palíndromo')
elif n % 2 != 0:
    for c in range(1, n//2+1):
        if f[c-1] == f[-c]:
            r = r + 1
    if r == n//2:
        print('Esta frase é um palíndromo')
    elif r != n//2:
        print('Esta frase não é um palíndromo')
'''
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto
    print('Temos um palíndromo!')
else:
    print(' frase digitada não é um palíndromo!')
'''