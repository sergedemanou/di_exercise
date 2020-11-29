import sqlite3




conn = sqlite3.connect('db.sqlite')
cursor = conn.cursor()
print("Opened database successfully")
# cursor.execute('''CREATE TABLE EMPLOYEE
#          (ID INT PRIMARY KEY     NOT NULL,
#          NAME           TEXT    NOT NULL,
#          AGE            INT     NOT NULL);''')
# cursor.close()
# cursor.execute("INSERT INTO EMPLOYEE (ID,NAME,AGE) VALUES (1, 'Razi', 14)");
# cursor.execute("INSERT INTO EMPLOYEE (ID,NAME,AGE) VALUES (2, 'Jon', 19)");
# cursor.execute("INSERT INTO EMPLOYEE (ID,NAME,AGE) VALUES (3, 'Martha', 35)");
# conn.commit()
# conn.close()
def add_emplyee():
    n = input('what is your name:')
    a = int(input('what is your age :'))
    cursor.execute("INSERT INTO EMPLOYEE (ID,NAME,AGE)values (5,?,?)", (n, a))
    conn.commit()
    conn.close()
# add_emplyee()
cursor.execute("SELECT * FROM EMPLOYEE;")
datas = cursor.fetchall()
for data in datas:
    print(data)