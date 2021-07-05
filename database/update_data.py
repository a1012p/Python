# 자료를 수정하는 코드

from lib.db.dbconn import getconn as g

def update_data():
    conn = g()
    cur = conn.cursor()
    #자료를 수정 - SQL언어 DML
    sql = "update member set name='이몽룡' where mem_num = 103"

    cur.execute(sql)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    update_data()