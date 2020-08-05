import sqlite3 as lite
con = lite.connect('db2.db')
c=con.cursor()
def create():
    c.execute('create table employee(EmpId INTEGER PRIMARY KEY, EmpName VARCHAR)')
def insert():
    c.execute('insert into employee values("01","Muheeb")')
    c.execute('insert into employee values("02","Krishna")')
    c.execute('insert into employee values("03","Tasmiya")')
    c.execute('insert into employee values("04","Nazreen")')
    con.commit()
def select():
    c.execute('select * from employee')
    data=c.fetchall()
    print(data)
    print(data[0])
    print(data[1])
    print(data[2])
    print(data[3])
    c.close()
    con.close()

create()
insert()
select()