#! python3
# searchpypi.py  - Opens several search results.

import requests, webbrowser, bs4

res = requests.get('https://nardisjazz.com/')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElems = soup.select('#evcal_list')
a = linkElems[0].get('class')

"""
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
    """