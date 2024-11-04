import urllib
import urllib.request

def site(msg, sit=False):
    url = input(msg)
    try:
        site = urllib.request.urlopen(url)
    except:
        print(f'Não foi possivel acessar o site {url}.')
    else:
        print(f'Deu para acessar o site {url}.')
        if sit:
            print(site.read())


site('Digite uma URL para tentar acessar: ', True)
