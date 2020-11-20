dias = float(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pago = dias * 60 + km * 0.15
print('O custo do aluguel foi:R${}{}'.format('\033[1;4;33m', pago))
