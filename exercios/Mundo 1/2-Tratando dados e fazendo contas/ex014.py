C = float(input('Informe a temperatura em °C: '))
F = C * 1.8 + 32
print('{}{}{}°C é equivalente a {}{:.2f}{}°F'.format('\033[1;4;35m', C, '\033[m', '\033[1;4;35m', F, '\033[m'))
