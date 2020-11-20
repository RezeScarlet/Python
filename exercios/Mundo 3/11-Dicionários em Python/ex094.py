amedia = []
mulheres = []
lista = []
pessoa = {}
co = media = 0

while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: ')).upper()
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('ERRO! Responda com F ou M')
    pessoa['idade'] = int(input('Idade: '))
    media += pessoa['idade']
    co += 1
    lista.append(pessoa.copy())
    while True:
        p = str(input('Continuar?[S/N]: ')).upper()
        if p in 'SN':
            break
        else:
            print('ERRO! Responda com S ou N')
    if p in 'N':
        break
media /= co
for c in lista:
    if 'F' == c['sexo']:
        mulheres.append(c['nome'])
    if c['idade'] > media:
        amedia.append(c)
print('<>'*15)
print(f'-> O grupo tem {co} pessoas\n'
      f'-> A média da idade dessas pessoas é {media:5.2f}\n'
      f'-> As mulheres são: {mulheres}\n'
      '-> As pessoas com a idade acima da média são:')
for c in amedia:
    print(f'nome = {c["nome"]}; sexo = {c["sexo"]}; idade = {"idade"}')
