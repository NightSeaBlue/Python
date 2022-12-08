'''
 data / sample.json 파일을 읽고 총 합을 구해서 출력해주세용
'''

import json
with open('./data/sample.json','rt',encoding='utf-8-sig') as f:
    data=f.read()
    jdata=json.loads(data)

co=0
for K,V in jdata.items():
    # print(K,V)
    co+=V['price']*V['count']
print(co)

