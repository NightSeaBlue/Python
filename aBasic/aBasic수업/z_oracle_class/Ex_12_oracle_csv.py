#Ex12_oracle_csv.py
import cx_Oracle as orc
import csv

def createDBTable():
    # 1. 연결객체 얻어오기 (Connection)
    conn = orc.connect('scott/tiger@127.0.0.1:1521/xe')
    # 2. sql 문장 만들기
    sql='''
    CREATE TABLE supply(
        id              number  primary key,
        Supplier_Name   varchar2(50),
        Invoice_Number  varchar2(50),
        Part_Number     varchar2(50),
        Cost            number(10),
        Purchase_Date   date
        )       
    '''
    sql2='create sequence seq_supply_id'
    # 3. cursor 얻어오기
    cursor=conn.cursor()
    #4. 실행
    cursor.execute(sql)
    cursor.execute(sql2)
    #5. 종료
    cursor.close()
    conn.close()

def saveDBTable(data):
    # 1. 연결객체 얻어오기 (Connection)
    conn = orc.connect('scott/tiger@127.0.0.1:1521/xe')
    # 2. sql 문장 만들기
    sql='''INSERT INTO SUPPLY 
    VALUES(seq_supply_id.NEXTVAL,:0,:1,:2,:3,:4)
    '''
    cursor = conn.cursor()
    # 4. 실행
    cursor.execute(sql,data)
    # 5. 종료
    cursor.close()
    conn.commit()       #잊지말자!  데이터 입력하고 커밋으로 저장해줘야 됨.
    conn.close()

def viewDBTable(tablename):
    # 1. 연결객체 얻어오기 (Connection)
    conn = orc.connect('scott/tiger@127.0.0.1:1521/xe')
    # 2. sql 문장 만들기
    sql = 'SELECT * FROM {}'.format(tablename)
    cursor = conn.cursor()
    # 4. 실행
    cursor.execute(sql)
    datas=cursor.fetchall()
    for data in datas:
        print(data)
    # 5. 종료
    cursor.close()
    conn.commit()  # 잊지말자!  데이터 입력하고 커밋으로 저장해줘야 됨.
    conn.close()

if __name__ == '__main__':
    # (1)테이블 생성
    # createDBTable()
    # (2-0) 입력확인
    # imsi=['kosmo','9999','8888',1000,'2022-12-24']
    # saveDBTable(imsi)
    #(2) csv 파일을 읽어서 -> db 입력
    # file=open('supply.csv','r')             #file을 읽어들이는 open 함수 실행
    # datas=csv.reader(file)                  # csv 파일을 읽기 위해 csv package를 임포트 하고, csv 함수인 reader 실행
    # print(datas)
    # header=next(datas,None)         #next를 통해 최상단 머리를 날릴 수 있음(csv 파일 첫 시작인 한 열의 정의들).
    # print(header)
    # print('-'*50)
    # for row in datas:                 # row (한  행) 이 datas 즉 csv file 에 존재하는 경우, 반복문을 실행함
    #     # print(row)
    #     saveDBTable(row)              # 한 행씩 DB 에 입력하는 함수 실행
    # (3) 테이블 출력
    viewDBTable('supply')

