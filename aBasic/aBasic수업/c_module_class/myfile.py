#import mymodule

#print('오늘의 날씨: ', mymodule.get_weather())
#print('오늘의 요일 : ',mymodule.get_date())

# import mymodule as mm     별칭을 주는 경우 별칭만 사용 가능
#
# print('오늘의 날씨: ', mm.get_weather())
# print('오늘의 요일 : ',mm.get_date())

# 특정 함수만 import 시키면, 함수 이름만 호출 가능
from mypackage.mymodule import get_weather, get_date

print('오늘의 날씨: ', get_weather())
print('오늘의 요일 : ', get_date(), "요일 입니다.")
