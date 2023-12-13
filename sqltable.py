import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',passwd='root', database = 'mydb')
obj=conn.cursor()
statement="create table student(age int, name varchar(30))"
obj.execute(statement)
print("Table Created");
conn.close()
