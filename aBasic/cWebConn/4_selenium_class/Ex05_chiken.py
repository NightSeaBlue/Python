from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('./webdrive/chromedriver.exe')
driver.implicitly_wait(2)


#[연습]

#요부분까지하면 페리카나 리스트 화면이 나오고
#html로 틀까지 볼 수 있다

#페이지 다읽음
for page_num in range(1,11):

    driver.get('https://pelicana.co.kr/store/stroe_search.html?page=%d' % page_num)
    #?page=%d 다음페이지용
    html = driver.page_source
    driver.implicitly_wait(5)
    #print(html)

    #추출 시작
    soup = BeautifulSoup(html,'html.parser')
    name = soup.select('.table tr>td:nth-child(1)')
    #print(name)
    tell = soup.select('.table tr>td:nth-child(3)')
    #print(tell)

    for name, tell in zip(name, tell):
        print(name.text.strip(), tell.text.strip())

#매장명 - 전화번호 만 추출