from ex115.lib.interface import *


def arqexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararq(nome):
    try:
        a = open(nome, 'wt+')
    except:
        print('\033[1;31mErro! não foi possivel criar o arquivo!\033[m')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerarq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[1;31mERRO ao ler arquivo!\033[m')
    else:
        cabeçalho('Pessoas Cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<28}{dado[1]:>3} anos')
    finally:
        a.close


def cadastrar(arq, nome='desconhecido', idade=1):
    try:
        a = open(arq, 'at')
    except:
        print('\033[1;31mERRO ao abrir arquivo!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}')
        except:
            print('\033[1;31mERRO ao registrar dados!\033[m')
    finally:
        a.close()