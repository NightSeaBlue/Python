"""
 urllib.parse.urljoin() : 상대경로를 절대경로로 변화하는 함수
"""




from urllib import parse

baseUrl = 'http://www.example.com/html/a.html'

#기존 url에 추가를 해주는 느낌
#http://www.example.com/html/b.html  > a.html' 가 바뀜 동일부분은 그대로인데
#달라진 url 부분이 추가되는듯
print(parse.urljoin(baseUrl, 'b.html'))

#http://www.example.com/html/sub/c.html
print(parse.urljoin(baseUrl, 'sub/c.html'))

#근데 절대경로로 주면 html 무시하고 도메인 바로 아래부터 실행된다
print(parse.urljoin(baseUrl, '/sub/d.html'))

# 상대경로로 부모한태 올라갔음 그다음 작성되니 > 내위치는 html임
#http://www.example.com/temp/e.html
print(parse.urljoin(baseUrl, '../temp/e.html'))

# 덮어쓰기 새로운 도메인은 덮어써버린다
print(parse.urljoin(baseUrl,'http://www.daum.net'))
