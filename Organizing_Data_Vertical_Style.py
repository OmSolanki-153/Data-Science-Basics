import pandas as pd
import sqlite3 as sq
sDatabaseName='C:/MScITPracs/DS/mydb.db'
conn1 = sq.connect(sDatabaseName)
sDatabaseName='C:/MScITPracs/DS/omsol.db'
conn2 = sq.connect(sDatabaseName)
sTable = 'student01'
sSQL="SELECT * FROM student01;"

PersonFrame0=pd.read_sql_query(sSQL, conn1)

print(PersonFrame0)

sSQL="SELECT height, weight, rank from student01;"

PersonFrame1=pd.read_sql_query(sSQL, conn1)
print(PersonFrame1)
DimPerson = PersonFrame1
DimPersonIndex=DimPerson.set_index(['rank'], inplace=False)
sTable = 'student2'

print('Storing', sDatabaseName,'\n Table:',sTable)
DimPersonIndex.to_sql(sTable, conn2, if_exists="replace")
print('Loading', sDatabaseName, 'Table:', sTable)

sSQL="SELECT * FROM student2;"

PersonFrame2 = pd.read_sql_query(sSQL, conn2)

print(PersonFrame2)

print('Student0l Table (Rows):', PersonFrame0.shape[0]) 
print('Student01 Table (Columns):',PersonFrame0.shape[1])
print('Student2 table (Rows):', PersonFrame2.shape[0])
print('Student2 table (Columns):', PersonFrame2.shape[1])
