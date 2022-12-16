from selenium import webdriver

# 나의 페이스북 아이디와 비번을 변수에 담는다
usr ='bcj0825@nate.com'
pwd = '@b01051642240'


#1.객체생성
driver = webdriver.Chrome('./webdrive/chromedriver.exe')

#2.페이스북의 로그인 화면으로 가게함
driver.get('https://www.facebook.com/')
driver.implicitly_wait(2)

#아이디와 비번 찾는 란의 id 값을 가져와서 변수에 담았다
em = driver.find_element_by_id('email')
pw = driver.find_element_by_id('pass')

#send_keys 이키를 담아줘야 그 텍스트란에 전달해줄 수 있는거임
em.send_keys(usr)
pw.send_keys(pwd)

#버튼 - 로그인버튼
btn = driver.find_element_by_name('login')

#로그인버튼이 클릭되면 
btn.click()
driver.implicitly_wait(2)



#최종적으로 내 아이디로 로그인이된다
