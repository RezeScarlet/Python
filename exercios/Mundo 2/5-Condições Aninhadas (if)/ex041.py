from datetime import date

l = '\033[m'
a = '\033[1;36m'
print('{}Categoria para natação{}'.format(a, l))
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    c = 'MIRIM'
elif 9 < idade <= 14:
    c = 'INFANTIL'
elif 14 < idade <= 19:
    c = 'JUNIOR'
elif 19 < idade <= 25:
    c = 'SÊNIOR'
elif idade > 25:
    c = 'MASTER'
else:
    c = 'ERRO TENTE NOVAMENTE'
print('Sua idade é {}, então esta na categoria {}{}{}'.format(idade, a, c, l))
c = int(input('Caso deseje saber os critérios para avaliação digite 1: '))
if c == 1:
    print('Até 9 anos     : {}MIRIM{}\n'
          'De 10 a 14 anos: {}INFANTIL{}\n'
          'De 15 a 19 anos: {}JUNIOR{}\n'
          'De 19 a 20 anos: {}SÊNIOR{}\n'
          'Mais de 20 anos: {}MASTER'.format(a, l, a, l, a, l, a, l, a, ))
