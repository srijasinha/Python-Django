import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123"
)
# cursor object c
c = db.cursor()

# create DB
c.execute("CREATE DATABASE employee_db")
c.execute("SHOW DATABASES")

for i in c:
    print(i)
c = db.cursor()

#create table
emptbl_create = CREATE TABLE 'employee_db'. 'tblemployee' (
    'empid' INT NOT NULL AUTO_INCREMENT,
    'empname' VARCHAR(45) NULL,
    'department' VARCHAR(45) NULL,
    'salary' INT NULL,
    PRIMARY KEY ('empid'))

c.execute(emptbl_create)

#Insert Table

employeetbl_insert = INSERT INTO tblemployee(empname,department,salary)
                      VALUES(%s, %s, %s)

data = [("Ram", "HR", "100000"),
        ("Krish", "Accounts", "60000"),
        ("Aman", "Sales", "25000"),
        ("Govind", "Marketing", "40000")]

c.executemany(employeetbl_insert, data)
db.commit()

#select query
employeetbl_select = Select * from tblemployee
c.execute(employeetbl_select)

#Delete
employeetbl_delete = Delete from tblemployee WHERE empid = 3
c.execute(employeetbl_delete)
db.commit()

#update
employeetbl_update = UPDATE tblemployee
SET salary = 115000 WHERE empid = 1
c.execute(employeetbl_update)
db.commit()


db.close()
