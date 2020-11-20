mais = total = co = menos = 0
while True:
    co += 1
    lu = 'a'
    nome = str(input('Nome: ')).strip()
    preco = float(input('Preço: R$'))
    total += preco
    if preco > 1000:
        mais += 1
    if preco < menos or co == 1:
        menos = preco
        menor = nome
    while lu not in 'sn':
        lu = str(input('Continuar?[S/N]: ')).lower()
    if lu == 'n':
        break
print(f'Total: R${total}\n'
      f'{mais} custam mais de R$1000\n'
      f'{menor} é o produto mais barato (R${menos})')
