#Ex02_csv.py

#csv 파일 > 엑셀에서도 열리고 일반 에디터에서도 열림
#Common String Value : 표 형태의 데이터를 저장하는 파일 형식, 한 줄이 한개의 행에 해당하며, 열 사이에는 쉼표를 넣어 구분한다.

data=[[1,'김','책임연구원'],[2,'박','선임연구원'],[3,'이','연구원']]
# csv package import
# encoding='utf-8-sig' : csv 파일의 한글 깨짐 방지
import csv
with open('./data/imsi.csv','wt',encoding='utf-8-sig') as f:
    #f.write()
    cout=csv.writer(f)                                      # csv Writer : csv 형태의 파일을 생성함
    cout.writerows(data)                                    # 한 행씩 데이터를 csv 파일에 입력

result=[]
with open('./data/imsi.csv','rt',encoding='utf-8-sig') as f:
    cin = csv.reader(f)
    result=[row for row in cin if row]      #if row = row 의 값이 있을 때

print(result)