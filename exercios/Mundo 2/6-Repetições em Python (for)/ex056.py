p = int(input('Quantas pessoas serão analisadas?: '))
media = 0
mais = 0
menos = 0
for c in range(1, p+1):
    print('☰☰☰☰☰ {}° pessoa ☰☰☰☰☰'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).upper()
    media = media + idade
    if idade > mais and sexo == 'M':
        mais = idade
        velho = nome
    if idade <= 20 and sexo == 'F':
        menos = menos + 1
media = media / 4
print('O homem mais velho se chama {} e tem {} anos'.format(velho, mais))
print('A idade média dessas pessoas é {:.1f}'.format(media))
if menos > 1:
   print('Entre essas pessoas {} são mulheres com menos de 20 anos de idade'.format(menos))
elif menos == 1:
   print('Entre essas pessoas apenas uma é uma mulher com menos de 20 anos de idade')
else:
   print('Nenhumas dessas pessoas é uma mulher com menos de 20 anos de idade')
# oiee faz um if para c == 1 e lá bota uma variavel unica para o nome da pessoa
