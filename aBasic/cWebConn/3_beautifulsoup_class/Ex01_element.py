"""
    bs4 라이브러리 : 웹에서 가져온 HTML코드를 파이썬에서 사용하기 편하게 파싱해주는 라이브러리
            [참고] 웹에서 가져온 HTML코드 가져오는 방법
                - requests 모듈
                - urllib 의 request 모듈

    BeautifulSoup 모듈
        - find()
        - find_all()
    
    [참고] 파서의 종류 
        - lxml : c로 만들어져 속도 빠름
        - html5lib : 파이썬으로 만들어서 lxml보다 느림
        - html.parser (*): 파이썬 버전을 확인해서 사용
"""

from bs4 import BeautifulSoup as Bs

#지금 어떤 웹페이지에서 응답을 받았다 생각하자  html
html = """
    <html><body>
        <h1>스크레이핑 연습</h1>
        <p>웹페이지 분석하자</p>
        <p>데이타 정제하기</p>
    </body></html>
"""


# 1. 데이타 파서하기
soup = Bs(html, 'html.parser')

# 2. 원하는 요소 접근하기
h1 = soup.html.body.h1
print(h1)

# 3. 요소의 내용 추출하기

pTags = soup.find_all('p') # p태그의 모든것
print(pTags) # 리스트로 나옴

