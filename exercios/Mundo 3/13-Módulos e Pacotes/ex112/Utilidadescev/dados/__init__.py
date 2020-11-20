def leiaDinheiro(msg):
    while True:
        n = input(msg).strip().replace(',', '.')
        try:
            float(n)
            break
        except ValueError:
            print('\033[31mErro, Digite novamente\033[m')
    return float(n)
