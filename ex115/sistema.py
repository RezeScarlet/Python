from ex115.lib.interface import *
from time import sleep
from ex115.lib.arquivo import *

arq = 'data.txt'
if arqexiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    criararq(arq)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resp == 1:
        # listar conteudo do arquivo data.txt
        lerarq(arq)
    elif resp == 2:
        # adicionar ao arquivo
        cabeçalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        # finalizar programa
        break
    else:
        print('\033[31;1mErro! Digite uma opção válida!\033[m')
    sleep(2)
cabeçalho('Você saiu do sistema, até a proxima')
