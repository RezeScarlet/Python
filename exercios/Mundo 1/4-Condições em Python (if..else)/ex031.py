km = float(input('Digite a distancia que você viajará em {}km{}: '.format('\033[30m', '\033[m')))
if km >= 200:
    preco = km * 0.45
else:
    preco = km * 0.50
print('O preço da sua passagem para uma viajem de {}{}km\033[m sera de {}R${:.2f}'
      .format('\033[34;1m', km, '\033[33;1m', preco))
# preço = km * 0.50 if km <= 200 else km * 0.45
