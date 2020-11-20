n = soma = co = 0
print('Digite os números que deseja somar(999 para parar):')
while n != 999:
    co += 1
    n = int(input(''))
    soma += n
print('A somas do {} números digitados é {}'.format(co - 1, soma - 999))
