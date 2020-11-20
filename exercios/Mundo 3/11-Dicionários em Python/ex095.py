lista = []
jogador = {}
while True:
    jogador['nome'] = str(input('Nome: '))
    part = int(input('Partidas: '))
    jogador['gols'] = []
    for c in range(0, part):
        jogador['gols'].append(int(input(f'Gols na partida {c+1}: ')))
        if c == 0:
            jogador['total'] = jogador['gols'][0]
        else:
            jogador['total'] += jogador['gols'][c]
    lista.append(jogador.copy())
    while True:
        p = str(input('Continuar?[S/N]:')).upper()[0]
        if p in 'SN':
            break
        else:
            print('Erro, responda  com S ou N')
    if p in 'nN':
        break
print('-<>-'*15)
print(f'{"cod":<4}{"Nome":<15}{"Gols":^10}{"Total":>15}')
print('----'*15)
co = -1
for c in lista:
    co += 1
    print(f'{co:<4}{c["nome"]:<15}{str(c["gols"]):^10}{c["total"]:>15}')
print('----'*15)
while True:
    p = int(input('Mostrar os dados de qual jogador[999 para]: '))
    if p == 999:
        break
    if p >= len(lista):
        print('ERRO jogador desconhecido')
    else:
        print('----'*15)
        print(f'O jogador {lista[p]["nome"]} jogou {len(lista[p]["gols"])+1} partidas.')
        co = 0
        for c in lista[p]["gols"]:
            co += 1
            print(f'-> Partida {co}, {c} gols.')
        print(f'Foi um total de {lista[p]["total"]} gols.')
print('-<>-'*15)
