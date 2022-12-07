"""
 [ 제어문 ]
    - 파이썬은 들여쓰기를 하여 블록{}을 대신 표현한다
    - 들여쓰기는 탭과 공백을 섞어 쓰지 말자
    - 가급적 탭으로만 정리할 것... 달리 정리했다 피보지 말으라..

    [ex]
    if a>b:
        print(a)
        print(b)  => 에러발생

    (1) if 문
        if 조건식A :
            문장들
        elif 조건식B :
            문장들
        else :
            문장들

        ` 조건식이나 else 뒤에는 콜론(:) 표시
        ` 조건식을 ( ) 괄호 필요없다
        ` 실행할 코드가 없으면 pass
        ` 파이썬은 switch 문 없음(!!!!)
"""

# 거짓(False)의 값
i = 0;
i2 = 0.0
i3 = ""
i4 = str()
i5 = list()
i6 = tuple()
i7 = set()
i8 = dict()
i9 = {}
i10 = None

a = -1
if a:
    print('True')
else:
    print('False')

a = 1
b = 0

if a and b:
    print('True2')  # 안나옴
if a or b:
    print('True3')  # True3

# and 와 or 의 경우 결정적인 결과를 출력해줌
print(a and b)  # 0 : False라는 결과를 가져오기 때문에 0 출력
print(a or b)  # -1 : True라는 결과가 결정되었기 때문에 -1 출력

a = 20
b = 0

if a:
    c = 2
elif b:
    c = 4
else:
    c = 6

print(c)  # 2 (a 는 20이라는 수를 가지고 있어 True 로 리턴됨.)
