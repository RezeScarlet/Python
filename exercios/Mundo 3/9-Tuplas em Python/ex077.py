pa = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
      'PROGRAMADOR', 'FUTURO')
for c1 in pa:
    print(f'\nNa palavra {c1:11} temos: ', end='')
    for c2 in range(0, len(c1)):
        for c3 in 'AEIOU':
            if c1[c2] == c3:
                print(f'{c3} ', end='')