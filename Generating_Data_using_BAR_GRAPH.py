import pandas as pd
import matplotlib.pyplot as plt
import sqlite3 as sq

sDatabaseName='C:/MScITPracs/DS/mydb.db'
conn1 = sq.connect(sDatabaseName)

sSQL="SELECT * FROM student01;"
df=pd.read_sql_query(sSQL, conn1)
print(df)
df.plot(kind="bar",x="name",y="height")
plt.show()
