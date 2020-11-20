aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))
print('<>'*10)
if aluno['media'] <= 4.5:
    aluno['situ'] = 'reprovado(a)'
elif 4.5<aluno['media']<7:
    aluno['situ'] = ' de recuperação'
else:
    aluno['situ'] = 'aprovado(a)'
print(f'Aluno: {aluno["nome"]}\n'
      f'Média: {aluno["media"]}\n'
      f'Sendo assim {aluno["nome"]} esta {aluno["situ"]}')
