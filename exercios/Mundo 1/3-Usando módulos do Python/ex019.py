from random import choice

a1 = input("Digite o nome de um aluno: ")
a2 = input("Digite o nome de outro aluno:")
a3 = input("digite o nome de mais um aluno: ")
a4 = input("Digite o nome do ultimo aluno: ")
ganhador = choice([a1, a2, a3, a4])
#                    ^pode fazer uma variavel ser uma lista
print('O aluno que ira apagar a lousa será: \033[1;4;32m{}'.format(ganhador))
