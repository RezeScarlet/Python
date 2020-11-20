import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
    print('O site esta online')
except urllib.error.URLError:
    print('O site esta fora do ar')
