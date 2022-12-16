"""
 간단하게 크롬 브라우저를 실행하여 페이지 열기
"""

#import webdriver / 드라이버 구글에서 다운받아와야함
from selenium import webdriver

# 1. webdriver 객체생성
#크롬에서 가져옴 > 인자로 다운받은 드라이버의 주소를넣어줌
driver = webdriver.Chrome('./webdrive/chromedriver.exe')

# 2. 페이지 접근
driver.get('https://www.naver.com')


# 3. 화면을 캡처해서 저장하기
driver.save_screenshot("naver.png")

driver.close()
