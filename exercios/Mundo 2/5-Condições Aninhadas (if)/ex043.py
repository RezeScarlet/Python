print('\033[1;30mCalculo de IMC (Índice de massa corporal)\033[m')
peso = float(input('Digite seu peso(kg): '))
alt = float(input('Digite sua altura(m): '))
imc = peso / (alt * alt)
print('IMC = {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade mórbida')
c = int(input('Para saber os criterios usados digite 1: '))
if c == 1:
    print('Abaixo de 18.5 : Abaixo do peso\n' 
          'Entre 18.5 e 25: Peso ideal\n'
          'entre 25 e 30  : Sobrepeso\n'
          'entre 30 e 40  : Obesidade\n'
          'acima de 40    : Obesidade mórbida\n')
