# member 테이블 전체 검색

from lib.db.dbconn import getconn as g

def select_data():
    conn = g()
    cur =conn.cursor()
    #자료 조회 SQL언어 DML
    sql ="select * from member"

    cur.execute(sql)
    rs = cur.fetchall() # 꺼내온 자료객체
    print("데이터 전체 조회")

    for i in rs:
        print(i)

    conn.close()

if __name__ == "__main__":
    select_data()