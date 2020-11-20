salario = float(input('Digite seu salário mensal: R$'))
casa = float(input('Digite o valor total da casa: R$'))
anos = int(input('Digite por quantos anos você pretende pagar: '))
mensal = casa / anos / 12
if mensal > salario / 100 * 30:
    print('Empréstimo não aprovada.\nMotivo:\nA prestação mensal excede o valor maximo para seu salario')
    inf = int(input('Caso queira saber mais detalhes digite 1: '))
    if inf == 1:
        print('Seu empréstimo não foi aprovador pois tendo como base:\nUm salario de R${}\nCasa no valor de R${}\nE '
              'pagamento durante {} anos\nO valor Mensal de pagamento excede os 30% de seu salario sendo assim, '
              'não pode ser aprovado'.format(salario, casa, anos, ))
else:
    print(
        'Tendo como base um salário de R${}\nCasa no valor de R${}\nE pagamento durante {} anos\nO valor '
        'valor da parcela mensal será de R${:.2f}'.format(salario, casa, anos, mensal))
