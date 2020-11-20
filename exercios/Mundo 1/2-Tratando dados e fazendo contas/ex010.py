r = float(input('Digite quanto reais você tem: R$'))
d = r / 5.27
a = '\033[4;35m'
b = '\033[m'
print('{}{:.2f}{} reais são equivalentes a {}{:.2f}{} dólares'.format(a, r,b,
                                                                      a, d, b))
