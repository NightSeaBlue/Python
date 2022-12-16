'''
1. 크롬웹드라이버로 구글 사이트 열기

2. 실제 크롬창에서 '파이썬'라고 검색버튼을 누른다.
    개발자모드(F12)에서 이 부분을 보면
    <input name='q' value='파이썬'~~ >
    그리고 'google검색' 버튼이 type='submit' 인거 확인
'''

# [1]
from selenium import webdriver

driver = webdriver.Chrome('./webdrive/chromedriver.exe')

driver.get('http://google.com')
#----------------------------------------------
# [2]
#name 이라는 요소찾기 / 구글의 검색창 부분
search_bt = driver.find_element_by_name('q')
search_bt.send_keys('코로나 극뽁')
search_bt.submit()

# 구글에서 알아서 채팅해서 서브밋해서 창보여줌

