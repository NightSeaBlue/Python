
# ------------------------------------------------------
"""
   (2) for문
        for <타켓변수> in 집합객체 :
            문장들
        else:
            문장들

        ` 반복문 뒤에 else는 반복하는 조건에 만족하지 않으면 실행

   (3) while 문
        while 조건문 :
            문장들
        else :
            문장들

"""
a = 112                  # 숫자형
b = ['1','2','3']       # 리스트
c = '987'                # 문자열
#d = tuple(b)             # 튜플
d=('1','2','3')             #튜플
e = dict(k=5, j=6)       # 딕셔너리 (K=V)
e = {'k':5,'j':6}           #딕셔너리 {'K':V}

for entry in e: # a는 반복이 안되지만 b부터 e까지는 반복된다.
   print(entry)


# 딕셔너리 인 경우
for entry in e: # a는 반복이 안되지만 b부터 e까지는 반복된다.
   print(entry,e[entry])
else:
    print('end')        #반복문 작동이 종료되었을 때 end 가 출력됨

# 1부터 10까지 합 구하기
'''
int sum=0;
for (int i=1; i <=10;i++) {
    sum+=i;
}
'''
sum=0
for i in range(1,11) :
    sum+=i

print('합계 : ',sum)

# 1부터 10까지 홀수 합 구하기
sum=0
for i in range(1,11,2) :    #1,3,5,7,9
    sum+=i

print('합계 : ',sum)





"""
[과제] 2단부터 9단까지 이중 반복문으로 출력
"""
for i in range(2,10):
    for j in range(1,10):
        print('{0} 단 : {0}*{1}={2}'.format(i,j,i*j),end='\t')
    print(" ")


print("="*200)

li=['z','y','x']
while li:
    data=li.pop()           #pop 을 통해 배열의 요소가 하나씩 사라짐, 따라서 반복문이 멈출 수 있음
    print(data)
else:
    print('end')