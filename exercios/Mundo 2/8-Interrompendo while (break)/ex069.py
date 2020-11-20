co1 = 0
co2 = 0
co3 = 0
while True:
    sexo = 'ana'
    idade = -1
    lu = 'ana'
    print('=='*10)
    while sexo not in 'fm':
        sexo = str(input('\nQual seu sexo?[F/M]: ')).lower()
    while 100 < idade or idade < 0:
        idade = int(input('Qual sua idade?: '))
    if idade >= 18:
        co1 += 1
    if sexo == 'm':
        co2 += 1
    if sexo == 'f' and idade <= 20:
        co3 += 1
    while lu not in 'sn':
        lu = str(input('Deseja continuar?[S/N]: ')).lower()
    if lu == 'n':
        break
print(f'{co1} tem mais de 18 anos\n{co2} são homens\n{co3} são mulheres com menus de 20 anos')
