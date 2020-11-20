n = int(input('Digite um número: '))
a = '\033[1;30;45m'
b = '\033[1;30;43m'
c = '\033[1;30;46m'

print('-=' * 7)
print('{}{} *  1 = {}\n{}{} *  2 = {}\n{}{} *  3 = {}\n{}{} *  4 = {}\n{}{} *  5 = {}\n{}{} *  6 = {}\n{}{} *  7 = {}'
      '\n{}{} *  8 = {}\n{}{} *  9 = {}\n{}{} * 10 = {}'.format(a, n, n, b, n, 2 * n,
                                                                c, n, 3 * n, a, n, 4 * n,
                                                                b, n, 5 * n, c, n, 6 * n,
                                                                a, n, 7 * n, b, n, 8 * n,
                                                                c, n, 9 * n, a, n, 10 * n))
print('\033[m-=' * 7)
# ta mt chato fazer isso aqui ^
