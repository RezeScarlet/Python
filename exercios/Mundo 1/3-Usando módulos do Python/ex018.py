from math import cos, radians, sin, tan

angulo = (float((input("Digite o angulo: "))))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print("O angulo de {}{}{} tem:\nO SENO de {}{:.2f}{}\nO COSSENO de {}{:.2f}{}\nE a TANGENTE de {}{:.2f}"
      .format('\033[1;4;36m', angulo, '\033[m', '\033[1;4;36m', seno, '\033[m',
              '\033[1;4;36m', cosseno, '\033[m', '\033[1;4;36m', tangente))
