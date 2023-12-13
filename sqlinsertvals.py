import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',passwd='root', database = 'mydb')
obj=conn.cursor()
statement="insert into student values(21,'om')"
obj.execute(statement)
print("Data Inserted");
conn.commit()
conn.close()
