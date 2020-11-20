c = 0
aluno = []
while True:
    aluno.append([])
    aluno[c].append(str(input('Nome: ')))
    aluno[c].append(float(input('Nota 1: ')))
    aluno[c].append(float(input('Nota 2: ')))
    c += 1
    para = str(input('Continuar?[S/N]: '))
    if para in 'nN':
        break
print('*----------------------*\n'
      '|No.     Nome     Média|\n'
      '|----------------------|')
for c, a in enumerate(aluno):
    print(f'|{c}  {a[0]:^15}{(a[1] + a[2]) / 2:>4}|')
print('*----------------------*')
while True:
    al = int(input('\nMostrar notas de qual aluno?(999->nenhum): '))
    if al <= len(aluno):
        print(f'Aluno(a): {aluno[al][0]}\n'
              f'Nota 1: {aluno[al][1]} |Nota 2: {aluno[al][2]}')
    else:
        break
