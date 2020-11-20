m = float(input('Digite uma quantidade de metros:'))
c = m * 100
mi = c * 10
v = '\033[1;31;40m'
l = '\033[m'
print('{}{}{} metros é equivalente a {}{}{} centímetros e a {}{}{} milímetros'.format(v, m, l,
                                                                                      v, c, l,
                                                                                      v, mi, l))
