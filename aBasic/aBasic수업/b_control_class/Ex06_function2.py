
# [추가] 함수도 객체이다
def case1():
    print('case-1')

def case2():
    print('case-2')

def case3():
    print('case-3')

# 함수를 객체로 선언 가능 // 임의의 Dict 에 K,V 지정 (V 에 함수 지정됨)
f={'a1':case1,'a2':case2,'a3':case3}        #Dict 아무것도 지정하지 않은 경우 기본값

print(f['a2'])          # 객체로 표시됨. 주소값도 알려준다.
f['a2']()               # 실제 함수 호출

byunsu='a3'                 # byunsu 에 key 지정 가능

f[byunsu]()

#---------------------------------------
# 글로벌 변수와 지역변수
# #(1)
# temp='글로벌'
# def func():
#     print('1>',temp)
# func()                  # 1>글로벌
# print('2>',temp)        # 2>글로벌

#(2)
temp='글로벌'              #글로벌 변수
def func():
    #print('0>',temp)      # 함수 내 지역변수가 있는 경우, 지역변수 선언이 최우선 되어야 함.
    temp = '지역'         # 지역 변수
    print('1>',temp)
func()                  # 1>지역
print('2>',temp)        # 2>글로벌     글로벌 변수가 선언되어 있지 않은 경우 에러 발생

# 파이썬의 경우, 에러에 대해 정확한 해결책을 제공해 줌

#(3)
temp ='글로벌'
def func():
    global temp
    temp='지역'
    print('1>',temp)

func()
print('2>',temp)

print('='*200)
'''
#----------------------------------------------
# 람다함수 - 한번 사용하고 버리는 함수
# 파이션에서는 람다함수를 한 줄로 작성???

    파이썬 3.x부터는 람다를 권장하지 않는다고.
    몇몇 개발자들이 람다함수 사용시 직관적이지 않다는 이유라는데
    
    종종 사용됨
'''
# 일반함수
def f(x,y):
    return x*y

print(f(3,2))

f=lambda x,y : x*y          #인자와 리턴값을 축약해 표기 가능

print(f(4,5))
print(f(5,6))


#-----------------------------------------------------------
"""  맵리듀스
    (1) map()
         ` 연속 데이터를 저장하는 시퀀스 자료형에서 요소마다 같은 기능을 적용할 때 사용
         ` 형식 : map(함수명, 리스트형식의 입력값)
         ` 파이썬 3.x에서는 list(map(calc, ex)) 반드시 list를 붙여야 리스트 형식으로 반환된다
           파이썬 2.x에서는 list 없이도 리스트 형식으로 반환
    (2) reduce()
         ` 리스트 같은 시퀀스 자료형에 차례대로 함수를 적용하여 모든 값을 통합하는 함수    
    
    파이썬 2.x에서는 많이 사용하던 함수이지만, 최근 문법의 복잡성으로 권장하지 않는 추세란다.
"""
def calc(x):
    return x*2

data=[1,2,3,4,5]

res=list(map(calc,data))        # 리스트의 요소를 1대1로 함수와 매칭시켜서, 결과를 리스트 형태로 담을 수 있음
print(res)

# reduce() 구경만
from functools import reduce

def f(x,y):
    return x*y
data=[1,2,3,4,5]

print(reduce(f,data))
