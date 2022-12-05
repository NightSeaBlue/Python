# 부울형 - 첫글자는 반드시 대문자(********) True, False, None 여야 한다
t = True
f = False
n = None    # 다른 언어의  null 값과 유사

hungry = True
sleepy = False

print(not hungry)              #False
print(not sleepy)              #True
print(hungry and sleepy)       #False
print(hungry or sleepy)        #True
print(hungry & sleepy)         #False
print(hungry | sleepy)         #True




"""
        자료형         값           부울형
    -----------------------------------------------------
        문자형       "문자"          True
                    ""                     False
        리스트       [1,2,3]         True       
                    []                     False
        튜플         ()                     False
        딕셔너리     {}                     False
        숫자형       0이아닌 숫자     True
                    0                      False
                    None                   False

"""

if '아':                        #True
    print('True')
else:
    print('False')

if []:                         #False2
    print('True2')
else:
    print('False2')

if 0:                         #False3
    print('True3')
else:
    print('False3')

print('='*50)
msg = '행복합시다'
if msg.find('행')==0:                   #msg 자체가 문자열로 인식되어서 그러함.
    print('ok')
else:
    print('no')

if msg.find('가')==-1:
    print('ok')
else:
    print('no')

if '행' in msg:
    print ('ok')
else :
    print('no')