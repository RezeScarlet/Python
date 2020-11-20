from random import randint
from time import sleep

num = randint(0, 5)
chute = (int(input('Qual é o numero aleatório de 0 a 5: ')))
print('\033[31mProcessando.')
sleep(1)
print('\033[33mProcessando..')
sleep(1)
print('\033[32mProcessando...\033[m')
sleep(1)
if chute == num:
    print('Parabéns você é um otimo vidente!')
else:
    print('Você ainda não dominou a arte oculta da adivinhação, treine mais!')
