"""
@ 파일 읽고 쓰기
    - 파일을 읽고 쓰기 전에 파일을 열어야 한다
    - fileObj = open ( filename, mode )
            mode 첫번째 글자 - 작업 표시
            r(read)  : 파일 읽기
            w(write) : 파일 쓰기 ( 파일이 없으면 생성하고 파일이 있으면 덮어쓴다 )
            x(write) : 파일 쓰기 ( 파일이 없을 때만 생성하고 쓴다 )
            a(append) : 파일 추가 ( 파일이 있으면 파일의 끝에서부터 추가하여 쓴다 )

            mode 두번째 글자 - 파일 타입
            t : 텍스트(text) 타입 ( 기본값 )
            b : 이진(binary) 타입
            두번째 글자가 없으면 텍스트 타입이다.

            encoding='utf-8' : 한글

    - 파일을 열고 사용 후에는 반드시 닫아야 한다 (close())
"""
'''
try:
    f=open('./data/data.txt','r',encoding='utf-8')
except FileNotFoundError as e:
    print('파일 못 찾아요 힝힝 ㅠㅠ :',e)
else:                   #예외가 발생하지 않았을 때
    while True:         # 반복문을 돌려, 이를 한줄 씩 읽는 함수 실행 후, 줄이 끝나면 멈춤
        line=f.readline()
        if not line: break
        print(line)
    f.close()       # Open 한 파일을 닫아줌
finally:
    print('종료했숴')
'''

# 자동으로 파일을 close() 하기 위해 with 구문을 사용함. (?!)
# with open('data/data.txt','r',encoding='utf-8') as f:
#     while True:  # 반복문을 돌려, 이를 한줄 씩 읽는 함수 실행 후, 줄이 끝나면 멈추고, close() 없이 자동 종료
#         line = f.readline()
#         if not line: break  #실행할 명령어가 한줄인 경우 콜론 옆에 위치해도 무방.
#         print(line)

# 파일 전체를 읽어버리기 !! read()
filename='./data/'+'data.txt'
with open(filename,'r',encoding='utf-8') as f:
    content=f.read()
    #print(content)
    words = content.split()
    print(words)
    print('총 단어 수 >',len(words))

try:
    with open('data/data.txt','r',encoding='utf-8') as f:
        content = f.read()
        words=content.split()

except FileNotFoundError as e:
    print('오류 >',e)

finally:
    print('총 단어 수 >', len(words))


