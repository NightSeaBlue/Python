#1
list_1 = [0, 3, 1, 7, 5, 0, 5, 8, 0, 4]
def quiz_2(list_data):
    a = set(list_data)      # a 를 호출하면서 set으로 선언됨과 동시에 정렬됨   
    return list(a)[1:5]     # set a의  idx 1 번부터 4번까지를 list 형태로 리턴함
print(quiz_2(list_1))

#2
def  delete_a_list_element(list_data, element_value):
	if element_value in list_data:      # 요소가 list_data라는 배열에 있는 경우
		list_data.remove(element_value) # 해당 요소를 제거함
		return list_data                # 배열 형태로 리턴
	else:
		return "False"                  # 아닌 경우 False 리턴

list_data = ['a', 1, 'gachon', '2016.0']
element = float(2016)       # 2016.0
result = delete_a_list_element(list_data, element)  
print(result)

#3
tuple_1 = (1, 2, 3)
tuple_2 = (4, 5, 6)
def quiz_1(tuple_1, tuple_2):
	result = []
	for i in (tuple_1 + tuple_2):       # (1,2,3,4,5,6)
		result.append(i)        # i = 1,2,3,4,5,6
	return result               # result=[1,2,3,4,5,6]

print(quiz_1(tuple_1, tuple_2))