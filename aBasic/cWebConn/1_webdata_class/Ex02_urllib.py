

#이번엔 내장 모듈이용

from urllib import request


url ='http://www.google.com' #get방식
site = request.urlopen(url) # 내부모튤은 url 오픈

page = site.read()
print(page) # 여기도 b' 이거로 나옴 1번의 컨텐트와 비슷

print(site.status) # status 응답 상태값 받아오기 200,400 등등

headers = site.getheaders()
print(headers) # 튜플로 헤더내용이나옴 1번에서는 딕셔너리로 나왔었는데 ㅎ

for k in headers:
    print(k[0],'--',k[1]) #튜플은 인덱스가있어서 인덱스로