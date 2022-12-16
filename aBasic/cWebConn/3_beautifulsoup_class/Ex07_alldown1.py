"""
    HTML 내부에 있는 링크를 추출하는 함수
        - a 링크 연결된 모든 파일을 가져오기
"""

from bs4 import BeautifulSoup
from urllib import parse
from urllib import request

'''
    함수명 : enum_links
    인자 : html, base
        > 인자로 아래 main에서 response 와 url을 받는다!
        >> 그래서 함수 인자로 html,base 이렇게 받아온다
    리턴값 : result 
        > 모든 a 태그중 속성값 href 찾아서 
        기본 베이스되는 주소에 join으로 주소를 붙힌다!
        붙힌후 리스트화 한걸 리턴해준다
    역활 : a태그의 링크를만들어서 전부 호출해주는 역활~
    

'''



def enum_links(html,base):
    #-------------------------------------
    soup = BeautifulSoup(html,'html.parser')
    links = soup.select('a')
    #print(links)

    result = []
    for aTag in links:
        #href 속성이 필요한데 보면 상대경로임
        href=aTag.attrs['href'] # 일단 속성이href 인것들을 가져온다
        url = parse.urljoin(base, href) # 'https://docs.python.org/3.7/library/' 기본베이스에 추가
        result.append(url)
    return result


if __name__ == '__main__':
    url = 'https://docs.python.org/3.7/library/'
    response = request.urlopen(url)   # urllib.request.urlopen() : BeautifulSoup을 통해 html 파서할(데이타를 가져올) 대상
    result = enum_links(response, url)
    print(result)