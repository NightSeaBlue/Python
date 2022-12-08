"""
0. DB에 저장할 테이블 생성
1. 사용자 입력 받아 확인
2. 모든 연락처 출력하기
3. 연락처 삭제하기
"""
import cx_Oracle as orc

class Contact:
    def __init__(self, name, phone_number, email, addr):
        self.name = name
        self.phone_name = phone_number
        self.email = email
        self.addr = addr

    def print_info(self):
        print("이름:", self.name)
        print("전화번호:", self.phone_name)
        print("이메일:", self.email)
        print("주소;", self.addr)


def print_menu():
    print('1. 연락처 입력')
    print('2. 연락처 출력')
    print('3. 연락처 삭제')
    print('4. 종료')
    menu = input('메뉴선택:')
    return int(menu)


def set_contact():
    # (1)
    # 이름, 전화번호, 이메일, 주소를 입력받아
    name = input("이름")
    phone_number = input("전화번호")
    email = input("이메일")
    addr = input("주소")
    # Contact 객체를 생성하고 DB 에 입력
    contact = Contact(name, phone_number, email, addr)
    # 연결객체를 얻어옴
    conn = orc.connect('scott/tiger@127.0.0.1:1521/xe')
    # sql 문장        # format 을 활용해, 생성된 contact 객체를 이용해서 DB에 정보 입력
    sql = "INSERT INTO CONTACT VALUES('{0}','{1}','{2}','{3}')".format(contact.name, contact.phone_name, contact.email,
                                                                       contact.addr)
    # cursor 객체 생성 및 전송
    cursor = conn.cursor()
    try:
        cursor.execute(sql)             # sql 문 전송
    except Exception as e:
        print('입력불가 > ', e)          # sql 문이 전송이 되지 않는 경우 예외 발생
    finally:
        cursor.close()
        conn.commit()
        conn.close()


def print_contact():
    # (2)
    #  테이블의 전체 레코드 출력
    # 연결 객체를 얻어옴
    conn = orc.connect('scott/tiger@127.0.0.1:1521/xe')
    # sql 문장
    sql = 'SELECT * FROM CONTACT'       # sql 문
    # CURSOR 객체 생성 및 전송
    cursor = conn.cursor()
    try :
        cursor.execute(sql)
        datas = cursor.fetchall()           # sql 문이 실행된 결과를 가져와 fetchall 을 통해, tuple로 받아옴
        for data in datas:
            c=Contact(data[0],data[1],data[2],data[3])      #data[0] : Name , data[1]: phone_name , data[2]=email , data[3]=addr
            c.print_info()
    except Exception as e:
        print('출력 불가 > ',e)
    finally:
        cursor.close()
        conn.commit()
        conn.close()


def delete_contact(name):
    # (3)
    # 해당이름과 같은 요소를 찾아서 삭제
    # 연결 객체를 얻어옴
    conn = orc.connect('scott/tiger@127.0.0.1:1521/xe')
    # sql 문장
    sql = "SELECT* FROM CONTACT WHERE NAME='{}'".format(name)       # 입력한 이름과 일치하는 정보가 있는지 찾아옴  , Oracle 특성상 '' 이 없는경우 값을 정확하게 인지하지 못하기 때문에, 쿼리문과 구별해서 사용.
    sql2= "DELETE FROM CONTACT WHERE NAME='{}'".format(name)        # Query 문 : "" , 입력받은 인자 : ''
    # CURSOR 객체 생성 및 전송
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
    except Exception as e:
        print('삭제 불가 > ',e)
    else:
        cursor.execute(sql2)
    finally:
        cursor.close()
        conn.commit()
        conn.close()




def run():
    while True:
        menu = print_menu()
        if menu == 4:  # 종료를 선택하면
            break
        elif menu == 1:  # 입력을 선택하면
            set_contact()
        elif menu == 2:  # 출력을 선택하면
            print_contact()
        elif menu == 3:  # 삭제를 선택하면
            name = input('삭제할 이름은?')
            delete_contact(name)


def createTable():
    # 1.연결객체 연결
    conn = orc.connect('scott/tiger@127.0.0.1:1521/xe')
    # 2. sql 문장
    sql = '''
        CREATE TABLE contact(
            name        varchar2(90),
            phone_name  varchar2(30) primary key,
            email       varchar2(300),
            addr        varchar2(600)       
        )
    '''
    # cursor 객체 얻어오기
    cursor = conn.cursor()
    # cursor 전송
    cursor.execute(sql)
    # 전송 종료 및 커밋
    cursor.close()
    conn.commit()
    conn.close()


if __name__ == "__main__":
    # createTable()
    run()
