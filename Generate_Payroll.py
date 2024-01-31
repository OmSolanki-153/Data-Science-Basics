import sqlite3 as sq
import pandas as pd

sInputFileName1='C:/MScITPracs/DS/Organizing data/Male.csv'
sInputFileName2='C:/MScITPracs/DS/Organizing data/Female.csv'
sDatabaseName='C:/MScITPracs/DS/Organizing data/omsol.db'
conn=sq.connect(sDatabaseName)

MaleRawData=pd.read_csv(sInputFileName1,header=0,low_memory=False,encoding="latin-1")
MaleRawData.rename(columns={'Namevalues':'Firstname'},inplace=True)
MaleRawData.drop_duplicates(subset=None,keep='first', inplace=True)

MaleData=MaleRawData

sTable='Assess_MaleName'

print('Storing :', sDatabaseName, ' Table:',sTable)

MaleData.to_sql(sTable, conn, if_exists="replace")
print('Storing :',sDatabaseName,' Table:',sTable)

FemaleRawData=pd.read_csv(sInputFileName2,header=0,low_memory=False,encoding="latin-1")
FemaleRawData.rename(columns={'Namevalues':'Firstname'},inplace=True)
FemaleRawData.drop_duplicates(subset=None,keep='first', inplace=True)
FemaleData=FemaleRawData
sTable='Assess_FemaleName'
print('Storing :', sDatabaseName, ' Table:',sTable)
FemaleData.to_sql(sTable, conn, if_exists='replace')
print('Storing :',sDatabaseName,' Table:',sTable)

sSQL="select FirstName, Salary from Assess_FemaleName where Salary>=25000;"
result1=pd.read_sql_query(sSQL, conn)
sTable='Assess_result1'
print('Storing:' ,sDatabaseName, 'Table:',sTable)
result1.to_sql(sTable, conn, if_exists = 'replace' )
print(result1);
      
sSQL="select FirstName, Salary from Assess_MaleName where Salary>=30000;"
result2=pd.read_sql_query(sSQL, conn)
sTable='Assess_result2'
print('Storing:', sDatabaseName, 'Table:',sTable)
result2.to_sql(sTable, conn, if_exists ='replace')
print(result2);

sSQL = "select distinct FirstName from Assess_result1 \
UNION\
 select distinct FirstName from Assess_result2;"
finalresult = pd.read_sql_query(sSQL, conn)
print("\nLoading data from two tables \n", finalresult)
