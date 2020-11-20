cor = {'l': '\033[m', 'km': '\033[33m', 'rs': '\033[32m'}
velocidade = float(input('Velocidade do automovel em {}km/h{}: '.format(cor['km'], cor['l'])))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você ultrapassou a velocidade maxima permitida de {}80km/h{} e recebeu uma multa de {}R${:.2f}'
          .format(cor['km'], cor['l'], cor['rs'], multa))
else:
    print('Você não passou do limite de velocidade, você é um otimo piloto!')
