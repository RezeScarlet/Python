def notas(*n, situ=False):
    """

    :param n: notas dos alunos
    :param situ: se a situação da sala será informada
    :return: a lista com todas as informações sobre a sala
    """
    media = 0
    for c, l in enumerate(n):
        if c == 0:
            menor = maior = l
        elif l > maior:
            maior = l
        elif l < menor:
            menor = l
        media += l
    media /= len(n)

    if media == 10:
        media = 'Muito bom'
    elif 10 > media > 6:
        sit = 'bom'
    elif 4 < media < 6:
        sit = 'ruim'
    elif media < 4:
        sit = 'muito ruim'

    al = {'Quantidade de notas': len(n),
          'Maior nota': maior,
          'Menor nota': menor,
          'A média da turma': media}
    if situ:
        al['Situação'] = sit
    return al


sala = notas(5.5, 2.5, 1.5, situ=True)
print(sala)
