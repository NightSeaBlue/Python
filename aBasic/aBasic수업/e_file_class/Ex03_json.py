#Ex03_json.py

f=open('./data/temp.json','rt',encoding='utf-8-sig')
data=f.read()
f.close()

print(data)
print(type(data))

import json
jdata=json.loads(data)              # json module 을 import 해 json형태의 파일을 읽어들이는 경우 loads 함수를 사용함( loads = 모든 데이터를 읽어들임)
                                    # Return Type : Dictionary
print(jdata)
print(type(jdata))

#items : dictionary 의 Key 와 Value를 뽑아냄
for K,V in jdata.items():
    print(K,':',V)
    print(K,'의 직업은 : ',V['Job'])