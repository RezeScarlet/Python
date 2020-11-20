br = ('Atlético-MG', 'Internacional', 'São Paulo', 'Palmeiras', 'Vasco da Gama', 'Flamengo', 'Sport Recife',
      'Santos', 'Fortaleza', 'Fluminense', 'Ceará SC', 'Grêmio', 'Corinthians', 'Atlético-GO', 'Athletico-PR',
      'Coritiba', 'Bragantino-SP', 'Botafogo', 'Bahia', 'Goiás')
print(f'A lista dos times: {br}')
print('-----'*40)
print(f'5 primeiros times: {br[0:5]}')
print('-----'*40)
print(f'4 ultimos times{br[-4:]}')
print('-----'*40)
print(f'Times em ordem alfabetica: {sorted(br)}')
print('-----'*40)
print('O Flamengo está na posição: {}'.format(br.index('Flamengo')+1))