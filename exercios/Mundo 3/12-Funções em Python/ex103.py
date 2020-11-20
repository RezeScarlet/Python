def ficha(j='<desconhecido>', gol=0):
    print(f'jogador: {j} |gols: {gol}')


n = str(input('Nome do jogador: ')).strip()
g = str(input('Número de gol(s): '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    ficha(gol=g)
else:
    ficha(n, g)
