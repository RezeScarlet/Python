nome = str(input('Qual seu nome?: '))
if nome == 'Gustavo':
    print('que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}'.format(nome))
# lembrar de colocar ':' no fim da linha do 'if' e do 'else'
# quando usar o '=' no 'if ele aparece como '=='

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
print('S sua nota média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
# print('PARABÉNS!' if m>=6 else 'ESTUDE MAIS!')