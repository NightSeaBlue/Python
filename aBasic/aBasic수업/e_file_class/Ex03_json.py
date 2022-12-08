#Ex03_json.py

f=open('./data/temp.json','rt',encoding='utf-8-sig')
data=f.read()
f.close()

print(data)
print(type(data))

import json
jdata=json.loads(data)

print(jdata)
print(type(jdata))

#items : dictonary 의 Key 와 Value를 뽑아냄
for K,V in jdata.items():
    print(K,':',V)
    print(K,'의 직업은 : ',V['Job'])