dic = {}
dic['nome'] = str(input('Nome: '))
part = int(input('Partidas: '))
dic['gols'] = []
for c in range(0, part):
    dic['gols'].append(int(input(f'Gols na partida {c+1}: ')))
    if c == 0:
        dic['total'] = dic['gols'][0]
    else:
        dic['total'] += dic['gols'][c]
print('-<>-'*15)
print(dic)
print('----'*15)
print(f'Nome: {dic["nome"]}\n'
      f'Gols: {dic["gols"]}\n'
      f'Total: {dic["total"]}')
print('----'*15)
print(f'O jogador {dic["nome"]} jogou {part} partidas.')
for c in range(0, part):
    print(f'-> Partida {c+1}, {dic["gols"][c]} gols.')
print(f'Foi um total de {dic["total"]} gols.')
print('-<>-'*15)
