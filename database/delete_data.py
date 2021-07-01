# 자료를 삭제하는 코드

from lib.db.dbconn import getconn as g

def delete_data():
    conn = g()
    cur = conn.cursor()
    #자료를 수정 - SQL언어 DML
    sql = "delete from member where name='최영'"

    cur.execute(sql)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    delete_data()