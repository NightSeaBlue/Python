"""
    파이썬에서 웹을 요청할 수 있는 라이브러리
        1- requests 라이브러리 (s붙음 주의) - 추가해야함 외장모듈이라 설치
        2- urllib 라이브러리 - 내장모듈 > 딱히 다운필요없음
            > 기본적 모듈

    차이점
        1- requests는 요청 메소드(get/post)를 구분하지만 urllib는 보내는 데이타 여부에 따라 구분됨
        2- 데이타 보낼 때 requests는 딕셔러니 형태로 urllib는 인코딩한 바이너리 형태로 보낸다
        
    requests 라이브러리 추가
    메뉴 > File > Settings > Project Interpreter > + 버튼 > 'requests' 검색 후 인스톨




[ requests 모듈 ]
(1) Rest API 지원
    import requests
    resp = requests.get('http://www.mywebsite.com/user')
    resp = requests.post('http://www.mywebsite.com/user')
    resp = requests.put('http://www.mywebsite.com/user/put')
    resp = requests.delete('http://www.mywebsite.com/user/delete')




(2) 파라미터가 딕셔너리 인수로 가능
    data = {'firstname':'John', 'lastname':'Kim', 'job':'baksu'}
    resp = requests.post('http://www.mywebsite.com/user', data=userdata)




(3) json 디코더 내장 (따로 json 모듈 사용 안해도 됨)
    resp.json()
"""

import requests #>다운받아줬던 외부 모듈

url ='http://www.google.com' #get방식

res = requests.get(url) # 외부모듈은 겟으로 가져오기

print(res) # 리스폰스 200뜸 즉 성공 / 그리고 객체로 표현됌
print('-'*50)
print(res.text) # 구글에서 소스보기했을떄 소스응답들이 뜸
print('-'*50)
print(res.content) # b ' 내용이뜸
print('='*50)
print(res.headers) # 웹에서 헤더들의 정보가 나옴 / 딕셔너리 방식으로 나옴 키 벨류

#그래서 키벨류 나오게 만듬
resH = res.headers
for k, v in resH.items():
    print(k,resH[k])





















