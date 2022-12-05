
# import datetime                 #datetime의 모든 plugin 사용시
# today = datetime.date.today()
# print('today is ', today)

from datetime import date       #datetime 중 date plugin 만 import 하는 경우 // 여러개 임포트 할 때 나열해서 작성해도 무관
today = date.today()
print('today is ', today)

print('='*50)
# 날짜 구하기
print('년도 : ',today.year)
print('월 : ',today.month)
print('일 : ',today.day)
day=['월','화','수','목','금','토','일']
print('요일 : ',day[today.weekday()])      #월~일 : 0-6

print('='*50)
from datetime import timedelta
#날짜 계산
print('어제 : ',today+timedelta(days=-1))
#일주일 전 날짜
print('일주일 전 : ',today+timedelta(days=-7))
#10일 후
print('10일 후 :',today+timedelta(days=10))

from datetime import datetime
day = datetime.today()
print(day)

#import datetime
#day = datetime.datetime.today()
#print(day)

print('='*50)
#날짜를 문자열 형태 (strftime() 이용)
print(day.strftime('%Y %m월 %d일 %H시 %M분'))       #h : 월의 표준형 나옴 dec 이런식으로

#문자열을 날짜형태(strptime() 이용)
naljja='2022-12-25 12:50:59'
print(type(naljja))
mydate = datetime.strptime(naljja,'%Y-%m-%d %H:%M:%S')
print(mydate)
print(type(mydate))