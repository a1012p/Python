# 자료를 삽입하는 코드

from lib.db.dbconn import getconn as g

def insert_data(name, age):
    conn = g()
    cur = conn.cursor()
    #자료를 추가 - SQL언어 DML
    sql = " insert into member values ('%s' ,%d) " % (name,age)

    # sql = """
    #     insert into member values ('최영',60),
    #     insert into member values ('이순신',50)
    # """

    cur.execute(sql)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_data('심청이',25)