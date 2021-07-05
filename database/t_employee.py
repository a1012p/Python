import sqlite3

from lib.db.dbconn import  getconn as g

def select_one():
    conn =g()
    cur = conn.cursor()

    sql = "select * from employee where emp_id = ?"
    cur.execute(sql,('e102',))
    rs = cur.fetchone()

    print(rs)

    conn.close()


def select_emp():
    conn =g()
    cur = conn.cursor()

    sql = "select * from employee"
    cur.execute(sql)
    rs = cur.fetchall()

    for i in rs:
        print(i)

    conn.close()

def insert_emp():
    "사원번호(char 4바이트) , 이름 , 나이 , 월급"
    conn =g()
    cur = conn.cursor()

    try:
        cur.execute("insert into employee(emp_id,name,age,salary) values (?,?,?,?)",('e104','김산',22,5000))
    except sqlite3.IntegrityError as IGE:
        print(IGE)

    conn.commit()
    conn.close()

def update_emp():
    conn =g()
    cur = conn.cursor()

    try:
        cur.execute("update employee set salary=? where name=?",(25000,'박인비'))
    except sqlite3.IntegrityError as IGE:
        print(IGE)

    conn.commit()
    conn.close()

def delete_emp():
    conn =g()
    cur = conn.cursor()

    try:
        #사원번호가 'e102'삭제
        cur.execute("delete from employee where emp_id=?",('e102',))
    except sqlite3.IntegrityError as IGE:
        print(IGE)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    # insert_emp()
    # update_emp()
    select_emp()
    delete_emp()
    select_emp()
    # select_one()
