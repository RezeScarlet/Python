a = float(input('Digite a altura da parede:'))
la = float(input('Digite a largura de sua parede:'))
li = (a*la) / 2
print('Será necessario {}{:.2f}{} litros de tinta para pintar uma parede de {}{:.2f}{}m²'
      .format(li, a*la))
