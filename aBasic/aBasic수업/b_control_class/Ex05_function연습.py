'''
[ 연습문제 ]

- 리스트를 인자로 받아 짝수만 갖는 리스트 반환하는 함수 ( 함수명 : even_filter )
    [ 실행 ]
        print(even_filter([1, 2, 4, 5, 8, 9, 10]))

- 주어진 수가 소수인지 아닌지 판단하는 함수 ( 함수명 : is_prime_number )
    [ 실행 ]
        print(is_prime_number(60))
        print(is_prime_number(61))

- 주어진 문자열에서 모음의 개수를 출력하는 함수 ( 함수명 : count_vowel )
    [ 실행 ]
        print(count_vowel("pythonian"))
'''


#(1)   함수명 : even_filter 역할 : 숫자를 리스트로 입력받아, 그 요소가 짝수인 것만 리스트로 재반환
def even_filter(list):
    result=[]
    for list in list:
        if list%2==0:
            result.append(list)
    return result
print(even_filter([1,2,4,5,8,9,10]))

def even_filter(list):
    return [x for x in list if x%2==0]
print(even_filter([1,2,3,4,5,6,7,8,9,10]))

#(2) 함수명 : is_prime_number 역할 : 숫자를 입력받아, 그 수가 소수인 경우 True 아닌 경우 False 리턴
def is_prime_number(x):
    for i in range(2,int(x/2)):
        if x%i==0:
            return False
    return True
print(is_prime_number(60))
print(is_prime_number(61))

#(3) 함수명 : count_vowel 역할 : 문자열을 입력받아 , 모음의 갯수를 세 그 갯수를 리턴함
def count_vowel(x):
    cnt=0
    for char in x:
        if char in ['a','e','i','o','u']:
            cnt+=1
    return cnt

print(count_vowel('pythonian'))