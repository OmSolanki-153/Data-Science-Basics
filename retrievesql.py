# Program to display the data 
import mysql.connector 

try:
 
  # define a connection object
  conn = mysql.connector.connect(host='localhost',user='root',passwd='root', database = 'mydb')
 
  # open cursor, define and run query, fetch results
  cursor = conn.cursor()
  query = 'SELECT * FROM student'
  cursor.execute(query)
  result = cursor.fetchall()
 
  # print the results in each row
  for r in result:
    print("AGE",r[0]);
    print("name",r[1]);
 
  # close the cursor and database connection
  cursor.close()
  conn.close()
 
# catch exception and print error message
except Error as err:
  print('Error message: ' + err.msg)
