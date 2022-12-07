"""
    [ 함수 ]

     - 반복적인 구문을 만들어 함수로 선언하여 간단하게 호출만 하고자 한다
     - 역할별 구문을 작성한다

     def 함수명(매개변수):
        수행할 문장들
"""

# #(0) 인자도 없고 리턴값도 없는 공함수
# def func():
#     print('Inside Func')
#
# func()
# result =func()
# print(result)       # Return 값이 없으므로 None 으로 나옴
#
# #-------------------------------------------------------------
# print('='*200)
#
# #(1) 리턴값이 있는 함수
# def func(arg):
#     return arg+5
#
# num = func(10)
# print(num)
#
# #(1) 리턴값이 여러개 있는 함수
# def func(arg):
#     return arg+5,arg-5,arg*5
#
# result=func(10)
# print(result)       #tuple 형태로 리턴
#
# a,b,c=func(10)       #Unpacking
# print(a,b,c)       #요소가 하나씩 뽑혀서 나열됨
#
# #(2) 위치인자   # 입력하는 순서대로 그 인자에 할당됨
# def func(greeting,name):
#     print(greeting,'!!!!',name,'님')
#
# func('오하이오','춘시쿠상')
# func('기리보이','아령하세요')
#
# #(3) 키워드인자  (Keyword argument)  #입력받는 인자의 매핑을 할 수 있음.
# func(name='기리보이',greeting='아령하세요')


#(4) 인자의 기본값
# def func(greeting,name='홍길동'):              # 값을 지정하지 않을 경우 기본인자 지정 가능.
#     print(greeting,'!!!!',name,'님')
#
# func('하이','박길동')
# func('안녕')                  #인자가 지정되지 않은 경우 기본값이 들어와 출력됨












'''
#----------------------------------------------------------------
# (5) 위치 인자 모으기 (*)

첫번째와 두번째는 인자가 반드시 들어가고 세번째는 인자가 들어갈 수도 있고 없으면 0으로 초기화한다
그러나 네번째 인자부터는 정확히 모른다면?

print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))       # args에 7,8,9가 튜플로 들어간다
'''
def func(a,b,c=0,*args):            #*args = 추가로 입력되는 인자들을 args로 처리함
    sum=a+b+c
    for i in args:
        sum+=i
    return sum

print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))       # args에 7,8,9가 튜플로 들어간다

print('='*200)

# (6) 키워드 인자 모으기
def func(a,b,c=100,*args,**kwargs):     #*args : 정확히 모르는 인자들 #**kwargs 정확히 모르는 키워드들
   sum=a+b+c
   for i in args:
       sum+=i
   for k in kwargs:
       sum+=kwargs[k]
   return sum

print(func(10,20))
print(func(1,2,3))
print(func(1,2,3,4,5,6))
print(func(1,2,kor=10,eng=20))
print(func(1,2,3,4,java=5,math=6,kor=7))
