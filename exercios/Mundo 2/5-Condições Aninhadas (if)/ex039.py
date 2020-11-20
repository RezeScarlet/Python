from datetime import date

print('\033[1;4;30mCaso você não tenha se alistado\033[m')
ano = int(input('Digite o ano em que você nasceu: '))
data = date.today()
idade = data.year - ano
if idade > 18:
    print('Você já devia ter se alistado a {} anos({})'.format(idade-18, ano+18))
elif idade < 18:
    print('Você irá se alistar daqui a {} anos({})'.format(18-idade, ano+18))
else:
    print('Você já esta na idade de se alistar!')
