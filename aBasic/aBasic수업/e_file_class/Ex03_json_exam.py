'''
 data / sample.json 파일을 읽고 총 합을 구해서 출력해주세용
'''

import json
with open('./data/sample.json','rt',encoding='utf-8-sig') as f:     # 특정 json 파일을 읽기 위해 json module을 import 함  module : 여러 기능을 하는 function을 모아두는 Application
    data=f.read()
    jdata=json.loads(data)

co=0                                                # co = 값의 총계를 구하기 위한 변수 선언
for K,V in jdata.items():
    # print(K,V)
    co+=V['price']*V['count']                       # Value 또한 Dictonary 형태로 넘어와 , 특정 Key 의 Value 를 찾아서 사용 가능함.
print(co)

