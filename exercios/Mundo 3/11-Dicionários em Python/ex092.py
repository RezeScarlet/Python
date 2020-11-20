from datetime import date
print(date.today().year)
dic = {'nome': str(input('Nome: ')), 'idade': date.today().year - int(input('Nascimento: ')),
       'ctps': int(input('Carteira de trabalho [0 não tem]: '))}
if dic['ctps'] != 0:
    dic['contratação'] = int(input('Ano de contratação: '))
    dic['salário'] = float(input('Salario: R$'))
print('>-<'*20)
print(dic)
print(f'Nome: {dic["nome"]}\n'
      f'Idade: {dic["idade"]}')
if dic['ctps'] != 0:
    print(f'CTPS: {dic["ctps"]}\n'
          f'Contratação: {dic["contratação"]}\n'
          f'Salário: {dic["salário"]}\n'
          f'Aposentadoria: {dic["contratação"]+35-date.today().year+dic["idade"]}\n')
