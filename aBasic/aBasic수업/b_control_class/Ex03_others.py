msg = '행복해'            # 문자열
li = ['a','b','c']       # 리스트
tpl = ('ㄱ','ㄴ','ㄷ')    # 튜플
di = {'k': 5, 'j': 6, 'l':7 }    # 딕셔너리
#-------------------------------------------
#1. Unpacking (요소 분해)

a,b,c=msg       #자동으로 인덱스가 지정되어 하나하나씩 담김.
print(a)
print(b)
print(c)

print('='*200)

alist=[(1,2),(3,4),(5,6)]

for temp in alist:
    print(temp)


for first,second in alist:
    print('{} + {} = {}'.format(first,second,first+second))
    
    

#-------------------------------------------------------------
# (2) enumerate() 함수
#               - 요소와 인덱스를 같이 뽑아주는 함수
'''
    [참고] 자바에서
        Iterator => Enumerator(이전버전)
'''

blist=['개발자','코더','전문가','노가다']

for value in blist :
    print(value)

for idx,value in enumerate(blist) :
    print(idx,value)

#-------------------------------------------------------------
# (3) zip() 함수

days=['월','화','수']
doit=['잘자기','숨쉬기','밥먹기','멍때리기']

print(zip(days,doit))
print(list(zip(days,doit)))
print(dict(zip(days,doit)))
print(tuple(zip(days,doit)))

for date,todo in zip(days,doit) :
    print(date,todo)                     # 튜플로 나옴.


month=[11,12,1]

print(list(zip(days,doit,month)))