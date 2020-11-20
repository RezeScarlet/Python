cidade = str(input('Qual o nome da sua cidade?: ')).upper().strip().split()
print('Sua cidade tem "{}Santo{}" em seu nome?'.format('\033[30m', '\033[m'))
print('SANTO' in (cidade[0]))
