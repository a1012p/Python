# 특정한 회원 검색하기

from lib.db.dbconn import getconn as g

def select_one():
    conn = g()
    cur =conn.cursor()
    #자료 조회 SQL언어 DML
    sql ="select * from member where name='황진이'"

    cur.execute(sql)
    rs = cur.fetchone() # 꺼내온 자료객체
    # rs = cur.fetchmany()
    print("황진이 검색")
    print(rs)

    # for i in rs:
    #     print(i)

    conn.close()

if __name__ == "__main__":
    select_one()