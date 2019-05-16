#! python3

import requests, sys, webbrowser, bs4
print ('Googling...')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# TODO: Obter os principais links da pesquisa.
soup = bs4.BeautifulSoup(res.text)

# TODO: Abre uma aba do navegador para cada resultado.
linkElems = soup.select('.LC201b a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
	webbrowser.open('http://www.google.com/' + linkElems[i].get('href'))

