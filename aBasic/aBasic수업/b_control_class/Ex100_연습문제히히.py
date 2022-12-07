#1
fruit = 'apple'
if fruit == 'Apple':
    fruit = 'Apple'
elif fruit == 'fruit':
    fruit = 'fruit'
else:
    fruit = fruit
print(fruit)        #apple

#2
number = ["1", 2, 3, float(4), str(5)]
if number[4] == 5:          #'5'
    print(type(number[0]))
elif number[3] == 4:        #4.0
    print(number[2:-1])     #[3,4.0]

#3
num = 0
i = 1
while i < 8:
    if i % 3 == 0:
        break
    i += 1
    num += i            #1+2+2(3에서 break 발생하나 값은 더해짐)
print(num)              #5

#4
result = 0
for i in range(5, -5, -2):      #5,3,1,-1,-3
    if i < -3:
        result += 1             #1+1+1+1+1=5
    else:
        result -= 1
print(result)

#5
num = ""
for i in range(10):         #0~9
    if i <= 5 and (i % 2)==0:   #0,2,4
        continue
    elif i == 7 or i == 10:     #7
        continue
    else:
        num = str(i) + num          #num 앞에 str형의 i 가 부착 즉 문자열 나열
print(num)                          #986531

#6
coupon = 0
money = 20000
coffee = 3500
while money > coffee:
    if coupon < 4:                  # cp:0 money:20000-3500 cp:1 money:16500-3500 cp:2 money:13000-3500 cp:3 money:9500-3500 cp:4 money: 6000-3500
        money = money - coffee      # cp:0 money: 5300 - 3500 : 1800
        coupon += 1

    else:
        money += 2800               # cp:4 money: 2500+2800 = 5300 > cp:0 으로 초기화
        coupon = 0
print(money)                        # 1800

#7
list_data_a = [1, 2]
list_data_b = [3, 4]
for i in list_data_a:               # 1,2
    for j in list_data_b:           # 3,4
        result = i + j              # 4 , 5 , 5, 6

print(result)                       # 출력이 반복문과 별도임, 따라서 반복문이 최종적으로 수행되고 나서 출력 즉 6
print('-'*200)
#--------------------------------------------------
#2차 문제
#1.
mylist = ['apple' ,'banana', 'grape']
result = list(enumerate(mylist))                # enumerate 실행 결과를 tuple 타입으로 받아 이를 다시 배열에 집어넣었음 (enumerate 실행결과 리턴이 None 이라 형태 지정 필요)
print(result)                                   # [(0,'apple'),(1,'banana'),(2,'grape')]

#2.
cat_song = "my cat has blue eyes, my cat is cute"       #split 결과 'my','cat','has','blue','eyes','my','cat','is','cute'
print({i:j for j,i in enumerate(cat_song.split())})     # split을 dict 형으로 변환하므로 중복 허용 불가 // 즉 최신으로 들어오는 값이 덮어씌워짐
# 그리고 인덱스와 결과가 뒤집어져있으므로 이거 잘 보고 찾아야 함
# {'my': 5, 'cat': 6, 'has': 2, 'blue': 3, 'eyes,': 4, 'is': 7, 'cute': 8}

#3.
colors = ['orange', 'pink', 'brown', 'black', 'white']
result = '&'.join(colors)           # join 의 return 형이 문자형
print(result)                       # orange&pink&brown&black&white

#4.
user_dict = {}
user_list = ["students","superuser", "professor", "employee"]
for value_1, value_2 in enumerate(user_list):                   # value_1 : idx ,value_2 : 'students','superuser','professor','employee'
    user_dict[value_2] = value_1                                # 키 값으로 value_2를 가지고 거기에 idx 를 value로 할당
print(user_dict)                                                # {'students': 0, 'superuser': 1, 'professor': 2, 'employee': 3}

#5
animal = ['Fox', 'Dog', 'Cat', 'Monkey', 'Horse', 'Panda', 'Owl']
print([ani for ani in animal if 'o' not in ani])                #['Cat', 'Panda', 'Owl'] 소문자 o를 가지고 있는 모든 문자 제외 컴프리헤션이 이뤄지는데 조건이 붙은것

#6
name = "Hanbit University"
student = ["Hong", "Gil", "Dong"]
split_name = name.split()                                       #'Hanbit','University'
join_student = ''.join(student)                                 # 'Hong''Gil''Dong'
print(join_student[-4:] + split_name[1])                        #Dong(문자열로 취급됨) + University

#7.
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2' ,'b3']
for a, b in tuple(zip(alist, blist)):                           # zip 의 경우 object 형으로 리턴 따라서 형태 지정 필요 (('a1,'b1'),('a2','b2'),('a3','b3'))
    print(a, b)                                                 # a1 b1 a2 b2 a3 b3

#8.
a = [1, 2, 3]
b = [4, 5, ]
c = [7, 8, 9]
print([[sum(k), len(k)] for k in zip(a, b, c)])     #zip(a,b,c) = ((1,4,7),(2,5,8))     #result=((12,3),(15,3))

#9.
week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
list_data = [week, rainbow]
print(list_data[1][2])                              # yellow

#10.
kor_score = [30, 79, 20, 100, 80]
math_score = [43, 59, 0, 30, 90]
eng_score = [49, 72, 48, 67, 15]
midterm_score = [kor_score, math_score, eng_score]
print ("score:",midterm_score[2][1])                #즉 eng_score의 idx 1번 : 72

#11.
alist = ["a", "b", "c"]
blist = ["1", "2", "3"]
abcd= []
for a, b in enumerate(zip(alist, blist)):           # [(0,('a','1')),(1,('b','2')),(2,('c','3'))]
    print(list(enumerate(zip(alist, blist))))
    try:
        abcd.append(b[a])                       #b[0] ,b[1] , b[2]
    except :IndexError
    abcd.append("error")

print(abcd)

#12
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h"]
nums = [i for i in range(20)]
answer = [alpha+str(num) for alpha in alphabet for num in nums if num%2==0]     #a0,a2...a18 * b to h 즉 a to h = 8 * 10
print(len(answer))