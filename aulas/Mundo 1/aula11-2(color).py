print("teste {}teste {}teste".format("\033[35m", "\033[m"))
print('-=' * 50)
nome = "GUI"
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho|branco': '\033[31;40m',
         'ne|verm|ama': '\033[1;31;43m'}
print("boa tarde senhor {}{}{}".format(cores['ne|verm|ama'], nome, cores['limpa']))
