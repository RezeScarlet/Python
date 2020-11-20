a = 0
b = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        b += 1
        a += c
print('A soma dos {} números solicitados é {}'.format(b, a))
