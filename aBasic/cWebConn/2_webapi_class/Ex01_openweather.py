"""
    전세계날씨제공 API : http://openweathermap.org

    1. 회원가입 : 메뉴 > Sign Up > 사용용도 : Education > 대충가입 (무료는 1번에 60번 호출 가능 )
    2. 개발자모드 : Sign In > API Keys 에서 내가 발급받은 키 (추가 키 가능)
    3. 발급받고 바로 지정 안됨 (시간소요)
"""
import requests
import json # 문자열 딕셔너리로 바꾸려고


# API 키를 지정합니다. 자신의 키로 변경해서 사용해주세요.
apikey = "1db47184ebbc18af53fd996be840d270"

# 날씨를 확인할 도시 지정하기
cities = ["Seoul,KR", "Tokyo,JP", "New York,US"]

# url 지정
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

# 켈빈 온도를 섭씨 온도로 변환하는 함수
k2c = lambda k: k - 273.15

# q={city}
for cityname in cities:
    url = api.format(city=cityname, key=apikey)
    print(url)
    res = requests.get(url)
    print(res.text)
    print(type(res.text)) # str 나옴 딕셔너리 형태를 띈 문자열임.. 딕셔너리로 바꿔 볼까?

    data = json.loads(res.text)
    print(type(data)) # 딕셔너리로 바꿈


    print('도시명 : ', data['name'])

    #print('날씨 :', data['weather']['description']) # 이거안나옴 리스트형식이라 풀어줘야함
    #weather라는 리스트안에 0번째중에 description를 찾은거임
    print('날씨 :', data['weather'][0]['description'])

    #최고온도
    print('최고온도 : ',k2c(data['main']['temp_max']))


    #최저온도
    print('최저온도 : ',k2c(data['main']['temp_min']))

    #습도
    print('습도 : ', data['main']['humidity'])


