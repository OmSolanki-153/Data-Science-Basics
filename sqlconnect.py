import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',passwd='root')
obj=conn.cursor()
statement="create database mydb"
obj.execute(statement)
print("CONNECTED");
conn.close()
