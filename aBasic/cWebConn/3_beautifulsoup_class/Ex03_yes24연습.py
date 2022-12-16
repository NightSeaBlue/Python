from bs4 import BeautifulSoup
from urllib import request as req


html = req.urlopen('http://www.yes24.com/Product/Search?domain=ALL&query=python')


soup = BeautifulSoup(html, 'html.parser')

#1번
'''
infos = soup.select('#yesSchList .gd_name')

for i in infos:
    print(i.text)

print(len(infos), '권이 검색되었슴')
'''
imgUrls = soup.select('#yesSchList div.itemUnit img')

for i in imgUrls:
    imgPath = i.attrs['data-original']
    bookName = i.attrs['alt'].strip()
    print(bookName,imgPath)

    req.urlretrieve(imgPath, 'imgs/' + bookName + '.jpg')
