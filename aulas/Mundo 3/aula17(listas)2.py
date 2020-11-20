teste = ['Gustavo', 40]
print(teste)
galera = list()
galera.append(teste)
print(galera)
teste[0] = 'Maria'
teste[1] = 22
print(galera)
# Quando uma lista é adicionada dentro de outra ambas ficam ligadas, a não ser que tenha [:] ex: galera.append(teste[:])

print('=-'*20)
galera = [['João', 19], ['Ana', 12], ['Joaquim', 13], ['Maria', 45]]
print(galera[0])
print(galera[2][1])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

print('=-'*20)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
    else:
        print(f'{p[0]} é menor de idade')

print('=-'*20)
galera = []
dado = []
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)