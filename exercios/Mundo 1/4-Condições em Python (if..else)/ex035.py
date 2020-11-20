r1 = float(input('Digite a medida do primeiro reta do triângulo: '))
r2 = float(input('Digite a medida do segundo reta do triângulo: '))
r3 = float(input('Digite a medida do terceiro reta do triângulo: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('Sim, é possivel formar um triangulo utilizando as medidas: \033[31m{}, {} e {}'.format(r1, r2, r3))
else:
    print('Não, não é possivel formar um triangulo utilizando as medidas: \033[31m{}, {} e {}'.format(r1, r2, r3))
