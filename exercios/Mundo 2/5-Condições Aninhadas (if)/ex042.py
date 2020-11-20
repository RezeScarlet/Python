r1 = float(input('Digite a medida do primeiro reta do triângulo: '))
r2 = float(input('Digite a medida do segundo reta do triângulo : '))
r3 = float(input('Digite a medida do terceiro reta do triângulo: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    if r1 == r2 == r3:
        t = 'EQUILÁTERO'
    elif r1 == r2 or r1 == r3 or r2 == r3:
        t = 'ISÓSCELES'
    else:
        t = 'ESCALENO'
    print('Sim, é possivel formar um triangulo {} utilizando as medidas: {}, {} e {}'.format(t, r1, r2, r3))
else:
    print('Não, não é possivel formar um triangulo utilizando as medidas: {}, {}, {}'.format(r1, r2, r3))
# https://www.youtube.com/watch?v=dQw4w9WgXcQ
