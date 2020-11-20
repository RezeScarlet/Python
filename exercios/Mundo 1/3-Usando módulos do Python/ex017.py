from math import sqrt

co = float(input("Digite o cateto oposto: "))
ca = float(input("Digite o cateto adjacente: "))
h = sqrt(co ** 2 + ca ** 2)
print("A hipotenusa de um triangulo com os catetos {} e {} é {:.3f} ".format(co, ca, h))
# invés de usar sqrt da para elevar a soma dos quadrados dos catetos por 1/2
