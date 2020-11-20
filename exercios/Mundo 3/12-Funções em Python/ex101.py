from datetime import date


def voto(i):
    if i < 16:
        return 'Negado'
    elif 65 > i >= 18:
        return 'Obrigatório'
    elif 16 <= i < 18 or i > 65:
        return 'Opcional'


idade = date.today().year - int(input('Ano de nascimento: '))
print(f'Com {idade} anos o voto é {voto(idade)}')
