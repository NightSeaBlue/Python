"""
     1) 클래스 기초

     ` __init__ 함수 : 객체 초기화 함수( 생성자 역할 )
     ` self : 객체 자신을 가리킨다.
"""

'''
    자바인 경우
    class Sample {
        String data="Hello";
        String name;
        Sample(String name) {
            this.name = name;
            }
    }
    
    Sample s = new Sample("홍길동");        
'''

# 파이썬 클래스는 삶을 죤내 윤택하게 해준다. 정말 편리함의 끝을 찍는다...
class Sample:
    data='Hello'
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('__init__ 호출')
    def __del__(self):
        print('__del__ 호출')


s=Sample("무야홍",27)
print(s.name)
print(s.data)
print(s.age)
del s               # 인터프리터 언어여서, 한 줄 씩 읽고 실행되므로 Class 삭제됨
print('-'*200)      # Class 삭제 이후 출력문 출력

"""
    2) 
    인스턴스 함수 :  'self'인 인스턴스를 인자로 받고 인스턴스 변수와 같이 하나의 인스턴스에만 한정된 데이터를 생성, 변경, 참조
    클래스   함수 :  'cls'인 클래스를 인자로 받고 모든 인스턴스가 공유하는 클래스 변수와 같은 데이터를 생성, 변경 또는 참조
     
    - 클래스 함수는 클래스명 접근
 
 [ 자바인 경우 ]
 class Sample {
    int a;
    static int b;
 }
 
 Sample s1 = new Sample();
 Sample s2 = new Sample();
 Sample s3 = new Sample();   
 
"""

class Book:
     cnt=0
     def __init__(self,title):
        self.title=title
        self.cnt+=1
     def output(self):      #단순 함수 생성시 인스턴스 변수인 self 만 잡힘
         pass               #pass : 아무 뜻 없이 스킵
     @classmethod       # @classmethod 선언시 class를 인자로 넘겨받을 수 있음.
     def output2(cls):
         cls.cnt+=1
         
     
b1=Book('행복이란')
b2=Book('무엇일까')
b3=Book('어디에나 있고')
b4=Book('어디에도 없구나')
b1.output2()
b2.output2()
print(Book.cnt)
print()




'''
     3) 클래스 상속
        - 파이션은 method overriding은 있지만 method overloading 개념은 없다
        - 파이션은 다중상속이 가능
        - 부모 클래스가 2개 이상인 경우 먼저 기술한 부모클래스에서 먼저 우선 해당 멤버를 찾음
'''
class Animal:
    def move(self):
        print('동물은 움직인다.')

class Human(Animal):        #상속 클래스 (부모 클래스)
    def move(self):
        print('인간은 두 발로 걷는다.')


class Wolf(Animal):
    def move(self):
        print('늑대는 네 발로 달린다.')

# 다중상속
class Werewolf(Wolf,Human):
    def move(self):
        print('늑대인간은 두 발로 걷고 네 발로 달린다')

ww=Werewolf()
ww.move()       # 맨 앞에 선언한 class의 overriding 된 함수가 호출됨
print('-'*200)
h=Human()
h.move()
w=Wolf()
w.move()