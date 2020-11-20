a = float(input('Qual seu salario:R$'))
s = a + a * 15 / 100
print('Seu salario com 15% de aumento é:R${}{:.2f}'.format('\033[4;31m', s))
