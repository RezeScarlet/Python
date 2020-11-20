frase = str(input('Digite uma frase: ')).strip().upper()
print(
    'Essa frase possui \033[31m{}\033[m letras A, sendo a primeira na posição \033[31m{}\033[m e a ultima na posição '
    '\033[31m{}'.format(
        frase.count('A'),
        frase.find('A') + 1,
        frase.rfind('A') + 1
        ))
