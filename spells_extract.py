import bs4 as bs
import urllib.request
import regex as re


sauce = urllib.request.urlopen("http://harrypotter.wikia.com/wiki/List_of_spells").read()

soup = bs.BeautifulSoup(sauce, 'lxml')

# for span in soup.find_all('span', class_="mw-headline"):
#     print(span.get_text())
#
# for div in soup.find_all('div', class_ = 'tabber'):
#     print(div)
#     print(div.get_text())

main_content = soup.find('div', class_ ='tabber')
#print(main_content)

titles = main_content.find_all('span', class_= 'mw-headline')
body = main_content.find_all('dl')
for title, body in zip(titles, body):
    #print(title.text)
    type = re.findall(r'^Type:.*', str(body.text))
    pronounciation = re.findall(r'Pronunciation:.*', body.text)
    print(pronounciation)
#    print(h[0])
#    if len(h)>0:
#         print(re.sub(r'Type: \b'," ",h[0]))
    if len(pronounciation)>0:
        print(re.sub(r'Pronunciation: \b'," ", pronounciation[0]))
    print(body.text)

# for span in main_content.find_all('span', class_= 'mw-headline'):
#     print(span.get_text())