# import mypackage.mymodule
#
# # package를 추가한 경우, import 시 패키지명.파일명 이렇게 넣어줘야 안에 있는 함수를 쓸 수 있다.
# print('오늘의 날씨: ', mypackage.mymodule.get_weather())
# print('오늘의 요일 : ',mypackage.mymodule.get_date(),"요일 입니다.")

# from mypackage import mymodule
#
# print('오늘의 날씨: ', mymodule.get_weather())
# print('오늘의 요일 : ', mymodule.get_date(), "요일 입니다.")

from mypackage import mymodule as mm    #내부 패키지 내부 파일 호출 후 별칭 부여

print('오늘의 날씨: ', mm.get_weather())
print('오늘의 요일 : ', mm.get_date(), "요일 입니다.")