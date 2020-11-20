print('{:=^40}'.format('LOJINHAAAAAAAA'))
preco = float(input('Digite o valor do produto que deseja comprar: R$'))
metodo = int(input('[1] Dinheiro/cheque\n[2] Cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão\nQual método? '))
if metodo == 1:
    total = preco - (preco / 100 * 10)
elif metodo == 2:
    total = preco - (preco / 100 * 5)
elif metodo == 3:
    total = preco
    print('Compra parcelada em 2x de R${:.2f} SEM JUROS'.format(total/2))
elif metodo == 4:
    total = preco + (preco / 100 * 20)
    vezes = int(input('Quantas parcela: '))
    print('Compra parcelada em {}x de R${:.2f} COM JUROS'.format(vezes, total / vezes))
else:
    total = 0
    print('OPÇÃO INVALIDADE, TENTE NOVAMENTE')
print('O valor total da compra será de R${}(metodo {})'.format(total, metodo))
