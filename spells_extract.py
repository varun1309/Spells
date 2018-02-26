import bs4 as bs
import urllib.request
import regex as re


sauce = urllib.request.urlopen("http://harrypotter.wikia.com/wiki/List_of_spells").read()

soup = bs.BeautifulSoup(sauce, 'lxml')

for span in soup.find_all('span', class_="mw-headline"):
    print(span.get_text())

for div in soup.find_all('div', class_ = 'tabber'):

    print(div.get_text())