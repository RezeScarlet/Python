from pyconverter import inttobin, bintooct, inttohex
num = int(input('Digite o número que será convertido: '))
con = int(input('Você deseja converter seu número para\n[1]Binario\n[2]Octal\n[3]Hexadecimal\nescolha: '))
b = inttobin(num)
o = bintooct(b)
h = inttohex(num)
if con == 1:
    print('{} em binario é: {}'.format(num, b))
elif con == 2:
    print('{} em octal é: {}'.format(num, o))
elif con == 3:
    print('{} em hexadecimal é: {}'.format(num, h))
else:
    print('Opção invalida, tente novamente')
