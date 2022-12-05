#1&2
a = [0, 1, 2, 3, 4]
print(a[:3], a[:-3])    #[0,1,2],[0,1]
print(a[::-1])          #[4,3,2,1,0]
#3
first = ["egg", "salad", "bread", "soup", "canafe"]
second = ["fish", "lamb", "pork", "beef", "chicken"]
third = ["apple", "banana", "orange", "grape", "mango"]
order = [first, second, third]
john = [order[0][:-2], second[1::3], third[0]] #[[egg,salad,bread],[lamb,chicken],[apple]]
del john[2]                         #[apple] drop
john.extend([order[2][0:1]])        #[apple] 추가
print(john)                         #[[egg,salad,bread],[lamb,chicken],[apple]]
#4
list_a = [3, 2, 1, 4]
list_b = list_a.sort()      #리턴이 없음 None
print(list_a, list_b)       #[1,2,3,4] None

#5
fruits = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry', 'melon']
print(fruits[-3:], fruits[1::3])        #[[orange,strawberry,melon],[banana,orange]]

#6
num = [1, 2, 3, 4]
print(num * 2)      #[1,2,3,4,1,2,3,4]

#7
a = [1, 2, 3, 5]
b = ['a', 'b', 'c','d','e']
a.append('g')
b.append(6)
print('g' in b, len(b))     #False,6

#8
list_a = ['Hankook', 'University', 'is', 'an', 'academic', 'institute', 'located', 'in', 'South Korea']
list_b = []
for i in range(len(list_a)):
    if i % 2 != 1:
      list_b.append(list_a[i])

print(list_b)       #[Hankook,is,academic,loacted,south_korea]

#9
#admission_year = input("입학 연도를 입력하세요: ")
#print(type(admission_year))    <class:str>,<class:str>

#10
country = ["Korea", "Japan", "China"]
capital = ["Seoul", "Tokyo", "Beijing"]
index = [1, 2, 3]
country.append(capital)
country[3][1] = index[1:]
print(country)     #[korea,japan,china,[seoul,[2,3],beiging]]

#11
a = [5, 4, 3, 2, 1]
b = a
c = [5, 4, 3, 2, 1]
a is b                  #True   가리키는 주소가 일치하므로 True로 리턴
print(a is b)
print(a is c)           #False  임의의 별도의 주소를 가리키므로 False 리턴

#15
list_1 = [[1, 2], [3], [4, 5, 6]]
a,b,c = list_1                      #a=[1,2] b=[3] c=[4,5,6]
list_2 = a + b + c                  #list_2=[1,2,3,4,5,6]
print(list_2)

#=================================================
#1. 자료형 정리
'''가.stack 나. queue(큐) 다.튜플 라.셋'''
#2
a = [3, "apple", 2016, 4]
b = a.pop(0)    #3
c = a.pop(1)    #2016
print(b + c)

#3.
dict_1 = {2:1, 4:2, 6:3, 8:4, 10:6}
dict_keys = list(dict_1.keys())
dict_values = list(dict_1.values())
dict_2 = dict()
for i in range(len(dict_keys)):
	dict_2[dict_values[i]] = dict_keys[i]
print(len(dict_keys ))
print(dict_2[2])

#4.
animal = ['cat', 'snake', 'monkey', 'ant', 'spider']
legs= [4, 0, 2, 4, 8]
animal_legs_dict = {}
for i in range(len(animal)):
	animal_legs_dict[legs[i]] = animal[i]
	animal_legs_dict['ant'] = 6

print(animal_legs_dict)         #{4:'ant','ant':6,0:'snake',2:'monkey',8:'spider'}

#5
Mydict = {'1' : 1, '2' : 2}
Copy = Mydict
Mydict['1'] = 5
result= Mydict['1'] + Copy['1']
print(result)

#6
a = list(range(10))
a.append(a[3])
a.pop(a[3])
a.insert(3, a[-1])
a.pop( )
print(a)                        #0,1,2,3,4,5,6,7,8,9

#7              # (1,),[1],error  // error,[1],(1,)
data_1 = {'one' : (1,2,3,4,5,6), 'two' : [1,2,3,4,5,6], 'three' : {'four' : 4, 'five' : 5}}
for k in ['one','two','three']:
	try:
		print(data_1[k][:1])
	except TypeError:
		print("error")

for k in ['one', 'two','three']:
	try:
		data_1[k][-1] = "a"
		print(data_1[k][-1])
	except TypeError :
		print("error")