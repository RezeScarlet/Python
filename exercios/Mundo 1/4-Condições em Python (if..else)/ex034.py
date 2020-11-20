salario = float(input('Digite seu salário:R$'))
if salario <= 1250.00:
    aumento = salario + (salario / 100 * 15)
    print('Seu salário de {}{}{} terá um aumento de \033[32m15%\033[m, sendo assim será de {}'.
          format('\033[1;36m', salario, '\033[m', '\033[1;36m', aumento))
else:
    aumento = salario + (salario / 10)
    print('Seu salário de {}{}{} terá um aumento de \033[32m10%\033[m, sendo assim será de {}'
          .format('\033[1;36m', salario, '\033[m', '\033[1;36m', aumento))
