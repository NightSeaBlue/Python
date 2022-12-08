# [파이썬 + 디비 절차]
# 1. 연결객체 얻어오기 (Connection)
# 2. sql 문장
# 3. cursor 객체 얻어오기 (전송)
# 4. 실행
# 5. cursor 객체 종료
# 6. 연결객체 종료

import cx_Oracle as orc
# 1. 연결객체 얻어오기 (Connection)
conn=orc.connect('scott/tiger@127.0.0.1:1521/xe')
print(conn.version)
#2. sql 문장
sql='select * from emp'
#3. cursor 객체 얻어오기
cursor=conn.cursor()
#4. 실행
cursor.execute(sql)
datas=cursor.fetchall()
#print(datas)
for row in datas:
    print(row[0] ,row[1],row[2])
#5. 커서객체종료
cursor.close()
#6. 연결객체 종료
conn.close()