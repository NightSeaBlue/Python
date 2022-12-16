"""
    파일을 다운받고 저장하는 함수

     [참고] 파이썬 정규식 표현 : https://wikidocs.net/4308
"""


'''


    함수명 : download_file
    인자 : url
    리턴값 : savepath 
    역활 : 

'''



from bs4 import BeautifulSoup
from urllib import parse
from urllib import request
import os, time, re  # re : 정규식

def download_file(url):
    p = parse.urlparse(url) # urlparse ? 란 ?
    # ParseResult(scheme='https', netloc='docs.python.org', path='/3.6/library/', params='', query='', fragment='')
    # 이렇게 url을 역활을 기준으로 잘라서 나타내준다
    # print('1 -',p)
    savepath = './' + p.netloc + p.path
    # print('2 -',savepath) # 필요한 netloc path 2개를 더한부분이 나옴

    # re 정규화 > /로 끝나는 녀석을 찾는다
    if re.search('/$', savepath):
        savepath += 'index.html'
        print('3-', savepath)
    # 즉 /로 끝나는 녀석이면 index.html을 붙혀준다 > /로 안끝나는 녀석은 뭐 if를 안타겠지


    # 이미 파일을 다운 받았을 경우 함수 종료
    if os.path.exists(savepath): return savepath

    # savepath 라는 폴더를 하나 만들꺼다
    # 다운 받은 파일이 저장될 폴더가 없을 경우 생성한다.
    savedir = os.path.dirname(savepath)
    if not os.path.exists(savedir):# 만약 폴더가 없다면 ~
        os.makedirs(savedir)    # makedir 을하면 하나만 만들어짐 하위가 안만들어짐 그래서 s붙혀주기

    try:
        request.urlretrieve(url, savepath)  # url 을 savepath에 저장하려고
        time.sleep(2)       # 파일 하나 다운 받고 2초 쉬기
        print('download - ', url)
        return savepath
    except:
        print('fail download :', url)
        return  None

if __name__ == '__main__':
    url = 'https://docs.python.org/3.6/library/'
    result = download_file(url)
    print(result)