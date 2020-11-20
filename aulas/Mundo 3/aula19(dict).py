pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(f'keys: {pessoas.keys()}')
print(f'values: {pessoas.values()}')
print(f'items: {pessoas.items()}')
# usar aspas duplas quando as aspas ja estão dentro de outras
# não é possivel pessoas[0], o certo é pessoas[nome]
print('=-'*20, '\n')

print('keys: ')
for k in pessoas.keys():
    print(k)
print('\nvalues: ')
for k in pessoas.values():
    print(k)
print('\nitems')
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('=-'*20, '\n')

pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
del(pessoas['sexo'])
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('=-'*20, '\n')

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
# dicionarios podem ficar dentro de listas ou tuplas
# usar 'dict'.copy() para copiar um dicionario
