from random import shuffle

a1 = input('Digite o nome de um aluno: ')
a2 = input('Digite o nome de mais um aluno: ')
a3 = input('Digite o nome de outro aluno: ')
a4 = input('Digite o nome mais outro aluno: ')
ordem = [a1, a2, a3, a4]
shuffle(ordem)
print('A ordem de apresentação do alunos será: \033[1;34m{}'.format(ordem))
