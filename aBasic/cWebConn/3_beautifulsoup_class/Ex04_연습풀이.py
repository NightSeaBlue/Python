'''
from bs4 import BeautifulSoup
from urllib import request as req
from urllib.parse import quote_plus
'''
#1번 문제
#html = req.urlopen('https://www.pythonscraping.com/pages/warandpeace.html')

#soup = BeautifulSoup(html, 'html.parser')

#greenText = soup.select('.green')

#for i in greenText:
  #  print(i)

#print('-----------------------------------')



#2번 문제
'''
html2 = req.urlopen("http://www.pythonscraping.com/pages/page3.html")


soup1 = BeautifulSoup(html2, 'html.parser')

for i in soup1:
    #1번 타이틀 3번 가격을 가져와서 둘을 zip으로 묶어서 뽑아냄
    product = soup1.select('.gift>td:nth-child(1)')
    price = soup1.select('.gift>td:nth-child(3)')
    for product, price in zip(product, price):
        print('타이틀 : ',product.text.strip() + '가격 : ', price.text.strip())
'''
        



from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import os
from urllib import request, parse

os.makedirs('wikiImage', exist_ok=True)

url='https://wikidocs.net/'
html = request.urlopen(url)

soup = BeautifulSoup(html,'html.parser')

#책제목
titles = soup.select('#books .book-subject')
#책 저자
author = soup.select('#books .book-detail .menu_link')
#사진
imgs = soup.select('#books .book-image')

#먼저 src 속성 확인해보기
for i in imgs:
    print(i.attrs['src'])

for t, a in zip(titles, author):
    print("책제목 : ",t.text, " - 책 저자 : ",a.text)

for i, t in zip(imgs, titles):
    try: # 기존 url에 조인으로 속성값을 붙혀주는 거고 사진명을 포멧으로 제목까지 붙힘
        request.urlretrieve(parse.urljoin(url,i.attrs['src']),'./wikiImage/{}.png'.format(t.text))
    except UnicodeEncodeError:
        i = quote_plus(parse.urljoin(url,i.attrs['src']),safe="://")
        request.urlretrieve(i,'./wikiImage/{}.png'.format(t.text))
print(len(titles))




