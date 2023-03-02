from urllib.request import urlopen
from bs4 import BeautifulSoup

# Open and parse the Wikipedia page
html = urlopen('https://en.wikipedia.org/wiki/Web_scraping')
bs = BeautifulSoup(html, 'html.parser')

# Find links in "See also" section and print the first paragraph of each
for link in bs.find('div', {'class': 'div-col'}).ul.find_all('a'):
    
    html = urlopen('https://en.wikipedia.org' + link.attrs['href'])
    bs = BeautifulSoup(html, 'html.parser')
    print('----')
    print('First paragraph of "' + link.get_text() + '" (https://en.wikipedia.org' + link.attrs['href'] + '):')
    print()
    # Check to skip the first empty <p> tag
    if bs.find('p', {'class': 'mw-empty-elt'}):
        print(bs.find('p').find_next('p').get_text())
    else:
        print(bs.find('p').get_text()) 