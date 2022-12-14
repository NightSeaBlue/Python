"""
    [에러와 예외]
    1. 에러
        문법적 오류
    2. 예외
        실행시 발생하는 오류로 예외가 발생하면 프로그램이 비정상 종료된다

    [예외처리]
    try:
        예외 발생 가능 문장들
    except Exception:
        예외가 발생한 후에 실행할 문장들
    else:
        예외가 발생하지 않았을 때 실행되는 문장들
    finally:
        예외 발생 여부와 상관없이 무조건 실행되는 문장들

    [참고] 파이썬 내장 예외
        https://docs.python.org/3/library/exceptions.html
"""
'''
# 0으로 나누기
#(1)
#10/0 #-> 예외발생 : ZeroDivisionError: division by zero

# (2)
try:
     10/0
except Exception:
    print("예외")
'''
# (3)
try:
     10/0
except Exception as e:  #Exception(예외) 는 별칭을 줘서 활용할 수 있음
    print("예외:", e)
else:                   #예외 미 발생시 실행
    print('예외가 없는 경우')
finally:                #예외와 관계없이 반드시 실행
    print('아노... 반드시 실행되어야 하무니다.')

