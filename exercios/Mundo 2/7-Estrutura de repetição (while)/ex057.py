sexo = 0
co = 0
while sexo != 'M' and sexo != 'F':
    co += 1
    if co != 1:
        print('Tente novamente (apenas use F ou M na resposta)')
    sexo = str(input('Digite seu sexo [F/M]: ')).upper().strip()[0]
print('Sexo {} registrado'.format(sexo))
