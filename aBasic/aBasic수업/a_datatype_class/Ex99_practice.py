# 파이썬 과제

# 1. 평균 계산
a=[]
sum=0
for i in range(5) :
    a.append(int(input('숫자를 입력하세요 : ')))
    sum+=a[i]
print('평균 : ',sum/5)
#2. 사용자에게 입력받은 문자들을 역순으로 출력
word = input('문자열 입력 : ')
print(word[::-1])

#3. 평균 및 표준편차 구하기
import numpy
list = [int(x) for x in input('정수리스트 입력 : ').split()]
print('평균 : {0}\n 표준편차 : {1}'.format(numpy.mean(list),numpy.std(list)))

#4. 키패드 숫자 문자열 처리시 숫자로 반환
s=input('문자열을 입력하세요. : ')
p={'':1, 'a':2, 'b':2, 'c':2,'d':3,'e':3,'f':3,'g':4,'h':4,'i':4,
'j':5,'k':5,'l':5,'m':6,'n':6,'o':6,'p':7,'q':7,'r':7,'s':7,'t':8,'u':8,
'v':8,'w':9,'x':9,'y':9,'z':9}
for char in s :
    print(p.get(char.lower()),end='')