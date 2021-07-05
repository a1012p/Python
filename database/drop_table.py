from lib.db.dbconn import getconn as g

def drop_table():
    conn = g()
    cur = conn.cursor()
    # DDL - 테이블 삭제 언어
    sql = "drop table member"

    cur.execute(sql)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    drop_table()