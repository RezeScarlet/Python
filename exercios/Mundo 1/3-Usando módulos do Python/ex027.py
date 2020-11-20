nome = input('Digite seu nome completo: ')
lista = nome.split()
print('Nome completo: \033[30m{}\033[m\nPrimeiro Nome: \033[30m{}\033[m\nUltimo Nome  : \033[30m{}'.format(nome, lista[0], lista[-1]))