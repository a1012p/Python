# mydb에 member테이블 생성
# db 프로세스
# 1. db에 연결
# 2. 테이블 생성
from lib.db.dbconn import getconn as g

def create_table():
    conn = g()                  #dbconn 모듈에서 getconn 호출(객체 생성 후 반환받음)
    cur = conn.cursor()         #db 작업을 하는 객체(cur)
    #테이블 생성 - DDL 언어
    sql = """
        create table member(
            mem_num int primary key, 
            name char(20),
            age int
        )
    """
    cur.execute(sql)

    conn.commit()               #트랜잭션 완료(수행)
    conn.close()                #네트워크 종료

if __name__ == "__main__":
    create_table()


