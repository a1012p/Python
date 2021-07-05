from lib.db.dbconn import getconn as g

def update_table():
    conn = g()                  #dbconn 모듈에서 getconn 호출(객체 생성 후 반환받음)
    cur = conn.cursor()         #db 작업을 하는 객체(cur)
    #테이블 변경 - DDL 언어
    sql = " alter table member add contents text"
    cur.execute(sql)

    conn.commit()               #트랜잭션 완료(수행)
    conn.close()                #네트워크 종료

if __name__ == "__main__":
    update_table()


