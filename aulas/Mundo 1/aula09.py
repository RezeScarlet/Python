frase = 'Curso em Vídeo Python'
print(frase[2:9:])
# quando não tem nada antes/depois do ":" significa que é o começo/final
# print("""Mama, just killed a man put a gun against his head
# Pulled my trigger, now he's dead
# Mama, life had just begun
# But now I've gone and thrown it all away
# Mama, ooh didn't mean to make you cry
# If I'm not back again this time tomorrow
# Carry on, carry on as if nothin' really matters
# Too late, my time has come send shivers down my spine
# My body's aching all the time
# Goodbye everybody, I've got to go
# Gotta leave you all behind and face the truth
# Mama, ooh""")
# as 3 aspas duplas selecionam tudo que está a frente dela independente de sua linha
print(frase.upper().count('O'))
# o upper deixa tudo maiusculo
print(len(frase.strip()))
# len mostra o tamanho da string e strip elimina os espaços desnecessarios
print(frase.replace('Python', 'Android'))
# nesse caso acima as a string é modificada apenas naquele comando, para modificar é preciso colocar "frase=..."
print('Curso' in frase)
# identifica se determinada parte da string existe
print(frase.lower().find('vídeo'))
# lower deixa tudo minusculo e find encontra a palavra
dividido = (frase.split())
# cria uma lista com as palavras presentes na string
print(dividido[2])
# "[]" o numero identifica quais palavras estão sendo selecionadas
