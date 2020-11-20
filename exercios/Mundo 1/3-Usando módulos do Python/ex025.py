nome = str(input('Digite seu nome completo:').strip().upper())
print('Você tem "{}Silva{}" como sobrenome? {}'.format('\033[30m', '\033[m', 'SILVA' in nome))
