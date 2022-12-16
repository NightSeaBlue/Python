"""
    BeautifulSoup 모듈에서
    - HTML의 구조(=트리구조)에서 요소를 검색할 때 : find() / find_all()
    - CSS 선택자 검색할 때 : select() /  select_one()
"""

from bs4 import BeautifulSoup

html = """
    <html><body>
        <div id='course'>
            <h1>빅데이터 과정</h1>
        </div>
        <div id='subjects'> 
            <ul class='subs'>
                <li>머신러닝</li>
                <li>데이터 처리</li>
                <li>데이타 분석</li>
            </ul>
        </div>
    </body></html>
"""

#늘 파싱 먼저해랑
soup = BeautifulSoup(html,'html.parser')


#1번 id로 찾기!
h = soup.select('#course > h1')
print(h) #select로 하면 하나여도 리스트로 잡힘
h2 = soup.select_one('#course > h1')
print(h2) #그래서 하나는 셀렉트온으로 가져오는게 더 깔꼼


#(2) 클래스로 검색

li = soup.select('.subs > li')
print(li)

for i in li:
    print(i.text)



