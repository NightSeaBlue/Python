"""
@ 네이버 금융에서 환률 정보 가져오기

` 크롬에서 네이버 > 금융 > 시장지표 > 미국 USD 금액을 부분을 개발자 모드로 확인
      <div class='head_info'>
         <span class='value'>1.098.50</span>
"""


from bs4 import BeautifulSoup
from urllib import request as req


# 웹 문서 가져오기
url = 'https://finance.naver.com/marketindex/'
res = req.urlopen(url)

#파싱하기
soup = BeautifulSoup(res,'html.parser')
#print(soup)
#추출하기
won = soup.select('#exchangeList span.value')


rows = []
for tag in won:
    name = tag.get_text()
    row = [name]
    rows.append(row)

print('달러: ' ,rows[0])
print('엔화: ', rows[1])
print('유로: ', rows[2])
print('켁켁: ', rows[3])









