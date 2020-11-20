nome = input('Qual o seu nome? ')
cores = {'limpa': '\033[m',
         'roxo': '\033[35m'}
print('é um prazer te conhecer {}{}{}!'.format(cores['roxo'], nome, cores['limpa']))
