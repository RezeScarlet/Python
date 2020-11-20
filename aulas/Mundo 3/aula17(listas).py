num = [2, 5, 9, 1]

num[2] = 3
# troca o numero
print(num)

num.append(7)
# add no final na lista
print(num)

num.sort(reverse=True)
print(num)
# organiza (reverse=True para ser de trás para frente)

print(len(num))
# mostra o tamanho da lista

num.insert(2, 0)
print(num)
# adiciona um numero num.insert(onde, qual numero)

num.pop(2)
print(num)
# remove um item da lista (vazio para ultimo)

num.remove(2)
print(num)
# deleta o 1° item citado
# apenas remove se o item existir


# não da para adicionar valores assim: num [4] = 7

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}...')
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'{a}\n{b}')
# b = a[:] para receber os valores sem linkar as listas

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

valores = list()
for cont in range(0, 3):
    valores.append(int(input('Digite um valor: ')))
for c in valores:
    print(f'{v}...')