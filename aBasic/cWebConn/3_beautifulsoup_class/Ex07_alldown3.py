"""
    파이썬은 파일하나를 모듈로 취급한다면 다른 파일의 함수를 복사하지 않고 바로 호출한다.

    [주의] import Ex07_alldown1 코드부터 에러발생하지만 실행은 됨

"""


from bs4 import BeautifulSoup
from urllib.parse import *
from urllib.request import *
import os, time, re

# 에러 발생해도 실행은됨
import Ex07_alldown1
import Ex07_alldown2

# ------------------------------------------------------
# (3) 이미 처리한 파일인지 확인하기 위한 변수
proc_files = {} #딕셔너리 빈 {] 모양 무저건 딕셔너리

# HTML을 분석하고 다운받는 함수
def analyze_html(url, root_url): # root_url은 보관용임 고정 그래서 아래서 인자2개보낸거임
    
    # (1) 다운받은에가 딕셔너리에있으면 패스 없으면 넣어주는 1번역할
    print("analyze_html=", url)

    savepath = Ex07_alldown2.download_file(url) # url을 브라우저에서 쳤을때
    #index.html이 생략되어있는데 아까 2번에서 html 파일다운 만든것처럼 만든거임

    if savepath is None: return # 혹시라도 네트웍때문에못받으면 리턴해버린당

    #딕셔너리 안에 세이브가 들어있으면임!
    if savepath in proc_files: return # 이미 처리된 파일이면 실행하지 않음
    #다운받은거에 딕셔너리가 없으면 아래실행
    proc_files[savepath] = True
    #proc_files = {} 이렇게 없으면 아래주소가 키값이된다라는 의미임
    #proc_files = {'https://docs.python.org/3.5/library/ : true'}
    #다음에 또 다운받으면 위 if문에 걸려서 그냥 리턴될꺼임
    # print(proc_files)





    # (2) 링크 추출
    f = open(savepath, "r", encoding="utf-8")
    html = f.read() # 오픈해서 읽는다 / index.html 파일을
    links = Ex07_alldown1.enum_links(html, url) # 아까 a태그에 html을 조인해서 만든 모음이 index.html 파일임
    #즉 완벽한 경로를 추출다해서 리스트를 links에다 준것이다
    
    
    #리스트를 하나씩 뽑는다 
    #root_url 처음 넘겨받은 맨처음 시작경로
    for link_url in links:
        # 링크가 루트 이외의 경로를 나타낸다면 무시 ( 여기서는 docs.python.org 경로가 아니면 무시 )
        if link_url.find(root_url) != 0: #루트경로가 베이스 경로와 다르다면 다버리고 다시시작한다임
            continue


        # HTML이라면 / 
        if re.search(".html$", link_url):
            # 재귀적으로 HTML 파일 분석하기
            analyze_html(link_url, root_url) #.html로 끝나는 파일이라면 !!!
            #함수를 재실행해서 계속 실행하겠다는거임 아닌파일들은 컨티뉴로 재시작되면서 다없어질꺼고
            continue


        # 기타 파일
        Ex07_alldown2.download_file(link_url)
        # 오래 걸려서 도중에 종료를 하면 지금까지 생성된 파일들이 보인다




if __name__ == "__main__":
    # URL에 있는 모든 것 다운받기
    url = "https://docs.python.org/3.5/library/"
    analyze_html(url, url)



