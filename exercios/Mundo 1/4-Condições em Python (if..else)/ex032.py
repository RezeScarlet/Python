from datetime import date
ano = int(input('Digite o ano que você deseja saber se é bissexto: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('O ano {}{}{} é um ano bissexto'.format('\033[1;31m', ano, '\033[m'))
        else:
            print('O ano {}{}{} não é bissexto'.format('\033[1;31m', ano, '\033[m'))
    else:
        print('O ano {}{}{} é bissexto'.format('\033[1;31m', ano, '\033[m'))
else:
    print('O ano {}{}{} não é bissexto'.format('\033[1;31m', ano, '\033[m'))
